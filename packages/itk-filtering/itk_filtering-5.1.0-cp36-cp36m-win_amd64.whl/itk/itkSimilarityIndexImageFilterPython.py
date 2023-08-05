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
    from . import _itkSimilarityIndexImageFilterPython
else:
    import _itkSimilarityIndexImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSimilarityIndexImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSimilarityIndexImageFilterPython.SWIG_PyStaticMethod_New

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
import itkFixedArrayPython
import pyBasePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkSizePython
import ITKCommonBasePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import itkPointPython
import vnl_matrix_fixedPython
import itkIndexPython
import itkOffsetPython
import itkImageRegionPython
import itkImageToImageFilterAPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython

def itkSimilarityIndexImageFilterID3ID3_New():
  return itkSimilarityIndexImageFilterID3ID3.New()


def itkSimilarityIndexImageFilterID2ID2_New():
  return itkSimilarityIndexImageFilterID2ID2.New()


def itkSimilarityIndexImageFilterIF3IF3_New():
  return itkSimilarityIndexImageFilterIF3IF3.New()


def itkSimilarityIndexImageFilterIF2IF2_New():
  return itkSimilarityIndexImageFilterIF2IF2.New()


def itkSimilarityIndexImageFilterIUS3IUS3_New():
  return itkSimilarityIndexImageFilterIUS3IUS3.New()


def itkSimilarityIndexImageFilterIUS2IUS2_New():
  return itkSimilarityIndexImageFilterIUS2IUS2.New()


def itkSimilarityIndexImageFilterIUC3IUC3_New():
  return itkSimilarityIndexImageFilterIUC3IUC3.New()


def itkSimilarityIndexImageFilterIUC2IUC2_New():
  return itkSimilarityIndexImageFilterIUC2IUC2.New()


def itkSimilarityIndexImageFilterISS3ISS3_New():
  return itkSimilarityIndexImageFilterISS3ISS3.New()


def itkSimilarityIndexImageFilterISS2ISS2_New():
  return itkSimilarityIndexImageFilterISS2ISS2.New()

class itkSimilarityIndexImageFilterID2ID2(itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    r"""Proxy of C++ itkSimilarityIndexImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID2ID2_Clone)
    SetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID2ID2_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID2ID2_SetInput2)
    GetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID2ID2_GetInput1)
    GetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID2ID2_GetInput2)
    GetSimilarityIndex = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID2ID2_GetSimilarityIndex)
    Input1HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID2ID2_Input1HasNumericTraitsCheck
    
    Input2HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID2ID2_Input2HasNumericTraitsCheck
    
    __swig_destroy__ = _itkSimilarityIndexImageFilterPython.delete_itkSimilarityIndexImageFilterID2ID2
    cast = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkSimilarityIndexImageFilterID2ID2

        Create a new object of the class itkSimilarityIndexImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSimilarityIndexImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSimilarityIndexImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSimilarityIndexImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSimilarityIndexImageFilterID2ID2 in _itkSimilarityIndexImageFilterPython:
_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID2ID2_swigregister(itkSimilarityIndexImageFilterID2ID2)
itkSimilarityIndexImageFilterID2ID2___New_orig__ = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID2ID2___New_orig__
itkSimilarityIndexImageFilterID2ID2_cast = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID2ID2_cast

class itkSimilarityIndexImageFilterID3ID3(itkImageToImageFilterAPython.itkImageToImageFilterID3ID3):
    r"""Proxy of C++ itkSimilarityIndexImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID3ID3_Clone)
    SetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID3ID3_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID3ID3_SetInput2)
    GetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID3ID3_GetInput1)
    GetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID3ID3_GetInput2)
    GetSimilarityIndex = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID3ID3_GetSimilarityIndex)
    Input1HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID3ID3_Input1HasNumericTraitsCheck
    
    Input2HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID3ID3_Input2HasNumericTraitsCheck
    
    __swig_destroy__ = _itkSimilarityIndexImageFilterPython.delete_itkSimilarityIndexImageFilterID3ID3
    cast = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkSimilarityIndexImageFilterID3ID3

        Create a new object of the class itkSimilarityIndexImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSimilarityIndexImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSimilarityIndexImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSimilarityIndexImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSimilarityIndexImageFilterID3ID3 in _itkSimilarityIndexImageFilterPython:
_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID3ID3_swigregister(itkSimilarityIndexImageFilterID3ID3)
itkSimilarityIndexImageFilterID3ID3___New_orig__ = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID3ID3___New_orig__
itkSimilarityIndexImageFilterID3ID3_cast = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterID3ID3_cast

class itkSimilarityIndexImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    r"""Proxy of C++ itkSimilarityIndexImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF2IF2_Clone)
    SetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF2IF2_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF2IF2_SetInput2)
    GetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF2IF2_GetInput1)
    GetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF2IF2_GetInput2)
    GetSimilarityIndex = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF2IF2_GetSimilarityIndex)
    Input1HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF2IF2_Input1HasNumericTraitsCheck
    
    Input2HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF2IF2_Input2HasNumericTraitsCheck
    
    __swig_destroy__ = _itkSimilarityIndexImageFilterPython.delete_itkSimilarityIndexImageFilterIF2IF2
    cast = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkSimilarityIndexImageFilterIF2IF2

        Create a new object of the class itkSimilarityIndexImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSimilarityIndexImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSimilarityIndexImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSimilarityIndexImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSimilarityIndexImageFilterIF2IF2 in _itkSimilarityIndexImageFilterPython:
_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF2IF2_swigregister(itkSimilarityIndexImageFilterIF2IF2)
itkSimilarityIndexImageFilterIF2IF2___New_orig__ = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF2IF2___New_orig__
itkSimilarityIndexImageFilterIF2IF2_cast = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF2IF2_cast

class itkSimilarityIndexImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    r"""Proxy of C++ itkSimilarityIndexImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF3IF3_Clone)
    SetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF3IF3_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF3IF3_SetInput2)
    GetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF3IF3_GetInput1)
    GetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF3IF3_GetInput2)
    GetSimilarityIndex = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF3IF3_GetSimilarityIndex)
    Input1HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF3IF3_Input1HasNumericTraitsCheck
    
    Input2HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF3IF3_Input2HasNumericTraitsCheck
    
    __swig_destroy__ = _itkSimilarityIndexImageFilterPython.delete_itkSimilarityIndexImageFilterIF3IF3
    cast = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkSimilarityIndexImageFilterIF3IF3

        Create a new object of the class itkSimilarityIndexImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSimilarityIndexImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSimilarityIndexImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSimilarityIndexImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSimilarityIndexImageFilterIF3IF3 in _itkSimilarityIndexImageFilterPython:
_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF3IF3_swigregister(itkSimilarityIndexImageFilterIF3IF3)
itkSimilarityIndexImageFilterIF3IF3___New_orig__ = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF3IF3___New_orig__
itkSimilarityIndexImageFilterIF3IF3_cast = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIF3IF3_cast

class itkSimilarityIndexImageFilterISS2ISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    r"""Proxy of C++ itkSimilarityIndexImageFilterISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS2ISS2_Clone)
    SetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS2ISS2_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS2ISS2_SetInput2)
    GetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS2ISS2_GetInput1)
    GetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS2ISS2_GetInput2)
    GetSimilarityIndex = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS2ISS2_GetSimilarityIndex)
    Input1HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS2ISS2_Input1HasNumericTraitsCheck
    
    Input2HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS2ISS2_Input2HasNumericTraitsCheck
    
    __swig_destroy__ = _itkSimilarityIndexImageFilterPython.delete_itkSimilarityIndexImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkSimilarityIndexImageFilterISS2ISS2

        Create a new object of the class itkSimilarityIndexImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSimilarityIndexImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSimilarityIndexImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSimilarityIndexImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSimilarityIndexImageFilterISS2ISS2 in _itkSimilarityIndexImageFilterPython:
_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS2ISS2_swigregister(itkSimilarityIndexImageFilterISS2ISS2)
itkSimilarityIndexImageFilterISS2ISS2___New_orig__ = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS2ISS2___New_orig__
itkSimilarityIndexImageFilterISS2ISS2_cast = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS2ISS2_cast

class itkSimilarityIndexImageFilterISS3ISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    r"""Proxy of C++ itkSimilarityIndexImageFilterISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS3ISS3_Clone)
    SetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS3ISS3_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS3ISS3_SetInput2)
    GetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS3ISS3_GetInput1)
    GetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS3ISS3_GetInput2)
    GetSimilarityIndex = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS3ISS3_GetSimilarityIndex)
    Input1HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS3ISS3_Input1HasNumericTraitsCheck
    
    Input2HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS3ISS3_Input2HasNumericTraitsCheck
    
    __swig_destroy__ = _itkSimilarityIndexImageFilterPython.delete_itkSimilarityIndexImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkSimilarityIndexImageFilterISS3ISS3

        Create a new object of the class itkSimilarityIndexImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSimilarityIndexImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSimilarityIndexImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSimilarityIndexImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSimilarityIndexImageFilterISS3ISS3 in _itkSimilarityIndexImageFilterPython:
_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS3ISS3_swigregister(itkSimilarityIndexImageFilterISS3ISS3)
itkSimilarityIndexImageFilterISS3ISS3___New_orig__ = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS3ISS3___New_orig__
itkSimilarityIndexImageFilterISS3ISS3_cast = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterISS3ISS3_cast

class itkSimilarityIndexImageFilterIUC2IUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    r"""Proxy of C++ itkSimilarityIndexImageFilterIUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC2IUC2_Clone)
    SetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC2IUC2_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC2IUC2_SetInput2)
    GetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC2IUC2_GetInput1)
    GetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC2IUC2_GetInput2)
    GetSimilarityIndex = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC2IUC2_GetSimilarityIndex)
    Input1HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC2IUC2_Input1HasNumericTraitsCheck
    
    Input2HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC2IUC2_Input2HasNumericTraitsCheck
    
    __swig_destroy__ = _itkSimilarityIndexImageFilterPython.delete_itkSimilarityIndexImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkSimilarityIndexImageFilterIUC2IUC2

        Create a new object of the class itkSimilarityIndexImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSimilarityIndexImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSimilarityIndexImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSimilarityIndexImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSimilarityIndexImageFilterIUC2IUC2 in _itkSimilarityIndexImageFilterPython:
_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC2IUC2_swigregister(itkSimilarityIndexImageFilterIUC2IUC2)
itkSimilarityIndexImageFilterIUC2IUC2___New_orig__ = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC2IUC2___New_orig__
itkSimilarityIndexImageFilterIUC2IUC2_cast = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC2IUC2_cast

class itkSimilarityIndexImageFilterIUC3IUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    r"""Proxy of C++ itkSimilarityIndexImageFilterIUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC3IUC3_Clone)
    SetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC3IUC3_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC3IUC3_SetInput2)
    GetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC3IUC3_GetInput1)
    GetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC3IUC3_GetInput2)
    GetSimilarityIndex = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC3IUC3_GetSimilarityIndex)
    Input1HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC3IUC3_Input1HasNumericTraitsCheck
    
    Input2HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC3IUC3_Input2HasNumericTraitsCheck
    
    __swig_destroy__ = _itkSimilarityIndexImageFilterPython.delete_itkSimilarityIndexImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkSimilarityIndexImageFilterIUC3IUC3

        Create a new object of the class itkSimilarityIndexImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSimilarityIndexImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSimilarityIndexImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSimilarityIndexImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSimilarityIndexImageFilterIUC3IUC3 in _itkSimilarityIndexImageFilterPython:
_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC3IUC3_swigregister(itkSimilarityIndexImageFilterIUC3IUC3)
itkSimilarityIndexImageFilterIUC3IUC3___New_orig__ = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC3IUC3___New_orig__
itkSimilarityIndexImageFilterIUC3IUC3_cast = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUC3IUC3_cast

class itkSimilarityIndexImageFilterIUS2IUS2(itkImageToImageFilterAPython.itkImageToImageFilterIUS2IUS2):
    r"""Proxy of C++ itkSimilarityIndexImageFilterIUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS2IUS2_Clone)
    SetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS2IUS2_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS2IUS2_SetInput2)
    GetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS2IUS2_GetInput1)
    GetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS2IUS2_GetInput2)
    GetSimilarityIndex = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS2IUS2_GetSimilarityIndex)
    Input1HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS2IUS2_Input1HasNumericTraitsCheck
    
    Input2HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS2IUS2_Input2HasNumericTraitsCheck
    
    __swig_destroy__ = _itkSimilarityIndexImageFilterPython.delete_itkSimilarityIndexImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkSimilarityIndexImageFilterIUS2IUS2

        Create a new object of the class itkSimilarityIndexImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSimilarityIndexImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSimilarityIndexImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSimilarityIndexImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSimilarityIndexImageFilterIUS2IUS2 in _itkSimilarityIndexImageFilterPython:
_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS2IUS2_swigregister(itkSimilarityIndexImageFilterIUS2IUS2)
itkSimilarityIndexImageFilterIUS2IUS2___New_orig__ = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS2IUS2___New_orig__
itkSimilarityIndexImageFilterIUS2IUS2_cast = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS2IUS2_cast

class itkSimilarityIndexImageFilterIUS3IUS3(itkImageToImageFilterAPython.itkImageToImageFilterIUS3IUS3):
    r"""Proxy of C++ itkSimilarityIndexImageFilterIUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS3IUS3_Clone)
    SetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS3IUS3_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS3IUS3_SetInput2)
    GetInput1 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS3IUS3_GetInput1)
    GetInput2 = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS3IUS3_GetInput2)
    GetSimilarityIndex = _swig_new_instance_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS3IUS3_GetSimilarityIndex)
    Input1HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS3IUS3_Input1HasNumericTraitsCheck
    
    Input2HasNumericTraitsCheck = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS3IUS3_Input2HasNumericTraitsCheck
    
    __swig_destroy__ = _itkSimilarityIndexImageFilterPython.delete_itkSimilarityIndexImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkSimilarityIndexImageFilterIUS3IUS3

        Create a new object of the class itkSimilarityIndexImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSimilarityIndexImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSimilarityIndexImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSimilarityIndexImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSimilarityIndexImageFilterIUS3IUS3 in _itkSimilarityIndexImageFilterPython:
_itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS3IUS3_swigregister(itkSimilarityIndexImageFilterIUS3IUS3)
itkSimilarityIndexImageFilterIUS3IUS3___New_orig__ = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS3IUS3___New_orig__
itkSimilarityIndexImageFilterIUS3IUS3_cast = _itkSimilarityIndexImageFilterPython.itkSimilarityIndexImageFilterIUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def similarity_index_image_filter(*args, **kwargs):
    """Procedural interface for SimilarityIndexImageFilter"""
    import itk
    instance = itk.SimilarityIndexImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def similarity_index_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.SimilarityIndexImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.SimilarityIndexImageFilter.values()[0]
    else:
        filter_object = itk.SimilarityIndexImageFilter

    similarity_index_image_filter.__doc__ = filter_object.__doc__
    similarity_index_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    similarity_index_image_filter.__doc__ += "Available Keyword Arguments:\n"
    similarity_index_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



