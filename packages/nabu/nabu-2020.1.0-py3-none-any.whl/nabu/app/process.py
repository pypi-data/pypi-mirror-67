import numpy as np

from ..utils import convert_index, ArrayPlaceHolder, is_device_backend
from ..resources.params import files_formats, FileFormat
from .logger import LoggerOrPrint
from .available_components import *
from .pipeline import Pipeline
from .component import ComponentDescription, ComponentName

from ..cuda.utils import __has_pycuda__, __pycuda_error_msg__, get_cuda_context
if __has_pycuda__:
    import pycuda.gpuarray as garray
from ..opencl.utils import __has_pyopencl__, __pyopencl_error_msg__, create_opencl_context
if __has_pyopencl__:
    import pyopencl.array as parray
    from pyopencl import CommandQueue
from ..cuda.utils import replace_array_memory as replace_cuarray_memory
from ..opencl.utils import replace_array_memory as replace_clarray_memory


class WorkerProcess:
    """
    Main function for processing a chunk of data.
    This class wraps all the tasks done by a "worker", regardless of the
    computation distribution method.
    """
    def __init__(
        self, process_config, sub_region,
        chunk_size=None, use_cuda=True, use_opencl=False, logger=None,
        cuda_ctx=None, cl_ctx=None, extra_options=None,
    ):
        """
        Initialize a "worker" to process a chunk.

        Parameters
        ----------
        processing_config: `nabu.resources.processcinfig.ProcessConfig`
            Process configuration.
        sub_region: tuple
            Sub-region to process in the volume for this worker, in the format
            `(start_x, end_x, start_z, end_z)`.
            See also: `chunk_size`.
        chunk_size: int, optional
            Specify a chunk size for processing on memory-limited devices.
            It is such that `chunk_size * Nx * Na` fits in device memory, where
            `Nx` and `Na` denote the detector width and the number of radios respectively.
            If not provided, it is set to `delta_z = sub_region[-1] - sub_region[-2]`.
            If `delta_z > chunk_size`, then the current sub-volume is cut into "sub-chunks",
            each having a height `chunk_size` (see Notes below).
        use_cuda: bool, optional
            Whether to use Cuda for the processing
        use_opencl: bool, optional
            Whether to use OpenCL for the processing
        logger: `nabu.app.logger.Logger`, optional
            Logger class
        cuda_ctx: `pyopencl.Context`, optional
            Use an already created OpenCL context.
        cl_ctx: `pycuda.driver.Context`, optional
            Use an already created Cuda context.
        extra_options: dict, optional
            Advanced extra options. Available options with their default:
               - cuda_device_id: 0
               - cuda_cleanup_at_exit: True
               - cl_platform_id: 0
               - cl_device_id: 0
               - clear_gpu_memory_when_possible False


        Important
        ----------
        When using Cuda or OpenCL, the parameter `chunk_size` must be such that
        `chunk_size * Nx * Na` voxel can fit in device memory. If not provided,
        `chunk_size` is equal to `delta_z = sub_region[-1] - sub_region[-2]`.
        So for wide detectors with a big number of radios, this is likely to fail.
        Providing a `chunk_size` accordingly enables to process the images by groups
        (see Notes below).


        Notes
        ------
        1. In the case where `use_opencl` is `True` and an OpenCL context is not provided,
        the context will be created using the options in `extra_options`.
        As the default values are poor choices (there is not way to know in advance
        the best OpenCL platform/device to use), it is strongly recommended to
        configure these options.
        The same holds (although in a lesser extent) for `use_cuda`.

        2. Let `Dz` be the subvolume height, `Nx` the number of pixels horizontally,
        and `Na` the number of angles (radios), as illustrated below::


                     _________________
                    /                /|
                   /                / |
                  /________________/  |
                 |                 |  /
              Dz |                 | / Na
                 |_________________|/
                       Nx


        If we use Cuda or OpenCL and if the subvolume to process (`Dz * Nx * Na` voxels)
        is too big for device memory, then images are processed by "groups"
        instead of processing the whole subvolume in one memory chunk.
        More precisely:
           - Radios are are processed by groups of `G` "vertical images"
             where `G` is such that `G * Dz * Nx` fits in memory
             (i.e `G * Dz * Nx = chunk_size * Nx * Na`)
           - Sinograms are processed by group of `chunk_size` "horizontal images"
             since by hypothesis `chunk_size * Nx * Na` fits in memory.
        """
        self._set_params(process_config, use_cuda, use_opencl, logger, extra_options)
        self._configure_options_for_worker(sub_region)
        self._set_subvolume_params(chunk_size)
        self._get_device_context(cuda_ctx, cl_ctx)
        self._allocate_memory()
        self._get_rec_array()
        self._init_pipeline()
        self._gpumem_cleared = False
        self._prepare_pipeline()


    # -------------------------------------------------------------------------
    # ----------------------- Initialization functions ------------------------
    # -------------------------------------------------------------------------

    def _set_params(self, process_config, use_cuda, use_opencl, logger, extra_options):
        """
        Set parameters that will not be changed.
        """
        self.process_config = process_config
        self.processing_steps = process_config.processing_steps
        self.dataset_infos = process_config.dataset_infos
        self.logger = LoggerOrPrint(logger)
        if use_cuda and use_opencl:
            # By design, the worker can either use Cuda or OpenCL.
            raise ValueError("Cannot use both Cuda and OpenCL")
        self.use_cuda = use_cuda
        self.use_opencl = use_opencl
        self._set_extra_options(extra_options)
        self._old_file_prefix = None


    def _set_extra_options(self, extra_options):
        if extra_options is None:
            extra_options = {}
        advanced_options = {
            "cuda_device_id": 0,
            "cuda_cleanup_at_exit": True,
            "cl_platform_id": 0,
            "cl_device_id": 0,
            "clear_gpu_memory_when_possible": False
        }
        advanced_options.update(extra_options)
        self.extra_options = advanced_options
        self._clear_gpumem = self.extra_options["clear_gpu_memory_when_possible"]


    def _configure_options_for_worker(self, sub_region):
        """
        Configure parameters specific to this worker.
        Perform a deep copy of the given structures, and mofity the new structures
        to specialize the tasks to the current worker.
        """
        self.sub_region = sub_region
        new_options = {}
        for key, val in self.process_config.processing_options.items():
            new_options[key] = {}
            for k2, v2 in val.items():
                new_options[key][k2] = v2
            new_options[key]["sub_region"] = self.sub_region
            new_options[key]["use_cuda"] = self.use_cuda
            new_options[key]["use_opencl"] = self.use_opencl
        if "read_chunk" not in new_options:
            raise ValueError("The step 'read_chunk' is required")
        # in rare cases, the conversion is not needed
        new_options["read_chunk"]["convert_float"] = True
        if "reconstruction" in new_options:
            new_options["reconstruction"]["start_z"] = self.sub_region[-2]
            new_options["reconstruction"]["end_z"] = self.sub_region[-1]-1
        self.processing_options = new_options


    def _set_subvolume_params(self, chunk_size):
        self.cut_chunk = False
        # When doing a binning in the vertical direction,
        # it has to be taken into account for chunk_size and sub_region
        # This is still quite fragile:
        #   - sub_region has to be provided as is there were no binning
        #   - it is passed "as is no binning" to ChunkReader
        #   - it however has to be updated here for allocating the arrays
        binning_z = self.process_config.dataset_infos.binning[-1]
        if binning_z > 1:
            zmin, zmax = self.sub_region[-2:]
            zmin //= binning_z
            zmax //= binning_z
            new_subregion = self.sub_region[:-2] + (zmin, zmax)
            self.logger.info(
                "binning_z: subregion processed %s --> %s"
                % (self.sub_region, new_subregion)
            )
            self.sub_region = new_subregion
        #
        x_min, x_max, z_min, z_max = self.sub_region
        Nx, Nz = self.dataset_infos.radio_dims
        self.Na = self.dataset_infos.n_angles
        self.Nx = Nx
        self.Nz = Nz
        # Absolute position in volume
        self.x_min = convert_index(x_min, Nx, 0)
        self.x_max = convert_index(x_max, Nx, Nx)
        self.z_min = convert_index(z_min, Nz, 0)
        self.z_max = convert_index(z_max, Nz, Nz)
        self.delta_z = self.z_max - self.z_min
        # Shape of the subvolume to be processed
        self.radios_total_shape = (self.Na, self.delta_z, self.Nx)
        self.sinos_total_shape = (self.delta_z, self.Na, self.Nx) # might vary

        # Adapt to "chunk"
        self.chunk_size = chunk_size
        if chunk_size is None:
            self.chunk_size = self.delta_z
        self.chunk_size = min(self.chunk_size, self.delta_z)
        # If sub_region is bigger than chunk_size, cut chunk into groups
        if (self.delta_z > self.chunk_size) and (self.use_cuda or self.use_opencl):
            self.cut_chunk = True
            self.logger.info(
                "Subvolume will be cut into groups: sub_region = %s (delta_z = %d) and chunk_size = %d"
                % (str(self.sub_region), self.delta_z, self.chunk_size)
            )
        self.sinos_group_size = self.chunk_size
        self.radios_group_size = self.Na
        if self.cut_chunk:
            self.radios_group_size = (self.Na * self.chunk_size) // self.delta_z
        self.radios_group_shape = (self.radios_group_size, ) + self.radios_total_shape[1:]
        self.sinos_group_shape = (self.sinos_group_size, ) + self.sinos_total_shape[1:]


    def _get_device_context(self, cuda_ctx, cl_ctx):
        """
        Get a Cuda/Opencl context
        """
        self.cuda_ctx = None
        self.cl_ctx = None
        if self.use_cuda:
            if not(__has_pycuda__):
                raise ValueError("Cannot use pycuda: %s" % __pycuda_error_msg__)
            if cuda_ctx is not None:
                self.cuda_ctx = cuda_ctx
            else:
                self.cuda_ctx = get_cuda_context(
                    self.extra_options["cuda_device_id"],
                    self.extra_options["cuda_cleanup_at_exit"]
                )
        if self.use_opencl:
            if not(__has_pyopencl__):
                raise ValueError("Cannot use pyopencl: %s" % __pyopencl_error_msg__)
            if cl_ctx is not None:
                self.cl_ctx = cl_ctx
            else:
                self.cl_ctx = create_opencl_context(
                    self.extra_options["cl_platform_id"],
                    self.extra_options["cl_device_id"]
                )
            self.queue = CommandQueue(self.cl_ctx)



    def _allocate_device_array(self, shape):
        if self.use_cuda:
            return garray.zeros(shape, "f")
        elif self.use_opencl:
            return parray.zeros(self.queue, shape, "f")
        else:
            raise ValueError("not using cuda nor opencl")


    def _allocate_memory(self):
        # For Numpy backend, radios are allocated on host by ChunkReader
        if self.use_cuda or self.use_opencl:
            self.d_radios = self._allocate_device_array(self.radios_group_shape)
            self.d_output = self._allocate_device_array(self.radios_group_shape[1:])
        self.d_recs = None


    def _get_rec_array(self):
        opts = self.processing_options["reconstruction"]
        x_s, x_e = opts["start_x"], opts["end_x"]+1
        y_s, y_e = opts["start_y"], opts["end_y"]+1
        z_s, z_e = opts["start_z"], opts["end_z"]+1
        self.rec_total_shape = (z_e - z_s, y_e - y_s, x_e - x_s)
        self.rec_shape = (self.sinos_group_size, ) + self.rec_total_shape[1:]
        if self.cut_chunk:
            self.recs = np.zeros(self.rec_total_shape, "f")
        else:
            self.recs = np.zeros(self.rec_shape, "f")


    def _init_pipeline(self):
        """
        One-time function for initializing the processing pipeline
        """
        steps = self.processing_steps
        options = self.processing_options
        # Initialize the pipeline with a "data provider"
        initial_pipeline = [
            ComponentDescription(
                ChunkReaderComponent,
                ["read_chunk", (1, 1, 1), options["read_chunk"]]
            )
        ]
        self.pipeline = Pipeline(initial_pipeline, logger=self.logger)
        self.radios_np = self.pipeline._original_data

        radios_placeholder = ArrayPlaceHolder(self.radios_group_shape, "f", name="d_radios")
        # Define the pipeline
        pipeline = []
        if "flatfield" in steps:
            pipeline.append(ComponentDescription(
                FlatFieldComponent,
                ["flatfield", self.radios_total_shape, options["flatfield"]],
                exec_args=[radios_placeholder]
            ))
        if "ccd_correction" in steps:
            pipeline.append(ComponentDescription(
                CCDFilterComponent,
                ["ccd_correction", self.radios_total_shape, options["ccd_correction"]],
                exec_args=[radios_placeholder]
            ))
        if "double_flatfield" in steps:
            pipeline.append(ComponentDescription(
                DoubleFlatFieldComponent,
                ["double_flatfield", self.radios_total_shape, options["double_flatfield"]],
                exec_args=[radios_placeholder]
            ))
        if "phase" in steps:
            pipeline.append(ComponentDescription(
                PhaseRetrievalComponent,
                ["phase", self.radios_total_shape, options["phase"]],
                exec_args=[radios_placeholder]
            ))
        if "unsharp_mask" in steps:
            pipeline.append(ComponentDescription(
                UnsharpMaskComponent,
                ["unsharp_mask", self.radios_total_shape, options["unsharp_mask"]],
                exec_args=[radios_placeholder]
            ))
        if "take_log" in steps:
            pipeline.append(ComponentDescription(
                NegativeLogComponent,
                ["take_log", self.radios_total_shape, options["take_log"]],
                exec_args=[radios_placeholder]
            ))
        if "build_sino" in steps:
            pipeline.append(ComponentDescription(
                SinoBuilderComponent,
                ["build_sino", self.radios_total_shape, options["build_sino"]],
                exec_args=[radios_placeholder],
                callback=self._build_sino_callback
            ))
        if "reconstruction" in steps:
            pipeline.append(ComponentDescription(
                FBPComponent,
                ["reconstruction", self.sinos_total_shape, options["reconstruction"]],
                exec_args=[ArrayPlaceHolder(self.sinos_total_shape, "f")],
            ))
        if "save" in steps: # TODO support other than save reconstructions
            self._configure_saving()
            options["save"]["nx_infos"] = self._get_output_nxinfos(pipeline[-1].name)
            pipeline.append(ComponentDescription(
                SavingComponent,
                ["save", self.recs.shape, options["save"]],
                exec_args=[self.recs],
            ))

        # Set common execution args/kwargs
        common_components_kwargs = {"logger": self.logger}
        if self.cut_chunk:
            common_components_kwargs["device_array"] = self.d_radios
        if self.use_cuda or self.use_opencl:
            # This array is not always needed, depending on the component
            common_components_kwargs["device_buffer"] = self.d_output
        for component_desc in pipeline:
            component_desc.kwargs.update(common_components_kwargs)

        # Now plug each step into the pipeline
        for component_desc in pipeline:
            self.pipeline.plug(component_desc)


    # -------------------------------------------------------------------------
    # ---------------------- Memory cleaning utils ----------------------------
    # -------------------------------------------------------------------------

    def _clear_device_array_from_pipeline(self, array_name, array_shape, components_using_array, reset_output=True):
        """
        Release GPU memory linked to array.
        Replace references to array with a placeholder in the pipeline.
        """
        # Release device memory
        d_arr = getattr(self, array_name)
        self._free_gpuarray(d_arr)
        # Replace array with a placeholder for future use
        array_pl = ArrayPlaceHolder(array_shape, "f", name=array_name)
        for comp_name in components_using_array:
            comp = self.pipeline.get_component(comp_name)
            if comp is None or not(is_device_backend(comp.backend)):
                continue
            if not(self.cut_chunk):
                comp.exec_args[0] = array_pl
                if reset_output:
                    comp.output = None
            else:
                comp.instance._set_device_array(array_pl)

    def _clear_device_radios(self):
        """
        Release GPU memory linked to self.d_radios.
        Replace references to self.d_radios with a placeholder in the pipeline.
        """
        components_using_d_radios = [
            "flatfield", "ccd_correction", "phase", "unsharp_mask", "take_log",
        ]
        self._clear_device_array_from_pipeline(
            "d_radios",
            self.radios_group_shape,
            components_using_d_radios,
            reset_output=True
        )
        self._clear_device_array_from_pipeline(
            "d_radios",
            self.radios_group_shape,
            ["build_sino"],
            reset_output=False
        )

    def _clear_device_sinos(self):
        self._clear_device_array_from_pipeline(
            "d_sinos",
            self.sinos_group_shape,
            ["reconstruction"]
        )
        sino_builder = self.pipeline.get_component("build_sino")
        if sino_builder is not None and is_device_backend(sino_builder.backend):
            sino_builder.output = None

    def _clear_device_recs(self):
        self._free_gpuarray(self.d_recs)
        self.d_recs = None


    def _free_gpuarray(self, arr):
        if self.use_cuda:
            return replace_cuarray_memory(arr, (1,))
        elif self.use_opencl:
            return replace_clarray_memory(arr, (1,))
        else:
            raise ValueError()


    def _destroy_gpu_context(self):
        """
        Dangerous ! Please use it if you know what you are doing
        """
        if self.use_cuda:
            self.logger.debug("Releasing cuda context")
            self.cuda_ctx.detach()


    # -------------------------------------------------------------------------
    # ----------------------- Saving utils ------------------------------------
    # -------------------------------------------------------------------------

    def _get_output_nxinfos(self, process_name):
        options = self.processing_options["save"]
        if FileFormat.from_value(files_formats[options["file_format"]]) != FileFormat.HDF5:
            return None
        entry = getattr(self.dataset_infos.dataset_scanner, "entry", None)
        nx_infos = {
            "process_name": process_name,
            "processing_index": 0,
            "config": self.process_config.nabu_config,
            "entry": entry,
        }
        return nx_infos


    def _configure_saving(self):
        out_cfg = self.processing_options["save"]
        if self._old_file_prefix is None:
            self._old_file_prefix = out_cfg["file_prefix"]
        out_cfg["file_prefix"] = self._old_file_prefix + "_%04d" % self.z_min


    # -------------------------------------------------------------------------
    # ----------------------- Callbacks ---------------------------------------
    # -------------------------------------------------------------------------

    def _build_sino_callback(self, comp_desc):
        """
        Default callback passed to build_sino
        """
        # assert comp_desc.instance.name == "build_sino"
        rec_component = self.pipeline.get_component("reconstruction")
        if rec_component is None:
            return
        reconstructor = rec_component.instance

        if self._clear_gpumem:
            self._clear_device_radios()

        # Now create the device array for reconstruction
        # TODO handle opencl
        if self.d_recs is None:
            self.d_recs = garray.zeros(self.rec_shape, "f")
        rec_component.exec_kwargs = {"output":  self.d_recs}
        # Reference the device sinogram
        self.d_sinos = self.pipeline.get_component("build_sino").output
        if self.cut_chunk:
            # In this case, building the sino is done on host,
            # but we still need a device array for reconstruction
            self.d_sinos = garray.zeros(self.sinos_group_shape, "f")
            reconstructor_set_device_array(self.d_sinos)
            rec_component.exec_kwargs["exec_output"] = self.recs


    # -------------------------------------------------------------------------
    # ----------------------- Pipeline execution ------------------------------
    # -------------------------------------------------------------------------

    def _prepare_pipeline(self):
        """
        Function called each time we want to process a new chunk of data
        """
        options = self.processing_options
        # Update data retriever
        chunk_reader = self.pipeline.get_component("read_chunk").instance.chunk_reader
        # reset the reader to prepare for a new chunk
        chunk_reader._set_subregion(self.sub_region)
        chunk_reader._init_reader()
        chunk_reader._loaded = False
        # Re-allocate memory if needed
        if self._gpumem_cleared:
            self.d_radios = self._allocate_device_array(self.radios_group_shape)
            self._gpumem_cleared = False
        # Update radios buffer passed to components
        for component_desc in self.pipeline.components:
            if not(self.cut_chunk):
                comp_input = component_desc.input_array
                if isinstance(comp_input, ArrayPlaceHolder) and comp_input.name == "d_radios":
                    if is_device_backend(component_desc.backend):
                        component_desc.exec_args[0] = self.d_radios
                    else:
                        component_desc.exec_args[0] = self.radios_np
            else:
                if not(component_desc.name.startswith("Memory transfer")):
                    component_desc.instance._set_device_array(self.d_radios)
        # Update some components options
        if "flatfield" in self.processing_steps:
            # Flatfield takes a "sub_region" option for loading darks/refs
            flatfield = self.pipeline.get_component("flatfield").instance.flatfield
            if flatfield.flats_reader._loaded:
                flatfield._set_subregion(self.sub_region)
                flatfield._init_reader()
                flatfield._loaded = False
        # Configure saving
        if "save" in self.processing_steps:
            saving_comp = self.pipeline.get_component("save")
            self._configure_saving()
            options["save"]["nx_infos"] = self._get_output_nxinfos("reconstruction")
            # Overwrite the class instance in the pipeline
            saving_comp.instance = saving_comp.Class(
                "save", self.recs.shape, options["save"],
            )
            saving_comp.exec_args=[self.recs]


    def process_chunk(self, sub_region=None):
        """
        Main function for processing a chunk of data.
        """
        if sub_region is not None and sub_region != self.sub_region:
            self.logger.debug("Setting new subregion to %s" % str(sub_region))
            dz0 = self.sub_region[-1] - self.sub_region[-2]
            dz = sub_region[-1] - sub_region[-2]
            if dz != dz0:
                raise ValueError(
                    "Cannot change delta_z: was %d, requested %d. Please instantiate a new class"
                    % (dz0, dz)
                )
            self.set_subregion(sub_region)

        self._prepare_pipeline()
        self.pipeline.execute_pipeline(reload_data=True)

        if self._clear_gpumem:
            self.logger.debug("Cleaning device memory")
            if "reconstruction" in self.processing_steps:
                self._clear_device_sinos()
                self._clear_device_recs()
            self.pipeline._reset_memcopies()
            self._gpumem_cleared = True


    def set_subregion(self, sub_region):
        """
        (re-)set subregion to process.
        """
        self._configure_options_for_worker(sub_region)
        self._set_subvolume_params(self.chunk_size)
