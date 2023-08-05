from os import linesep
from math import ceil
from silx.utils.enum import Enum
from ..utils import ArrayPlaceHolder, get_2D_3D_shape, array_tostring, check_supported
from .logger import LoggerOrPrint


class Backend:
    def __init__(self, name=None, available=None, priority=None):
        self.name = name
        self.available = available
        self.priority = priority

    def __repr__(self):
        return "Backend(name=%s, available=%s, priority=%s)" % (self.name, self.available, self.priority)



class Component:
    """
    Application (or processing pipeline) component.

    This class has several purposes:
      -  Wrap Processing-like classes (`FlatField`, `PhaseRetrieval`, etc)
         in a wider context (the processing pipeline), by translating the user options
         to final Processing parameters
      - Handle the implementation differences in backends (ex. FlatField and CudaFlatField)
      - Handle inputs/outputs arrays, ensure that resources like memory are
        efficiently used
      - Ensure that the processing is done in-place when possible

    A component basically processes a chunk of images, so it takes a 3D array
    as an input, and outputs a 3D array. The processing is done in-place, so
    usually the output array has the same as the input array.

    A component is primarily characterized by: its name, the input array shape,
    the output array shape, the instantiation options, and the execution options.
    Once instantiated, it is called with its `execute()` method.


    Parameters
    -----------
    name: str
        Name of the component.
    shape: tuple
        Shape of the input data (ex. the arrays passed to `execute()` method).
    options: dict
        Dictionary of processing options. Keys and values depend on the individual component.
    output_shape: tuple, optional
        Shape of the output data. Usually the same as `shape`.
    device_array: `pycuda.gpuarray.GPUArray` or `pyopencl.array.Array`, optional
        This option is used when the component uses the cuda/opencl backend
        AND the images chunk is too big to be processed directly on device memory.
        Otherwise, device arrays should be passed directly to the `execute()` method.
        If this option is not `None`, it means that the images chunk is too big to
        fit in memory ; the array passed to the `execute()` method is a `numpy.ndarray`
        (holding the images chunk) and `device_array` serves as a buffer for processing
        parts of the chunk. Please see Notes below.
    device_buffer: `pycuda.gpuarray.GPUArray` or `pyopencl.array.Array`, optional
        This is a device array serving when the processing cannot be done in-place,
        when using the Cuda/opencl backend.
        Note that this array can be provided while `device_array` is not provided:
        it serves as temporary array depending on the component implementation.
        Its dimensions are not necessarily the same as `device_array` or `shape`.
        The required dimensions depend on the specific component.
    logger: `Logger`, optional
        logging object
    preferred_backend: str, optional
        Preferred backend. Can be "auto", "cuda", "opencl" or "numpy".
        The component backend is chosen according to a priority mechanism.
        With this option, you can set the highest priority to a given backend.
        Note that depending on the component, the preferable backend might not be implemented.


    Important
    ----------
    There are two important assumptions for components:
       - The first argument `execute()` is an array.
       - The ONLY output of `execute()` is an array

    Notes
    ------
    When using Cuda/Opencl, if the images chunk is too big to fit in device memory,
    then the chunk can be processed by "sub-chunks". To do so, the option `device_array`
    has to be used.
    To sum up, when using the Cuda/Opencl backend:
      - If all the images chunk fits in device memory: `device_array` is not set, and
        the device array containing the images chunk is passed directly to
        the component `execute()` method.
      - Otherwise, if the images chunk does not fit in device memory, then `device_array`
        is set. The first argument of the `execute()` is a numpy array containing
        the images chunk, which will be cut into parts that are transferred to
        `device_array` for processing.

    The option `device_buffer` is almost always provided when using the Cuda/Opencl
    backend ; except when the processing can be done entirely in-place.
    """


    def __init__(
        self, name, shape, options,
        output_shape=None,
        device_array=None, device_buffer=None,
        logger=None, preferred_backend="auto",
    ):
        """
        Initialize a `Component` object.
        This class should not be called directly.
        """
        self.name = name
        self._set_shape(shape, output_shape)
        self.processing_options = options
        self.options = options # shorthand
        self.logger = LoggerOrPrint(logger)
        self._set_device_array(device_array)
        self._set_device_buffer(device_buffer)
        self.backends = {
            "cuda": Backend(name="cuda", available=True, priority=2),
            "opencl": Backend(name="opencl", available=True, priority=1),
            "numpy": Backend(name="numpy", available=True, priority=0),
        }
        self.preferred_backend = preferred_backend
        self.backend = None # not set


    def _set_shape(self, shape, output_shape):
        self._shape = get_2D_3D_shape(shape)
        if output_shape is None:
            output_shape = self._shape
        self._output_shape = output_shape
        self.processing_shape = self._shape


    @property
    def shape(self):
        """
        Get the shape of the images chunk processed by this component.
        """
        return self._shape


    @property
    def output_shape(self):
        """
        Get the shape of the output array after calling the execute() method.
        """
        return self._output_shape


    def _set_device_array(self, device_array):
        self.device_array = device_array
        self.exec_by_groups = False
        if device_array is not None:
            if device_array.shape == self._shape:
                raise ValueError(
                    "Makes no sense to provide device_array with the same shape as the component shape."
                )
            self.exec_by_groups = True
            assert device_array.dtype == "f"
            assert device_array.ndim == 3
            self.processing_shape = self.device_array.shape

    def _set_device_buffer(self, device_buffer):
        self.device_buffer = device_buffer
        if device_buffer is not None:
            assert device_buffer.dtype == "f"


    def _check_device_buffer(self, check_3D=True):
        if self.device_buffer is None:
            raise ValueError(
                "%s with back-end %s: 'device_buffer' has to be provided"
                % (self.name, self.backend)
            )
            if self.device_buffer.ndim == 3 and check_3D:
                if self.device_buffer.shape != self.shape:
                    raise ValueError(
                        "If providing 3D device_buffer, its shape must be the same as 'shape'"
                    )


    def _update_available_backends(self, backends_requirements):
        if backends_requirements is None:
            return
        # Update priority of preferred backend
        preferred_backend = self.preferred_backend
        if preferred_backend == "auto":
            preferred_backend = None
        if preferred_backend is not None:
            check_supported(self.preferred_backend, list(self.backends.keys()), "backend")
            self.backends[preferred_backend].priority += 10
        # Python < 3.6 does not guarantee the dict items order
        backends_priorities = [
            b.priority
            for b in sorted(
                self.backends.values(), key=lambda b: b.priority, reverse=True
            )
        ]
        for backend_name, requirement in backends_requirements.items():
            requirement_fulfilled, err_msg = requirement
            # handle user preferences is self.options["use_XX"]
            for b in ["cuda", "opencl"]:
                if backend_name != b:
                    continue
                opt_name = "use_" + b
                if opt_name in self.options and not(self.options[opt_name]):
                    # This backend is explicitly disabled by user
                    requirement_fulfilled = False
                    err_msg = "disabled"
            #
            if not(requirement_fulfilled):
                if self.backends[backend_name].priority == backends_priorities[0]:
                    self.logger.warning(
                        "%s: cannot use the %s backend: %s" % (self.name, backend_name, err_msg)
                    )
                    backends_priorities.pop(0)
                self.backends[backend_name].available = False


    def get_backend(self, backends_requirements):
        """
        Get one of the available backends.

        Parameters
        -----------
        backends_requirements: dict
            Dictionary of backends. The key is the backend name, and the value is
            a tuple (bool, str) containing the requirement condition and the error message.
        """
        self._update_available_backends(backends_requirements)
        usable_backends = list(filter(lambda b: b.available, self.backends.values()))
        usable_backends.sort(key=lambda b: b.priority, reverse=True)
        if usable_backends == []:
            raise ValueError("%s: no usable backend was found. Cannot proceed" % self.name)
        self._backend = usable_backends[0]
        self.backend = self._backend.name
        if self.backend == "numpy":
            self.logger.warning("%s: chosen backend was numpy but device_array was provided. It will not be used (data will not be processed by groups)" % self.name)
            self.exec_by_groups = False


    def execute_by_groups(
        self, images,
        exec_output=None, group_size=None,
        **exec_onegroup_kwargs
    ):
        """
        Process group of images.
        Needs `execute_onegroup()` to be implemented by child class.

        Parameters
        -----------
        images: `numpy.ndarray`
            Array holding all the (sub)volume. Stack of images (ex. radios, sinos)
        exec_output: `numpy.ndarray`, optional
            Output array. By default, the processing is done in-place.
        group_size: int, optional
            Number of images to process in one group. By default, it is the number
            of images in `self.device_array`.

        Other Parameters
        -----------------
        exec_onechunk_kwargs: named arguments
            Named arguments of the `execute_onegroup` method (implemented in child class).
        """
        assert images.ndim == 3, "Expected 3D array"
        # assert backend is a device backend (otherwise makes no sense)
        # Check isinstance(images, np.ndarray) ?
        if exec_output is not None:
            output = exec_output
        else:
            output = images
        if group_size is None:
            group_size = self.device_array.shape[0]
        n_images = images.shape[0]
        n_groups = int(ceil(n_images / group_size))
        for i in range(n_groups):
            self.logger.debug("processing group %d/%d" % (i+1, n_groups))
            start_idx = i * group_size
            end_idx = min((i + 1) * group_size, n_images)
            transfer_size = end_idx - start_idx
            # Copy H2D
            self.device_array[:transfer_size, :, :] = images[start_idx:end_idx, :, :]
            # Process a (sub)chunk
            processed_array = self.execute_onegroup(
                self.device_array,
                **exec_onegroup_kwargs
            )
            # Copy D2H
            # memcpy D2H not working, I have to get()...
            # ~ output[start_idx:end_idx, :, :] = processed_array[:transfer_size, :, :]
            tmp = processed_array[:transfer_size, :, :].get()
            output[start_idx:end_idx, :, :] = tmp[:, :, :]
        return output


    def execute_onegroup(images, **kwargs):
        raise ValueError("This must be implemented by child class")


    def execute(self, images, exec_output=None, group_size=None, **kwargs):
        self.logger.info("%s: start processing chunk" % self.name)
        if self.exec_by_groups:
            res = self.execute_by_groups(
                images, exec_output=exec_output, group_size=group_size,
                **kwargs
            )
        else:
            res = self.execute_onegroup(images, **kwargs)
        self.logger.info("%s: end processing chunk" % self.name)
        return res

    __call__ = execute



class ComponentName(Enum):
    FLATFIELD = "flatfield"
    CCD_CORRECTION = "ccd_correction"
    PHASE = "phase"
    UNSHARP_MASK = "unsharp_mask"
    TAKE_LOG = "take_log"
    BUILD_SINO = "build_sino"
    RECONSTRUCTION = "reconstruction"
    SAVE = "save"


class ComponentDescription:
    """
    A high-level description of `Component` aiming at being used by a pipeline
    with instantiation as late as possible.
    """
    def __init__(
        self, Class, args,
        kwargs=None, exec_args=None, exec_kwargs=None,
        callback=None
    ):
        self.Class = Class
        self.instance = None # not instantiated yet
        self.args = args or []
        self.kwargs = kwargs or {}
        self.exec_args = exec_args or []
        self.exec_kwargs = exec_kwargs or {}
        self.callback = callback
        self.output = None # not executed yet


    def instantiate(self):
        self.instance = self.Class(*self.args, **self.kwargs)
        return self.instance


    def execute(self):
        output = self.instance.execute(*self.exec_args, self.exec_kwargs)
        self.output = output
        self.output_array = output
        return output


    @property
    def backend(self):
        return self.instance.backend

    @property
    def shape(self):
        return self.instance.shape

    @property
    def output_shape(self):
        return self.instance.output_shape

    @property
    def name(self):
        if self.instance is not None:
            return self.instance.name
        else:
            return self.args[0]

    @property
    def input_array(self):
        if self.exec_args != []:
            return self.exec_args[0]
        else:
            return ArrayPlaceHolder(self.shape, "f")

    @property
    def output_array(self):
        if self.output is None:
            return ArrayPlaceHolder(self.output_shape, "f")
        else:
            return self.output


    def execute(self):
        if self.instance is None:
            raise ValueError("cannot execute a non-initialized component")
        res = self.instance.execute(*self.exec_args, **self.exec_kwargs)
        self.output = res
        # Callback is pipeline responsibility
        # if self.callback is not None:
        #    self.callback(self)
        return res


    def _get_class_str(self):
        return str(self.Class).replace("'", "").replace('"', '').split(".")[-1].split(">")[0]


    def __repr__(self):
        return str(
            "%s(name=%s, input=%s, output=%s)"
            % (
                self._get_class_str(),
                self.name,
                array_tostring(self.input_array),
                array_tostring(self.output_array)
            )
        )
