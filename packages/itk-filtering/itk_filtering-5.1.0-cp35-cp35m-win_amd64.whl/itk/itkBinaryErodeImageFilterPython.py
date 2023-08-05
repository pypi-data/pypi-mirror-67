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
    from . import _itkBinaryErodeImageFilterPython
else:
    import _itkBinaryErodeImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBinaryErodeImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBinaryErodeImageFilterPython.SWIG_PyStaticMethod_New

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
import itkBinaryDilateImageFilterPython
import itkOffsetPython
import itkSizePython
import itkFlatStructuringElementPython
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
import itkIndexPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkNeighborhoodPython
import itkBoxImageFilterPython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkBinaryErodeImageFilterID3ID3SE3_New():
  return itkBinaryErodeImageFilterID3ID3SE3.New()


def itkBinaryErodeImageFilterIF3IF3SE3_New():
  return itkBinaryErodeImageFilterIF3IF3SE3.New()


def itkBinaryErodeImageFilterIUS3IUS3SE3_New():
  return itkBinaryErodeImageFilterIUS3IUS3SE3.New()


def itkBinaryErodeImageFilterIUC3IUC3SE3_New():
  return itkBinaryErodeImageFilterIUC3IUC3SE3.New()


def itkBinaryErodeImageFilterISS3ISS3SE3_New():
  return itkBinaryErodeImageFilterISS3ISS3SE3.New()


def itkBinaryErodeImageFilterID2ID2SE2_New():
  return itkBinaryErodeImageFilterID2ID2SE2.New()


def itkBinaryErodeImageFilterIF2IF2SE2_New():
  return itkBinaryErodeImageFilterIF2IF2SE2.New()


def itkBinaryErodeImageFilterIUS2IUS2SE2_New():
  return itkBinaryErodeImageFilterIUS2IUS2SE2.New()


def itkBinaryErodeImageFilterIUC2IUC2SE2_New():
  return itkBinaryErodeImageFilterIUC2IUC2SE2.New()


def itkBinaryErodeImageFilterISS2ISS2SE2_New():
  return itkBinaryErodeImageFilterISS2ISS2SE2.New()

class itkBinaryErodeImageFilterID2ID2SE2(itkBinaryDilateImageFilterPython.itkBinaryDilateImageFilterID2ID2SE2_Superclass):
    r"""Proxy of C++ itkBinaryErodeImageFilterID2ID2SE2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterID2ID2SE2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterID2ID2SE2_Clone)
    SetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterID2ID2SE2_SetErodeValue)
    GetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterID2ID2SE2_GetErodeValue)
    __swig_destroy__ = _itkBinaryErodeImageFilterPython.delete_itkBinaryErodeImageFilterID2ID2SE2
    cast = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterID2ID2SE2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryErodeImageFilterID2ID2SE2

        Create a new object of the class itkBinaryErodeImageFilterID2ID2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryErodeImageFilterID2ID2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryErodeImageFilterID2ID2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryErodeImageFilterID2ID2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryErodeImageFilterID2ID2SE2 in _itkBinaryErodeImageFilterPython:
_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterID2ID2SE2_swigregister(itkBinaryErodeImageFilterID2ID2SE2)
itkBinaryErodeImageFilterID2ID2SE2___New_orig__ = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterID2ID2SE2___New_orig__
itkBinaryErodeImageFilterID2ID2SE2_cast = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterID2ID2SE2_cast

class itkBinaryErodeImageFilterID3ID3SE3(itkBinaryDilateImageFilterPython.itkBinaryDilateImageFilterID3ID3SE3_Superclass):
    r"""Proxy of C++ itkBinaryErodeImageFilterID3ID3SE3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterID3ID3SE3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterID3ID3SE3_Clone)
    SetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterID3ID3SE3_SetErodeValue)
    GetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterID3ID3SE3_GetErodeValue)
    __swig_destroy__ = _itkBinaryErodeImageFilterPython.delete_itkBinaryErodeImageFilterID3ID3SE3
    cast = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterID3ID3SE3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryErodeImageFilterID3ID3SE3

        Create a new object of the class itkBinaryErodeImageFilterID3ID3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryErodeImageFilterID3ID3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryErodeImageFilterID3ID3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryErodeImageFilterID3ID3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryErodeImageFilterID3ID3SE3 in _itkBinaryErodeImageFilterPython:
_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterID3ID3SE3_swigregister(itkBinaryErodeImageFilterID3ID3SE3)
itkBinaryErodeImageFilterID3ID3SE3___New_orig__ = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterID3ID3SE3___New_orig__
itkBinaryErodeImageFilterID3ID3SE3_cast = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterID3ID3SE3_cast

class itkBinaryErodeImageFilterIF2IF2SE2(itkBinaryDilateImageFilterPython.itkBinaryDilateImageFilterIF2IF2SE2_Superclass):
    r"""Proxy of C++ itkBinaryErodeImageFilterIF2IF2SE2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_Clone)
    SetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_SetErodeValue)
    GetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_GetErodeValue)
    __swig_destroy__ = _itkBinaryErodeImageFilterPython.delete_itkBinaryErodeImageFilterIF2IF2SE2
    cast = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryErodeImageFilterIF2IF2SE2

        Create a new object of the class itkBinaryErodeImageFilterIF2IF2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryErodeImageFilterIF2IF2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryErodeImageFilterIF2IF2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryErodeImageFilterIF2IF2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryErodeImageFilterIF2IF2SE2 in _itkBinaryErodeImageFilterPython:
_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_swigregister(itkBinaryErodeImageFilterIF2IF2SE2)
itkBinaryErodeImageFilterIF2IF2SE2___New_orig__ = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2___New_orig__
itkBinaryErodeImageFilterIF2IF2SE2_cast = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF2IF2SE2_cast

class itkBinaryErodeImageFilterIF3IF3SE3(itkBinaryDilateImageFilterPython.itkBinaryDilateImageFilterIF3IF3SE3_Superclass):
    r"""Proxy of C++ itkBinaryErodeImageFilterIF3IF3SE3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_Clone)
    SetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_SetErodeValue)
    GetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_GetErodeValue)
    __swig_destroy__ = _itkBinaryErodeImageFilterPython.delete_itkBinaryErodeImageFilterIF3IF3SE3
    cast = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryErodeImageFilterIF3IF3SE3

        Create a new object of the class itkBinaryErodeImageFilterIF3IF3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryErodeImageFilterIF3IF3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryErodeImageFilterIF3IF3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryErodeImageFilterIF3IF3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryErodeImageFilterIF3IF3SE3 in _itkBinaryErodeImageFilterPython:
_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_swigregister(itkBinaryErodeImageFilterIF3IF3SE3)
itkBinaryErodeImageFilterIF3IF3SE3___New_orig__ = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3___New_orig__
itkBinaryErodeImageFilterIF3IF3SE3_cast = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIF3IF3SE3_cast

class itkBinaryErodeImageFilterISS2ISS2SE2(itkBinaryDilateImageFilterPython.itkBinaryDilateImageFilterISS2ISS2SE2_Superclass):
    r"""Proxy of C++ itkBinaryErodeImageFilterISS2ISS2SE2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_Clone)
    SetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_SetErodeValue)
    GetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_GetErodeValue)
    __swig_destroy__ = _itkBinaryErodeImageFilterPython.delete_itkBinaryErodeImageFilterISS2ISS2SE2
    cast = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryErodeImageFilterISS2ISS2SE2

        Create a new object of the class itkBinaryErodeImageFilterISS2ISS2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryErodeImageFilterISS2ISS2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryErodeImageFilterISS2ISS2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryErodeImageFilterISS2ISS2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryErodeImageFilterISS2ISS2SE2 in _itkBinaryErodeImageFilterPython:
_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_swigregister(itkBinaryErodeImageFilterISS2ISS2SE2)
itkBinaryErodeImageFilterISS2ISS2SE2___New_orig__ = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2___New_orig__
itkBinaryErodeImageFilterISS2ISS2SE2_cast = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS2ISS2SE2_cast

class itkBinaryErodeImageFilterISS3ISS3SE3(itkBinaryDilateImageFilterPython.itkBinaryDilateImageFilterISS3ISS3SE3_Superclass):
    r"""Proxy of C++ itkBinaryErodeImageFilterISS3ISS3SE3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_Clone)
    SetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_SetErodeValue)
    GetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_GetErodeValue)
    __swig_destroy__ = _itkBinaryErodeImageFilterPython.delete_itkBinaryErodeImageFilterISS3ISS3SE3
    cast = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryErodeImageFilterISS3ISS3SE3

        Create a new object of the class itkBinaryErodeImageFilterISS3ISS3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryErodeImageFilterISS3ISS3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryErodeImageFilterISS3ISS3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryErodeImageFilterISS3ISS3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryErodeImageFilterISS3ISS3SE3 in _itkBinaryErodeImageFilterPython:
_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_swigregister(itkBinaryErodeImageFilterISS3ISS3SE3)
itkBinaryErodeImageFilterISS3ISS3SE3___New_orig__ = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3___New_orig__
itkBinaryErodeImageFilterISS3ISS3SE3_cast = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterISS3ISS3SE3_cast

class itkBinaryErodeImageFilterIUC2IUC2SE2(itkBinaryDilateImageFilterPython.itkBinaryDilateImageFilterIUC2IUC2SE2_Superclass):
    r"""Proxy of C++ itkBinaryErodeImageFilterIUC2IUC2SE2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_Clone)
    SetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_SetErodeValue)
    GetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_GetErodeValue)
    __swig_destroy__ = _itkBinaryErodeImageFilterPython.delete_itkBinaryErodeImageFilterIUC2IUC2SE2
    cast = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryErodeImageFilterIUC2IUC2SE2

        Create a new object of the class itkBinaryErodeImageFilterIUC2IUC2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryErodeImageFilterIUC2IUC2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryErodeImageFilterIUC2IUC2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryErodeImageFilterIUC2IUC2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryErodeImageFilterIUC2IUC2SE2 in _itkBinaryErodeImageFilterPython:
_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_swigregister(itkBinaryErodeImageFilterIUC2IUC2SE2)
itkBinaryErodeImageFilterIUC2IUC2SE2___New_orig__ = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2___New_orig__
itkBinaryErodeImageFilterIUC2IUC2SE2_cast = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC2IUC2SE2_cast

class itkBinaryErodeImageFilterIUC3IUC3SE3(itkBinaryDilateImageFilterPython.itkBinaryDilateImageFilterIUC3IUC3SE3_Superclass):
    r"""Proxy of C++ itkBinaryErodeImageFilterIUC3IUC3SE3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_Clone)
    SetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_SetErodeValue)
    GetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_GetErodeValue)
    __swig_destroy__ = _itkBinaryErodeImageFilterPython.delete_itkBinaryErodeImageFilterIUC3IUC3SE3
    cast = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryErodeImageFilterIUC3IUC3SE3

        Create a new object of the class itkBinaryErodeImageFilterIUC3IUC3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryErodeImageFilterIUC3IUC3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryErodeImageFilterIUC3IUC3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryErodeImageFilterIUC3IUC3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryErodeImageFilterIUC3IUC3SE3 in _itkBinaryErodeImageFilterPython:
_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_swigregister(itkBinaryErodeImageFilterIUC3IUC3SE3)
itkBinaryErodeImageFilterIUC3IUC3SE3___New_orig__ = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3___New_orig__
itkBinaryErodeImageFilterIUC3IUC3SE3_cast = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUC3IUC3SE3_cast

class itkBinaryErodeImageFilterIUS2IUS2SE2(itkBinaryDilateImageFilterPython.itkBinaryDilateImageFilterIUS2IUS2SE2_Superclass):
    r"""Proxy of C++ itkBinaryErodeImageFilterIUS2IUS2SE2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUS2IUS2SE2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUS2IUS2SE2_Clone)
    SetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUS2IUS2SE2_SetErodeValue)
    GetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUS2IUS2SE2_GetErodeValue)
    __swig_destroy__ = _itkBinaryErodeImageFilterPython.delete_itkBinaryErodeImageFilterIUS2IUS2SE2
    cast = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUS2IUS2SE2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryErodeImageFilterIUS2IUS2SE2

        Create a new object of the class itkBinaryErodeImageFilterIUS2IUS2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryErodeImageFilterIUS2IUS2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryErodeImageFilterIUS2IUS2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryErodeImageFilterIUS2IUS2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryErodeImageFilterIUS2IUS2SE2 in _itkBinaryErodeImageFilterPython:
_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUS2IUS2SE2_swigregister(itkBinaryErodeImageFilterIUS2IUS2SE2)
itkBinaryErodeImageFilterIUS2IUS2SE2___New_orig__ = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUS2IUS2SE2___New_orig__
itkBinaryErodeImageFilterIUS2IUS2SE2_cast = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUS2IUS2SE2_cast

class itkBinaryErodeImageFilterIUS3IUS3SE3(itkBinaryDilateImageFilterPython.itkBinaryDilateImageFilterIUS3IUS3SE3_Superclass):
    r"""Proxy of C++ itkBinaryErodeImageFilterIUS3IUS3SE3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUS3IUS3SE3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUS3IUS3SE3_Clone)
    SetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUS3IUS3SE3_SetErodeValue)
    GetErodeValue = _swig_new_instance_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUS3IUS3SE3_GetErodeValue)
    __swig_destroy__ = _itkBinaryErodeImageFilterPython.delete_itkBinaryErodeImageFilterIUS3IUS3SE3
    cast = _swig_new_static_method(_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUS3IUS3SE3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryErodeImageFilterIUS3IUS3SE3

        Create a new object of the class itkBinaryErodeImageFilterIUS3IUS3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryErodeImageFilterIUS3IUS3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryErodeImageFilterIUS3IUS3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryErodeImageFilterIUS3IUS3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryErodeImageFilterIUS3IUS3SE3 in _itkBinaryErodeImageFilterPython:
_itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUS3IUS3SE3_swigregister(itkBinaryErodeImageFilterIUS3IUS3SE3)
itkBinaryErodeImageFilterIUS3IUS3SE3___New_orig__ = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUS3IUS3SE3___New_orig__
itkBinaryErodeImageFilterIUS3IUS3SE3_cast = _itkBinaryErodeImageFilterPython.itkBinaryErodeImageFilterIUS3IUS3SE3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def binary_erode_image_filter(*args, **kwargs):
    """Procedural interface for BinaryErodeImageFilter"""
    import itk
    instance = itk.BinaryErodeImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def binary_erode_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.BinaryErodeImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.BinaryErodeImageFilter.values()[0]
    else:
        filter_object = itk.BinaryErodeImageFilter

    binary_erode_image_filter.__doc__ = filter_object.__doc__
    binary_erode_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    binary_erode_image_filter.__doc__ += "Available Keyword Arguments:\n"
    binary_erode_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



