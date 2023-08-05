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
    from . import _itkSpeckleNoiseImageFilterPython
else:
    import _itkSpeckleNoiseImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSpeckleNoiseImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSpeckleNoiseImageFilterPython.SWIG_PyStaticMethod_New

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
import itkNoiseBaseImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkImagePython
import itkPointPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkRGBAPixelPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython

def itkSpeckleNoiseImageFilterID3ID3_New():
  return itkSpeckleNoiseImageFilterID3ID3.New()


def itkSpeckleNoiseImageFilterID2ID2_New():
  return itkSpeckleNoiseImageFilterID2ID2.New()


def itkSpeckleNoiseImageFilterIF3IF3_New():
  return itkSpeckleNoiseImageFilterIF3IF3.New()


def itkSpeckleNoiseImageFilterIF2IF2_New():
  return itkSpeckleNoiseImageFilterIF2IF2.New()


def itkSpeckleNoiseImageFilterIUS3IUS3_New():
  return itkSpeckleNoiseImageFilterIUS3IUS3.New()


def itkSpeckleNoiseImageFilterIUS2IUS2_New():
  return itkSpeckleNoiseImageFilterIUS2IUS2.New()


def itkSpeckleNoiseImageFilterIUC3IUC3_New():
  return itkSpeckleNoiseImageFilterIUC3IUC3.New()


def itkSpeckleNoiseImageFilterIUC2IUC2_New():
  return itkSpeckleNoiseImageFilterIUC2IUC2.New()


def itkSpeckleNoiseImageFilterISS3ISS3_New():
  return itkSpeckleNoiseImageFilterISS3ISS3.New()


def itkSpeckleNoiseImageFilterISS2ISS2_New():
  return itkSpeckleNoiseImageFilterISS2ISS2.New()

class itkSpeckleNoiseImageFilterID2ID2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterID2ID2):
    r"""Proxy of C++ itkSpeckleNoiseImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID2ID2_Clone)
    GetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID2ID2_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID2ID2_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID2ID2_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSpeckleNoiseImageFilterPython.delete_itkSpeckleNoiseImageFilterID2ID2
    cast = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkSpeckleNoiseImageFilterID2ID2

        Create a new object of the class itkSpeckleNoiseImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpeckleNoiseImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpeckleNoiseImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpeckleNoiseImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSpeckleNoiseImageFilterID2ID2 in _itkSpeckleNoiseImageFilterPython:
_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID2ID2_swigregister(itkSpeckleNoiseImageFilterID2ID2)
itkSpeckleNoiseImageFilterID2ID2___New_orig__ = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID2ID2___New_orig__
itkSpeckleNoiseImageFilterID2ID2_cast = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID2ID2_cast

class itkSpeckleNoiseImageFilterID3ID3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterID3ID3):
    r"""Proxy of C++ itkSpeckleNoiseImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID3ID3_Clone)
    GetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID3ID3_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID3ID3_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID3ID3_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSpeckleNoiseImageFilterPython.delete_itkSpeckleNoiseImageFilterID3ID3
    cast = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkSpeckleNoiseImageFilterID3ID3

        Create a new object of the class itkSpeckleNoiseImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpeckleNoiseImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpeckleNoiseImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpeckleNoiseImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSpeckleNoiseImageFilterID3ID3 in _itkSpeckleNoiseImageFilterPython:
_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID3ID3_swigregister(itkSpeckleNoiseImageFilterID3ID3)
itkSpeckleNoiseImageFilterID3ID3___New_orig__ = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID3ID3___New_orig__
itkSpeckleNoiseImageFilterID3ID3_cast = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterID3ID3_cast

class itkSpeckleNoiseImageFilterIF2IF2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIF2IF2):
    r"""Proxy of C++ itkSpeckleNoiseImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_Clone)
    GetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSpeckleNoiseImageFilterPython.delete_itkSpeckleNoiseImageFilterIF2IF2
    cast = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkSpeckleNoiseImageFilterIF2IF2

        Create a new object of the class itkSpeckleNoiseImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpeckleNoiseImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpeckleNoiseImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpeckleNoiseImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSpeckleNoiseImageFilterIF2IF2 in _itkSpeckleNoiseImageFilterPython:
_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_swigregister(itkSpeckleNoiseImageFilterIF2IF2)
itkSpeckleNoiseImageFilterIF2IF2___New_orig__ = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2___New_orig__
itkSpeckleNoiseImageFilterIF2IF2_cast = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF2IF2_cast

class itkSpeckleNoiseImageFilterIF3IF3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIF3IF3):
    r"""Proxy of C++ itkSpeckleNoiseImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_Clone)
    GetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSpeckleNoiseImageFilterPython.delete_itkSpeckleNoiseImageFilterIF3IF3
    cast = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkSpeckleNoiseImageFilterIF3IF3

        Create a new object of the class itkSpeckleNoiseImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpeckleNoiseImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpeckleNoiseImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpeckleNoiseImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSpeckleNoiseImageFilterIF3IF3 in _itkSpeckleNoiseImageFilterPython:
_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_swigregister(itkSpeckleNoiseImageFilterIF3IF3)
itkSpeckleNoiseImageFilterIF3IF3___New_orig__ = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3___New_orig__
itkSpeckleNoiseImageFilterIF3IF3_cast = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIF3IF3_cast

class itkSpeckleNoiseImageFilterISS2ISS2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterISS2ISS2):
    r"""Proxy of C++ itkSpeckleNoiseImageFilterISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_Clone)
    GetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSpeckleNoiseImageFilterPython.delete_itkSpeckleNoiseImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkSpeckleNoiseImageFilterISS2ISS2

        Create a new object of the class itkSpeckleNoiseImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpeckleNoiseImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpeckleNoiseImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpeckleNoiseImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSpeckleNoiseImageFilterISS2ISS2 in _itkSpeckleNoiseImageFilterPython:
_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_swigregister(itkSpeckleNoiseImageFilterISS2ISS2)
itkSpeckleNoiseImageFilterISS2ISS2___New_orig__ = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2___New_orig__
itkSpeckleNoiseImageFilterISS2ISS2_cast = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS2ISS2_cast

class itkSpeckleNoiseImageFilterISS3ISS3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterISS3ISS3):
    r"""Proxy of C++ itkSpeckleNoiseImageFilterISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_Clone)
    GetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSpeckleNoiseImageFilterPython.delete_itkSpeckleNoiseImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkSpeckleNoiseImageFilterISS3ISS3

        Create a new object of the class itkSpeckleNoiseImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpeckleNoiseImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpeckleNoiseImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpeckleNoiseImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSpeckleNoiseImageFilterISS3ISS3 in _itkSpeckleNoiseImageFilterPython:
_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_swigregister(itkSpeckleNoiseImageFilterISS3ISS3)
itkSpeckleNoiseImageFilterISS3ISS3___New_orig__ = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3___New_orig__
itkSpeckleNoiseImageFilterISS3ISS3_cast = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterISS3ISS3_cast

class itkSpeckleNoiseImageFilterIUC2IUC2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIUC2IUC2):
    r"""Proxy of C++ itkSpeckleNoiseImageFilterIUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_Clone)
    GetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSpeckleNoiseImageFilterPython.delete_itkSpeckleNoiseImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkSpeckleNoiseImageFilterIUC2IUC2

        Create a new object of the class itkSpeckleNoiseImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpeckleNoiseImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpeckleNoiseImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpeckleNoiseImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSpeckleNoiseImageFilterIUC2IUC2 in _itkSpeckleNoiseImageFilterPython:
_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_swigregister(itkSpeckleNoiseImageFilterIUC2IUC2)
itkSpeckleNoiseImageFilterIUC2IUC2___New_orig__ = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2___New_orig__
itkSpeckleNoiseImageFilterIUC2IUC2_cast = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC2IUC2_cast

class itkSpeckleNoiseImageFilterIUC3IUC3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIUC3IUC3):
    r"""Proxy of C++ itkSpeckleNoiseImageFilterIUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_Clone)
    GetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSpeckleNoiseImageFilterPython.delete_itkSpeckleNoiseImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkSpeckleNoiseImageFilterIUC3IUC3

        Create a new object of the class itkSpeckleNoiseImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpeckleNoiseImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpeckleNoiseImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpeckleNoiseImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSpeckleNoiseImageFilterIUC3IUC3 in _itkSpeckleNoiseImageFilterPython:
_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_swigregister(itkSpeckleNoiseImageFilterIUC3IUC3)
itkSpeckleNoiseImageFilterIUC3IUC3___New_orig__ = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3___New_orig__
itkSpeckleNoiseImageFilterIUC3IUC3_cast = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUC3IUC3_cast

class itkSpeckleNoiseImageFilterIUS2IUS2(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIUS2IUS2):
    r"""Proxy of C++ itkSpeckleNoiseImageFilterIUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS2IUS2_Clone)
    GetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS2IUS2_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS2IUS2_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS2IUS2_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSpeckleNoiseImageFilterPython.delete_itkSpeckleNoiseImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkSpeckleNoiseImageFilterIUS2IUS2

        Create a new object of the class itkSpeckleNoiseImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpeckleNoiseImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpeckleNoiseImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpeckleNoiseImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSpeckleNoiseImageFilterIUS2IUS2 in _itkSpeckleNoiseImageFilterPython:
_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS2IUS2_swigregister(itkSpeckleNoiseImageFilterIUS2IUS2)
itkSpeckleNoiseImageFilterIUS2IUS2___New_orig__ = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS2IUS2___New_orig__
itkSpeckleNoiseImageFilterIUS2IUS2_cast = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS2IUS2_cast

class itkSpeckleNoiseImageFilterIUS3IUS3(itkNoiseBaseImageFilterPython.itkNoiseBaseImageFilterIUS3IUS3):
    r"""Proxy of C++ itkSpeckleNoiseImageFilterIUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS3IUS3_Clone)
    GetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS3IUS3_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS3IUS3_SetStandardDeviation)
    InputConvertibleToOutputCheck = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS3IUS3_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSpeckleNoiseImageFilterPython.delete_itkSpeckleNoiseImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkSpeckleNoiseImageFilterIUS3IUS3

        Create a new object of the class itkSpeckleNoiseImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpeckleNoiseImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpeckleNoiseImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpeckleNoiseImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSpeckleNoiseImageFilterIUS3IUS3 in _itkSpeckleNoiseImageFilterPython:
_itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS3IUS3_swigregister(itkSpeckleNoiseImageFilterIUS3IUS3)
itkSpeckleNoiseImageFilterIUS3IUS3___New_orig__ = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS3IUS3___New_orig__
itkSpeckleNoiseImageFilterIUS3IUS3_cast = _itkSpeckleNoiseImageFilterPython.itkSpeckleNoiseImageFilterIUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def speckle_noise_image_filter(*args, **kwargs):
    """Procedural interface for SpeckleNoiseImageFilter"""
    import itk
    instance = itk.SpeckleNoiseImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def speckle_noise_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.SpeckleNoiseImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.SpeckleNoiseImageFilter.values()[0]
    else:
        filter_object = itk.SpeckleNoiseImageFilter

    speckle_noise_image_filter.__doc__ = filter_object.__doc__
    speckle_noise_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    speckle_noise_image_filter.__doc__ += "Available Keyword Arguments:\n"
    speckle_noise_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



