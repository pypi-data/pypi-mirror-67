from ..utils import get_2D_3D_shape
from ..cuda.utils import __has_pycuda__
from ..preproc.phase import PaganinPhaseRetrieval
from .component import Component

if __has_pycuda__:
    from ..preproc.phase_cuda import CudaPaganinPhaseRetrieval, __have_cufft__

#
#  CudaPaganinPhaseRetrieval(PaganinPhaseRetrieval):  only 2D
#    apply_filter: can be done in-place or out-of-place (padded FFT)
#
class PhaseRetrievalComponent(Component):
    """
    Phase retrieval application component.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_backend({
            "cuda": (__has_pycuda__ and __have_cufft__, "pycuda and scikit-cuda must be installed"),
            "opencl": (False, "not implemented yet")
        })
        self._init_phase_retrieval()


    def _init_phase_retrieval(self):
        if (self.options["energy_kev"] == 0):
            raise ValueError("Energy is zero. Cannot retrieve phase.")
        phaseretr_cls = PaganinPhaseRetrieval
        phaseretr_args = [self.shape[1:]] # 2D
        phaseretr_kwargs = {
            "energy": self.options["energy_kev"],
            "distance": self.options["distance_cm"],
            "delta_beta": self.options["delta_beta"],
            "pixel_size": self.options["pixel_size_microns"],
            "padding": self.options["padding_type"],
            "margin": None,  # TODO
            "use_R2C": True,
        }
        if self.backend == "cuda":
            phaseretr_cls = CudaPaganinPhaseRetrieval
            phaseretr_kwargs.pop("use_R2C")
            phaseretr_kwargs["cuda_options"] = {} # TODO

        self.phase_retrieval = phaseretr_cls(
            *phaseretr_args,
            **phaseretr_kwargs
        )
        self.logger.debug(
            "Phase retrieval initialized with backend %s" % self.backend
        )


    def execute_onegroup(self, radios):
        """
        Perform a phase retrieval on a chunk of radios.
        """
        n_a, n_z, n_x = get_2D_3D_shape(radios.shape)
        for i in range(n_a):
            self.phase_retrieval.apply_filter(
                radios[i], output=radios[i]
            )
        # ~ self.logger.debug("Done phase retrieval")
        return radios
