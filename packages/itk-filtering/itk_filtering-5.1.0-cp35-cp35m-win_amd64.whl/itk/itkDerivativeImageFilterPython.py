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
    from . import _itkDerivativeImageFilterPython
else:
    import _itkDerivativeImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkDerivativeImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkDerivativeImageFilterPython.SWIG_PyStaticMethod_New

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
import itkImagePython
import itkPointPython
import itkFixedArrayPython
import pyBasePython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkRGBAPixelPython
import ITKCommonBasePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkDerivativeImageFilterID3ID3_New():
  return itkDerivativeImageFilterID3ID3.New()


def itkDerivativeImageFilterID2ID2_New():
  return itkDerivativeImageFilterID2ID2.New()


def itkDerivativeImageFilterIF3IF3_New():
  return itkDerivativeImageFilterIF3IF3.New()


def itkDerivativeImageFilterIF2IF2_New():
  return itkDerivativeImageFilterIF2IF2.New()


def itkDerivativeImageFilterISS3ISS3_New():
  return itkDerivativeImageFilterISS3ISS3.New()


def itkDerivativeImageFilterISS2ISS2_New():
  return itkDerivativeImageFilterISS2ISS2.New()

class itkDerivativeImageFilterID2ID2(itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    r"""Proxy of C++ itkDerivativeImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID2ID2_Clone)
    SignedOutputPixelType = _itkDerivativeImageFilterPython.itkDerivativeImageFilterID2ID2_SignedOutputPixelType
    
    SetOrder = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID2ID2_SetOrder)
    GetOrder = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID2ID2_GetOrder)
    SetDirection = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID2ID2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID2ID2_GetDirection)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID2ID2_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID2ID2_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID2ID2_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID2ID2_GetUseImageSpacing)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID2ID2_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkDerivativeImageFilterPython.delete_itkDerivativeImageFilterID2ID2
    cast = _swig_new_static_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkDerivativeImageFilterID2ID2

        Create a new object of the class itkDerivativeImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDerivativeImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDerivativeImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDerivativeImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDerivativeImageFilterID2ID2 in _itkDerivativeImageFilterPython:
_itkDerivativeImageFilterPython.itkDerivativeImageFilterID2ID2_swigregister(itkDerivativeImageFilterID2ID2)
itkDerivativeImageFilterID2ID2___New_orig__ = _itkDerivativeImageFilterPython.itkDerivativeImageFilterID2ID2___New_orig__
itkDerivativeImageFilterID2ID2_cast = _itkDerivativeImageFilterPython.itkDerivativeImageFilterID2ID2_cast

class itkDerivativeImageFilterID3ID3(itkImageToImageFilterAPython.itkImageToImageFilterID3ID3):
    r"""Proxy of C++ itkDerivativeImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID3ID3_Clone)
    SignedOutputPixelType = _itkDerivativeImageFilterPython.itkDerivativeImageFilterID3ID3_SignedOutputPixelType
    
    SetOrder = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID3ID3_SetOrder)
    GetOrder = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID3ID3_GetOrder)
    SetDirection = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID3ID3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID3ID3_GetDirection)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID3ID3_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID3ID3_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID3ID3_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID3ID3_GetUseImageSpacing)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID3ID3_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkDerivativeImageFilterPython.delete_itkDerivativeImageFilterID3ID3
    cast = _swig_new_static_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkDerivativeImageFilterID3ID3

        Create a new object of the class itkDerivativeImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDerivativeImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDerivativeImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDerivativeImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDerivativeImageFilterID3ID3 in _itkDerivativeImageFilterPython:
_itkDerivativeImageFilterPython.itkDerivativeImageFilterID3ID3_swigregister(itkDerivativeImageFilterID3ID3)
itkDerivativeImageFilterID3ID3___New_orig__ = _itkDerivativeImageFilterPython.itkDerivativeImageFilterID3ID3___New_orig__
itkDerivativeImageFilterID3ID3_cast = _itkDerivativeImageFilterPython.itkDerivativeImageFilterID3ID3_cast

class itkDerivativeImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    r"""Proxy of C++ itkDerivativeImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_Clone)
    SignedOutputPixelType = _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SignedOutputPixelType
    
    SetOrder = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SetOrder)
    GetOrder = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_GetOrder)
    SetDirection = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_GetDirection)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_GetUseImageSpacing)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkDerivativeImageFilterPython.delete_itkDerivativeImageFilterIF2IF2
    cast = _swig_new_static_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkDerivativeImageFilterIF2IF2

        Create a new object of the class itkDerivativeImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDerivativeImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDerivativeImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDerivativeImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDerivativeImageFilterIF2IF2 in _itkDerivativeImageFilterPython:
_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_swigregister(itkDerivativeImageFilterIF2IF2)
itkDerivativeImageFilterIF2IF2___New_orig__ = _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2___New_orig__
itkDerivativeImageFilterIF2IF2_cast = _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF2IF2_cast

class itkDerivativeImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    r"""Proxy of C++ itkDerivativeImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_Clone)
    SignedOutputPixelType = _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SignedOutputPixelType
    
    SetOrder = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SetOrder)
    GetOrder = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_GetOrder)
    SetDirection = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_GetDirection)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_GetUseImageSpacing)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkDerivativeImageFilterPython.delete_itkDerivativeImageFilterIF3IF3
    cast = _swig_new_static_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkDerivativeImageFilterIF3IF3

        Create a new object of the class itkDerivativeImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDerivativeImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDerivativeImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDerivativeImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDerivativeImageFilterIF3IF3 in _itkDerivativeImageFilterPython:
_itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_swigregister(itkDerivativeImageFilterIF3IF3)
itkDerivativeImageFilterIF3IF3___New_orig__ = _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3___New_orig__
itkDerivativeImageFilterIF3IF3_cast = _itkDerivativeImageFilterPython.itkDerivativeImageFilterIF3IF3_cast

class itkDerivativeImageFilterISS2ISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    r"""Proxy of C++ itkDerivativeImageFilterISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_Clone)
    SignedOutputPixelType = _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SignedOutputPixelType
    
    SetOrder = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SetOrder)
    GetOrder = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_GetOrder)
    SetDirection = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_GetDirection)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_GetUseImageSpacing)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkDerivativeImageFilterPython.delete_itkDerivativeImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkDerivativeImageFilterISS2ISS2

        Create a new object of the class itkDerivativeImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDerivativeImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDerivativeImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDerivativeImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDerivativeImageFilterISS2ISS2 in _itkDerivativeImageFilterPython:
_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_swigregister(itkDerivativeImageFilterISS2ISS2)
itkDerivativeImageFilterISS2ISS2___New_orig__ = _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2___New_orig__
itkDerivativeImageFilterISS2ISS2_cast = _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS2ISS2_cast

class itkDerivativeImageFilterISS3ISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    r"""Proxy of C++ itkDerivativeImageFilterISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_Clone)
    SignedOutputPixelType = _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SignedOutputPixelType
    
    SetOrder = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SetOrder)
    GetOrder = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_GetOrder)
    SetDirection = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_GetDirection)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_GetUseImageSpacing)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkDerivativeImageFilterPython.delete_itkDerivativeImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkDerivativeImageFilterISS3ISS3

        Create a new object of the class itkDerivativeImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDerivativeImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDerivativeImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDerivativeImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDerivativeImageFilterISS3ISS3 in _itkDerivativeImageFilterPython:
_itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_swigregister(itkDerivativeImageFilterISS3ISS3)
itkDerivativeImageFilterISS3ISS3___New_orig__ = _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3___New_orig__
itkDerivativeImageFilterISS3ISS3_cast = _itkDerivativeImageFilterPython.itkDerivativeImageFilterISS3ISS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def derivative_image_filter(*args, **kwargs):
    """Procedural interface for DerivativeImageFilter"""
    import itk
    instance = itk.DerivativeImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def derivative_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.DerivativeImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.DerivativeImageFilter.values()[0]
    else:
        filter_object = itk.DerivativeImageFilter

    derivative_image_filter.__doc__ = filter_object.__doc__
    derivative_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    derivative_image_filter.__doc__ += "Available Keyword Arguments:\n"
    derivative_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



