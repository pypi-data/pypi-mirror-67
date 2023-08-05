from .component import Component
from ..cuda.utils import __has_pycuda__, replace_array_memory
from ..opencl.utils import __has_pyopencl__
from ..preproc.sinogram import SinoProcessing
if __has_pycuda__:
    from ..preproc.sinogram_cuda import CudaSinoProcessing

class SinoBuilderComponent(Component):
    def __init__(self, *args, **kwargs):
        """
        Initialize a sinogram builder component.
        """
        super().__init__(*args, **kwargs)

        # If data does not fit into device memory, then the execute() method
        # will be called on a numpy array.
        # In this case, it makes little sense to use a "device backend"
        use_cuda = __has_pycuda__ and not(self.exec_by_groups)
        use_opencl = __has_pyopencl__ and not(self.exec_by_groups)
        self._get_options()
        # Implementation not complete !
        use_cuda *= not(self.halftomo)
        use_opencl = False
        #
        self.get_backend({
            "cuda": (use_cuda, "Processing data by sub-chunks"),
            "opencl": (use_opencl, "Processing data by sub-chunks"),
        })
        self._init_sinobuilder()


    def _get_options(self):
        self.rot_center = self.options["rotation_axis_position"]
        self.axis_correction = self.options["axis_correction"]
        self.halftomo = self.options["enable_halftomo"]


    def _init_sinobuilder(self):
        if self.exec_by_groups:
            radios_shape = self.device_array.shape
        else:
            radios_shape = self.shape
        self.radios_shape = radios_shape
        self.rot_center = self.rot_center

        sinoproc_cls = SinoProcessing
        sinoproc_kwargs = {
            "radios_shape": self.radios_shape,
            "rot_center": self.rot_center,
            "halftomo": self.halftomo,
        }
        if self.backend == "cuda":
            sinoproc_cls = CudaSinoProcessing
            sinoproc_kwargs["cuda_options"] = None # TODO
        self.sinoprocessing = sinoproc_cls(**sinoproc_kwargs)


    def execute_onegroup(self, radios):
        return self.sinoprocessing.radios_to_sinos(radios, copy=True)

