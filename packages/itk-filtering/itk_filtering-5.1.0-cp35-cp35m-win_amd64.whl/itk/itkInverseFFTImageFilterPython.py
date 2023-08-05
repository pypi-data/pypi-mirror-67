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
    from . import _itkInverseFFTImageFilterPython
else:
    import _itkInverseFFTImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkInverseFFTImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkInverseFFTImageFilterPython.SWIG_PyStaticMethod_New

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

def itkInverseFFTImageFilterICF3IF3_New():
  return itkInverseFFTImageFilterICF3IF3.New()


def itkInverseFFTImageFilterICF2IF2_New():
  return itkInverseFFTImageFilterICF2IF2.New()

class itkInverseFFTImageFilterICF2IF2(itkImageToImageFilterBPython.itkImageToImageFilterICF2IF2):
    r"""Proxy of C++ itkInverseFFTImageFilterICF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2___New_orig__)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkInverseFFTImageFilterPython.delete_itkInverseFFTImageFilterICF2IF2
    cast = _swig_new_static_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkInverseFFTImageFilterICF2IF2

        Create a new object of the class itkInverseFFTImageFilterICF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseFFTImageFilterICF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkInverseFFTImageFilterICF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkInverseFFTImageFilterICF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkInverseFFTImageFilterICF2IF2 in _itkInverseFFTImageFilterPython:
_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_swigregister(itkInverseFFTImageFilterICF2IF2)
itkInverseFFTImageFilterICF2IF2___New_orig__ = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2___New_orig__
itkInverseFFTImageFilterICF2IF2_cast = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_cast

class itkInverseFFTImageFilterICF3IF3(itkImageToImageFilterBPython.itkImageToImageFilterICF3IF3):
    r"""Proxy of C++ itkInverseFFTImageFilterICF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3___New_orig__)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkInverseFFTImageFilterPython.delete_itkInverseFFTImageFilterICF3IF3
    cast = _swig_new_static_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkInverseFFTImageFilterICF3IF3

        Create a new object of the class itkInverseFFTImageFilterICF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseFFTImageFilterICF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkInverseFFTImageFilterICF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkInverseFFTImageFilterICF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkInverseFFTImageFilterICF3IF3 in _itkInverseFFTImageFilterPython:
_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_swigregister(itkInverseFFTImageFilterICF3IF3)
itkInverseFFTImageFilterICF3IF3___New_orig__ = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3___New_orig__
itkInverseFFTImageFilterICF3IF3_cast = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def inverse_fft_image_filter(*args, **kwargs):
    """Procedural interface for InverseFFTImageFilter"""
    import itk
    instance = itk.InverseFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def inverse_fft_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.InverseFFTImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.InverseFFTImageFilter.values()[0]
    else:
        filter_object = itk.InverseFFTImageFilter

    inverse_fft_image_filter.__doc__ = filter_object.__doc__
    inverse_fft_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    inverse_fft_image_filter.__doc__ += "Available Keyword Arguments:\n"
    inverse_fft_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



