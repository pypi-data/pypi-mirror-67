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
    from . import _itkGrayscaleFillholeImageFilterPython
else:
    import _itkGrayscaleFillholeImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkGrayscaleFillholeImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkGrayscaleFillholeImageFilterPython.SWIG_PyStaticMethod_New

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

def itkGrayscaleFillholeImageFilterID3ID3_New():
  return itkGrayscaleFillholeImageFilterID3ID3.New()


def itkGrayscaleFillholeImageFilterID2ID2_New():
  return itkGrayscaleFillholeImageFilterID2ID2.New()


def itkGrayscaleFillholeImageFilterIF3IF3_New():
  return itkGrayscaleFillholeImageFilterIF3IF3.New()


def itkGrayscaleFillholeImageFilterIF2IF2_New():
  return itkGrayscaleFillholeImageFilterIF2IF2.New()


def itkGrayscaleFillholeImageFilterIUS3IUS3_New():
  return itkGrayscaleFillholeImageFilterIUS3IUS3.New()


def itkGrayscaleFillholeImageFilterIUS2IUS2_New():
  return itkGrayscaleFillholeImageFilterIUS2IUS2.New()


def itkGrayscaleFillholeImageFilterIUC3IUC3_New():
  return itkGrayscaleFillholeImageFilterIUC3IUC3.New()


def itkGrayscaleFillholeImageFilterIUC2IUC2_New():
  return itkGrayscaleFillholeImageFilterIUC2IUC2.New()


def itkGrayscaleFillholeImageFilterISS3ISS3_New():
  return itkGrayscaleFillholeImageFilterISS3ISS3.New()


def itkGrayscaleFillholeImageFilterISS2ISS2_New():
  return itkGrayscaleFillholeImageFilterISS2ISS2.New()

class itkGrayscaleFillholeImageFilterID2ID2(itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    r"""Proxy of C++ itkGrayscaleFillholeImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID2ID2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID2ID2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID2ID2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID2ID2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID2ID2_FullyConnectedOff)
    InputOStreamWritableCheck = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID2ID2_InputOStreamWritableCheck
    
    __swig_destroy__ = _itkGrayscaleFillholeImageFilterPython.delete_itkGrayscaleFillholeImageFilterID2ID2
    cast = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkGrayscaleFillholeImageFilterID2ID2

        Create a new object of the class itkGrayscaleFillholeImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGrayscaleFillholeImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGrayscaleFillholeImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGrayscaleFillholeImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGrayscaleFillholeImageFilterID2ID2 in _itkGrayscaleFillholeImageFilterPython:
_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID2ID2_swigregister(itkGrayscaleFillholeImageFilterID2ID2)
itkGrayscaleFillholeImageFilterID2ID2___New_orig__ = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID2ID2___New_orig__
itkGrayscaleFillholeImageFilterID2ID2_cast = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID2ID2_cast

class itkGrayscaleFillholeImageFilterID3ID3(itkImageToImageFilterAPython.itkImageToImageFilterID3ID3):
    r"""Proxy of C++ itkGrayscaleFillholeImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID3ID3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID3ID3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID3ID3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID3ID3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID3ID3_FullyConnectedOff)
    InputOStreamWritableCheck = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID3ID3_InputOStreamWritableCheck
    
    __swig_destroy__ = _itkGrayscaleFillholeImageFilterPython.delete_itkGrayscaleFillholeImageFilterID3ID3
    cast = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkGrayscaleFillholeImageFilterID3ID3

        Create a new object of the class itkGrayscaleFillholeImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGrayscaleFillholeImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGrayscaleFillholeImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGrayscaleFillholeImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGrayscaleFillholeImageFilterID3ID3 in _itkGrayscaleFillholeImageFilterPython:
_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID3ID3_swigregister(itkGrayscaleFillholeImageFilterID3ID3)
itkGrayscaleFillholeImageFilterID3ID3___New_orig__ = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID3ID3___New_orig__
itkGrayscaleFillholeImageFilterID3ID3_cast = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterID3ID3_cast

class itkGrayscaleFillholeImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    r"""Proxy of C++ itkGrayscaleFillholeImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF2IF2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF2IF2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF2IF2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF2IF2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF2IF2_FullyConnectedOff)
    InputOStreamWritableCheck = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF2IF2_InputOStreamWritableCheck
    
    __swig_destroy__ = _itkGrayscaleFillholeImageFilterPython.delete_itkGrayscaleFillholeImageFilterIF2IF2
    cast = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkGrayscaleFillholeImageFilterIF2IF2

        Create a new object of the class itkGrayscaleFillholeImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGrayscaleFillholeImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGrayscaleFillholeImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGrayscaleFillholeImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGrayscaleFillholeImageFilterIF2IF2 in _itkGrayscaleFillholeImageFilterPython:
_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF2IF2_swigregister(itkGrayscaleFillholeImageFilterIF2IF2)
itkGrayscaleFillholeImageFilterIF2IF2___New_orig__ = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF2IF2___New_orig__
itkGrayscaleFillholeImageFilterIF2IF2_cast = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF2IF2_cast

class itkGrayscaleFillholeImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    r"""Proxy of C++ itkGrayscaleFillholeImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF3IF3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF3IF3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF3IF3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF3IF3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF3IF3_FullyConnectedOff)
    InputOStreamWritableCheck = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF3IF3_InputOStreamWritableCheck
    
    __swig_destroy__ = _itkGrayscaleFillholeImageFilterPython.delete_itkGrayscaleFillholeImageFilterIF3IF3
    cast = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkGrayscaleFillholeImageFilterIF3IF3

        Create a new object of the class itkGrayscaleFillholeImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGrayscaleFillholeImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGrayscaleFillholeImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGrayscaleFillholeImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGrayscaleFillholeImageFilterIF3IF3 in _itkGrayscaleFillholeImageFilterPython:
_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF3IF3_swigregister(itkGrayscaleFillholeImageFilterIF3IF3)
itkGrayscaleFillholeImageFilterIF3IF3___New_orig__ = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF3IF3___New_orig__
itkGrayscaleFillholeImageFilterIF3IF3_cast = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIF3IF3_cast

class itkGrayscaleFillholeImageFilterISS2ISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    r"""Proxy of C++ itkGrayscaleFillholeImageFilterISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS2ISS2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS2ISS2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS2ISS2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS2ISS2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS2ISS2_FullyConnectedOff)
    InputOStreamWritableCheck = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS2ISS2_InputOStreamWritableCheck
    
    __swig_destroy__ = _itkGrayscaleFillholeImageFilterPython.delete_itkGrayscaleFillholeImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkGrayscaleFillholeImageFilterISS2ISS2

        Create a new object of the class itkGrayscaleFillholeImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGrayscaleFillholeImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGrayscaleFillholeImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGrayscaleFillholeImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGrayscaleFillholeImageFilterISS2ISS2 in _itkGrayscaleFillholeImageFilterPython:
_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS2ISS2_swigregister(itkGrayscaleFillholeImageFilterISS2ISS2)
itkGrayscaleFillholeImageFilterISS2ISS2___New_orig__ = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS2ISS2___New_orig__
itkGrayscaleFillholeImageFilterISS2ISS2_cast = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS2ISS2_cast

class itkGrayscaleFillholeImageFilterISS3ISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    r"""Proxy of C++ itkGrayscaleFillholeImageFilterISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS3ISS3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS3ISS3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS3ISS3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS3ISS3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS3ISS3_FullyConnectedOff)
    InputOStreamWritableCheck = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS3ISS3_InputOStreamWritableCheck
    
    __swig_destroy__ = _itkGrayscaleFillholeImageFilterPython.delete_itkGrayscaleFillholeImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkGrayscaleFillholeImageFilterISS3ISS3

        Create a new object of the class itkGrayscaleFillholeImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGrayscaleFillholeImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGrayscaleFillholeImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGrayscaleFillholeImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGrayscaleFillholeImageFilterISS3ISS3 in _itkGrayscaleFillholeImageFilterPython:
_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS3ISS3_swigregister(itkGrayscaleFillholeImageFilterISS3ISS3)
itkGrayscaleFillholeImageFilterISS3ISS3___New_orig__ = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS3ISS3___New_orig__
itkGrayscaleFillholeImageFilterISS3ISS3_cast = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterISS3ISS3_cast

class itkGrayscaleFillholeImageFilterIUC2IUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    r"""Proxy of C++ itkGrayscaleFillholeImageFilterIUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC2IUC2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC2IUC2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC2IUC2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC2IUC2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC2IUC2_FullyConnectedOff)
    InputOStreamWritableCheck = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC2IUC2_InputOStreamWritableCheck
    
    __swig_destroy__ = _itkGrayscaleFillholeImageFilterPython.delete_itkGrayscaleFillholeImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkGrayscaleFillholeImageFilterIUC2IUC2

        Create a new object of the class itkGrayscaleFillholeImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGrayscaleFillholeImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGrayscaleFillholeImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGrayscaleFillholeImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGrayscaleFillholeImageFilterIUC2IUC2 in _itkGrayscaleFillholeImageFilterPython:
_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC2IUC2_swigregister(itkGrayscaleFillholeImageFilterIUC2IUC2)
itkGrayscaleFillholeImageFilterIUC2IUC2___New_orig__ = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC2IUC2___New_orig__
itkGrayscaleFillholeImageFilterIUC2IUC2_cast = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC2IUC2_cast

class itkGrayscaleFillholeImageFilterIUC3IUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    r"""Proxy of C++ itkGrayscaleFillholeImageFilterIUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC3IUC3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC3IUC3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC3IUC3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC3IUC3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC3IUC3_FullyConnectedOff)
    InputOStreamWritableCheck = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC3IUC3_InputOStreamWritableCheck
    
    __swig_destroy__ = _itkGrayscaleFillholeImageFilterPython.delete_itkGrayscaleFillholeImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkGrayscaleFillholeImageFilterIUC3IUC3

        Create a new object of the class itkGrayscaleFillholeImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGrayscaleFillholeImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGrayscaleFillholeImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGrayscaleFillholeImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGrayscaleFillholeImageFilterIUC3IUC3 in _itkGrayscaleFillholeImageFilterPython:
_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC3IUC3_swigregister(itkGrayscaleFillholeImageFilterIUC3IUC3)
itkGrayscaleFillholeImageFilterIUC3IUC3___New_orig__ = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC3IUC3___New_orig__
itkGrayscaleFillholeImageFilterIUC3IUC3_cast = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUC3IUC3_cast

class itkGrayscaleFillholeImageFilterIUS2IUS2(itkImageToImageFilterAPython.itkImageToImageFilterIUS2IUS2):
    r"""Proxy of C++ itkGrayscaleFillholeImageFilterIUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS2IUS2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS2IUS2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS2IUS2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS2IUS2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS2IUS2_FullyConnectedOff)
    InputOStreamWritableCheck = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS2IUS2_InputOStreamWritableCheck
    
    __swig_destroy__ = _itkGrayscaleFillholeImageFilterPython.delete_itkGrayscaleFillholeImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkGrayscaleFillholeImageFilterIUS2IUS2

        Create a new object of the class itkGrayscaleFillholeImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGrayscaleFillholeImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGrayscaleFillholeImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGrayscaleFillholeImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGrayscaleFillholeImageFilterIUS2IUS2 in _itkGrayscaleFillholeImageFilterPython:
_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS2IUS2_swigregister(itkGrayscaleFillholeImageFilterIUS2IUS2)
itkGrayscaleFillholeImageFilterIUS2IUS2___New_orig__ = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS2IUS2___New_orig__
itkGrayscaleFillholeImageFilterIUS2IUS2_cast = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS2IUS2_cast

class itkGrayscaleFillholeImageFilterIUS3IUS3(itkImageToImageFilterAPython.itkImageToImageFilterIUS3IUS3):
    r"""Proxy of C++ itkGrayscaleFillholeImageFilterIUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS3IUS3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS3IUS3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS3IUS3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS3IUS3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS3IUS3_FullyConnectedOff)
    InputOStreamWritableCheck = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS3IUS3_InputOStreamWritableCheck
    
    __swig_destroy__ = _itkGrayscaleFillholeImageFilterPython.delete_itkGrayscaleFillholeImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkGrayscaleFillholeImageFilterIUS3IUS3

        Create a new object of the class itkGrayscaleFillholeImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGrayscaleFillholeImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGrayscaleFillholeImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGrayscaleFillholeImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGrayscaleFillholeImageFilterIUS3IUS3 in _itkGrayscaleFillholeImageFilterPython:
_itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS3IUS3_swigregister(itkGrayscaleFillholeImageFilterIUS3IUS3)
itkGrayscaleFillholeImageFilterIUS3IUS3___New_orig__ = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS3IUS3___New_orig__
itkGrayscaleFillholeImageFilterIUS3IUS3_cast = _itkGrayscaleFillholeImageFilterPython.itkGrayscaleFillholeImageFilterIUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def grayscale_fillhole_image_filter(*args, **kwargs):
    """Procedural interface for GrayscaleFillholeImageFilter"""
    import itk
    instance = itk.GrayscaleFillholeImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def grayscale_fillhole_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.GrayscaleFillholeImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.GrayscaleFillholeImageFilter.values()[0]
    else:
        filter_object = itk.GrayscaleFillholeImageFilter

    grayscale_fillhole_image_filter.__doc__ = filter_object.__doc__
    grayscale_fillhole_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    grayscale_fillhole_image_filter.__doc__ += "Available Keyword Arguments:\n"
    grayscale_fillhole_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



