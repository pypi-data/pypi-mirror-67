import pycuda.gpuarray as garray
from ..cuda.convolution import Convolution
from pycuda.elementwise import ElementwiseKernel
from ..cuda.processing import CudaProcessing
from .unsharp import UnsharpMask

class CudaUnsharpMask(UnsharpMask, CudaProcessing):
    def __init__(self, shape, sigma, coeff, mode="reflect", method="gaussian",
                 ctx=None, device_id=None, cleanup_at_exit=True):
        """
        NB: For now, this class is designed to use the lowest amount of GPU memory
        as possible. Therefore, the input and output image/volumes are assumed
        to be already on device.
        """
        CudaProcessing.__init__(
            self, device_id=device_id, ctx=ctx, cleanup_at_exit=cleanup_at_exit
        )
        UnsharpMask.__init__(self, shape, sigma, coeff, mode=mode, method=method)
        self._init_convolution()
        self._init_mad_kernel()

    def _init_convolution(self):
        self.convolution = Convolution(
            self.shape,
            self._gaussian_kernel,
            mode=self.mode,
            extra_options={ # Use the lowest amount of memory
                "allocate_input_array": False,
                "allocate_output_array": False,
                "allocate_tmp_array": True,
            }
        )

    def _init_mad_kernel(self):
        # garray.GPUArray.mul_add is out of place...
        self.mad_kernel = ElementwiseKernel(
            "float* array, float fac, float* other, float otherfac",
            "array[i] = fac * array[i] + otherfac * other[i]",
            name="mul_add"
        )

    def unsharp(self, image, output):
        # For now image and output are assumed to be already allocated on device
        assert isinstance(image, garray.GPUArray)
        assert isinstance(output, garray.GPUArray)
        self.convolution(image, output=output)
        if self.method == "gaussian":
            self.mad_kernel(output, -self.coeff, image, 1. + self.coeff)
        else: # log
            self.mad_kernel(output, self.coeff, image, 1.)
        return output
