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
    from . import _itkBinaryGrindPeakImageFilterPython
else:
    import _itkBinaryGrindPeakImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBinaryGrindPeakImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBinaryGrindPeakImageFilterPython.SWIG_PyStaticMethod_New

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
import itkImageToImageFilterAPython
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

def itkBinaryGrindPeakImageFilterIUS3_New():
  return itkBinaryGrindPeakImageFilterIUS3.New()


def itkBinaryGrindPeakImageFilterIUS2_New():
  return itkBinaryGrindPeakImageFilterIUS2.New()


def itkBinaryGrindPeakImageFilterIUC3_New():
  return itkBinaryGrindPeakImageFilterIUC3.New()


def itkBinaryGrindPeakImageFilterIUC2_New():
  return itkBinaryGrindPeakImageFilterIUC2.New()


def itkBinaryGrindPeakImageFilterISS3_New():
  return itkBinaryGrindPeakImageFilterISS3.New()


def itkBinaryGrindPeakImageFilterISS2_New():
  return itkBinaryGrindPeakImageFilterISS2.New()

class itkBinaryGrindPeakImageFilterISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    r"""Proxy of C++ itkBinaryGrindPeakImageFilterISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS2_FullyConnectedOff)
    InputOStreamWritableCheck = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS2_InputOStreamWritableCheck
    
    SetForegroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS2_GetForegroundValue)
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS2_GetBackgroundValue)
    __swig_destroy__ = _itkBinaryGrindPeakImageFilterPython.delete_itkBinaryGrindPeakImageFilterISS2
    cast = _swig_new_static_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryGrindPeakImageFilterISS2

        Create a new object of the class itkBinaryGrindPeakImageFilterISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryGrindPeakImageFilterISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryGrindPeakImageFilterISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryGrindPeakImageFilterISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryGrindPeakImageFilterISS2 in _itkBinaryGrindPeakImageFilterPython:
_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS2_swigregister(itkBinaryGrindPeakImageFilterISS2)
itkBinaryGrindPeakImageFilterISS2___New_orig__ = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS2___New_orig__
itkBinaryGrindPeakImageFilterISS2_cast = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS2_cast

class itkBinaryGrindPeakImageFilterISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    r"""Proxy of C++ itkBinaryGrindPeakImageFilterISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS3_FullyConnectedOff)
    InputOStreamWritableCheck = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS3_InputOStreamWritableCheck
    
    SetForegroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS3_GetForegroundValue)
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS3_GetBackgroundValue)
    __swig_destroy__ = _itkBinaryGrindPeakImageFilterPython.delete_itkBinaryGrindPeakImageFilterISS3
    cast = _swig_new_static_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryGrindPeakImageFilterISS3

        Create a new object of the class itkBinaryGrindPeakImageFilterISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryGrindPeakImageFilterISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryGrindPeakImageFilterISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryGrindPeakImageFilterISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryGrindPeakImageFilterISS3 in _itkBinaryGrindPeakImageFilterPython:
_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS3_swigregister(itkBinaryGrindPeakImageFilterISS3)
itkBinaryGrindPeakImageFilterISS3___New_orig__ = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS3___New_orig__
itkBinaryGrindPeakImageFilterISS3_cast = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterISS3_cast

class itkBinaryGrindPeakImageFilterIUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    r"""Proxy of C++ itkBinaryGrindPeakImageFilterIUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC2_FullyConnectedOff)
    InputOStreamWritableCheck = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC2_InputOStreamWritableCheck
    
    SetForegroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC2_GetForegroundValue)
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC2_GetBackgroundValue)
    __swig_destroy__ = _itkBinaryGrindPeakImageFilterPython.delete_itkBinaryGrindPeakImageFilterIUC2
    cast = _swig_new_static_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryGrindPeakImageFilterIUC2

        Create a new object of the class itkBinaryGrindPeakImageFilterIUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryGrindPeakImageFilterIUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryGrindPeakImageFilterIUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryGrindPeakImageFilterIUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryGrindPeakImageFilterIUC2 in _itkBinaryGrindPeakImageFilterPython:
_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC2_swigregister(itkBinaryGrindPeakImageFilterIUC2)
itkBinaryGrindPeakImageFilterIUC2___New_orig__ = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC2___New_orig__
itkBinaryGrindPeakImageFilterIUC2_cast = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC2_cast

class itkBinaryGrindPeakImageFilterIUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    r"""Proxy of C++ itkBinaryGrindPeakImageFilterIUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC3_FullyConnectedOff)
    InputOStreamWritableCheck = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC3_InputOStreamWritableCheck
    
    SetForegroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC3_GetForegroundValue)
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC3_GetBackgroundValue)
    __swig_destroy__ = _itkBinaryGrindPeakImageFilterPython.delete_itkBinaryGrindPeakImageFilterIUC3
    cast = _swig_new_static_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryGrindPeakImageFilterIUC3

        Create a new object of the class itkBinaryGrindPeakImageFilterIUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryGrindPeakImageFilterIUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryGrindPeakImageFilterIUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryGrindPeakImageFilterIUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryGrindPeakImageFilterIUC3 in _itkBinaryGrindPeakImageFilterPython:
_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC3_swigregister(itkBinaryGrindPeakImageFilterIUC3)
itkBinaryGrindPeakImageFilterIUC3___New_orig__ = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC3___New_orig__
itkBinaryGrindPeakImageFilterIUC3_cast = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUC3_cast

class itkBinaryGrindPeakImageFilterIUS2(itkImageToImageFilterAPython.itkImageToImageFilterIUS2IUS2):
    r"""Proxy of C++ itkBinaryGrindPeakImageFilterIUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS2_FullyConnectedOff)
    InputOStreamWritableCheck = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS2_InputOStreamWritableCheck
    
    SetForegroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS2_GetForegroundValue)
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS2_GetBackgroundValue)
    __swig_destroy__ = _itkBinaryGrindPeakImageFilterPython.delete_itkBinaryGrindPeakImageFilterIUS2
    cast = _swig_new_static_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryGrindPeakImageFilterIUS2

        Create a new object of the class itkBinaryGrindPeakImageFilterIUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryGrindPeakImageFilterIUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryGrindPeakImageFilterIUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryGrindPeakImageFilterIUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryGrindPeakImageFilterIUS2 in _itkBinaryGrindPeakImageFilterPython:
_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS2_swigregister(itkBinaryGrindPeakImageFilterIUS2)
itkBinaryGrindPeakImageFilterIUS2___New_orig__ = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS2___New_orig__
itkBinaryGrindPeakImageFilterIUS2_cast = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS2_cast

class itkBinaryGrindPeakImageFilterIUS3(itkImageToImageFilterAPython.itkImageToImageFilterIUS3IUS3):
    r"""Proxy of C++ itkBinaryGrindPeakImageFilterIUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS3_FullyConnectedOff)
    InputOStreamWritableCheck = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS3_InputOStreamWritableCheck
    
    SetForegroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS3_GetForegroundValue)
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS3_GetBackgroundValue)
    __swig_destroy__ = _itkBinaryGrindPeakImageFilterPython.delete_itkBinaryGrindPeakImageFilterIUS3
    cast = _swig_new_static_method(_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryGrindPeakImageFilterIUS3

        Create a new object of the class itkBinaryGrindPeakImageFilterIUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryGrindPeakImageFilterIUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryGrindPeakImageFilterIUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryGrindPeakImageFilterIUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryGrindPeakImageFilterIUS3 in _itkBinaryGrindPeakImageFilterPython:
_itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS3_swigregister(itkBinaryGrindPeakImageFilterIUS3)
itkBinaryGrindPeakImageFilterIUS3___New_orig__ = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS3___New_orig__
itkBinaryGrindPeakImageFilterIUS3_cast = _itkBinaryGrindPeakImageFilterPython.itkBinaryGrindPeakImageFilterIUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def binary_grind_peak_image_filter(*args, **kwargs):
    """Procedural interface for BinaryGrindPeakImageFilter"""
    import itk
    instance = itk.BinaryGrindPeakImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def binary_grind_peak_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.BinaryGrindPeakImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.BinaryGrindPeakImageFilter.values()[0]
    else:
        filter_object = itk.BinaryGrindPeakImageFilter

    binary_grind_peak_image_filter.__doc__ = filter_object.__doc__
    binary_grind_peak_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    binary_grind_peak_image_filter.__doc__ += "Available Keyword Arguments:\n"
    binary_grind_peak_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



