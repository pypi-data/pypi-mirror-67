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
    from . import _itkIsoContourDistanceImageFilterPython
else:
    import _itkIsoContourDistanceImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkIsoContourDistanceImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkIsoContourDistanceImageFilterPython.SWIG_PyStaticMethod_New

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


import ITKCommonBasePython
import pyBasePython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import ITKNarrowBandBasePython
import itkImageToImageFilterAPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
import itkImagePython
import itkMatrixPython
import vnl_matrixPython
import vnl_vectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkSymmetricSecondRankTensorPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython

def itkIsoContourDistanceImageFilterID3ID3_New():
  return itkIsoContourDistanceImageFilterID3ID3.New()


def itkIsoContourDistanceImageFilterID2ID2_New():
  return itkIsoContourDistanceImageFilterID2ID2.New()


def itkIsoContourDistanceImageFilterIF3IF3_New():
  return itkIsoContourDistanceImageFilterIF3IF3.New()


def itkIsoContourDistanceImageFilterIF2IF2_New():
  return itkIsoContourDistanceImageFilterIF2IF2.New()

class itkIsoContourDistanceImageFilterID2ID2(itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    r"""Proxy of C++ itkIsoContourDistanceImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_Clone)
    SetLevelSetValue = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_SetLevelSetValue)
    GetLevelSetValue = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_GetLevelSetValue)
    SetFarValue = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_SetFarValue)
    GetFarValue = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_GetFarValue)
    SetNarrowBanding = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_SetNarrowBanding)
    GetNarrowBanding = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_GetNarrowBanding)
    NarrowBandingOn = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_NarrowBandingOn)
    NarrowBandingOff = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_NarrowBandingOff)
    SetNarrowBand = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_SetNarrowBand)
    GetNarrowBand = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_GetNarrowBand)
    InputEqualityComparableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_InputEqualityComparableCheck
    
    OutputEqualityComparableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_OutputEqualityComparableCheck
    
    SameDimensionCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_SameDimensionCheck
    
    DoubleConvertibleToOutputCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_DoubleConvertibleToOutputCheck
    
    InputConvertibleToOutputCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_InputConvertibleToOutputCheck
    
    OutputAdditiveOperatorsCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_OutputAdditiveOperatorsCheck
    
    InputOStreamWritableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_InputOStreamWritableCheck
    
    OutputOStreamWritableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_OutputOStreamWritableCheck
    
    __swig_destroy__ = _itkIsoContourDistanceImageFilterPython.delete_itkIsoContourDistanceImageFilterID2ID2
    cast = _swig_new_static_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkIsoContourDistanceImageFilterID2ID2

        Create a new object of the class itkIsoContourDistanceImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoContourDistanceImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoContourDistanceImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoContourDistanceImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIsoContourDistanceImageFilterID2ID2 in _itkIsoContourDistanceImageFilterPython:
_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_swigregister(itkIsoContourDistanceImageFilterID2ID2)
itkIsoContourDistanceImageFilterID2ID2___New_orig__ = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2___New_orig__
itkIsoContourDistanceImageFilterID2ID2_cast = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID2ID2_cast

class itkIsoContourDistanceImageFilterID3ID3(itkImageToImageFilterAPython.itkImageToImageFilterID3ID3):
    r"""Proxy of C++ itkIsoContourDistanceImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_Clone)
    SetLevelSetValue = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_SetLevelSetValue)
    GetLevelSetValue = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_GetLevelSetValue)
    SetFarValue = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_SetFarValue)
    GetFarValue = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_GetFarValue)
    SetNarrowBanding = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_SetNarrowBanding)
    GetNarrowBanding = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_GetNarrowBanding)
    NarrowBandingOn = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_NarrowBandingOn)
    NarrowBandingOff = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_NarrowBandingOff)
    SetNarrowBand = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_SetNarrowBand)
    GetNarrowBand = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_GetNarrowBand)
    InputEqualityComparableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_InputEqualityComparableCheck
    
    OutputEqualityComparableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_OutputEqualityComparableCheck
    
    SameDimensionCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_SameDimensionCheck
    
    DoubleConvertibleToOutputCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_DoubleConvertibleToOutputCheck
    
    InputConvertibleToOutputCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_InputConvertibleToOutputCheck
    
    OutputAdditiveOperatorsCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_OutputAdditiveOperatorsCheck
    
    InputOStreamWritableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_InputOStreamWritableCheck
    
    OutputOStreamWritableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_OutputOStreamWritableCheck
    
    __swig_destroy__ = _itkIsoContourDistanceImageFilterPython.delete_itkIsoContourDistanceImageFilterID3ID3
    cast = _swig_new_static_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkIsoContourDistanceImageFilterID3ID3

        Create a new object of the class itkIsoContourDistanceImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoContourDistanceImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoContourDistanceImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoContourDistanceImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIsoContourDistanceImageFilterID3ID3 in _itkIsoContourDistanceImageFilterPython:
_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_swigregister(itkIsoContourDistanceImageFilterID3ID3)
itkIsoContourDistanceImageFilterID3ID3___New_orig__ = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3___New_orig__
itkIsoContourDistanceImageFilterID3ID3_cast = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterID3ID3_cast

class itkIsoContourDistanceImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    r"""Proxy of C++ itkIsoContourDistanceImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_Clone)
    SetLevelSetValue = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_SetLevelSetValue)
    GetLevelSetValue = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_GetLevelSetValue)
    SetFarValue = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_SetFarValue)
    GetFarValue = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_GetFarValue)
    SetNarrowBanding = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_SetNarrowBanding)
    GetNarrowBanding = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_GetNarrowBanding)
    NarrowBandingOn = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_NarrowBandingOn)
    NarrowBandingOff = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_NarrowBandingOff)
    SetNarrowBand = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_SetNarrowBand)
    GetNarrowBand = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_GetNarrowBand)
    InputEqualityComparableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_InputEqualityComparableCheck
    
    OutputEqualityComparableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_OutputEqualityComparableCheck
    
    SameDimensionCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_SameDimensionCheck
    
    DoubleConvertibleToOutputCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    
    InputConvertibleToOutputCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_InputConvertibleToOutputCheck
    
    OutputAdditiveOperatorsCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_OutputAdditiveOperatorsCheck
    
    InputOStreamWritableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_InputOStreamWritableCheck
    
    OutputOStreamWritableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_OutputOStreamWritableCheck
    
    __swig_destroy__ = _itkIsoContourDistanceImageFilterPython.delete_itkIsoContourDistanceImageFilterIF2IF2
    cast = _swig_new_static_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkIsoContourDistanceImageFilterIF2IF2

        Create a new object of the class itkIsoContourDistanceImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoContourDistanceImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoContourDistanceImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoContourDistanceImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIsoContourDistanceImageFilterIF2IF2 in _itkIsoContourDistanceImageFilterPython:
_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_swigregister(itkIsoContourDistanceImageFilterIF2IF2)
itkIsoContourDistanceImageFilterIF2IF2___New_orig__ = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2___New_orig__
itkIsoContourDistanceImageFilterIF2IF2_cast = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF2IF2_cast

class itkIsoContourDistanceImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    r"""Proxy of C++ itkIsoContourDistanceImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_Clone)
    SetLevelSetValue = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_SetLevelSetValue)
    GetLevelSetValue = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_GetLevelSetValue)
    SetFarValue = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_SetFarValue)
    GetFarValue = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_GetFarValue)
    SetNarrowBanding = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_SetNarrowBanding)
    GetNarrowBanding = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_GetNarrowBanding)
    NarrowBandingOn = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_NarrowBandingOn)
    NarrowBandingOff = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_NarrowBandingOff)
    SetNarrowBand = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_SetNarrowBand)
    GetNarrowBand = _swig_new_instance_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_GetNarrowBand)
    InputEqualityComparableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_InputEqualityComparableCheck
    
    OutputEqualityComparableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_OutputEqualityComparableCheck
    
    SameDimensionCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_SameDimensionCheck
    
    DoubleConvertibleToOutputCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    
    InputConvertibleToOutputCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_InputConvertibleToOutputCheck
    
    OutputAdditiveOperatorsCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_OutputAdditiveOperatorsCheck
    
    InputOStreamWritableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_InputOStreamWritableCheck
    
    OutputOStreamWritableCheck = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_OutputOStreamWritableCheck
    
    __swig_destroy__ = _itkIsoContourDistanceImageFilterPython.delete_itkIsoContourDistanceImageFilterIF3IF3
    cast = _swig_new_static_method(_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkIsoContourDistanceImageFilterIF3IF3

        Create a new object of the class itkIsoContourDistanceImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoContourDistanceImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoContourDistanceImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoContourDistanceImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIsoContourDistanceImageFilterIF3IF3 in _itkIsoContourDistanceImageFilterPython:
_itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_swigregister(itkIsoContourDistanceImageFilterIF3IF3)
itkIsoContourDistanceImageFilterIF3IF3___New_orig__ = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3___New_orig__
itkIsoContourDistanceImageFilterIF3IF3_cast = _itkIsoContourDistanceImageFilterPython.itkIsoContourDistanceImageFilterIF3IF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def iso_contour_distance_image_filter(*args, **kwargs):
    """Procedural interface for IsoContourDistanceImageFilter"""
    import itk
    instance = itk.IsoContourDistanceImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def iso_contour_distance_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.IsoContourDistanceImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.IsoContourDistanceImageFilter.values()[0]
    else:
        filter_object = itk.IsoContourDistanceImageFilter

    iso_contour_distance_image_filter.__doc__ = filter_object.__doc__
    iso_contour_distance_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    iso_contour_distance_image_filter.__doc__ += "Available Keyword Arguments:\n"
    iso_contour_distance_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



