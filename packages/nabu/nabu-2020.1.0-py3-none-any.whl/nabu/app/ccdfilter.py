from math import ceil
from ..utils import is_device_backend
from ..cuda.utils import __has_pycuda__
from ..preproc.ccd import CCDCorrection
from .component import Component

if __has_pycuda__:
    from ..preproc.ccd_cuda import CudaCCDCorrection
    import pycuda.gpuarray as garray


# CudaCCDCorrection
#   cuda.medfilt.MedianFilter : can take 3D arrays, not inplace
#     MedianFilter.medfilt2 : if output not provided, is allocated
# approach:
#   - If "low memory": process image by image  radios[i] -> d_output -> radios[i]
#     where d_output is a 2D image.
#       pros: almost no memory footprint, cons: many small mem copies
#   - Otherwise: medfilt2(images, output=d_output) where d_output is a volume
#     then "swap" images and d_output by returning d_output.
#       pros: very efficient ; cons: memory usage

class CCDFilterComponent(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_backend({
            "cuda": (__has_pycuda__, "pycuda must be installed"),
            "opencl": (False, "not implemented yet")
        })
        self._init_ccd_filter()


    def _init_ccd_filter(self):
        self.radios_shape = self.shape
        ccdfilter_cls = CCDCorrection
        ccdfilter_cls_args = [radios_shape]
        ccdfilter_cls_kwargs = {
            "correction_type": self.options["type"],
            "median_clip_thresh": self.options["median_clip_thresh"]
        }
        if self.backend == "cuda":
            ccdfilter_cls = CudaCCDCorrection
            if self.exec_by_groups:
                chunk_shape = self.device_array.shape
            else:
                chunk_shape = radios_shape
            ccdfilter_cls_args = [chunk_shape]
            # Process image by image. It entails many small memcpy2D, but avoids
            # allocating twice the data volume.
            chunk_shape = (1, ) + chunk_shape[1:]
            ccdfilter_cls_kwargs["cuda_options"] = {} # TODO
        self.ccd_filter = ccdfilter_cls(*ccdfilter_cls_args, **ccdfilter_cls_kwargs)
        # With the cuda/opencl implementation, median filter cannot be done in-place
        if is_device_backend(self.backend):
            self._check_device_buffer(check_3D=True)
        self.logger.debug("CCD Filter initialized with backend %s" % self.backend)


    def _execute_numpy(self, radios):
        return self.ccd_filter.median_clip_correction(radios, inplace=True)


    def _execute_cuda(self, d_radios):
        d_output = self.device_buffer
        if not(d_output.ndim == 2):
            for i in range(d_radios.shape[0]):
                self.ccd_filter.median_clip_correction(d_radios[i], output=d_output)
                d_radios[i, :, :] = d_output[:, :] # small memcpy D2D
            return d_radios
        else: # 3
            return self.ccd_filter.median_clip_correction(
                d_radios,
                output=d_output
            ) # will return d_output = self.device_buffer


    def execute_onegroup(self, radios):
        if self.backend == "cuda":
            return self._execute_cuda(radios)
        else: # numpy
            return self._execute_numpy(radios)

