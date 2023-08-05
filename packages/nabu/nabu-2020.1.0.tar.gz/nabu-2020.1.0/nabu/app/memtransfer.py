from ..utils import is_device_backend, array_tostring
from ..cuda.utils import __has_pycuda__, copy_big_gpuarray
from ..opencl.utils import __has_pyopencl__
from .component import Component
from .logger import LoggerOrPrint
if __has_pycuda__:
    import pycuda.gpuarray as garray
if __has_pyopencl__:
    import pyopencl.array as parray


# This class does not inherit from Component as it does not need all the
# backend/options/data stuff.
# For now it is limited to simple transfers, i.e arrays of the same shape.
class MemoryTransferComponent:
    def __init__(self, src_backend, dst_backend, logger=None):
        self.name = "Memory transfer"
        self.logger = LoggerOrPrint(logger)
        if is_device_backend(src_backend) and is_device_backend(dst_backend):
            if src_backend != dst_backend:
                # intermediate step on numpy array ?
                raise NotImplementedError(
                    "Transfers between Cuda and OpenCL contexts are not supported"
                )
            # if src_backend == dst_backend, it makes no sense to do a copy
            # when shapes are the same
        self.backends = [src_backend, dst_backend]
        self.name += ": %s_to_%s" % (src_backend, dst_backend)

        self.copy_function_name = "_cpy_%s_to_%s" % (src_backend, dst_backend)
        self.copy_function = getattr(self, self.copy_function_name)

        self.shape = None # not known at init
        self.output_shape = None # not known at init


    @property
    def backend(self):
        if "cuda" in self.backends:
            return "cuda"
        if "opencl" in self.backends:
            return "opencl"
        return "numpy"


    def _cpy_cuda_to_cuda(self, dst, src):
        # D2D copies are relying on 32 bits indices, thus failing on too big arrays
        copy_big_gpuarray(dst, src)

    def _cpy_cuda_to_numpy(self, dst, src):
        # It looks like host[:] = device[:] does not work as expected
        # ~ src.get(ary=dst)
        copy_big_gpuarray(dst, src)

    def _cpy_numpy_to_cuda(self, dst, src):
        dst.set(src)

    def _cpy_opencl_to_opencl(self, dst, src):
        # not sure if clEnqueueCopy suffers from the same 32bits issue as Cuda
        dst[:] = src[:]

    def _cpy_opencl_to_numpy(self, dst, src):
        src.get(ary=dst)

    def _cpy_numpy_to_opencl(self, dst, src):
        dst.set(src)

    def _cpy_numpy_to_numpy(self, dst, src):
        # Makes little sense in our context
        dst[:] = src[:]

    def _cpy_opencl_to_cuda(self, dst, src):
        raise NotImplementedError()

    def _cpy_cuda_to_opencl(self, dst, src):
        raise NotImplementedError()


    # Overwrite parent class
    def execute(self, src, dst):
        self.logger.info(
            "memcpy %s -> %s"
            % (array_tostring(src), array_tostring(dst))
        )
        self.copy_function(dst, src)
        self.logger.debug("end memcpy")
        return dst


