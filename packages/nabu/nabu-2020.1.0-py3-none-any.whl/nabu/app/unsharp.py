from .component import Component
from ..cuda.utils import __has_pycuda__
from ..opencl.utils import __has_pyopencl__
from ..misc.unsharp import UnsharpMask

if __has_pycuda__:
    import pycuda.gpuarray as garray
    from ..misc.unsharp_cuda import CudaUnsharpMask
    from ..cuda.utils import copy_big_gpuarray
if __has_pyopencl__:
    import pyopencl.array as parray


#
# CudaUnsharpMask(UnsharpMask): can take 3D array
#   unsharp: cannot be done in-place, assumes output allocated
# approach: always use the "low memory" approach: use on 2D arrays only
#   if d_output has the same shape as d_radios: make only one big memcpy
#     or swap images...
#   otherwise: many small memcpy
#
class UnsharpMaskComponent(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_backend({
            "cuda": (__has_pycuda__, "pycuda must be installed"),
            "opencl": (__has_pycuda__, "pyopencl must be installed"),
        })
        self._init_unsharpmask()


    def _init_unsharpmask(self):
        unsharp_cls = UnsharpMask
        unsharp_cls_args = [
            self.shape[1:],
            self.options["unsharp_sigma"],
            self.options["unsharp_coeff"]
        ]
        unsharp_cls_kwargs = {
            "mode": "reflect",
            "method": "gaussian",
        }
        if self.backend == "cuda":
            unsharp_cls = CudaUnsharpMask
            cuda_options = {} # TODO
            unsharp_cls_kwargs.update(cuda_options)
        if self.backend == "opencl":
            # This import has to be done here since silx.opencl creates opencl
            # contexts all over the place in some cases, incompatible with cuda
            # see https://github.com/silx-kit/silx/issues/2703
            from ..misc.unsharp_opencl import OpenclUnsharpMask
            unsharp_cls = OpenclUnsharpMask
            opencl_options = {} # TODO
            unsharp_cls_kwargs.update(opencl_options)
        self.unsharp_mask = unsharp_cls(*unsharp_cls_args, **unsharp_cls_kwargs)
        if self.backend in ["cuda", "opencl"]:
            self._check_device_buffer(check_3D=True)
        self.logger.debug("Unsharp mask initialized with backend %s" % self.backend)


    def _execute_numpy(self, radios):
        for i in range(radios.shape[0]):
            radios[i] = self.unsharp_mask.unsharp(radio)
        return radios


    def _execute_cuda_opencl(self, radios):
        # radios is a 3D device array.
        # However "unsharp" cannot be done in-place
        # (especially due to the tmp array used by convolution)
        # so we process image by image.
        n_a = radios.shape[0]
        d_output = self.device_buffer
        if d_output.ndim == 2:
            for i in range(n_a):
                self.unsharp_mask.unsharp(radios[i], d_output)
                radios[i, :, :] = d_output[:, :] # "small" memcpy D2D
            return radios
        else: # 3
            for i in range(n_a):
                self.unsharp_mask.unsharp(radios[i], d_output[i])
            return d_output # no memcpy


    def execute_onegroup(self, radios):
        if self.backend in ["cuda", "opencl"]:
            res = self._execute_cuda_opencl(radios)
        else:
            res = self._execute_numpy(radios)
        return res


