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
    from . import _itkParallelSparseFieldLevelSetImageFilterPython
else:
    import _itkParallelSparseFieldLevelSetImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkParallelSparseFieldLevelSetImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkParallelSparseFieldLevelSetImageFilterPython.SWIG_PyStaticMethod_New

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


import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import ITKCommonBasePython
import itkFiniteDifferenceImageFilterPython
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
import itkFiniteDifferenceFunctionPython

def itkSparseFieldLayerPSFLSNI3_New():
  return itkSparseFieldLayerPSFLSNI3.New()


def itkSparseFieldLayerPSFLSNI2_New():
  return itkSparseFieldLayerPSFLSNI2.New()


def itkParallelSparseFieldLevelSetImageFilterID3ID3_New():
  return itkParallelSparseFieldLevelSetImageFilterID3ID3.New()


def itkParallelSparseFieldLevelSetImageFilterID2ID2_New():
  return itkParallelSparseFieldLevelSetImageFilterID2ID2.New()


def itkParallelSparseFieldLevelSetImageFilterIF3IF3_New():
  return itkParallelSparseFieldLevelSetImageFilterIF3IF3.New()


def itkParallelSparseFieldLevelSetImageFilterIF2IF2_New():
  return itkParallelSparseFieldLevelSetImageFilterIF2IF2.New()

class itkParallelSparseFieldLevelSetImageFilterID2ID2(itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterID2ID2):
    r"""Proxy of C++ itkParallelSparseFieldLevelSetImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID2ID2_Clone)
    SetNumberOfLayers = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID2ID2_SetNumberOfLayers)
    GetNumberOfLayers = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID2ID2_GetNumberOfLayers)
    SetIsoSurfaceValue = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID2ID2_SetIsoSurfaceValue)
    GetIsoSurfaceValue = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID2ID2_GetIsoSurfaceValue)
    GetActiveListForIndex = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID2ID2_GetActiveListForIndex)
    OutputEqualityComparableCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID2ID2_OutputEqualityComparableCheck
    
    DoubleConvertibleToOutputCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID2ID2_DoubleConvertibleToOutputCheck
    
    OutputOStreamWritableCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID2ID2_OutputOStreamWritableCheck
    
    __swig_destroy__ = _itkParallelSparseFieldLevelSetImageFilterPython.delete_itkParallelSparseFieldLevelSetImageFilterID2ID2
    cast = _swig_new_static_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkParallelSparseFieldLevelSetImageFilterID2ID2

        Create a new object of the class itkParallelSparseFieldLevelSetImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkParallelSparseFieldLevelSetImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkParallelSparseFieldLevelSetImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkParallelSparseFieldLevelSetImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkParallelSparseFieldLevelSetImageFilterID2ID2 in _itkParallelSparseFieldLevelSetImageFilterPython:
_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID2ID2_swigregister(itkParallelSparseFieldLevelSetImageFilterID2ID2)
itkParallelSparseFieldLevelSetImageFilterID2ID2___New_orig__ = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID2ID2___New_orig__
itkParallelSparseFieldLevelSetImageFilterID2ID2_cast = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID2ID2_cast

class itkParallelSparseFieldLevelSetImageFilterID3ID3(itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterID3ID3):
    r"""Proxy of C++ itkParallelSparseFieldLevelSetImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID3ID3_Clone)
    SetNumberOfLayers = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID3ID3_SetNumberOfLayers)
    GetNumberOfLayers = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID3ID3_GetNumberOfLayers)
    SetIsoSurfaceValue = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID3ID3_SetIsoSurfaceValue)
    GetIsoSurfaceValue = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID3ID3_GetIsoSurfaceValue)
    GetActiveListForIndex = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID3ID3_GetActiveListForIndex)
    OutputEqualityComparableCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID3ID3_OutputEqualityComparableCheck
    
    DoubleConvertibleToOutputCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID3ID3_DoubleConvertibleToOutputCheck
    
    OutputOStreamWritableCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID3ID3_OutputOStreamWritableCheck
    
    __swig_destroy__ = _itkParallelSparseFieldLevelSetImageFilterPython.delete_itkParallelSparseFieldLevelSetImageFilterID3ID3
    cast = _swig_new_static_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkParallelSparseFieldLevelSetImageFilterID3ID3

        Create a new object of the class itkParallelSparseFieldLevelSetImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkParallelSparseFieldLevelSetImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkParallelSparseFieldLevelSetImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkParallelSparseFieldLevelSetImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkParallelSparseFieldLevelSetImageFilterID3ID3 in _itkParallelSparseFieldLevelSetImageFilterPython:
_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID3ID3_swigregister(itkParallelSparseFieldLevelSetImageFilterID3ID3)
itkParallelSparseFieldLevelSetImageFilterID3ID3___New_orig__ = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID3ID3___New_orig__
itkParallelSparseFieldLevelSetImageFilterID3ID3_cast = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterID3ID3_cast

class itkParallelSparseFieldLevelSetImageFilterIF2IF2(itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterIF2IF2):
    r"""Proxy of C++ itkParallelSparseFieldLevelSetImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_Clone)
    SetNumberOfLayers = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_SetNumberOfLayers)
    GetNumberOfLayers = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_GetNumberOfLayers)
    SetIsoSurfaceValue = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_SetIsoSurfaceValue)
    GetIsoSurfaceValue = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_GetIsoSurfaceValue)
    GetActiveListForIndex = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_GetActiveListForIndex)
    OutputEqualityComparableCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_OutputEqualityComparableCheck
    
    DoubleConvertibleToOutputCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    
    OutputOStreamWritableCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_OutputOStreamWritableCheck
    
    __swig_destroy__ = _itkParallelSparseFieldLevelSetImageFilterPython.delete_itkParallelSparseFieldLevelSetImageFilterIF2IF2
    cast = _swig_new_static_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkParallelSparseFieldLevelSetImageFilterIF2IF2

        Create a new object of the class itkParallelSparseFieldLevelSetImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkParallelSparseFieldLevelSetImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkParallelSparseFieldLevelSetImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkParallelSparseFieldLevelSetImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkParallelSparseFieldLevelSetImageFilterIF2IF2 in _itkParallelSparseFieldLevelSetImageFilterPython:
_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_swigregister(itkParallelSparseFieldLevelSetImageFilterIF2IF2)
itkParallelSparseFieldLevelSetImageFilterIF2IF2___New_orig__ = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2___New_orig__
itkParallelSparseFieldLevelSetImageFilterIF2IF2_cast = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF2IF2_cast

class itkParallelSparseFieldLevelSetImageFilterIF3IF3(itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterIF3IF3):
    r"""Proxy of C++ itkParallelSparseFieldLevelSetImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_Clone)
    SetNumberOfLayers = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_SetNumberOfLayers)
    GetNumberOfLayers = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_GetNumberOfLayers)
    SetIsoSurfaceValue = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_SetIsoSurfaceValue)
    GetIsoSurfaceValue = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_GetIsoSurfaceValue)
    GetActiveListForIndex = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_GetActiveListForIndex)
    OutputEqualityComparableCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_OutputEqualityComparableCheck
    
    DoubleConvertibleToOutputCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    
    OutputOStreamWritableCheck = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_OutputOStreamWritableCheck
    
    __swig_destroy__ = _itkParallelSparseFieldLevelSetImageFilterPython.delete_itkParallelSparseFieldLevelSetImageFilterIF3IF3
    cast = _swig_new_static_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkParallelSparseFieldLevelSetImageFilterIF3IF3

        Create a new object of the class itkParallelSparseFieldLevelSetImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkParallelSparseFieldLevelSetImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkParallelSparseFieldLevelSetImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkParallelSparseFieldLevelSetImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkParallelSparseFieldLevelSetImageFilterIF3IF3 in _itkParallelSparseFieldLevelSetImageFilterPython:
_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_swigregister(itkParallelSparseFieldLevelSetImageFilterIF3IF3)
itkParallelSparseFieldLevelSetImageFilterIF3IF3___New_orig__ = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3___New_orig__
itkParallelSparseFieldLevelSetImageFilterIF3IF3_cast = _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetImageFilterIF3IF3_cast

class itkParallelSparseFieldLevelSetNodeI2(object):
    r"""Proxy of C++ itkParallelSparseFieldLevelSetNodeI2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(itkParallelSparseFieldLevelSetNodeI2 self) -> itkParallelSparseFieldLevelSetNodeI2
        __init__(itkParallelSparseFieldLevelSetNodeI2 self, itkParallelSparseFieldLevelSetNodeI2 arg0) -> itkParallelSparseFieldLevelSetNodeI2
        """
        _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetNodeI2_swiginit(self, _itkParallelSparseFieldLevelSetImageFilterPython.new_itkParallelSparseFieldLevelSetNodeI2(*args))
    __swig_destroy__ = _itkParallelSparseFieldLevelSetImageFilterPython.delete_itkParallelSparseFieldLevelSetNodeI2

# Register itkParallelSparseFieldLevelSetNodeI2 in _itkParallelSparseFieldLevelSetImageFilterPython:
_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetNodeI2_swigregister(itkParallelSparseFieldLevelSetNodeI2)

class itkParallelSparseFieldLevelSetNodeI3(object):
    r"""Proxy of C++ itkParallelSparseFieldLevelSetNodeI3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(itkParallelSparseFieldLevelSetNodeI3 self) -> itkParallelSparseFieldLevelSetNodeI3
        __init__(itkParallelSparseFieldLevelSetNodeI3 self, itkParallelSparseFieldLevelSetNodeI3 arg0) -> itkParallelSparseFieldLevelSetNodeI3
        """
        _itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetNodeI3_swiginit(self, _itkParallelSparseFieldLevelSetImageFilterPython.new_itkParallelSparseFieldLevelSetNodeI3(*args))
    __swig_destroy__ = _itkParallelSparseFieldLevelSetImageFilterPython.delete_itkParallelSparseFieldLevelSetNodeI3

# Register itkParallelSparseFieldLevelSetNodeI3 in _itkParallelSparseFieldLevelSetImageFilterPython:
_itkParallelSparseFieldLevelSetImageFilterPython.itkParallelSparseFieldLevelSetNodeI3_swigregister(itkParallelSparseFieldLevelSetNodeI3)

class itkSparseFieldLayerPSFLSNI2(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkSparseFieldLayerPSFLSNI2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2___New_orig__)
    Clone = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_Clone)
    Front = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_Front)
    PopFront = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_PopFront)
    PushFront = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_PushFront)
    Unlink = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_Unlink)
    Empty = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_Empty)
    Size = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_Size)
    SplitRegions = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_SplitRegions)
    __swig_destroy__ = _itkParallelSparseFieldLevelSetImageFilterPython.delete_itkSparseFieldLayerPSFLSNI2
    cast = _swig_new_static_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_cast)

    def New(*args, **kargs):
        """New() -> itkSparseFieldLayerPSFLSNI2

        Create a new object of the class itkSparseFieldLayerPSFLSNI2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSparseFieldLayerPSFLSNI2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSparseFieldLayerPSFLSNI2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSparseFieldLayerPSFLSNI2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSparseFieldLayerPSFLSNI2 in _itkParallelSparseFieldLevelSetImageFilterPython:
_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_swigregister(itkSparseFieldLayerPSFLSNI2)
itkSparseFieldLayerPSFLSNI2___New_orig__ = _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2___New_orig__
itkSparseFieldLayerPSFLSNI2_cast = _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI2_cast

class itkSparseFieldLayerPSFLSNI3(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkSparseFieldLayerPSFLSNI3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3___New_orig__)
    Clone = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_Clone)
    Front = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_Front)
    PopFront = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_PopFront)
    PushFront = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_PushFront)
    Unlink = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_Unlink)
    Empty = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_Empty)
    Size = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_Size)
    SplitRegions = _swig_new_instance_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_SplitRegions)
    __swig_destroy__ = _itkParallelSparseFieldLevelSetImageFilterPython.delete_itkSparseFieldLayerPSFLSNI3
    cast = _swig_new_static_method(_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_cast)

    def New(*args, **kargs):
        """New() -> itkSparseFieldLayerPSFLSNI3

        Create a new object of the class itkSparseFieldLayerPSFLSNI3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSparseFieldLayerPSFLSNI3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSparseFieldLayerPSFLSNI3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSparseFieldLayerPSFLSNI3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSparseFieldLayerPSFLSNI3 in _itkParallelSparseFieldLevelSetImageFilterPython:
_itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_swigregister(itkSparseFieldLayerPSFLSNI3)
itkSparseFieldLayerPSFLSNI3___New_orig__ = _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3___New_orig__
itkSparseFieldLayerPSFLSNI3_cast = _itkParallelSparseFieldLevelSetImageFilterPython.itkSparseFieldLayerPSFLSNI3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def parallel_sparse_field_level_set_image_filter(*args, **kwargs):
    """Procedural interface for ParallelSparseFieldLevelSetImageFilter"""
    import itk
    instance = itk.ParallelSparseFieldLevelSetImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def parallel_sparse_field_level_set_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ParallelSparseFieldLevelSetImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.ParallelSparseFieldLevelSetImageFilter.values()[0]
    else:
        filter_object = itk.ParallelSparseFieldLevelSetImageFilter

    parallel_sparse_field_level_set_image_filter.__doc__ = filter_object.__doc__
    parallel_sparse_field_level_set_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    parallel_sparse_field_level_set_image_filter.__doc__ += "Available Keyword Arguments:\n"
    parallel_sparse_field_level_set_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



