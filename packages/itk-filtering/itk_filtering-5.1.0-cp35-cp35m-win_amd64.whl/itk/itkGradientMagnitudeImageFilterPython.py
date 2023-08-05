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
    from . import _itkGradientMagnitudeImageFilterPython
else:
    import _itkGradientMagnitudeImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkGradientMagnitudeImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkGradientMagnitudeImageFilterPython.SWIG_PyStaticMethod_New

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


import itkImageToImageFilterAPython
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

def itkGradientMagnitudeImageFilterID3ID3_New():
  return itkGradientMagnitudeImageFilterID3ID3.New()


def itkGradientMagnitudeImageFilterID2ID2_New():
  return itkGradientMagnitudeImageFilterID2ID2.New()


def itkGradientMagnitudeImageFilterIF3IF3_New():
  return itkGradientMagnitudeImageFilterIF3IF3.New()


def itkGradientMagnitudeImageFilterIF2IF2_New():
  return itkGradientMagnitudeImageFilterIF2IF2.New()


def itkGradientMagnitudeImageFilterIUS3IUS3_New():
  return itkGradientMagnitudeImageFilterIUS3IUS3.New()


def itkGradientMagnitudeImageFilterIUS2IUS2_New():
  return itkGradientMagnitudeImageFilterIUS2IUS2.New()


def itkGradientMagnitudeImageFilterIUC3IUC3_New():
  return itkGradientMagnitudeImageFilterIUC3IUC3.New()


def itkGradientMagnitudeImageFilterIUC2IUC2_New():
  return itkGradientMagnitudeImageFilterIUC2IUC2.New()


def itkGradientMagnitudeImageFilterISS3ISS3_New():
  return itkGradientMagnitudeImageFilterISS3ISS3.New()


def itkGradientMagnitudeImageFilterISS2ISS2_New():
  return itkGradientMagnitudeImageFilterISS2ISS2.New()

class itkGradientMagnitudeImageFilterID2ID2(itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    r"""Proxy of C++ itkGradientMagnitudeImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID2ID2_Clone)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID2ID2_GenerateInputRequestedRegion)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID2ID2_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID2ID2_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID2ID2_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID2ID2_GetUseImageSpacing)
    InputHasNumericTraitsCheck = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID2ID2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientMagnitudeImageFilterPython.delete_itkGradientMagnitudeImageFilterID2ID2
    cast = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkGradientMagnitudeImageFilterID2ID2

        Create a new object of the class itkGradientMagnitudeImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientMagnitudeImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientMagnitudeImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientMagnitudeImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientMagnitudeImageFilterID2ID2 in _itkGradientMagnitudeImageFilterPython:
_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID2ID2_swigregister(itkGradientMagnitudeImageFilterID2ID2)
itkGradientMagnitudeImageFilterID2ID2___New_orig__ = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID2ID2___New_orig__
itkGradientMagnitudeImageFilterID2ID2_cast = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID2ID2_cast

class itkGradientMagnitudeImageFilterID3ID3(itkImageToImageFilterAPython.itkImageToImageFilterID3ID3):
    r"""Proxy of C++ itkGradientMagnitudeImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID3ID3_Clone)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID3ID3_GenerateInputRequestedRegion)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID3ID3_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID3ID3_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID3ID3_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID3ID3_GetUseImageSpacing)
    InputHasNumericTraitsCheck = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID3ID3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientMagnitudeImageFilterPython.delete_itkGradientMagnitudeImageFilterID3ID3
    cast = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkGradientMagnitudeImageFilterID3ID3

        Create a new object of the class itkGradientMagnitudeImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientMagnitudeImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientMagnitudeImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientMagnitudeImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientMagnitudeImageFilterID3ID3 in _itkGradientMagnitudeImageFilterPython:
_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID3ID3_swigregister(itkGradientMagnitudeImageFilterID3ID3)
itkGradientMagnitudeImageFilterID3ID3___New_orig__ = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID3ID3___New_orig__
itkGradientMagnitudeImageFilterID3ID3_cast = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterID3ID3_cast

class itkGradientMagnitudeImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    r"""Proxy of C++ itkGradientMagnitudeImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF2IF2_Clone)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF2IF2_GenerateInputRequestedRegion)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF2IF2_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF2IF2_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF2IF2_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF2IF2_GetUseImageSpacing)
    InputHasNumericTraitsCheck = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF2IF2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientMagnitudeImageFilterPython.delete_itkGradientMagnitudeImageFilterIF2IF2
    cast = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkGradientMagnitudeImageFilterIF2IF2

        Create a new object of the class itkGradientMagnitudeImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientMagnitudeImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientMagnitudeImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientMagnitudeImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientMagnitudeImageFilterIF2IF2 in _itkGradientMagnitudeImageFilterPython:
_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF2IF2_swigregister(itkGradientMagnitudeImageFilterIF2IF2)
itkGradientMagnitudeImageFilterIF2IF2___New_orig__ = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF2IF2___New_orig__
itkGradientMagnitudeImageFilterIF2IF2_cast = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF2IF2_cast

class itkGradientMagnitudeImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    r"""Proxy of C++ itkGradientMagnitudeImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF3IF3_Clone)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF3IF3_GenerateInputRequestedRegion)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF3IF3_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF3IF3_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF3IF3_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF3IF3_GetUseImageSpacing)
    InputHasNumericTraitsCheck = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF3IF3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientMagnitudeImageFilterPython.delete_itkGradientMagnitudeImageFilterIF3IF3
    cast = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkGradientMagnitudeImageFilterIF3IF3

        Create a new object of the class itkGradientMagnitudeImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientMagnitudeImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientMagnitudeImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientMagnitudeImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientMagnitudeImageFilterIF3IF3 in _itkGradientMagnitudeImageFilterPython:
_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF3IF3_swigregister(itkGradientMagnitudeImageFilterIF3IF3)
itkGradientMagnitudeImageFilterIF3IF3___New_orig__ = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF3IF3___New_orig__
itkGradientMagnitudeImageFilterIF3IF3_cast = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIF3IF3_cast

class itkGradientMagnitudeImageFilterISS2ISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    r"""Proxy of C++ itkGradientMagnitudeImageFilterISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS2ISS2_Clone)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS2ISS2_GenerateInputRequestedRegion)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS2ISS2_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS2ISS2_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS2ISS2_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS2ISS2_GetUseImageSpacing)
    InputHasNumericTraitsCheck = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS2ISS2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientMagnitudeImageFilterPython.delete_itkGradientMagnitudeImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkGradientMagnitudeImageFilterISS2ISS2

        Create a new object of the class itkGradientMagnitudeImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientMagnitudeImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientMagnitudeImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientMagnitudeImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientMagnitudeImageFilterISS2ISS2 in _itkGradientMagnitudeImageFilterPython:
_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS2ISS2_swigregister(itkGradientMagnitudeImageFilterISS2ISS2)
itkGradientMagnitudeImageFilterISS2ISS2___New_orig__ = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS2ISS2___New_orig__
itkGradientMagnitudeImageFilterISS2ISS2_cast = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS2ISS2_cast

class itkGradientMagnitudeImageFilterISS3ISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    r"""Proxy of C++ itkGradientMagnitudeImageFilterISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS3ISS3_Clone)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS3ISS3_GenerateInputRequestedRegion)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS3ISS3_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS3ISS3_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS3ISS3_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS3ISS3_GetUseImageSpacing)
    InputHasNumericTraitsCheck = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS3ISS3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientMagnitudeImageFilterPython.delete_itkGradientMagnitudeImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkGradientMagnitudeImageFilterISS3ISS3

        Create a new object of the class itkGradientMagnitudeImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientMagnitudeImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientMagnitudeImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientMagnitudeImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientMagnitudeImageFilterISS3ISS3 in _itkGradientMagnitudeImageFilterPython:
_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS3ISS3_swigregister(itkGradientMagnitudeImageFilterISS3ISS3)
itkGradientMagnitudeImageFilterISS3ISS3___New_orig__ = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS3ISS3___New_orig__
itkGradientMagnitudeImageFilterISS3ISS3_cast = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterISS3ISS3_cast

class itkGradientMagnitudeImageFilterIUC2IUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    r"""Proxy of C++ itkGradientMagnitudeImageFilterIUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC2IUC2_Clone)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC2IUC2_GenerateInputRequestedRegion)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC2IUC2_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC2IUC2_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC2IUC2_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC2IUC2_GetUseImageSpacing)
    InputHasNumericTraitsCheck = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC2IUC2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientMagnitudeImageFilterPython.delete_itkGradientMagnitudeImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkGradientMagnitudeImageFilterIUC2IUC2

        Create a new object of the class itkGradientMagnitudeImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientMagnitudeImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientMagnitudeImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientMagnitudeImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientMagnitudeImageFilterIUC2IUC2 in _itkGradientMagnitudeImageFilterPython:
_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC2IUC2_swigregister(itkGradientMagnitudeImageFilterIUC2IUC2)
itkGradientMagnitudeImageFilterIUC2IUC2___New_orig__ = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC2IUC2___New_orig__
itkGradientMagnitudeImageFilterIUC2IUC2_cast = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC2IUC2_cast

class itkGradientMagnitudeImageFilterIUC3IUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    r"""Proxy of C++ itkGradientMagnitudeImageFilterIUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC3IUC3_Clone)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC3IUC3_GenerateInputRequestedRegion)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC3IUC3_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC3IUC3_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC3IUC3_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC3IUC3_GetUseImageSpacing)
    InputHasNumericTraitsCheck = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC3IUC3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientMagnitudeImageFilterPython.delete_itkGradientMagnitudeImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkGradientMagnitudeImageFilterIUC3IUC3

        Create a new object of the class itkGradientMagnitudeImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientMagnitudeImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientMagnitudeImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientMagnitudeImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientMagnitudeImageFilterIUC3IUC3 in _itkGradientMagnitudeImageFilterPython:
_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC3IUC3_swigregister(itkGradientMagnitudeImageFilterIUC3IUC3)
itkGradientMagnitudeImageFilterIUC3IUC3___New_orig__ = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC3IUC3___New_orig__
itkGradientMagnitudeImageFilterIUC3IUC3_cast = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUC3IUC3_cast

class itkGradientMagnitudeImageFilterIUS2IUS2(itkImageToImageFilterAPython.itkImageToImageFilterIUS2IUS2):
    r"""Proxy of C++ itkGradientMagnitudeImageFilterIUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS2IUS2_Clone)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS2IUS2_GenerateInputRequestedRegion)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS2IUS2_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS2IUS2_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS2IUS2_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS2IUS2_GetUseImageSpacing)
    InputHasNumericTraitsCheck = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS2IUS2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientMagnitudeImageFilterPython.delete_itkGradientMagnitudeImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkGradientMagnitudeImageFilterIUS2IUS2

        Create a new object of the class itkGradientMagnitudeImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientMagnitudeImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientMagnitudeImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientMagnitudeImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientMagnitudeImageFilterIUS2IUS2 in _itkGradientMagnitudeImageFilterPython:
_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS2IUS2_swigregister(itkGradientMagnitudeImageFilterIUS2IUS2)
itkGradientMagnitudeImageFilterIUS2IUS2___New_orig__ = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS2IUS2___New_orig__
itkGradientMagnitudeImageFilterIUS2IUS2_cast = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS2IUS2_cast

class itkGradientMagnitudeImageFilterIUS3IUS3(itkImageToImageFilterAPython.itkImageToImageFilterIUS3IUS3):
    r"""Proxy of C++ itkGradientMagnitudeImageFilterIUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS3IUS3_Clone)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS3IUS3_GenerateInputRequestedRegion)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS3IUS3_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS3IUS3_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS3IUS3_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS3IUS3_GetUseImageSpacing)
    InputHasNumericTraitsCheck = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS3IUS3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientMagnitudeImageFilterPython.delete_itkGradientMagnitudeImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkGradientMagnitudeImageFilterIUS3IUS3

        Create a new object of the class itkGradientMagnitudeImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientMagnitudeImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientMagnitudeImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientMagnitudeImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientMagnitudeImageFilterIUS3IUS3 in _itkGradientMagnitudeImageFilterPython:
_itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS3IUS3_swigregister(itkGradientMagnitudeImageFilterIUS3IUS3)
itkGradientMagnitudeImageFilterIUS3IUS3___New_orig__ = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS3IUS3___New_orig__
itkGradientMagnitudeImageFilterIUS3IUS3_cast = _itkGradientMagnitudeImageFilterPython.itkGradientMagnitudeImageFilterIUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def gradient_magnitude_image_filter(*args, **kwargs):
    """Procedural interface for GradientMagnitudeImageFilter"""
    import itk
    instance = itk.GradientMagnitudeImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def gradient_magnitude_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.GradientMagnitudeImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.GradientMagnitudeImageFilter.values()[0]
    else:
        filter_object = itk.GradientMagnitudeImageFilter

    gradient_magnitude_image_filter.__doc__ = filter_object.__doc__
    gradient_magnitude_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    gradient_magnitude_image_filter.__doc__ += "Available Keyword Arguments:\n"
    gradient_magnitude_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



