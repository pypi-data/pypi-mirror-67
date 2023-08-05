import numpy as np
import pycuda.gpuarray as garray
from .sinogram import SinoProcessing
from ..cuda.processing import CudaProcessing

class CudaSinoProcessing(SinoProcessing, CudaProcessing):
    def __init__(self, sinos_shape=None, radios_shape=None, rot_center=None, halftomo=False, vertical_shifts=None, cuda_options=None):
        """
        Initialize a CudaSinoProcessing instance.
        Please see the documentation of nabu.preproc.sinogram.SinoProcessing
        and nabu.cuda.processing.CudaProcessing.
        """
        SinoProcessing.__init__(
            self, sinos_shape=sinos_shape, radios_shape=radios_shape, rot_center=rot_center,
            halftomo=halftomo, vertical_shifts=vertical_shifts
        )
        if cuda_options is None:
            cuda_options = {}
        CudaProcessing.__init__(self, **cuda_options)


    # Overwrite parent method
    def _radios_to_sinos_simple(self, radios, output, copy=False):
        if not(copy) and output is None:
            return radios.transpose(axes=(1, 0, 2)) # view
        if output is None: # copy and output is None
            na, nz, nx = radios.shape
            output = garray.zeros((nz, na, nx), "f")
        # not(copy) and output is not None
        for i in range(output.shape[0]):
            output[i, :, :] = radios[:, i, :]
        return output


