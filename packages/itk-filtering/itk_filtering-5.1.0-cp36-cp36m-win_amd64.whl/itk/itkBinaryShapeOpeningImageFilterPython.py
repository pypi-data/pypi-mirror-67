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
    from . import _itkBinaryShapeOpeningImageFilterPython
else:
    import _itkBinaryShapeOpeningImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBinaryShapeOpeningImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBinaryShapeOpeningImageFilterPython.SWIG_PyStaticMethod_New

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

def itkBinaryShapeOpeningImageFilterIUS3_New():
  return itkBinaryShapeOpeningImageFilterIUS3.New()


def itkBinaryShapeOpeningImageFilterIUS2_New():
  return itkBinaryShapeOpeningImageFilterIUS2.New()


def itkBinaryShapeOpeningImageFilterIUC3_New():
  return itkBinaryShapeOpeningImageFilterIUC3.New()


def itkBinaryShapeOpeningImageFilterIUC2_New():
  return itkBinaryShapeOpeningImageFilterIUC2.New()


def itkBinaryShapeOpeningImageFilterISS3_New():
  return itkBinaryShapeOpeningImageFilterISS3.New()


def itkBinaryShapeOpeningImageFilterISS2_New():
  return itkBinaryShapeOpeningImageFilterISS2.New()

class itkBinaryShapeOpeningImageFilterISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    r"""Proxy of C++ itkBinaryShapeOpeningImageFilterISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_FullyConnectedOff)
    InputEqualityComparableCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_InputEqualityComparableCheck
    
    IntConvertibleToInputCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_IntConvertibleToInputCheck
    
    InputOStreamWritableCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_InputOStreamWritableCheck
    
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_GetForegroundValue)
    GetLambda = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_GetLambda)
    SetLambda = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_SetLambda)
    GetReverseOrdering = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_GetReverseOrdering)
    SetReverseOrdering = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_SetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_SetAttribute)
    __swig_destroy__ = _itkBinaryShapeOpeningImageFilterPython.delete_itkBinaryShapeOpeningImageFilterISS2
    cast = _swig_new_static_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryShapeOpeningImageFilterISS2

        Create a new object of the class itkBinaryShapeOpeningImageFilterISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryShapeOpeningImageFilterISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryShapeOpeningImageFilterISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryShapeOpeningImageFilterISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryShapeOpeningImageFilterISS2 in _itkBinaryShapeOpeningImageFilterPython:
_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_swigregister(itkBinaryShapeOpeningImageFilterISS2)
itkBinaryShapeOpeningImageFilterISS2___New_orig__ = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2___New_orig__
itkBinaryShapeOpeningImageFilterISS2_cast = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS2_cast

class itkBinaryShapeOpeningImageFilterISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    r"""Proxy of C++ itkBinaryShapeOpeningImageFilterISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_FullyConnectedOff)
    InputEqualityComparableCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_InputEqualityComparableCheck
    
    IntConvertibleToInputCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_IntConvertibleToInputCheck
    
    InputOStreamWritableCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_InputOStreamWritableCheck
    
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_GetForegroundValue)
    GetLambda = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_GetLambda)
    SetLambda = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_SetLambda)
    GetReverseOrdering = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_GetReverseOrdering)
    SetReverseOrdering = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_SetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_SetAttribute)
    __swig_destroy__ = _itkBinaryShapeOpeningImageFilterPython.delete_itkBinaryShapeOpeningImageFilterISS3
    cast = _swig_new_static_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryShapeOpeningImageFilterISS3

        Create a new object of the class itkBinaryShapeOpeningImageFilterISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryShapeOpeningImageFilterISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryShapeOpeningImageFilterISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryShapeOpeningImageFilterISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryShapeOpeningImageFilterISS3 in _itkBinaryShapeOpeningImageFilterPython:
_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_swigregister(itkBinaryShapeOpeningImageFilterISS3)
itkBinaryShapeOpeningImageFilterISS3___New_orig__ = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3___New_orig__
itkBinaryShapeOpeningImageFilterISS3_cast = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterISS3_cast

class itkBinaryShapeOpeningImageFilterIUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    r"""Proxy of C++ itkBinaryShapeOpeningImageFilterIUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_FullyConnectedOff)
    InputEqualityComparableCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_InputEqualityComparableCheck
    
    IntConvertibleToInputCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_IntConvertibleToInputCheck
    
    InputOStreamWritableCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_InputOStreamWritableCheck
    
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_GetForegroundValue)
    GetLambda = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_GetLambda)
    SetLambda = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_SetLambda)
    GetReverseOrdering = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_GetReverseOrdering)
    SetReverseOrdering = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_SetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_SetAttribute)
    __swig_destroy__ = _itkBinaryShapeOpeningImageFilterPython.delete_itkBinaryShapeOpeningImageFilterIUC2
    cast = _swig_new_static_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryShapeOpeningImageFilterIUC2

        Create a new object of the class itkBinaryShapeOpeningImageFilterIUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryShapeOpeningImageFilterIUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryShapeOpeningImageFilterIUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryShapeOpeningImageFilterIUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryShapeOpeningImageFilterIUC2 in _itkBinaryShapeOpeningImageFilterPython:
_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_swigregister(itkBinaryShapeOpeningImageFilterIUC2)
itkBinaryShapeOpeningImageFilterIUC2___New_orig__ = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2___New_orig__
itkBinaryShapeOpeningImageFilterIUC2_cast = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC2_cast

class itkBinaryShapeOpeningImageFilterIUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    r"""Proxy of C++ itkBinaryShapeOpeningImageFilterIUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_FullyConnectedOff)
    InputEqualityComparableCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_InputEqualityComparableCheck
    
    IntConvertibleToInputCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_IntConvertibleToInputCheck
    
    InputOStreamWritableCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_InputOStreamWritableCheck
    
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_GetForegroundValue)
    GetLambda = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_GetLambda)
    SetLambda = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_SetLambda)
    GetReverseOrdering = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_GetReverseOrdering)
    SetReverseOrdering = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_SetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_SetAttribute)
    __swig_destroy__ = _itkBinaryShapeOpeningImageFilterPython.delete_itkBinaryShapeOpeningImageFilterIUC3
    cast = _swig_new_static_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryShapeOpeningImageFilterIUC3

        Create a new object of the class itkBinaryShapeOpeningImageFilterIUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryShapeOpeningImageFilterIUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryShapeOpeningImageFilterIUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryShapeOpeningImageFilterIUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryShapeOpeningImageFilterIUC3 in _itkBinaryShapeOpeningImageFilterPython:
_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_swigregister(itkBinaryShapeOpeningImageFilterIUC3)
itkBinaryShapeOpeningImageFilterIUC3___New_orig__ = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3___New_orig__
itkBinaryShapeOpeningImageFilterIUC3_cast = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUC3_cast

class itkBinaryShapeOpeningImageFilterIUS2(itkImageToImageFilterAPython.itkImageToImageFilterIUS2IUS2):
    r"""Proxy of C++ itkBinaryShapeOpeningImageFilterIUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_FullyConnectedOff)
    InputEqualityComparableCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_InputEqualityComparableCheck
    
    IntConvertibleToInputCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_IntConvertibleToInputCheck
    
    InputOStreamWritableCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_InputOStreamWritableCheck
    
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_GetForegroundValue)
    GetLambda = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_GetLambda)
    SetLambda = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_SetLambda)
    GetReverseOrdering = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_GetReverseOrdering)
    SetReverseOrdering = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_SetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_SetAttribute)
    __swig_destroy__ = _itkBinaryShapeOpeningImageFilterPython.delete_itkBinaryShapeOpeningImageFilterIUS2
    cast = _swig_new_static_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryShapeOpeningImageFilterIUS2

        Create a new object of the class itkBinaryShapeOpeningImageFilterIUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryShapeOpeningImageFilterIUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryShapeOpeningImageFilterIUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryShapeOpeningImageFilterIUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryShapeOpeningImageFilterIUS2 in _itkBinaryShapeOpeningImageFilterPython:
_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_swigregister(itkBinaryShapeOpeningImageFilterIUS2)
itkBinaryShapeOpeningImageFilterIUS2___New_orig__ = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2___New_orig__
itkBinaryShapeOpeningImageFilterIUS2_cast = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS2_cast

class itkBinaryShapeOpeningImageFilterIUS3(itkImageToImageFilterAPython.itkImageToImageFilterIUS3IUS3):
    r"""Proxy of C++ itkBinaryShapeOpeningImageFilterIUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_FullyConnectedOff)
    InputEqualityComparableCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_InputEqualityComparableCheck
    
    IntConvertibleToInputCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_IntConvertibleToInputCheck
    
    InputOStreamWritableCheck = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_InputOStreamWritableCheck
    
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_GetForegroundValue)
    GetLambda = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_GetLambda)
    SetLambda = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_SetLambda)
    GetReverseOrdering = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_GetReverseOrdering)
    SetReverseOrdering = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_SetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_SetAttribute)
    __swig_destroy__ = _itkBinaryShapeOpeningImageFilterPython.delete_itkBinaryShapeOpeningImageFilterIUS3
    cast = _swig_new_static_method(_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryShapeOpeningImageFilterIUS3

        Create a new object of the class itkBinaryShapeOpeningImageFilterIUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryShapeOpeningImageFilterIUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryShapeOpeningImageFilterIUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryShapeOpeningImageFilterIUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryShapeOpeningImageFilterIUS3 in _itkBinaryShapeOpeningImageFilterPython:
_itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_swigregister(itkBinaryShapeOpeningImageFilterIUS3)
itkBinaryShapeOpeningImageFilterIUS3___New_orig__ = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3___New_orig__
itkBinaryShapeOpeningImageFilterIUS3_cast = _itkBinaryShapeOpeningImageFilterPython.itkBinaryShapeOpeningImageFilterIUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def binary_shape_opening_image_filter(*args, **kwargs):
    """Procedural interface for BinaryShapeOpeningImageFilter"""
    import itk
    instance = itk.BinaryShapeOpeningImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def binary_shape_opening_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.BinaryShapeOpeningImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.BinaryShapeOpeningImageFilter.values()[0]
    else:
        filter_object = itk.BinaryShapeOpeningImageFilter

    binary_shape_opening_image_filter.__doc__ = filter_object.__doc__
    binary_shape_opening_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    binary_shape_opening_image_filter.__doc__ += "Available Keyword Arguments:\n"
    binary_shape_opening_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



