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
    from . import _itkFastMarchingImageFilterBasePython
else:
    import _itkFastMarchingImageFilterBasePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkFastMarchingImageFilterBasePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkFastMarchingImageFilterBasePython.SWIG_PyStaticMethod_New

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


import ITKFastMarchingBasePython
import itkNodePairPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import itkImagePython
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
import itkLevelSetNodePython
import itkFastMarchingStoppingCriterionBasePython
import itkImageToImageFilterAPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython

def itkFastMarchingImageFilterBaseID3ID3_New():
  return itkFastMarchingImageFilterBaseID3ID3.New()


def itkFastMarchingImageFilterBaseID2ID2_New():
  return itkFastMarchingImageFilterBaseID2ID2.New()


def itkFastMarchingImageFilterBaseIF3IF3_New():
  return itkFastMarchingImageFilterBaseIF3IF3.New()


def itkFastMarchingImageFilterBaseIF2IF2_New():
  return itkFastMarchingImageFilterBaseIF2IF2.New()

class itkFastMarchingImageFilterBaseID2ID2(ITKFastMarchingBasePython.itkFastMarchingBaseID2ID2):
    r"""Proxy of C++ itkFastMarchingImageFilterBaseID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_Clone)
    GetModifiableLabelImage = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_GetModifiableLabelImage)
    GetLabelImage = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_GetLabelImage)
    SetOutputSize = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_SetOutputSize)
    GetOutputSize = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_GetOutputSize)
    SetOutputRegion = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_SetOutputRegion)
    GetOutputRegion = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_GetOutputRegion)
    SetOutputSpacing = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_SetOutputSpacing)
    GetOutputSpacing = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_GetOutputSpacing)
    SetOutputDirection = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_SetOutputDirection)
    GetOutputDirection = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_GetOutputDirection)
    SetOutputOrigin = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_SetOutputOrigin)
    GetOutputOrigin = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_GetOutputOrigin)
    SetOverrideOutputInformation = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_SetOverrideOutputInformation)
    GetOverrideOutputInformation = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_GetOverrideOutputInformation)
    OverrideOutputInformationOn = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_OverrideOutputInformationOn)
    OverrideOutputInformationOff = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_OverrideOutputInformationOff)
    __swig_destroy__ = _itkFastMarchingImageFilterBasePython.delete_itkFastMarchingImageFilterBaseID2ID2
    cast = _swig_new_static_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingImageFilterBaseID2ID2

        Create a new object of the class itkFastMarchingImageFilterBaseID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageFilterBaseID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageFilterBaseID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingImageFilterBaseID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingImageFilterBaseID2ID2 in _itkFastMarchingImageFilterBasePython:
_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_swigregister(itkFastMarchingImageFilterBaseID2ID2)
itkFastMarchingImageFilterBaseID2ID2___New_orig__ = _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2___New_orig__
itkFastMarchingImageFilterBaseID2ID2_cast = _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2_cast

class itkFastMarchingImageFilterBaseID3ID3(ITKFastMarchingBasePython.itkFastMarchingBaseID3ID3):
    r"""Proxy of C++ itkFastMarchingImageFilterBaseID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_Clone)
    GetModifiableLabelImage = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_GetModifiableLabelImage)
    GetLabelImage = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_GetLabelImage)
    SetOutputSize = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_SetOutputSize)
    GetOutputSize = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_GetOutputSize)
    SetOutputRegion = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_SetOutputRegion)
    GetOutputRegion = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_GetOutputRegion)
    SetOutputSpacing = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_SetOutputSpacing)
    GetOutputSpacing = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_GetOutputSpacing)
    SetOutputDirection = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_SetOutputDirection)
    GetOutputDirection = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_GetOutputDirection)
    SetOutputOrigin = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_SetOutputOrigin)
    GetOutputOrigin = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_GetOutputOrigin)
    SetOverrideOutputInformation = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_SetOverrideOutputInformation)
    GetOverrideOutputInformation = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_GetOverrideOutputInformation)
    OverrideOutputInformationOn = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_OverrideOutputInformationOn)
    OverrideOutputInformationOff = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_OverrideOutputInformationOff)
    __swig_destroy__ = _itkFastMarchingImageFilterBasePython.delete_itkFastMarchingImageFilterBaseID3ID3
    cast = _swig_new_static_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingImageFilterBaseID3ID3

        Create a new object of the class itkFastMarchingImageFilterBaseID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageFilterBaseID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageFilterBaseID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingImageFilterBaseID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingImageFilterBaseID3ID3 in _itkFastMarchingImageFilterBasePython:
_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_swigregister(itkFastMarchingImageFilterBaseID3ID3)
itkFastMarchingImageFilterBaseID3ID3___New_orig__ = _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3___New_orig__
itkFastMarchingImageFilterBaseID3ID3_cast = _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3_cast

class itkFastMarchingImageFilterBaseIF2IF2(ITKFastMarchingBasePython.itkFastMarchingBaseIF2IF2):
    r"""Proxy of C++ itkFastMarchingImageFilterBaseIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_Clone)
    GetModifiableLabelImage = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetModifiableLabelImage)
    GetLabelImage = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetLabelImage)
    SetOutputSize = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOutputSize)
    GetOutputSize = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOutputSize)
    SetOutputRegion = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOutputRegion)
    GetOutputRegion = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOutputRegion)
    SetOutputSpacing = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOutputSpacing)
    GetOutputSpacing = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOutputSpacing)
    SetOutputDirection = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOutputDirection)
    GetOutputDirection = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOutputDirection)
    SetOutputOrigin = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOutputOrigin)
    GetOutputOrigin = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOutputOrigin)
    SetOverrideOutputInformation = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_SetOverrideOutputInformation)
    GetOverrideOutputInformation = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_GetOverrideOutputInformation)
    OverrideOutputInformationOn = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_OverrideOutputInformationOn)
    OverrideOutputInformationOff = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_OverrideOutputInformationOff)
    __swig_destroy__ = _itkFastMarchingImageFilterBasePython.delete_itkFastMarchingImageFilterBaseIF2IF2
    cast = _swig_new_static_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingImageFilterBaseIF2IF2

        Create a new object of the class itkFastMarchingImageFilterBaseIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageFilterBaseIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageFilterBaseIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingImageFilterBaseIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingImageFilterBaseIF2IF2 in _itkFastMarchingImageFilterBasePython:
_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_swigregister(itkFastMarchingImageFilterBaseIF2IF2)
itkFastMarchingImageFilterBaseIF2IF2___New_orig__ = _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2___New_orig__
itkFastMarchingImageFilterBaseIF2IF2_cast = _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2_cast

class itkFastMarchingImageFilterBaseIF3IF3(ITKFastMarchingBasePython.itkFastMarchingBaseIF3IF3):
    r"""Proxy of C++ itkFastMarchingImageFilterBaseIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_Clone)
    GetModifiableLabelImage = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetModifiableLabelImage)
    GetLabelImage = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetLabelImage)
    SetOutputSize = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOutputSize)
    GetOutputSize = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOutputSize)
    SetOutputRegion = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOutputRegion)
    GetOutputRegion = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOutputRegion)
    SetOutputSpacing = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOutputSpacing)
    GetOutputSpacing = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOutputSpacing)
    SetOutputDirection = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOutputDirection)
    GetOutputDirection = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOutputDirection)
    SetOutputOrigin = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOutputOrigin)
    GetOutputOrigin = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOutputOrigin)
    SetOverrideOutputInformation = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_SetOverrideOutputInformation)
    GetOverrideOutputInformation = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_GetOverrideOutputInformation)
    OverrideOutputInformationOn = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_OverrideOutputInformationOn)
    OverrideOutputInformationOff = _swig_new_instance_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_OverrideOutputInformationOff)
    __swig_destroy__ = _itkFastMarchingImageFilterBasePython.delete_itkFastMarchingImageFilterBaseIF3IF3
    cast = _swig_new_static_method(_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingImageFilterBaseIF3IF3

        Create a new object of the class itkFastMarchingImageFilterBaseIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageFilterBaseIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageFilterBaseIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingImageFilterBaseIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingImageFilterBaseIF3IF3 in _itkFastMarchingImageFilterBasePython:
_itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_swigregister(itkFastMarchingImageFilterBaseIF3IF3)
itkFastMarchingImageFilterBaseIF3IF3___New_orig__ = _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3___New_orig__
itkFastMarchingImageFilterBaseIF3IF3_cast = _itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def fast_marching_image_filter_base(*args, **kwargs):
    """Procedural interface for FastMarchingImageFilterBase"""
    import itk
    instance = itk.FastMarchingImageFilterBase.New(*args, **kwargs)
    return instance.__internal_call__()

def fast_marching_image_filter_base_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.FastMarchingImageFilterBase, itkTemplate.itkTemplate):
        filter_object = itk.FastMarchingImageFilterBase.values()[0]
    else:
        filter_object = itk.FastMarchingImageFilterBase

    fast_marching_image_filter_base.__doc__ = filter_object.__doc__
    fast_marching_image_filter_base.__doc__ += "\n Args are Input(s) to the filter.\n"
    fast_marching_image_filter_base.__doc__ += "Available Keyword Arguments:\n"
    fast_marching_image_filter_base.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



