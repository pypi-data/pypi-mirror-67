"""
map-like operations on arrays
"""
from ..utils import is_device_backend
from ..cuda.utils import __has_pycuda__
from ..preproc.ccd import CCDProcessing
from .component import Component

if __has_pycuda__:
    from ..preproc.ccd_cuda import CudaLog

#
# CudaLog: 3D, in-place.
#
class NegativeLogComponent(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_backend({
            "cuda": (__has_pycuda__, "pycuda must be installed"),
            "opencl": (False, "not implemented yet"),
        })
        self._init_minuslog()


    def _init_minuslog(self):
        mlog_cls = CCDProcessing
        if self.exec_by_groups:
            radios_shape = self.device_array.shape
        else:
            radios_shape = self.shape
        mlog_cls_args = [radios_shape]
        mlog_cls_kwargs = {}
        if self.backend == "cuda":
            mlog_cls = CudaLog
        self.minuslog = mlog_cls(*mlog_cls_args, **mlog_cls_kwargs)
        if is_device_backend(self.backend):
            self._check_device_buffer()
        self.logger.debug("-log() initialized with backend %s" % self.backend)


    def execute_onegroup(self, radios):
        self.minuslog.take_logarithm(
            radios,
            clip_min=self.options["log_min_clip"],
            clip_max=self.options["log_max_clip"]
        )
        # ~ self.logger.info("Done taking -log()")
        return radios

