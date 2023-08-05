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
    from . import _itkHalfToFullHermitianImageFilterPython
else:
    import _itkHalfToFullHermitianImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkHalfToFullHermitianImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkHalfToFullHermitianImageFilterPython.SWIG_PyStaticMethod_New

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
import itkImageToImageFilterCommonPython
import pyBasePython
import ITKCommonBasePython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkImagePython
import itkFixedArrayPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import itkPointPython
import vnl_matrix_fixedPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkSimpleDataObjectDecoratorPython
import itkArrayPython

def itkHalfToFullHermitianImageFilterICF3_New():
  return itkHalfToFullHermitianImageFilterICF3.New()


def itkHalfToFullHermitianImageFilterICF2_New():
  return itkHalfToFullHermitianImageFilterICF2.New()

class itkHalfToFullHermitianImageFilterICF2(itkImageToImageFilterBPython.itkImageToImageFilterICF2ICF2):
    r"""Proxy of C++ itkHalfToFullHermitianImageFilterICF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2___New_orig__)
    Clone = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_Clone)
    SetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_SetActualXDimensionIsOddInput)
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_GetActualXDimensionIsOddInput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_ActualXDimensionIsOddOff)
    __swig_destroy__ = _itkHalfToFullHermitianImageFilterPython.delete_itkHalfToFullHermitianImageFilterICF2
    cast = _swig_new_static_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_cast)

    def New(*args, **kargs):
        """New() -> itkHalfToFullHermitianImageFilterICF2

        Create a new object of the class itkHalfToFullHermitianImageFilterICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfToFullHermitianImageFilterICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHalfToFullHermitianImageFilterICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHalfToFullHermitianImageFilterICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHalfToFullHermitianImageFilterICF2 in _itkHalfToFullHermitianImageFilterPython:
_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_swigregister(itkHalfToFullHermitianImageFilterICF2)
itkHalfToFullHermitianImageFilterICF2___New_orig__ = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2___New_orig__
itkHalfToFullHermitianImageFilterICF2_cast = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_cast

class itkHalfToFullHermitianImageFilterICF3(itkImageToImageFilterBPython.itkImageToImageFilterICF3ICF3):
    r"""Proxy of C++ itkHalfToFullHermitianImageFilterICF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3___New_orig__)
    Clone = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_Clone)
    SetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_SetActualXDimensionIsOddInput)
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_GetActualXDimensionIsOddInput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_ActualXDimensionIsOddOff)
    __swig_destroy__ = _itkHalfToFullHermitianImageFilterPython.delete_itkHalfToFullHermitianImageFilterICF3
    cast = _swig_new_static_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_cast)

    def New(*args, **kargs):
        """New() -> itkHalfToFullHermitianImageFilterICF3

        Create a new object of the class itkHalfToFullHermitianImageFilterICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfToFullHermitianImageFilterICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHalfToFullHermitianImageFilterICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHalfToFullHermitianImageFilterICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHalfToFullHermitianImageFilterICF3 in _itkHalfToFullHermitianImageFilterPython:
_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_swigregister(itkHalfToFullHermitianImageFilterICF3)
itkHalfToFullHermitianImageFilterICF3___New_orig__ = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3___New_orig__
itkHalfToFullHermitianImageFilterICF3_cast = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def half_to_full_hermitian_image_filter(*args, **kwargs):
    """Procedural interface for HalfToFullHermitianImageFilter"""
    import itk
    instance = itk.HalfToFullHermitianImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def half_to_full_hermitian_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.HalfToFullHermitianImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.HalfToFullHermitianImageFilter.values()[0]
    else:
        filter_object = itk.HalfToFullHermitianImageFilter

    half_to_full_hermitian_image_filter.__doc__ = filter_object.__doc__
    half_to_full_hermitian_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    half_to_full_hermitian_image_filter.__doc__ += "Available Keyword Arguments:\n"
    half_to_full_hermitian_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



