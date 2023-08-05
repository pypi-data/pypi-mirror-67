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
    from . import _itkApproximateSignedDistanceMapImageFilterPython
else:
    import _itkApproximateSignedDistanceMapImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkApproximateSignedDistanceMapImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkApproximateSignedDistanceMapImageFilterPython.SWIG_PyStaticMethod_New

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
import ITKCommonBasePython
import pyBasePython
import itkVectorImagePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
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
import itkImageRegionPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython

def itkApproximateSignedDistanceMapImageFilterID3ID3_New():
  return itkApproximateSignedDistanceMapImageFilterID3ID3.New()


def itkApproximateSignedDistanceMapImageFilterID2ID2_New():
  return itkApproximateSignedDistanceMapImageFilterID2ID2.New()


def itkApproximateSignedDistanceMapImageFilterIF3IF3_New():
  return itkApproximateSignedDistanceMapImageFilterIF3IF3.New()


def itkApproximateSignedDistanceMapImageFilterIF2IF2_New():
  return itkApproximateSignedDistanceMapImageFilterIF2IF2.New()


def itkApproximateSignedDistanceMapImageFilterISS3ISS3_New():
  return itkApproximateSignedDistanceMapImageFilterISS3ISS3.New()


def itkApproximateSignedDistanceMapImageFilterISS2ISS2_New():
  return itkApproximateSignedDistanceMapImageFilterISS2ISS2.New()

class itkApproximateSignedDistanceMapImageFilterID2ID2(itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    r"""Proxy of C++ itkApproximateSignedDistanceMapImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID2ID2_Clone)
    SetInsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID2ID2_SetInsideValue)
    GetInsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID2ID2_GetInsideValue)
    SetOutsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID2ID2_SetOutsideValue)
    GetOutsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID2ID2_GetOutsideValue)
    InputEqualityComparableCheck = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID2ID2_InputEqualityComparableCheck
    
    __swig_destroy__ = _itkApproximateSignedDistanceMapImageFilterPython.delete_itkApproximateSignedDistanceMapImageFilterID2ID2
    cast = _swig_new_static_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkApproximateSignedDistanceMapImageFilterID2ID2

        Create a new object of the class itkApproximateSignedDistanceMapImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkApproximateSignedDistanceMapImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkApproximateSignedDistanceMapImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkApproximateSignedDistanceMapImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkApproximateSignedDistanceMapImageFilterID2ID2 in _itkApproximateSignedDistanceMapImageFilterPython:
_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID2ID2_swigregister(itkApproximateSignedDistanceMapImageFilterID2ID2)
itkApproximateSignedDistanceMapImageFilterID2ID2___New_orig__ = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID2ID2___New_orig__
itkApproximateSignedDistanceMapImageFilterID2ID2_cast = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID2ID2_cast

class itkApproximateSignedDistanceMapImageFilterID3ID3(itkImageToImageFilterAPython.itkImageToImageFilterID3ID3):
    r"""Proxy of C++ itkApproximateSignedDistanceMapImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID3ID3_Clone)
    SetInsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID3ID3_SetInsideValue)
    GetInsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID3ID3_GetInsideValue)
    SetOutsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID3ID3_SetOutsideValue)
    GetOutsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID3ID3_GetOutsideValue)
    InputEqualityComparableCheck = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID3ID3_InputEqualityComparableCheck
    
    __swig_destroy__ = _itkApproximateSignedDistanceMapImageFilterPython.delete_itkApproximateSignedDistanceMapImageFilterID3ID3
    cast = _swig_new_static_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkApproximateSignedDistanceMapImageFilterID3ID3

        Create a new object of the class itkApproximateSignedDistanceMapImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkApproximateSignedDistanceMapImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkApproximateSignedDistanceMapImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkApproximateSignedDistanceMapImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkApproximateSignedDistanceMapImageFilterID3ID3 in _itkApproximateSignedDistanceMapImageFilterPython:
_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID3ID3_swigregister(itkApproximateSignedDistanceMapImageFilterID3ID3)
itkApproximateSignedDistanceMapImageFilterID3ID3___New_orig__ = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID3ID3___New_orig__
itkApproximateSignedDistanceMapImageFilterID3ID3_cast = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterID3ID3_cast

class itkApproximateSignedDistanceMapImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    r"""Proxy of C++ itkApproximateSignedDistanceMapImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_Clone)
    SetInsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_SetInsideValue)
    GetInsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_GetInsideValue)
    SetOutsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_SetOutsideValue)
    GetOutsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_GetOutsideValue)
    InputEqualityComparableCheck = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_InputEqualityComparableCheck
    
    __swig_destroy__ = _itkApproximateSignedDistanceMapImageFilterPython.delete_itkApproximateSignedDistanceMapImageFilterIF2IF2
    cast = _swig_new_static_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkApproximateSignedDistanceMapImageFilterIF2IF2

        Create a new object of the class itkApproximateSignedDistanceMapImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkApproximateSignedDistanceMapImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkApproximateSignedDistanceMapImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkApproximateSignedDistanceMapImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkApproximateSignedDistanceMapImageFilterIF2IF2 in _itkApproximateSignedDistanceMapImageFilterPython:
_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_swigregister(itkApproximateSignedDistanceMapImageFilterIF2IF2)
itkApproximateSignedDistanceMapImageFilterIF2IF2___New_orig__ = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2___New_orig__
itkApproximateSignedDistanceMapImageFilterIF2IF2_cast = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF2IF2_cast

class itkApproximateSignedDistanceMapImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    r"""Proxy of C++ itkApproximateSignedDistanceMapImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_Clone)
    SetInsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_SetInsideValue)
    GetInsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_GetInsideValue)
    SetOutsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_SetOutsideValue)
    GetOutsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_GetOutsideValue)
    InputEqualityComparableCheck = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_InputEqualityComparableCheck
    
    __swig_destroy__ = _itkApproximateSignedDistanceMapImageFilterPython.delete_itkApproximateSignedDistanceMapImageFilterIF3IF3
    cast = _swig_new_static_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkApproximateSignedDistanceMapImageFilterIF3IF3

        Create a new object of the class itkApproximateSignedDistanceMapImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkApproximateSignedDistanceMapImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkApproximateSignedDistanceMapImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkApproximateSignedDistanceMapImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkApproximateSignedDistanceMapImageFilterIF3IF3 in _itkApproximateSignedDistanceMapImageFilterPython:
_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_swigregister(itkApproximateSignedDistanceMapImageFilterIF3IF3)
itkApproximateSignedDistanceMapImageFilterIF3IF3___New_orig__ = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3___New_orig__
itkApproximateSignedDistanceMapImageFilterIF3IF3_cast = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterIF3IF3_cast

class itkApproximateSignedDistanceMapImageFilterISS2ISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    r"""Proxy of C++ itkApproximateSignedDistanceMapImageFilterISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_Clone)
    SetInsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_SetInsideValue)
    GetInsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_GetInsideValue)
    SetOutsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_SetOutsideValue)
    GetOutsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_GetOutsideValue)
    InputEqualityComparableCheck = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_InputEqualityComparableCheck
    
    __swig_destroy__ = _itkApproximateSignedDistanceMapImageFilterPython.delete_itkApproximateSignedDistanceMapImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkApproximateSignedDistanceMapImageFilterISS2ISS2

        Create a new object of the class itkApproximateSignedDistanceMapImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkApproximateSignedDistanceMapImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkApproximateSignedDistanceMapImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkApproximateSignedDistanceMapImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkApproximateSignedDistanceMapImageFilterISS2ISS2 in _itkApproximateSignedDistanceMapImageFilterPython:
_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_swigregister(itkApproximateSignedDistanceMapImageFilterISS2ISS2)
itkApproximateSignedDistanceMapImageFilterISS2ISS2___New_orig__ = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2___New_orig__
itkApproximateSignedDistanceMapImageFilterISS2ISS2_cast = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS2ISS2_cast

class itkApproximateSignedDistanceMapImageFilterISS3ISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    r"""Proxy of C++ itkApproximateSignedDistanceMapImageFilterISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_Clone)
    SetInsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_SetInsideValue)
    GetInsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_GetInsideValue)
    SetOutsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_SetOutsideValue)
    GetOutsideValue = _swig_new_instance_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_GetOutsideValue)
    InputEqualityComparableCheck = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_InputEqualityComparableCheck
    
    __swig_destroy__ = _itkApproximateSignedDistanceMapImageFilterPython.delete_itkApproximateSignedDistanceMapImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkApproximateSignedDistanceMapImageFilterISS3ISS3

        Create a new object of the class itkApproximateSignedDistanceMapImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkApproximateSignedDistanceMapImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkApproximateSignedDistanceMapImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkApproximateSignedDistanceMapImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkApproximateSignedDistanceMapImageFilterISS3ISS3 in _itkApproximateSignedDistanceMapImageFilterPython:
_itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_swigregister(itkApproximateSignedDistanceMapImageFilterISS3ISS3)
itkApproximateSignedDistanceMapImageFilterISS3ISS3___New_orig__ = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3___New_orig__
itkApproximateSignedDistanceMapImageFilterISS3ISS3_cast = _itkApproximateSignedDistanceMapImageFilterPython.itkApproximateSignedDistanceMapImageFilterISS3ISS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def approximate_signed_distance_map_image_filter(*args, **kwargs):
    """Procedural interface for ApproximateSignedDistanceMapImageFilter"""
    import itk
    instance = itk.ApproximateSignedDistanceMapImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def approximate_signed_distance_map_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ApproximateSignedDistanceMapImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.ApproximateSignedDistanceMapImageFilter.values()[0]
    else:
        filter_object = itk.ApproximateSignedDistanceMapImageFilter

    approximate_signed_distance_map_image_filter.__doc__ = filter_object.__doc__
    approximate_signed_distance_map_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    approximate_signed_distance_map_image_filter.__doc__ += "Available Keyword Arguments:\n"
    approximate_signed_distance_map_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



