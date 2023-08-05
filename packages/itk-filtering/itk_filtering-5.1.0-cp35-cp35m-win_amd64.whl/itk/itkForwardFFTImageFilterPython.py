# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkForwardFFTImageFilterPython
else:
    import _itkForwardFFTImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkForwardFFTImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkForwardFFTImageFilterPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import itkImageToImageFilterBPython
import itkImagePython
import itkPointPython
import itkFixedArrayPython
import pyBasePython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkRGBAPixelPython
import ITKCommonBasePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkForwardFFTImageFilterIF3ICF3_New():
  return itkForwardFFTImageFilterIF3ICF3.New()


def itkForwardFFTImageFilterIF2ICF2_New():
  return itkForwardFFTImageFilterIF2ICF2.New()

class itkForwardFFTImageFilterIF2ICF2(itkImageToImageFilterBPython.itkImageToImageFilterIF2ICF2):
    r"""Proxy of C++ itkForwardFFTImageFilterIF2ICF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2___New_orig__)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkForwardFFTImageFilterPython.delete_itkForwardFFTImageFilterIF2ICF2
    cast = _swig_new_static_method(_itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2_cast)

    def New(*args, **kargs):
        """New() -> itkForwardFFTImageFilterIF2ICF2

        Create a new object of the class itkForwardFFTImageFilterIF2ICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkForwardFFTImageFilterIF2ICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkForwardFFTImageFilterIF2ICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkForwardFFTImageFilterIF2ICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkForwardFFTImageFilterIF2ICF2 in _itkForwardFFTImageFilterPython:
_itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2_swigregister(itkForwardFFTImageFilterIF2ICF2)
itkForwardFFTImageFilterIF2ICF2___New_orig__ = _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2___New_orig__
itkForwardFFTImageFilterIF2ICF2_cast = _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2_cast

class itkForwardFFTImageFilterIF3ICF3(itkImageToImageFilterBPython.itkImageToImageFilterIF3ICF3):
    r"""Proxy of C++ itkForwardFFTImageFilterIF3ICF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3___New_orig__)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkForwardFFTImageFilterPython.delete_itkForwardFFTImageFilterIF3ICF3
    cast = _swig_new_static_method(_itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3_cast)

    def New(*args, **kargs):
        """New() -> itkForwardFFTImageFilterIF3ICF3

        Create a new object of the class itkForwardFFTImageFilterIF3ICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkForwardFFTImageFilterIF3ICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkForwardFFTImageFilterIF3ICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkForwardFFTImageFilterIF3ICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkForwardFFTImageFilterIF3ICF3 in _itkForwardFFTImageFilterPython:
_itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3_swigregister(itkForwardFFTImageFilterIF3ICF3)
itkForwardFFTImageFilterIF3ICF3___New_orig__ = _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3___New_orig__
itkForwardFFTImageFilterIF3ICF3_cast = _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def forward_fft_image_filter(*args, **kwargs):
    """Procedural interface for ForwardFFTImageFilter"""
    import itk
    instance = itk.ForwardFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def forward_fft_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ForwardFFTImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.ForwardFFTImageFilter.values()[0]
    else:
        filter_object = itk.ForwardFFTImageFilter

    forward_fft_image_filter.__doc__ = filter_object.__doc__
    forward_fft_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    forward_fft_image_filter.__doc__ += "Available Keyword Arguments:\n"
    forward_fft_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



