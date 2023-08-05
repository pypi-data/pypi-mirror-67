from .component import Component
from ..io.reader import ChunkReader
from ..utils import PlaceHolder

class ChunkReaderComponent(Component):
    def __init__(self, *args, **kwargs):
        """
        Initialize a PhaseRetrieval component object.
        Please see `nabu.app.component.Component` for documentation details.
        """
        super().__init__(*args, **kwargs)
        self.backend = "numpy"
        self.exec_by_groups = False
        self._init_chunk_reader()
        # A "data provider" component must always have a ".data" field referring
        # to the data which will be used by further processing components.
        self.data = self.chunk_reader.files_data

    def _get_subregion(self, accept_placeholder=False):
        subregion = self.options["sub_region"]
        if isinstance(subregion, PlaceHolder):
            if not(accept_placeholder):
                raise ValueError("sub_region option is not specified. You must provide it in the form (start_x, end_x, start_y, end_y). Set to None to read all the volume.")
            else:
                subregion = None
        self._sub_region = subregion

    def _init_chunk_reader(self):
        self._get_subregion()
        # By default, convert to float for further processing
        convert_float = self.options.get("convert_float", True)
        self.chunk_reader = ChunkReader(
            self.options["files"],
            sub_region=self._sub_region,
            pre_allocate=True,
            convert_float=convert_float,
            binning=self.options["binning"]
        )
        self._set_shape(self.chunk_reader.chunk_shape, None)


    @property
    def sub_region(self):
        return self.chunk_reader.sub_region


    def execute(self, overwrite=False):
        self.logger.info("Start reading data")
        self.logger.debug("Region = %s" % str(self.sub_region))
        self.chunk_reader.load_files(overwrite=overwrite)
        self.logger.info("Done reading data")
        return self.chunk_reader.files_data
