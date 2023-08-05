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
    from . import _itkBinaryFillholeImageFilterPython
else:
    import _itkBinaryFillholeImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBinaryFillholeImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBinaryFillholeImageFilterPython.SWIG_PyStaticMethod_New

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

def itkBinaryFillholeImageFilterIUS3_New():
  return itkBinaryFillholeImageFilterIUS3.New()


def itkBinaryFillholeImageFilterIUS2_New():
  return itkBinaryFillholeImageFilterIUS2.New()


def itkBinaryFillholeImageFilterIUC3_New():
  return itkBinaryFillholeImageFilterIUC3.New()


def itkBinaryFillholeImageFilterIUC2_New():
  return itkBinaryFillholeImageFilterIUC2.New()


def itkBinaryFillholeImageFilterISS3_New():
  return itkBinaryFillholeImageFilterISS3.New()


def itkBinaryFillholeImageFilterISS2_New():
  return itkBinaryFillholeImageFilterISS2.New()

class itkBinaryFillholeImageFilterISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    r"""Proxy of C++ itkBinaryFillholeImageFilterISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_FullyConnectedOff)
    InputOStreamWritableCheck = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_InputOStreamWritableCheck
    
    SetForegroundValue = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_GetForegroundValue)
    __swig_destroy__ = _itkBinaryFillholeImageFilterPython.delete_itkBinaryFillholeImageFilterISS2
    cast = _swig_new_static_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryFillholeImageFilterISS2

        Create a new object of the class itkBinaryFillholeImageFilterISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryFillholeImageFilterISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryFillholeImageFilterISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryFillholeImageFilterISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryFillholeImageFilterISS2 in _itkBinaryFillholeImageFilterPython:
_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_swigregister(itkBinaryFillholeImageFilterISS2)
itkBinaryFillholeImageFilterISS2___New_orig__ = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2___New_orig__
itkBinaryFillholeImageFilterISS2_cast = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS2_cast

class itkBinaryFillholeImageFilterISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    r"""Proxy of C++ itkBinaryFillholeImageFilterISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_FullyConnectedOff)
    InputOStreamWritableCheck = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_InputOStreamWritableCheck
    
    SetForegroundValue = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_GetForegroundValue)
    __swig_destroy__ = _itkBinaryFillholeImageFilterPython.delete_itkBinaryFillholeImageFilterISS3
    cast = _swig_new_static_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryFillholeImageFilterISS3

        Create a new object of the class itkBinaryFillholeImageFilterISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryFillholeImageFilterISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryFillholeImageFilterISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryFillholeImageFilterISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryFillholeImageFilterISS3 in _itkBinaryFillholeImageFilterPython:
_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_swigregister(itkBinaryFillholeImageFilterISS3)
itkBinaryFillholeImageFilterISS3___New_orig__ = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3___New_orig__
itkBinaryFillholeImageFilterISS3_cast = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterISS3_cast

class itkBinaryFillholeImageFilterIUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    r"""Proxy of C++ itkBinaryFillholeImageFilterIUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_FullyConnectedOff)
    InputOStreamWritableCheck = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_InputOStreamWritableCheck
    
    SetForegroundValue = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_GetForegroundValue)
    __swig_destroy__ = _itkBinaryFillholeImageFilterPython.delete_itkBinaryFillholeImageFilterIUC2
    cast = _swig_new_static_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryFillholeImageFilterIUC2

        Create a new object of the class itkBinaryFillholeImageFilterIUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryFillholeImageFilterIUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryFillholeImageFilterIUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryFillholeImageFilterIUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryFillholeImageFilterIUC2 in _itkBinaryFillholeImageFilterPython:
_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_swigregister(itkBinaryFillholeImageFilterIUC2)
itkBinaryFillholeImageFilterIUC2___New_orig__ = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2___New_orig__
itkBinaryFillholeImageFilterIUC2_cast = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC2_cast

class itkBinaryFillholeImageFilterIUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    r"""Proxy of C++ itkBinaryFillholeImageFilterIUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_FullyConnectedOff)
    InputOStreamWritableCheck = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_InputOStreamWritableCheck
    
    SetForegroundValue = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_GetForegroundValue)
    __swig_destroy__ = _itkBinaryFillholeImageFilterPython.delete_itkBinaryFillholeImageFilterIUC3
    cast = _swig_new_static_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryFillholeImageFilterIUC3

        Create a new object of the class itkBinaryFillholeImageFilterIUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryFillholeImageFilterIUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryFillholeImageFilterIUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryFillholeImageFilterIUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryFillholeImageFilterIUC3 in _itkBinaryFillholeImageFilterPython:
_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_swigregister(itkBinaryFillholeImageFilterIUC3)
itkBinaryFillholeImageFilterIUC3___New_orig__ = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3___New_orig__
itkBinaryFillholeImageFilterIUC3_cast = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUC3_cast

class itkBinaryFillholeImageFilterIUS2(itkImageToImageFilterAPython.itkImageToImageFilterIUS2IUS2):
    r"""Proxy of C++ itkBinaryFillholeImageFilterIUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS2_FullyConnectedOff)
    InputOStreamWritableCheck = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS2_InputOStreamWritableCheck
    
    SetForegroundValue = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS2_GetForegroundValue)
    __swig_destroy__ = _itkBinaryFillholeImageFilterPython.delete_itkBinaryFillholeImageFilterIUS2
    cast = _swig_new_static_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryFillholeImageFilterIUS2

        Create a new object of the class itkBinaryFillholeImageFilterIUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryFillholeImageFilterIUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryFillholeImageFilterIUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryFillholeImageFilterIUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryFillholeImageFilterIUS2 in _itkBinaryFillholeImageFilterPython:
_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS2_swigregister(itkBinaryFillholeImageFilterIUS2)
itkBinaryFillholeImageFilterIUS2___New_orig__ = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS2___New_orig__
itkBinaryFillholeImageFilterIUS2_cast = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS2_cast

class itkBinaryFillholeImageFilterIUS3(itkImageToImageFilterAPython.itkImageToImageFilterIUS3IUS3):
    r"""Proxy of C++ itkBinaryFillholeImageFilterIUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS3_FullyConnectedOff)
    InputOStreamWritableCheck = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS3_InputOStreamWritableCheck
    
    SetForegroundValue = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS3_GetForegroundValue)
    __swig_destroy__ = _itkBinaryFillholeImageFilterPython.delete_itkBinaryFillholeImageFilterIUS3
    cast = _swig_new_static_method(_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryFillholeImageFilterIUS3

        Create a new object of the class itkBinaryFillholeImageFilterIUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryFillholeImageFilterIUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryFillholeImageFilterIUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryFillholeImageFilterIUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryFillholeImageFilterIUS3 in _itkBinaryFillholeImageFilterPython:
_itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS3_swigregister(itkBinaryFillholeImageFilterIUS3)
itkBinaryFillholeImageFilterIUS3___New_orig__ = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS3___New_orig__
itkBinaryFillholeImageFilterIUS3_cast = _itkBinaryFillholeImageFilterPython.itkBinaryFillholeImageFilterIUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def binary_fillhole_image_filter(*args, **kwargs):
    """Procedural interface for BinaryFillholeImageFilter"""
    import itk
    instance = itk.BinaryFillholeImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def binary_fillhole_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.BinaryFillholeImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.BinaryFillholeImageFilter.values()[0]
    else:
        filter_object = itk.BinaryFillholeImageFilter

    binary_fillhole_image_filter.__doc__ = filter_object.__doc__
    binary_fillhole_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    binary_fillhole_image_filter.__doc__ += "Available Keyword Arguments:\n"
    binary_fillhole_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



