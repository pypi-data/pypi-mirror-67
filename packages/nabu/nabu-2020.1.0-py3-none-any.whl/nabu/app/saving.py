from os import path
from math import ceil
import numpy as np
from ..utils import check_supported
from ..io.writer import Writers
from .component import Component

class SavingComponent(Component):

    available_formats = list(Writers.keys())
    _nx_infos_keys = ["process_name", "processing_index", "config"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.backend = "numpy"
        self.exec_by_groups = False #
        self.nx_infos = self.options["nx_infos"]
        self._get_output_preferences()
        self._saved = False


    def _get_output_preferences(self):
        opts = self.options
        self.file_format = opts["file_format"]
        check_supported(
            self.file_format,
            self.available_formats,
            "output file format"
        )
        self.fname = path.join(opts["location"], opts["file_prefix"] + "." + opts["file_format"])
        if path.exists(self.fname):
            err = "File already exists: %s" % self.fname
            if self.options["overwrite"]:
                if self.options.get("warn_overwrite", True):
                    self.logger.warning(err + ". It will be overwritten on user request")
                    self.options["warn_overwrite"] = False
            else:
                self.logger.fatal(err)
                raise ValueError(err)
        if self.file_format.lower() in ["h5", "hdf5", "nx", "nexus"]:
            self._check_nx_infos()

        writer_cls = Writers[self.file_format]
        writer_args = [self.fname]
        writer_kwargs = {}

        self._writer_exec_args = []
        self._writer_exec_kwargs = {}
        if self.nx_infos is not None:
            writer_kwargs["entry"] = self.nx_infos["entry"]
            writer_kwargs["filemode"] = "w" if self.options["overwrite"] else "a"
            self._writer_exec_args.append(self.nx_infos["process_name"])
            self._writer_exec_kwargs["processing_index"] = self.nx_infos["processing_index"]
            self._writer_exec_kwargs["config"] = self.nx_infos["config"]
        self.writer = writer_cls(*writer_args, **writer_kwargs)


    def _check_nx_infos(self):
        nx_infos = self.nx_infos
        if nx_infos is None:
            nx_infos = {}
        for key_name in self._nx_infos_keys:
            if key_name not in nx_infos:
                raise ValueError("Expected nx_info to have the key %s" % key_name)


    def execute(self, arr, *args, **kwargs):
        self.logger.info("Saving to %s" % self.fname)
        self.writer.write(arr, *self._writer_exec_args, **self._writer_exec_kwargs)
        self.logger.debug("Data saved")
        self._saved = True
        return arr
