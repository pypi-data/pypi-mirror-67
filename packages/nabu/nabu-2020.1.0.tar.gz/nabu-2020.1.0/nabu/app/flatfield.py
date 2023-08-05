from .component import Component
from ..cuda.utils import __has_pycuda__
from ..preproc.ccd import FlatField
from ..preproc.double_flat_field import DoubleFlatField

if __has_pycuda__:
    from ..preproc.ccd_cuda import CudaFlatField
    import pycuda.gpuarray as garray

# CudaFlatField : can take 3D arrays
#   normalize_radios: in-place
class FlatFieldComponent(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_backend({
            "cuda": (__has_pycuda__, "pycuda must be installed"),
            "opencl": (False, "not implemented yet")
        })
        self.dataset_infos = self.options["dataset_infos"]
        self._init_flatfield()

    def _init_flatfield(self):
        flatfield_cls = FlatField
        flatfield_args = [
            self.processing_shape,
            self.dataset_infos.flats,
            self.dataset_infos.darks,
        ]
        flatfield_kwargs = {
            "radios_indices": sorted(self.dataset_infos.projections.keys()),
            "interpolation": "linear",
            "sub_region": self.options["sub_region"],
            "binning": self.options["binning"],
            "convert_float": True, #
        }
        if self.backend == "cuda":
            flatfield_cls = CudaFlatField
            flatfield_kwargs["cuda_options"] = {} # TODO

        self.flatfield = flatfield_cls(*flatfield_args, **flatfield_kwargs)
        self.logger.debug("Flat-field initialized with backend %s" % self.backend)


    def execute_onegroup(self, radios):
        res = self.flatfield.normalize_radios(radios)
        return res # radios





class DoubleFlatFieldComponent(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_backend({
            "cuda": (False, "not implemented yet"),
            "opencl": (False, "not implemented yet")
        })
        self._init_dff()


    def _init_dff(self):
        dff_cls = DoubleFlatField
        dff_args = [
            self.processing_shape,
        ]
        # In this context, it seems that it is not useful to dump the double flatfield
        # computation result in a file, because each "worker" is responsible for
        # its own radios chunk
        dff_kwargs = {
            "result_url": None,
            "input_is_mlog": False,
            "output_is_mlog": False,
            "average_is_on_log": False,
            "sigma_filter": self.options["sigma"],
        }

        self.doubleflatfield = dff_cls(*dff_args, **dff_kwargs)
        self.logger.debug("Double Flat-field initialized with backend %s" % self.backend)


    def execute_onegroup(self, radios):
        res = self.doubleflatfield.apply_double_flatfield(radios)
        return res # radios

