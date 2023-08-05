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
    from . import _itkAdditiveGaussianNoiseImageFilterPython
else:
    import _itkAdditiveGaussianNoiseImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkAdditiveGaussianNoiseImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkAdditiveGaussianNoiseImageFilterPython.SWIG_PyStaticMethod_New

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


import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import ITKCommonBasePython
import itkNoiseBaseImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
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
import itkImageToImageFilterAPython

def itkAdditiveGaussianNoiseImageFilterID3ID3_New():
  return itkAdditiveGaussianNoiseImageFilterID3ID3.New()


def itkAdditiveGaussianNoiseImageFilterID2ID2_New():
  return itkAdditiveGaussianNoiseImageFilterID2ID2.New()


def itkAdditiveGaussianNoiseImageFilterIF3IF3_New():
  return itkAdditiveGaussianNoiseImageFilterIF3IF3.New()


def itkAdditiveGaussianNoiseImageFilterIF2IF2_New():
  return itkAdditiveGaussianNoiseImageFilterIF2IF2.New()


def itkAdditiveGaussianNoiseImageFilterIUS3IUS3_New():
  return itkAdditiveGaussianNoiseImageFilterIUS3IUS3.New()


def itkAdditiveGaussianNoiseImageFilterIUS2IUS2_New():
  return itkAdditiveGaussianNoiseImageFilterIUS2IUS2.New()


def itkAdditiveGaussianNoiseImageFilterIUC3IUC3_New():
  return itkAdditiveGaussianNoiseImageFilterIUC3IUC3.New()


def itkAdditiveGaussianNoiseImageFilterIUC2IUC2_New():
  return itkAdditiveGaussianNoiseImageFilterIUC2IUC2.New()


def itkAdditiveGaussianNoiseImageFilterISS3ISS3_New():
  return itkAdditiveGaussianNoiseImageFilterISS3ISS3.New()


def itkAdditiveGaussianNoiseImageFilterISS2ISS2_New():
  return itkAdditiveGaussianNoiseImageFilterISS2ISS2.New()

class itkAdditiveGaussianNoiseImageFilterID2ID2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterID2ID2):
    r"""Proxy of C++ itkAdditiveGaussianNoiseImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID2ID2_Clone)
    GetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID2ID2_GetMean)
    SetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID2ID2_SetMean)
    GetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID2ID2_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID2ID2_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID2ID2_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAdditiveGaussianNoiseImageFilterPython.delete_itkAdditiveGaussianNoiseImageFilterID2ID2
    cast = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkAdditiveGaussianNoiseImageFilterID2ID2

        Create a new object of the class itkAdditiveGaussianNoiseImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAdditiveGaussianNoiseImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAdditiveGaussianNoiseImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAdditiveGaussianNoiseImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAdditiveGaussianNoiseImageFilterID2ID2 in _itkAdditiveGaussianNoiseImageFilterPython:
_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID2ID2_swigregister(itkAdditiveGaussianNoiseImageFilterID2ID2)
itkAdditiveGaussianNoiseImageFilterID2ID2___New_orig__ = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID2ID2___New_orig__
itkAdditiveGaussianNoiseImageFilterID2ID2_cast = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID2ID2_cast

class itkAdditiveGaussianNoiseImageFilterID3ID3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterID3ID3):
    r"""Proxy of C++ itkAdditiveGaussianNoiseImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID3ID3_Clone)
    GetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID3ID3_GetMean)
    SetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID3ID3_SetMean)
    GetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID3ID3_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID3ID3_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID3ID3_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAdditiveGaussianNoiseImageFilterPython.delete_itkAdditiveGaussianNoiseImageFilterID3ID3
    cast = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkAdditiveGaussianNoiseImageFilterID3ID3

        Create a new object of the class itkAdditiveGaussianNoiseImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAdditiveGaussianNoiseImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAdditiveGaussianNoiseImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAdditiveGaussianNoiseImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAdditiveGaussianNoiseImageFilterID3ID3 in _itkAdditiveGaussianNoiseImageFilterPython:
_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID3ID3_swigregister(itkAdditiveGaussianNoiseImageFilterID3ID3)
itkAdditiveGaussianNoiseImageFilterID3ID3___New_orig__ = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID3ID3___New_orig__
itkAdditiveGaussianNoiseImageFilterID3ID3_cast = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterID3ID3_cast

class itkAdditiveGaussianNoiseImageFilterIF2IF2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIF2IF2):
    r"""Proxy of C++ itkAdditiveGaussianNoiseImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF2IF2_Clone)
    GetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF2IF2_GetMean)
    SetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF2IF2_SetMean)
    GetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF2IF2_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF2IF2_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF2IF2_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAdditiveGaussianNoiseImageFilterPython.delete_itkAdditiveGaussianNoiseImageFilterIF2IF2
    cast = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkAdditiveGaussianNoiseImageFilterIF2IF2

        Create a new object of the class itkAdditiveGaussianNoiseImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAdditiveGaussianNoiseImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAdditiveGaussianNoiseImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAdditiveGaussianNoiseImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAdditiveGaussianNoiseImageFilterIF2IF2 in _itkAdditiveGaussianNoiseImageFilterPython:
_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF2IF2_swigregister(itkAdditiveGaussianNoiseImageFilterIF2IF2)
itkAdditiveGaussianNoiseImageFilterIF2IF2___New_orig__ = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF2IF2___New_orig__
itkAdditiveGaussianNoiseImageFilterIF2IF2_cast = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF2IF2_cast

class itkAdditiveGaussianNoiseImageFilterIF3IF3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIF3IF3):
    r"""Proxy of C++ itkAdditiveGaussianNoiseImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF3IF3_Clone)
    GetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF3IF3_GetMean)
    SetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF3IF3_SetMean)
    GetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF3IF3_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF3IF3_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF3IF3_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAdditiveGaussianNoiseImageFilterPython.delete_itkAdditiveGaussianNoiseImageFilterIF3IF3
    cast = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkAdditiveGaussianNoiseImageFilterIF3IF3

        Create a new object of the class itkAdditiveGaussianNoiseImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAdditiveGaussianNoiseImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAdditiveGaussianNoiseImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAdditiveGaussianNoiseImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAdditiveGaussianNoiseImageFilterIF3IF3 in _itkAdditiveGaussianNoiseImageFilterPython:
_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF3IF3_swigregister(itkAdditiveGaussianNoiseImageFilterIF3IF3)
itkAdditiveGaussianNoiseImageFilterIF3IF3___New_orig__ = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF3IF3___New_orig__
itkAdditiveGaussianNoiseImageFilterIF3IF3_cast = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIF3IF3_cast

class itkAdditiveGaussianNoiseImageFilterISS2ISS2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterISS2ISS2):
    r"""Proxy of C++ itkAdditiveGaussianNoiseImageFilterISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS2ISS2_Clone)
    GetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS2ISS2_GetMean)
    SetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS2ISS2_SetMean)
    GetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS2ISS2_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS2ISS2_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS2ISS2_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAdditiveGaussianNoiseImageFilterPython.delete_itkAdditiveGaussianNoiseImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkAdditiveGaussianNoiseImageFilterISS2ISS2

        Create a new object of the class itkAdditiveGaussianNoiseImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAdditiveGaussianNoiseImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAdditiveGaussianNoiseImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAdditiveGaussianNoiseImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAdditiveGaussianNoiseImageFilterISS2ISS2 in _itkAdditiveGaussianNoiseImageFilterPython:
_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS2ISS2_swigregister(itkAdditiveGaussianNoiseImageFilterISS2ISS2)
itkAdditiveGaussianNoiseImageFilterISS2ISS2___New_orig__ = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS2ISS2___New_orig__
itkAdditiveGaussianNoiseImageFilterISS2ISS2_cast = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS2ISS2_cast

class itkAdditiveGaussianNoiseImageFilterISS3ISS3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterISS3ISS3):
    r"""Proxy of C++ itkAdditiveGaussianNoiseImageFilterISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS3ISS3_Clone)
    GetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS3ISS3_GetMean)
    SetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS3ISS3_SetMean)
    GetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS3ISS3_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS3ISS3_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS3ISS3_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAdditiveGaussianNoiseImageFilterPython.delete_itkAdditiveGaussianNoiseImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkAdditiveGaussianNoiseImageFilterISS3ISS3

        Create a new object of the class itkAdditiveGaussianNoiseImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAdditiveGaussianNoiseImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAdditiveGaussianNoiseImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAdditiveGaussianNoiseImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAdditiveGaussianNoiseImageFilterISS3ISS3 in _itkAdditiveGaussianNoiseImageFilterPython:
_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS3ISS3_swigregister(itkAdditiveGaussianNoiseImageFilterISS3ISS3)
itkAdditiveGaussianNoiseImageFilterISS3ISS3___New_orig__ = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS3ISS3___New_orig__
itkAdditiveGaussianNoiseImageFilterISS3ISS3_cast = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterISS3ISS3_cast

class itkAdditiveGaussianNoiseImageFilterIUC2IUC2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIUC2IUC2):
    r"""Proxy of C++ itkAdditiveGaussianNoiseImageFilterIUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC2IUC2_Clone)
    GetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC2IUC2_GetMean)
    SetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC2IUC2_SetMean)
    GetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC2IUC2_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC2IUC2_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC2IUC2_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAdditiveGaussianNoiseImageFilterPython.delete_itkAdditiveGaussianNoiseImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkAdditiveGaussianNoiseImageFilterIUC2IUC2

        Create a new object of the class itkAdditiveGaussianNoiseImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAdditiveGaussianNoiseImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAdditiveGaussianNoiseImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAdditiveGaussianNoiseImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAdditiveGaussianNoiseImageFilterIUC2IUC2 in _itkAdditiveGaussianNoiseImageFilterPython:
_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC2IUC2_swigregister(itkAdditiveGaussianNoiseImageFilterIUC2IUC2)
itkAdditiveGaussianNoiseImageFilterIUC2IUC2___New_orig__ = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC2IUC2___New_orig__
itkAdditiveGaussianNoiseImageFilterIUC2IUC2_cast = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC2IUC2_cast

class itkAdditiveGaussianNoiseImageFilterIUC3IUC3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIUC3IUC3):
    r"""Proxy of C++ itkAdditiveGaussianNoiseImageFilterIUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC3IUC3_Clone)
    GetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC3IUC3_GetMean)
    SetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC3IUC3_SetMean)
    GetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC3IUC3_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC3IUC3_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC3IUC3_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAdditiveGaussianNoiseImageFilterPython.delete_itkAdditiveGaussianNoiseImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkAdditiveGaussianNoiseImageFilterIUC3IUC3

        Create a new object of the class itkAdditiveGaussianNoiseImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAdditiveGaussianNoiseImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAdditiveGaussianNoiseImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAdditiveGaussianNoiseImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAdditiveGaussianNoiseImageFilterIUC3IUC3 in _itkAdditiveGaussianNoiseImageFilterPython:
_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC3IUC3_swigregister(itkAdditiveGaussianNoiseImageFilterIUC3IUC3)
itkAdditiveGaussianNoiseImageFilterIUC3IUC3___New_orig__ = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC3IUC3___New_orig__
itkAdditiveGaussianNoiseImageFilterIUC3IUC3_cast = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUC3IUC3_cast

class itkAdditiveGaussianNoiseImageFilterIUS2IUS2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIUS2IUS2):
    r"""Proxy of C++ itkAdditiveGaussianNoiseImageFilterIUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS2IUS2_Clone)
    GetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS2IUS2_GetMean)
    SetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS2IUS2_SetMean)
    GetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS2IUS2_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS2IUS2_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS2IUS2_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAdditiveGaussianNoiseImageFilterPython.delete_itkAdditiveGaussianNoiseImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkAdditiveGaussianNoiseImageFilterIUS2IUS2

        Create a new object of the class itkAdditiveGaussianNoiseImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAdditiveGaussianNoiseImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAdditiveGaussianNoiseImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAdditiveGaussianNoiseImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAdditiveGaussianNoiseImageFilterIUS2IUS2 in _itkAdditiveGaussianNoiseImageFilterPython:
_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS2IUS2_swigregister(itkAdditiveGaussianNoiseImageFilterIUS2IUS2)
itkAdditiveGaussianNoiseImageFilterIUS2IUS2___New_orig__ = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS2IUS2___New_orig__
itkAdditiveGaussianNoiseImageFilterIUS2IUS2_cast = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS2IUS2_cast

class itkAdditiveGaussianNoiseImageFilterIUS3IUS3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIUS3IUS3):
    r"""Proxy of C++ itkAdditiveGaussianNoiseImageFilterIUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS3IUS3_Clone)
    GetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS3IUS3_GetMean)
    SetMean = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS3IUS3_SetMean)
    GetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS3IUS3_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS3IUS3_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS3IUS3_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAdditiveGaussianNoiseImageFilterPython.delete_itkAdditiveGaussianNoiseImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkAdditiveGaussianNoiseImageFilterIUS3IUS3

        Create a new object of the class itkAdditiveGaussianNoiseImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAdditiveGaussianNoiseImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAdditiveGaussianNoiseImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAdditiveGaussianNoiseImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAdditiveGaussianNoiseImageFilterIUS3IUS3 in _itkAdditiveGaussianNoiseImageFilterPython:
_itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS3IUS3_swigregister(itkAdditiveGaussianNoiseImageFilterIUS3IUS3)
itkAdditiveGaussianNoiseImageFilterIUS3IUS3___New_orig__ = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS3IUS3___New_orig__
itkAdditiveGaussianNoiseImageFilterIUS3IUS3_cast = _itkAdditiveGaussianNoiseImageFilterPython.itkAdditiveGaussianNoiseImageFilterIUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def additive_gaussian_noise_image_filter(*args, **kwargs):
    """Procedural interface for AdditiveGaussianNoiseImageFilter"""
    import itk
    instance = itk.AdditiveGaussianNoiseImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def additive_gaussian_noise_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.AdditiveGaussianNoiseImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.AdditiveGaussianNoiseImageFilter.values()[0]
    else:
        filter_object = itk.AdditiveGaussianNoiseImageFilter

    additive_gaussian_noise_image_filter.__doc__ = filter_object.__doc__
    additive_gaussian_noise_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    additive_gaussian_noise_image_filter.__doc__ += "Available Keyword Arguments:\n"
    additive_gaussian_noise_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



