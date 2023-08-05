from ..utils import is_device_backend, ArrayPlaceHolder, array_tostring
from .memtransfer import MemoryTransferComponent
from .logger import LoggerOrPrint
from .component import ComponentDescription


class Pipeline:
    """
    A high-level processing pipeline handling.
    A Pipeline aims at seamlessly pluging together `Component`s.
    It does not allocate memory on its own
    (this is done by a `WorkerProcess` using one instance of this class).
    """

    def __init__(
        self,
        pipeline_description,
        logger=None,
    ):
        """
        Initialize a processing pipeline.
        A pipeline always needs to be initialized from a "data reader component".

        Parameters
        ----------
        pipeline_description: list of ComponentDescription
            Description of the processing pipeline. Each item of the list is a
            `ComponentDescription` object.
        logger: `Logger`, optional
            Logging object.
        """
        self.logger = LoggerOrPrint(logger)
        self._init_pipeline(pipeline_description)


    def _init_pipeline(self, pipeline_description):
        self._initialized = False
        if pipeline_description == []:
            return
        # The first component of the pipeline is always the "data provider"
        data_provider_desc = pipeline_description.pop(0)
        self._init_data_provider(data_provider_desc)
        for component_desc in pipeline_description:
            self.plug(component_desc)


    def _init_data_provider(self, dataprovider_desc):
        data_provider = dataprovider_desc.instantiate()
        if not (hasattr(data_provider, "data")):
            raise ValueError(
                "First component must be a data provider, i.e have a .data field"
            )
        self._original_data = data_provider.data
        self.data_provider = dataprovider_desc
        self.components = [dataprovider_desc]
        self._initialized = True
        self._data_read = False


    #
    # Memory transfer and placeholder related functions
    #

    def _plug_memtransfer(self, previous_component, current_component):
        """
        Plug a memory transfer between "previous_component" and "current_component"
        """
        src_backend = previous_component.backend
        dst_backend = current_component.backend

        # src is the output of previous component - certainly a placeholder,
        # since it is not known at this stage (component not executed yet)
        src = previous_component.output_array
        # dst is the input of the current component
        dst = current_component.input_array

        memtransfer_desc = ComponentDescription(
            MemoryTransferComponent,
            [src_backend, dst_backend],
            kwargs={"logger": self.logger},
            exec_args=[src, dst],
        )
        memtransfer_desc.instantiate()
        self.components.append(memtransfer_desc)


    def _update_component_input(self, current_component, previous_component):
        if isinstance(current_component.input_array, ArrayPlaceHolder):
            self.logger.debug(
                "Pipeline: %s: replacing input %s with output of %s: %s"
                % (
                    current_component.name,
                    array_tostring(current_component.input_array),
                    previous_component.name,
                    array_tostring(previous_component.output_array),
                )
            )
            current_component.exec_args[0] = previous_component.output_array


    def _update_component_placeholders(self, component, component_idx):
        prev_component = self.components[component_idx-1]
        self._update_component_input(component, prev_component)
        if component.name.startswith("Memory transfer"):
            if isinstance(component.exec_args[1], ArrayPlaceHolder):
                next_component = self.components[component_idx+1]
                self.logger.debug(
                    "Pipeline: %s: replacing destination %s with input of %s: %s"
                    % (
                        component.name,
                        array_tostring(component.exec_args[1]),
                        next_component.name,
                        array_tostring(next_component.input_array),
                    )
                )
                component.exec_args[1] = next_component.input_array
            src, dst = component.exec_args[:2]
            if isinstance(src, ArrayPlaceHolder) or isinstance(dst, ArrayPlaceHolder):
                raise ValueError(
                    "%s: ArrayPlaceHolder is still there - could not find out what to use instead"
                    % component.name
                )


    def _reset_memcopies(self, shape=None):
        for comp in self.components:
            if comp.name.startswith("Memory transfer"):
                shp = shape if shape is not None else comp.exec_args[0].shape
                comp.exec_args[0] = ArrayPlaceHolder(shp, "f")
                comp.exec_args[1] = ArrayPlaceHolder(shp, "f")
                comp.output = None

    #
    # Public methods
    #

    def plug(self, component_desc):
        """
        Plug a component into the current processing pipeline.

        Parameters
        -----------
        component_desc: ComponentDescription
            A component description object.
        """
        assert isinstance(component_desc, ComponentDescription)
        component_desc.instantiate()
        previous_component = self.components[-1]
        #
        previous_backend = previous_component.backend
        current_backend = component_desc.backend
        # Backend is different between components - have to transfer memory
        # unless we are processing by groups
        prev_is_groupping = previous_component.instance.exec_by_groups
        curr_is_groupping = component_desc.instance.exec_by_groups
        prev_uses_np_array = not(is_device_backend(previous_backend)) or prev_is_groupping
        curr_uses_np_array = not(is_device_backend(current_backend)) or curr_is_groupping
        if prev_uses_np_array ^ curr_uses_np_array:
            self.logger.debug(
                "Pipeline: plugging memtransfer between %s and %s"
                % (previous_component.name, component_desc.name)
            )
            self._plug_memtransfer(previous_component, component_desc)
        #
        self.components.append(component_desc)


    def get_data(self, reload_data=False):
        """
        Execute the "0st step" of the pipeline, i.e get the data.

        Parameters
        ----------
        reload_data: bool, optional
            Whether to force re-loading data. By default, once the data is read,
            it will not be read again for re-executing the pipeline.
        """
        self.data_provider.exec_kwargs.update({"overwrite": reload_data})
        self.data_provider.execute()
        self._data_read = True
        self.data_provider.exec_kwargs.update({"overwrite": False})  # not very elegant


    def execute_pipeline(self, reload_data=False):
        """
        Execute the whole processing pipeline.

        Parameters
        ----------
        reload_data: bool, optional
            Whether to force re-loading data. By default, once the data is read,
            it will not be read again for re-executing the pipeline.
        """
        if not(self._data_read) or reload_data:
            self.get_data(reload_data=True)
        for i, component_desc in enumerate(self.components[1:]):
            self._update_component_placeholders(component_desc, i+1)
            component_desc.execute()
            # Callback
            if component_desc.callback is not None:
                component_desc.callback(component_desc)

    def get_component(self, name):
        """
        Get a component by name.
        """
        for comp in self.components:
            if comp.name == name:
                return comp
        return None


    def __repr__(self):
        return str(list(map(lambda x: x.name, self.components)))

    def __len__(self):
        return len(self.components)

    def __getitem__(self, key):
        return self.components[key]

