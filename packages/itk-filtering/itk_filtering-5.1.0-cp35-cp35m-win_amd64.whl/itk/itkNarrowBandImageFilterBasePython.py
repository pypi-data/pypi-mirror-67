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
    from . import _itkNarrowBandImageFilterBasePython
else:
    import _itkNarrowBandImageFilterBasePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkNarrowBandImageFilterBasePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkNarrowBandImageFilterBasePython.SWIG_PyStaticMethod_New

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


import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
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
import ITKCommonBasePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython
import itkFiniteDifferenceFunctionPython
import ITKNarrowBandBasePython

def itkNarrowBandImageFilterBaseID3ID3_New():
  return itkNarrowBandImageFilterBaseID3ID3.New()


def itkNarrowBandImageFilterBaseID2ID2_New():
  return itkNarrowBandImageFilterBaseID2ID2.New()


def itkNarrowBandImageFilterBaseIF3IF3_New():
  return itkNarrowBandImageFilterBaseIF3IF3.New()


def itkNarrowBandImageFilterBaseIF2IF2_New():
  return itkNarrowBandImageFilterBaseIF2IF2.New()

class itkNarrowBandImageFilterBaseID2ID2(itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterID2ID2):
    r"""Proxy of C++ itkNarrowBandImageFilterBaseID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_SetIsoSurfaceValue)
    GetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_GetIsoSurfaceValue)
    InsertNarrowBandNode = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_InsertNarrowBandNode)
    SetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_SetNarrowBandTotalRadius)
    GetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_GetNarrowBandTotalRadius)
    SetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_SetNarrowBandInnerRadius)
    GetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_GetNarrowBandInnerRadius)
    CreateNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_CreateNarrowBand)
    SetNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_SetNarrowBand)
    CopyInputToOutput = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_CopyInputToOutput)
    __swig_destroy__ = _itkNarrowBandImageFilterBasePython.delete_itkNarrowBandImageFilterBaseID2ID2
    cast = _swig_new_static_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkNarrowBandImageFilterBaseID2ID2

        Create a new object of the class itkNarrowBandImageFilterBaseID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNarrowBandImageFilterBaseID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNarrowBandImageFilterBaseID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNarrowBandImageFilterBaseID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkNarrowBandImageFilterBaseID2ID2 in _itkNarrowBandImageFilterBasePython:
_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_swigregister(itkNarrowBandImageFilterBaseID2ID2)
itkNarrowBandImageFilterBaseID2ID2_cast = _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_cast

class itkNarrowBandImageFilterBaseID3ID3(itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterID3ID3):
    r"""Proxy of C++ itkNarrowBandImageFilterBaseID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_SetIsoSurfaceValue)
    GetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_GetIsoSurfaceValue)
    InsertNarrowBandNode = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_InsertNarrowBandNode)
    SetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_SetNarrowBandTotalRadius)
    GetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_GetNarrowBandTotalRadius)
    SetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_SetNarrowBandInnerRadius)
    GetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_GetNarrowBandInnerRadius)
    CreateNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_CreateNarrowBand)
    SetNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_SetNarrowBand)
    CopyInputToOutput = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_CopyInputToOutput)
    __swig_destroy__ = _itkNarrowBandImageFilterBasePython.delete_itkNarrowBandImageFilterBaseID3ID3
    cast = _swig_new_static_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkNarrowBandImageFilterBaseID3ID3

        Create a new object of the class itkNarrowBandImageFilterBaseID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNarrowBandImageFilterBaseID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNarrowBandImageFilterBaseID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNarrowBandImageFilterBaseID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkNarrowBandImageFilterBaseID3ID3 in _itkNarrowBandImageFilterBasePython:
_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_swigregister(itkNarrowBandImageFilterBaseID3ID3)
itkNarrowBandImageFilterBaseID3ID3_cast = _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_cast

class itkNarrowBandImageFilterBaseIF2IF2(itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterIF2IF2):
    r"""Proxy of C++ itkNarrowBandImageFilterBaseIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_SetIsoSurfaceValue)
    GetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_GetIsoSurfaceValue)
    InsertNarrowBandNode = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_InsertNarrowBandNode)
    SetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_SetNarrowBandTotalRadius)
    GetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_GetNarrowBandTotalRadius)
    SetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_SetNarrowBandInnerRadius)
    GetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_GetNarrowBandInnerRadius)
    CreateNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_CreateNarrowBand)
    SetNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_SetNarrowBand)
    CopyInputToOutput = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_CopyInputToOutput)
    __swig_destroy__ = _itkNarrowBandImageFilterBasePython.delete_itkNarrowBandImageFilterBaseIF2IF2
    cast = _swig_new_static_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkNarrowBandImageFilterBaseIF2IF2

        Create a new object of the class itkNarrowBandImageFilterBaseIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNarrowBandImageFilterBaseIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNarrowBandImageFilterBaseIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNarrowBandImageFilterBaseIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkNarrowBandImageFilterBaseIF2IF2 in _itkNarrowBandImageFilterBasePython:
_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_swigregister(itkNarrowBandImageFilterBaseIF2IF2)
itkNarrowBandImageFilterBaseIF2IF2_cast = _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_cast

class itkNarrowBandImageFilterBaseIF3IF3(itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterIF3IF3):
    r"""Proxy of C++ itkNarrowBandImageFilterBaseIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_SetIsoSurfaceValue)
    GetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_GetIsoSurfaceValue)
    InsertNarrowBandNode = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_InsertNarrowBandNode)
    SetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_SetNarrowBandTotalRadius)
    GetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_GetNarrowBandTotalRadius)
    SetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_SetNarrowBandInnerRadius)
    GetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_GetNarrowBandInnerRadius)
    CreateNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_CreateNarrowBand)
    SetNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_SetNarrowBand)
    CopyInputToOutput = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_CopyInputToOutput)
    __swig_destroy__ = _itkNarrowBandImageFilterBasePython.delete_itkNarrowBandImageFilterBaseIF3IF3
    cast = _swig_new_static_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkNarrowBandImageFilterBaseIF3IF3

        Create a new object of the class itkNarrowBandImageFilterBaseIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNarrowBandImageFilterBaseIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNarrowBandImageFilterBaseIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNarrowBandImageFilterBaseIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkNarrowBandImageFilterBaseIF3IF3 in _itkNarrowBandImageFilterBasePython:
_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_swigregister(itkNarrowBandImageFilterBaseIF3IF3)
itkNarrowBandImageFilterBaseIF3IF3_cast = _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def narrow_band_image_filter_base(*args, **kwargs):
    """Procedural interface for NarrowBandImageFilterBase"""
    import itk
    instance = itk.NarrowBandImageFilterBase.New(*args, **kwargs)
    return instance.__internal_call__()

def narrow_band_image_filter_base_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.NarrowBandImageFilterBase, itkTemplate.itkTemplate):
        filter_object = itk.NarrowBandImageFilterBase.values()[0]
    else:
        filter_object = itk.NarrowBandImageFilterBase

    narrow_band_image_filter_base.__doc__ = filter_object.__doc__
    narrow_band_image_filter_base.__doc__ += "\n Args are Input(s) to the filter.\n"
    narrow_band_image_filter_base.__doc__ += "Available Keyword Arguments:\n"
    narrow_band_image_filter_base.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



