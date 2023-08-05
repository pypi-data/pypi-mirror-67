import numpy as np
from math import floor, ceil
from .component import Component
from ..cuda.utils import __has_pycuda__
from ..opencl.utils import __has_pyopencl__

if __has_pycuda__:
    import pycuda.gpuarray as garray
    from silx.math.fft.cufft import __have_cufft__
    from ..reconstruction.fbp import Backprojector
if __has_pyopencl__:
    import pyopencl.array as parray


class FBPComponent(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_backend({
            "cuda": (__has_pycuda__ and __have_cufft__, "pycuda and cufft must be installed"),
            "opencl": (__has_pyopencl__, "pyopencl must be installed"),
            "numpy": (False, "numpy FBP is not implemented")
        })
        self._get_reconstruction_options()
        self._init_fbp()


    def _get_reconstruction_roi(self):
        Y, X = self.options["radio_dims_y_x"]
        opts = self.options
        x_s, x_e = opts["start_x"], opts["end_x"]+1
        y_s, y_e = opts["start_y"], opts["end_y"]+1
        z_s, z_e = opts["start_z"], opts["end_z"]+1
        self._rec_roi = (x_s, x_e, y_s, y_e, z_s, z_e)
        self.rec_shape = (y_s - y_e, x_s - x_e)


    def _get_reconstruction_options(self):
        self.sino_shape = self.shape[1:]
        self.n_z = self.shape[0]
        self._get_reconstruction_roi()


    def _init_fbp(self):
        self._check_device_buffer()
        # For now we are using only 2D backprojector
        self._is_3D_backprojector = False
        rec_cls_args = [
            self.sino_shape,
        ]
        rec_cls_kwargs = {
            "slice_roi": self._rec_roi[:-2],
            "angles": self.options["angles"],
            "rot_center": self.options["rotation_axis_position"],
            "filter_name": self.options["fbp_filter_type"],
            "scale_factor": 1./self.options["pixel_size_cm"],
            "extra_options": {
                "padding_mode": self.options["padding_type"],
                "axis_correction": self.options["axis_correction"],
            },
            "cuda_options": {}, # TODO
        }
        if self.backend == "cuda":
            rec_cls = Backprojector
        else: # opencl
            # This import has to be done here since silx.opencl creates opencl
            # contexts all over the place in some cases, incompatible with cuda
            # see https://github.com/silx-kit/silx/issues/2703
            from ..reconstruction.fbp_opencl import Backprojector as CLBackprojector
            rec_cls = CLBackprojector
        self.backprojector = rec_cls(*rec_cls_args, **rec_cls_kwargs)
        self.logger.debug("FBP initialized with backend %s" % self.backend)
        # TODO take "fbp_filter_type = 'none' into account
        # For now we use this ugly hack
        if self.options["fbp_filter_type"] is None:
            self.backprojector.fbp = self.backprojector.backproj


    def execute_onegroup(self, sinos, output=None):
        # sinos is a device array
        n_z = sinos.shape[0]
        if output is None:
            # Not really good to return a numpy array when backend is cuda
            output = np.zeros((n_z, ) + self.rec_shape, "f")
            for i in range(n_z):
                output[i] = self.backprojector.fbp(sinos[i])
        else:
            for i in range(n_z):
                output[i] = self.backprojector.fbp(sinos[i], output=output[i])
        return output

