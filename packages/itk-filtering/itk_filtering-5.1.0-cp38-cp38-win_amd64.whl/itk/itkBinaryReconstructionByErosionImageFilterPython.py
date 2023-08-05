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
    from . import _itkBinaryReconstructionByErosionImageFilterPython
else:
    import _itkBinaryReconstructionByErosionImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBinaryReconstructionByErosionImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBinaryReconstructionByErosionImageFilterPython.SWIG_PyStaticMethod_New

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


import itkImagePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import ITKCommonBasePython
import itkMatrixPython
import vnl_matrixPython
import stdcomplexPython
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
import itkImageToImageFilterAPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython

def itkBinaryReconstructionByErosionImageFilterIUS3_New():
  return itkBinaryReconstructionByErosionImageFilterIUS3.New()


def itkBinaryReconstructionByErosionImageFilterIUS2_New():
  return itkBinaryReconstructionByErosionImageFilterIUS2.New()


def itkBinaryReconstructionByErosionImageFilterIUC3_New():
  return itkBinaryReconstructionByErosionImageFilterIUC3.New()


def itkBinaryReconstructionByErosionImageFilterIUC2_New():
  return itkBinaryReconstructionByErosionImageFilterIUC2.New()


def itkBinaryReconstructionByErosionImageFilterISS3_New():
  return itkBinaryReconstructionByErosionImageFilterISS3.New()


def itkBinaryReconstructionByErosionImageFilterISS2_New():
  return itkBinaryReconstructionByErosionImageFilterISS2.New()

class itkBinaryReconstructionByErosionImageFilterISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    r"""Proxy of C++ itkBinaryReconstructionByErosionImageFilterISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_FullyConnectedOff)
    InputEqualityComparableCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_InputEqualityComparableCheck
    
    IntConvertibleToInputCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_IntConvertibleToInputCheck
    
    InputOStreamWritableCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_InputOStreamWritableCheck
    
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_GetForegroundValue)
    SetMarkerImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_SetMarkerImage)
    GetMarkerImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_GetMarkerImage)
    SetMaskImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_SetMaskImage)
    GetMaskImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_GetMaskImage)
    __swig_destroy__ = _itkBinaryReconstructionByErosionImageFilterPython.delete_itkBinaryReconstructionByErosionImageFilterISS2
    cast = _swig_new_static_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryReconstructionByErosionImageFilterISS2

        Create a new object of the class itkBinaryReconstructionByErosionImageFilterISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryReconstructionByErosionImageFilterISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryReconstructionByErosionImageFilterISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryReconstructionByErosionImageFilterISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryReconstructionByErosionImageFilterISS2 in _itkBinaryReconstructionByErosionImageFilterPython:
_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_swigregister(itkBinaryReconstructionByErosionImageFilterISS2)
itkBinaryReconstructionByErosionImageFilterISS2___New_orig__ = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2___New_orig__
itkBinaryReconstructionByErosionImageFilterISS2_cast = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS2_cast

class itkBinaryReconstructionByErosionImageFilterISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    r"""Proxy of C++ itkBinaryReconstructionByErosionImageFilterISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_FullyConnectedOff)
    InputEqualityComparableCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_InputEqualityComparableCheck
    
    IntConvertibleToInputCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_IntConvertibleToInputCheck
    
    InputOStreamWritableCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_InputOStreamWritableCheck
    
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_GetForegroundValue)
    SetMarkerImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_SetMarkerImage)
    GetMarkerImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_GetMarkerImage)
    SetMaskImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_SetMaskImage)
    GetMaskImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_GetMaskImage)
    __swig_destroy__ = _itkBinaryReconstructionByErosionImageFilterPython.delete_itkBinaryReconstructionByErosionImageFilterISS3
    cast = _swig_new_static_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryReconstructionByErosionImageFilterISS3

        Create a new object of the class itkBinaryReconstructionByErosionImageFilterISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryReconstructionByErosionImageFilterISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryReconstructionByErosionImageFilterISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryReconstructionByErosionImageFilterISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryReconstructionByErosionImageFilterISS3 in _itkBinaryReconstructionByErosionImageFilterPython:
_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_swigregister(itkBinaryReconstructionByErosionImageFilterISS3)
itkBinaryReconstructionByErosionImageFilterISS3___New_orig__ = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3___New_orig__
itkBinaryReconstructionByErosionImageFilterISS3_cast = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterISS3_cast

class itkBinaryReconstructionByErosionImageFilterIUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    r"""Proxy of C++ itkBinaryReconstructionByErosionImageFilterIUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_FullyConnectedOff)
    InputEqualityComparableCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_InputEqualityComparableCheck
    
    IntConvertibleToInputCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_IntConvertibleToInputCheck
    
    InputOStreamWritableCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_InputOStreamWritableCheck
    
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_GetForegroundValue)
    SetMarkerImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_SetMarkerImage)
    GetMarkerImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_GetMarkerImage)
    SetMaskImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_SetMaskImage)
    GetMaskImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_GetMaskImage)
    __swig_destroy__ = _itkBinaryReconstructionByErosionImageFilterPython.delete_itkBinaryReconstructionByErosionImageFilterIUC2
    cast = _swig_new_static_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryReconstructionByErosionImageFilterIUC2

        Create a new object of the class itkBinaryReconstructionByErosionImageFilterIUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryReconstructionByErosionImageFilterIUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryReconstructionByErosionImageFilterIUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryReconstructionByErosionImageFilterIUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryReconstructionByErosionImageFilterIUC2 in _itkBinaryReconstructionByErosionImageFilterPython:
_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_swigregister(itkBinaryReconstructionByErosionImageFilterIUC2)
itkBinaryReconstructionByErosionImageFilterIUC2___New_orig__ = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2___New_orig__
itkBinaryReconstructionByErosionImageFilterIUC2_cast = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC2_cast

class itkBinaryReconstructionByErosionImageFilterIUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    r"""Proxy of C++ itkBinaryReconstructionByErosionImageFilterIUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_FullyConnectedOff)
    InputEqualityComparableCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_InputEqualityComparableCheck
    
    IntConvertibleToInputCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_IntConvertibleToInputCheck
    
    InputOStreamWritableCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_InputOStreamWritableCheck
    
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_GetForegroundValue)
    SetMarkerImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_SetMarkerImage)
    GetMarkerImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_GetMarkerImage)
    SetMaskImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_SetMaskImage)
    GetMaskImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_GetMaskImage)
    __swig_destroy__ = _itkBinaryReconstructionByErosionImageFilterPython.delete_itkBinaryReconstructionByErosionImageFilterIUC3
    cast = _swig_new_static_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryReconstructionByErosionImageFilterIUC3

        Create a new object of the class itkBinaryReconstructionByErosionImageFilterIUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryReconstructionByErosionImageFilterIUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryReconstructionByErosionImageFilterIUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryReconstructionByErosionImageFilterIUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryReconstructionByErosionImageFilterIUC3 in _itkBinaryReconstructionByErosionImageFilterPython:
_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_swigregister(itkBinaryReconstructionByErosionImageFilterIUC3)
itkBinaryReconstructionByErosionImageFilterIUC3___New_orig__ = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3___New_orig__
itkBinaryReconstructionByErosionImageFilterIUC3_cast = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUC3_cast

class itkBinaryReconstructionByErosionImageFilterIUS2(itkImageToImageFilterAPython.itkImageToImageFilterIUS2IUS2):
    r"""Proxy of C++ itkBinaryReconstructionByErosionImageFilterIUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_FullyConnectedOff)
    InputEqualityComparableCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_InputEqualityComparableCheck
    
    IntConvertibleToInputCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_IntConvertibleToInputCheck
    
    InputOStreamWritableCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_InputOStreamWritableCheck
    
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_GetForegroundValue)
    SetMarkerImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_SetMarkerImage)
    GetMarkerImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_GetMarkerImage)
    SetMaskImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_SetMaskImage)
    GetMaskImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_GetMaskImage)
    __swig_destroy__ = _itkBinaryReconstructionByErosionImageFilterPython.delete_itkBinaryReconstructionByErosionImageFilterIUS2
    cast = _swig_new_static_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryReconstructionByErosionImageFilterIUS2

        Create a new object of the class itkBinaryReconstructionByErosionImageFilterIUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryReconstructionByErosionImageFilterIUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryReconstructionByErosionImageFilterIUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryReconstructionByErosionImageFilterIUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryReconstructionByErosionImageFilterIUS2 in _itkBinaryReconstructionByErosionImageFilterPython:
_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_swigregister(itkBinaryReconstructionByErosionImageFilterIUS2)
itkBinaryReconstructionByErosionImageFilterIUS2___New_orig__ = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2___New_orig__
itkBinaryReconstructionByErosionImageFilterIUS2_cast = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS2_cast

class itkBinaryReconstructionByErosionImageFilterIUS3(itkImageToImageFilterAPython.itkImageToImageFilterIUS3IUS3):
    r"""Proxy of C++ itkBinaryReconstructionByErosionImageFilterIUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_FullyConnectedOff)
    InputEqualityComparableCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_InputEqualityComparableCheck
    
    IntConvertibleToInputCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_IntConvertibleToInputCheck
    
    InputOStreamWritableCheck = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_InputOStreamWritableCheck
    
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_GetForegroundValue)
    SetMarkerImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_SetMarkerImage)
    GetMarkerImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_GetMarkerImage)
    SetMaskImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_SetMaskImage)
    GetMaskImage = _swig_new_instance_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_GetMaskImage)
    __swig_destroy__ = _itkBinaryReconstructionByErosionImageFilterPython.delete_itkBinaryReconstructionByErosionImageFilterIUS3
    cast = _swig_new_static_method(_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryReconstructionByErosionImageFilterIUS3

        Create a new object of the class itkBinaryReconstructionByErosionImageFilterIUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryReconstructionByErosionImageFilterIUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryReconstructionByErosionImageFilterIUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryReconstructionByErosionImageFilterIUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryReconstructionByErosionImageFilterIUS3 in _itkBinaryReconstructionByErosionImageFilterPython:
_itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_swigregister(itkBinaryReconstructionByErosionImageFilterIUS3)
itkBinaryReconstructionByErosionImageFilterIUS3___New_orig__ = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3___New_orig__
itkBinaryReconstructionByErosionImageFilterIUS3_cast = _itkBinaryReconstructionByErosionImageFilterPython.itkBinaryReconstructionByErosionImageFilterIUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def binary_reconstruction_by_erosion_image_filter(*args, **kwargs):
    """Procedural interface for BinaryReconstructionByErosionImageFilter"""
    import itk
    instance = itk.BinaryReconstructionByErosionImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def binary_reconstruction_by_erosion_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.BinaryReconstructionByErosionImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.BinaryReconstructionByErosionImageFilter.values()[0]
    else:
        filter_object = itk.BinaryReconstructionByErosionImageFilter

    binary_reconstruction_by_erosion_image_filter.__doc__ = filter_object.__doc__
    binary_reconstruction_by_erosion_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    binary_reconstruction_by_erosion_image_filter.__doc__ += "Available Keyword Arguments:\n"
    binary_reconstruction_by_erosion_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



