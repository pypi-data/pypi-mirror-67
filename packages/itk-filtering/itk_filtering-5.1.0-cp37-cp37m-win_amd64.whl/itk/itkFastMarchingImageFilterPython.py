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
    from . import _itkFastMarchingImageFilterPython
else:
    import _itkFastMarchingImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkFastMarchingImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkFastMarchingImageFilterPython.SWIG_PyStaticMethod_New

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
import ITKCommonBasePython
import pyBasePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImagePython
import stdcomplexPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkCovariantVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import ITKFastMarchingBasePython
import itkNodePairPython
import itkFastMarchingStoppingCriterionBasePython
import itkLevelSetNodePython

def itkFastMarchingImageFilterID3ID3_New():
  return itkFastMarchingImageFilterID3ID3.New()


def itkFastMarchingImageFilterID2ID2_New():
  return itkFastMarchingImageFilterID2ID2.New()


def itkFastMarchingImageFilterIF3IF3_New():
  return itkFastMarchingImageFilterIF3IF3.New()


def itkFastMarchingImageFilterIF2IF2_New():
  return itkFastMarchingImageFilterIF2IF2.New()

class itkFastMarchingImageFilterEnums(object):
    r"""Proxy of C++ itkFastMarchingImageFilterEnums class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Label_FarPoint = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterEnums_Label_FarPoint
    
    Label_AlivePoint = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterEnums_Label_AlivePoint
    
    Label_TrialPoint = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterEnums_Label_TrialPoint
    
    Label_InitialTrialPoint = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterEnums_Label_InitialTrialPoint
    
    Label_OutsidePoint = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterEnums_Label_OutsidePoint
    

    def __init__(self, *args):
        r"""
        __init__(itkFastMarchingImageFilterEnums self) -> itkFastMarchingImageFilterEnums
        __init__(itkFastMarchingImageFilterEnums self, itkFastMarchingImageFilterEnums arg0) -> itkFastMarchingImageFilterEnums
        """
        _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterEnums_swiginit(self, _itkFastMarchingImageFilterPython.new_itkFastMarchingImageFilterEnums(*args))
    __swig_destroy__ = _itkFastMarchingImageFilterPython.delete_itkFastMarchingImageFilterEnums

# Register itkFastMarchingImageFilterEnums in _itkFastMarchingImageFilterPython:
_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterEnums_swigregister(itkFastMarchingImageFilterEnums)

class itkFastMarchingImageFilterID2ID2(itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    r"""Proxy of C++ itkFastMarchingImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_Clone)
    SetOutsidePoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_SetOutsidePoints)
    SetAlivePoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_SetAlivePoints)
    GetAlivePoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_GetAlivePoints)
    SetTrialPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_SetTrialPoints)
    GetTrialPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_GetTrialPoints)
    GetLabelImage = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_GetLabelImage)
    SetSpeedConstant = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_SetSpeedConstant)
    GetSpeedConstant = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_GetSpeedConstant)
    SetNormalizationFactor = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_SetNormalizationFactor)
    GetNormalizationFactor = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_GetNormalizationFactor)
    SetStoppingValue = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_SetStoppingValue)
    GetStoppingValue = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_GetStoppingValue)
    SetCollectPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_SetCollectPoints)
    GetCollectPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_GetCollectPoints)
    CollectPointsOn = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_CollectPointsOn)
    CollectPointsOff = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_CollectPointsOff)
    GetProcessedPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_GetProcessedPoints)
    SetOutputSize = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_SetOutputSize)
    GetOutputSize = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_GetOutputSize)
    SetOutputRegion = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_SetOutputRegion)
    GetOutputRegion = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_GetOutputRegion)
    SetOutputSpacing = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_SetOutputSpacing)
    GetOutputSpacing = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_GetOutputSpacing)
    SetOutputDirection = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_SetOutputDirection)
    GetOutputDirection = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_GetOutputDirection)
    SetOutputOrigin = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_SetOutputOrigin)
    GetOutputOrigin = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_GetOutputOrigin)
    SetOverrideOutputInformation = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_SetOverrideOutputInformation)
    GetOverrideOutputInformation = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_GetOverrideOutputInformation)
    OverrideOutputInformationOn = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_OverrideOutputInformationOn)
    OverrideOutputInformationOff = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_OverrideOutputInformationOff)
    SameDimensionCheck = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_SameDimensionCheck
    
    SpeedConvertibleToDoubleCheck = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_SpeedConvertibleToDoubleCheck
    
    DoubleConvertibleToLevelSetCheck = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_DoubleConvertibleToLevelSetCheck
    
    LevelSetOStreamWritableCheck = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_LevelSetOStreamWritableCheck
    
    __swig_destroy__ = _itkFastMarchingImageFilterPython.delete_itkFastMarchingImageFilterID2ID2
    cast = _swig_new_static_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingImageFilterID2ID2

        Create a new object of the class itkFastMarchingImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingImageFilterID2ID2 in _itkFastMarchingImageFilterPython:
_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_swigregister(itkFastMarchingImageFilterID2ID2)
itkFastMarchingImageFilterID2ID2___New_orig__ = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2___New_orig__
itkFastMarchingImageFilterID2ID2_cast = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2_cast

class itkFastMarchingImageFilterID3ID3(itkImageToImageFilterAPython.itkImageToImageFilterID3ID3):
    r"""Proxy of C++ itkFastMarchingImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_Clone)
    SetOutsidePoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_SetOutsidePoints)
    SetAlivePoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_SetAlivePoints)
    GetAlivePoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_GetAlivePoints)
    SetTrialPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_SetTrialPoints)
    GetTrialPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_GetTrialPoints)
    GetLabelImage = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_GetLabelImage)
    SetSpeedConstant = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_SetSpeedConstant)
    GetSpeedConstant = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_GetSpeedConstant)
    SetNormalizationFactor = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_SetNormalizationFactor)
    GetNormalizationFactor = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_GetNormalizationFactor)
    SetStoppingValue = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_SetStoppingValue)
    GetStoppingValue = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_GetStoppingValue)
    SetCollectPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_SetCollectPoints)
    GetCollectPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_GetCollectPoints)
    CollectPointsOn = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_CollectPointsOn)
    CollectPointsOff = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_CollectPointsOff)
    GetProcessedPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_GetProcessedPoints)
    SetOutputSize = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_SetOutputSize)
    GetOutputSize = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_GetOutputSize)
    SetOutputRegion = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_SetOutputRegion)
    GetOutputRegion = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_GetOutputRegion)
    SetOutputSpacing = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_SetOutputSpacing)
    GetOutputSpacing = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_GetOutputSpacing)
    SetOutputDirection = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_SetOutputDirection)
    GetOutputDirection = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_GetOutputDirection)
    SetOutputOrigin = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_SetOutputOrigin)
    GetOutputOrigin = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_GetOutputOrigin)
    SetOverrideOutputInformation = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_SetOverrideOutputInformation)
    GetOverrideOutputInformation = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_GetOverrideOutputInformation)
    OverrideOutputInformationOn = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_OverrideOutputInformationOn)
    OverrideOutputInformationOff = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_OverrideOutputInformationOff)
    SameDimensionCheck = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_SameDimensionCheck
    
    SpeedConvertibleToDoubleCheck = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_SpeedConvertibleToDoubleCheck
    
    DoubleConvertibleToLevelSetCheck = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_DoubleConvertibleToLevelSetCheck
    
    LevelSetOStreamWritableCheck = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_LevelSetOStreamWritableCheck
    
    __swig_destroy__ = _itkFastMarchingImageFilterPython.delete_itkFastMarchingImageFilterID3ID3
    cast = _swig_new_static_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingImageFilterID3ID3

        Create a new object of the class itkFastMarchingImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingImageFilterID3ID3 in _itkFastMarchingImageFilterPython:
_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_swigregister(itkFastMarchingImageFilterID3ID3)
itkFastMarchingImageFilterID3ID3___New_orig__ = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3___New_orig__
itkFastMarchingImageFilterID3ID3_cast = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3_cast

class itkFastMarchingImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    r"""Proxy of C++ itkFastMarchingImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_Clone)
    SetOutsidePoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_SetOutsidePoints)
    SetAlivePoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_SetAlivePoints)
    GetAlivePoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_GetAlivePoints)
    SetTrialPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_SetTrialPoints)
    GetTrialPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_GetTrialPoints)
    GetLabelImage = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_GetLabelImage)
    SetSpeedConstant = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_SetSpeedConstant)
    GetSpeedConstant = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_GetSpeedConstant)
    SetNormalizationFactor = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_SetNormalizationFactor)
    GetNormalizationFactor = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_GetNormalizationFactor)
    SetStoppingValue = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_SetStoppingValue)
    GetStoppingValue = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_GetStoppingValue)
    SetCollectPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_SetCollectPoints)
    GetCollectPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_GetCollectPoints)
    CollectPointsOn = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_CollectPointsOn)
    CollectPointsOff = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_CollectPointsOff)
    GetProcessedPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_GetProcessedPoints)
    SetOutputSize = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_SetOutputSize)
    GetOutputSize = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_GetOutputSize)
    SetOutputRegion = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_SetOutputRegion)
    GetOutputRegion = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_GetOutputRegion)
    SetOutputSpacing = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_SetOutputSpacing)
    GetOutputSpacing = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_GetOutputSpacing)
    SetOutputDirection = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_SetOutputDirection)
    GetOutputDirection = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_GetOutputDirection)
    SetOutputOrigin = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_SetOutputOrigin)
    GetOutputOrigin = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_GetOutputOrigin)
    SetOverrideOutputInformation = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_SetOverrideOutputInformation)
    GetOverrideOutputInformation = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_GetOverrideOutputInformation)
    OverrideOutputInformationOn = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_OverrideOutputInformationOn)
    OverrideOutputInformationOff = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_OverrideOutputInformationOff)
    SameDimensionCheck = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_SameDimensionCheck
    
    SpeedConvertibleToDoubleCheck = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_SpeedConvertibleToDoubleCheck
    
    DoubleConvertibleToLevelSetCheck = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_DoubleConvertibleToLevelSetCheck
    
    LevelSetOStreamWritableCheck = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_LevelSetOStreamWritableCheck
    
    __swig_destroy__ = _itkFastMarchingImageFilterPython.delete_itkFastMarchingImageFilterIF2IF2
    cast = _swig_new_static_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingImageFilterIF2IF2

        Create a new object of the class itkFastMarchingImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingImageFilterIF2IF2 in _itkFastMarchingImageFilterPython:
_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_swigregister(itkFastMarchingImageFilterIF2IF2)
itkFastMarchingImageFilterIF2IF2___New_orig__ = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2___New_orig__
itkFastMarchingImageFilterIF2IF2_cast = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2_cast

class itkFastMarchingImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    r"""Proxy of C++ itkFastMarchingImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_Clone)
    SetOutsidePoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_SetOutsidePoints)
    SetAlivePoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_SetAlivePoints)
    GetAlivePoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_GetAlivePoints)
    SetTrialPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_SetTrialPoints)
    GetTrialPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_GetTrialPoints)
    GetLabelImage = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_GetLabelImage)
    SetSpeedConstant = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_SetSpeedConstant)
    GetSpeedConstant = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_GetSpeedConstant)
    SetNormalizationFactor = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_SetNormalizationFactor)
    GetNormalizationFactor = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_GetNormalizationFactor)
    SetStoppingValue = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_SetStoppingValue)
    GetStoppingValue = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_GetStoppingValue)
    SetCollectPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_SetCollectPoints)
    GetCollectPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_GetCollectPoints)
    CollectPointsOn = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_CollectPointsOn)
    CollectPointsOff = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_CollectPointsOff)
    GetProcessedPoints = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_GetProcessedPoints)
    SetOutputSize = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_SetOutputSize)
    GetOutputSize = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_GetOutputSize)
    SetOutputRegion = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_SetOutputRegion)
    GetOutputRegion = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_GetOutputRegion)
    SetOutputSpacing = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_SetOutputSpacing)
    GetOutputSpacing = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_GetOutputSpacing)
    SetOutputDirection = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_SetOutputDirection)
    GetOutputDirection = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_GetOutputDirection)
    SetOutputOrigin = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_SetOutputOrigin)
    GetOutputOrigin = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_GetOutputOrigin)
    SetOverrideOutputInformation = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_SetOverrideOutputInformation)
    GetOverrideOutputInformation = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_GetOverrideOutputInformation)
    OverrideOutputInformationOn = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_OverrideOutputInformationOn)
    OverrideOutputInformationOff = _swig_new_instance_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_OverrideOutputInformationOff)
    SameDimensionCheck = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_SameDimensionCheck
    
    SpeedConvertibleToDoubleCheck = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_SpeedConvertibleToDoubleCheck
    
    DoubleConvertibleToLevelSetCheck = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_DoubleConvertibleToLevelSetCheck
    
    LevelSetOStreamWritableCheck = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_LevelSetOStreamWritableCheck
    
    __swig_destroy__ = _itkFastMarchingImageFilterPython.delete_itkFastMarchingImageFilterIF3IF3
    cast = _swig_new_static_method(_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingImageFilterIF3IF3

        Create a new object of the class itkFastMarchingImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingImageFilterIF3IF3 in _itkFastMarchingImageFilterPython:
_itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_swigregister(itkFastMarchingImageFilterIF3IF3)
itkFastMarchingImageFilterIF3IF3___New_orig__ = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3___New_orig__
itkFastMarchingImageFilterIF3IF3_cast = _itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def fast_marching_image_filter(*args, **kwargs):
    """Procedural interface for FastMarchingImageFilter"""
    import itk
    instance = itk.FastMarchingImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def fast_marching_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.FastMarchingImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.FastMarchingImageFilter.values()[0]
    else:
        filter_object = itk.FastMarchingImageFilter

    fast_marching_image_filter.__doc__ = filter_object.__doc__
    fast_marching_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    fast_marching_image_filter.__doc__ += "Available Keyword Arguments:\n"
    fast_marching_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



