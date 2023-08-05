import numpy as np
from typing import Union, Any
from ..preproc.ccd import CCDProcessing, CCDCorrection, FlatField
from ..cuda.kernel import CudaKernel
from ..cuda.medfilt import MedianFilter
from ..utils import get_cuda_srcfile, updiv
import pycuda.gpuarray as garray


class CudaFlatField(FlatField):
    def __init__(
        self,
        radios_shape: tuple,
        flats: dict,
        darks: dict,
        radios_indices=None,
        interpolation: str = "linear",
        cuda_options: Union[dict, None] = None,
        **chunk_reader_kwargs
    ):
        """
        Initialize a flat-field normalization CUDA process.
        Please read the documentation of nabu.preproc.ccd.FlatField for help
        on the parameters.
        """
        super().__init__(
            radios_shape,
            flats,
            darks,
            radios_indices=radios_indices,
            interpolation=interpolation,
            **chunk_reader_kwargs
        )
        self._set_cuda_options(cuda_options)
        self._init_cuda_kernels()
        self._load_flats_and_darks_on_gpu()

    def _set_cuda_options(self, user_cuda_options):
        self.cuda_options = {"device_id": None, "ctx": None, "cleanup_at_exit": None}
        if user_cuda_options is None:
            user_cuda_options = {}
        self.cuda_options.update(user_cuda_options)

    def _init_cuda_kernels(self):
        # TODO
        if self.interpolation != "linear":
            raise ValueError(
                "Interpolation other than linar is not yet implemented in the cuda back-end"
            )
        self._cuda_fname = get_cuda_srcfile("flatfield.cu")
        self.cuda_kernel = CudaKernel(
            "flatfield_normalization",
            self._cuda_fname,
            signature="PPPiiiPPP",
            options=[
                "-DN_FLATS=%d" % self.n_flats,
                "-DN_DARKS=%d" % self.n_darks,
            ]
        )
        self._nx = np.int32(self.shape[1])
        self._ny = np.int32(self.shape[0])

    def _load_flats_and_darks_on_gpu(self):
        # Flats
        self.d_flats = garray.zeros((self.n_flats,) + self.shape, np.float32)
        # ~ for i, flat_arr in enumerate(self.flats_arr.values()):
        for i, flat_idx in enumerate(self._sorted_flat_indices):
            self.d_flats[i].set(np.ascontiguousarray(self.flats_arr[flat_idx], dtype=np.float32))
        self.d_flats_indices = garray.to_gpu(
            np.array(self._sorted_flat_indices, dtype=np.int32)
        )
        # Darks
        self.d_darks = garray.zeros((self.n_darks,) + self.shape, np.float32)
        # ~ for i, dark_arr in enumerate(self.darks_arr.values()):
        for i, dark_idx in enumerate(self._sorted_dark_indices):
            self.d_darks[i].set(np.ascontiguousarray(self.darks_arr[dark_idx], dtype=np.float32))
        self.d_darks_indices = garray.to_gpu(
            np.array(self._sorted_dark_indices, dtype=np.int32)
        )
        # Radios indices
        self.d_radios_indices = garray.to_gpu(self.radios_indices)


    def normalize_radios(self, radios):
        """
        Apply a flat-field correction, with the current parameters, to a stack
        of radios.

        Parameters
        -----------
        radios_shape: `pycuda.gpuarray.GPUArray`
            Radios chunk.
        """
        if not(isinstance(radios, garray.GPUArray)):
            raise ValueError("Expected a pycuda.gpuarray (got %s)" % str(type(radios)))
        if radios.dtype != np.float32:
            raise ValueError("radios must be in float32 dtype (got %s)" % str(radios.dtype))
        if radios.shape != self.radios_shape:
            raise ValueError("Expected radios shape = %s but got %s" % (str(self.radios_shape), str(radios.shape)))
        self.cuda_kernel(
            radios,
            self.d_flats,
            self.d_darks,
            self._nx,
            self._ny,
            np.int32(self.n_radios),
            self.d_flats_indices,
            self.d_darks_indices,
            self.d_radios_indices
        )
        return radios


class CudaCCDCorrection(CCDCorrection):
    def __init__(
        self,
        radios_shape: tuple,
        correction_type: str = "median_clip",
        median_clip_thresh: float = 0.1,
        cuda_options: Union[dict, None] = None,
    ):
        """
        Initialize a CudaCCDCorrection instance.
        Please refer to the documentation of CCDCorrection.
        """
        super().__init__(
            radios_shape,
            correction_type=correction_type,
            median_clip_thresh=median_clip_thresh,
        )
        self._set_cuda_options(cuda_options)
        self.cuda_median_filter = None
        if correction_type == "median_clip":
            self.cuda_median_filter = MedianFilter(
                (self.n_radios,) + self.shape,
                footprint=(3, 3),
                mode="reflect",
                threshold=median_clip_thresh,
                device_id=self.cuda_options["device_id"],
                ctx=self.cuda_options["ctx"],
                cleanup_at_exit=self.cuda_options["cleanup_at_exit"],
            )

    def _set_cuda_options(self, user_cuda_options):
        self.cuda_options = {"device_id": None, "ctx": None, "cleanup_at_exit": None}
        if user_cuda_options is None:
            user_cuda_options = {}
        self.cuda_options.update(user_cuda_options)


    def median_clip_correction(self, radios, output=None):
        """
        Compute the median clip correction on one image.
        NOTE: this processing cannot be done in-place.

        Parameters
        ----------
        radios: pycuda.gpuarray
            Radios chunk.
        output: pycuda.gpuarray, optional
            Output data.
        """
        assert radios.ndim == 3
        assert radios.shape == self.radios_shape
        return self.cuda_median_filter.medfilt2(radios, output=output)



class CudaLog(CCDProcessing):
    """
    Helper class to take -log(radios)
    """
    def __init__(self, radios_shape, clip_min=None, clip_max=None):
        super().__init__(radios_shape)
        self.clip_min = clip_min
        self.clip_max = clip_max
        self._init_kernels()

    def _init_kernels(self):
        self._do_clip_min = int(self.clip_min is not None)
        self._do_clip_max = int(self.clip_max is not None)
        self.clip_min = np.float32(self.clip_min or 0)
        self.clip_max = np.float32(self.clip_max or 1)
        self._nlog_srcfile = get_cuda_srcfile("ElementOp.cu")
        nz, ny, nx = self.radios_shape
        self._nx = np.int32(nx)
        self._ny = np.int32(ny)
        self._nz = np.int32(nz)
        self._nthreadsperblock = (16, 16, 4) # TODO tune ?
        self._nblocks = tuple([updiv(n, p) for n, p in zip([nx, ny, nz], self._nthreadsperblock)])

        self.nlog_kernel = CudaKernel(
            "nlog",
            filename=self._nlog_srcfile,
            signature="Piiiff",
            options=[
                "-DDO_CLIP_MIN=%d" % self._do_clip_min,
                "-DDO_CLIP_MAX=%d" % self._do_clip_max,
            ]
        )

    def take_logarithm(self, radios, clip_min=None, clip_max=None):
        """
        Take the negative logarithm of a radios chunk.

        Parameters
        -----------
        radios: `pycuda.gpuarray.GPUArray`
            Radios chunk
            If not provided, a new GPU array is created.
        clip_min: float, optional
            Before taking the logarithm, the values are clipped to this minimum.
        clip_max: float, optional
            Before taking the logarithm, the values are clipped to this maximum.
        """
        clip_min = clip_min or self.clip_min
        clip_max = clip_max or self.clip_max
        self.nlog_kernel(
            radios,
            self._nx,
            self._ny,
            self._nz,
            clip_min,
            clip_max,
            grid=self._nblocks,
            block=self._nthreadsperblock
        )
        return radios

