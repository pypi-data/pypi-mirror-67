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
    from . import _itkFastMarchingUpwindGradientImageFilterPython
else:
    import _itkFastMarchingUpwindGradientImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkFastMarchingUpwindGradientImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkFastMarchingUpwindGradientImageFilterPython.SWIG_PyStaticMethod_New

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
import itkFastMarchingImageFilterPython

def itkFastMarchingUpwindGradientImageFilterID3ID3_New():
  return itkFastMarchingUpwindGradientImageFilterID3ID3.New()


def itkFastMarchingUpwindGradientImageFilterID2ID2_New():
  return itkFastMarchingUpwindGradientImageFilterID2ID2.New()


def itkFastMarchingUpwindGradientImageFilterIF3IF3_New():
  return itkFastMarchingUpwindGradientImageFilterIF3IF3.New()


def itkFastMarchingUpwindGradientImageFilterIF2IF2_New():
  return itkFastMarchingUpwindGradientImageFilterIF2IF2.New()

class itkFastMarchingUpwindGradientImageFilterID2ID2(itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID2ID2):
    r"""Proxy of C++ itkFastMarchingUpwindGradientImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_Clone)
    SetTargetPoints = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_SetTargetPoints)
    GetTargetPoints = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_GetTargetPoints)
    GetReachedTargetPoints = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_GetReachedTargetPoints)
    GetGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_GetGradientImage)
    SetGenerateGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_SetGenerateGradientImage)
    GetGenerateGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_GetGenerateGradientImage)
    GenerateGradientImageOn = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_GenerateGradientImageOn)
    GenerateGradientImageOff = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_GenerateGradientImageOff)
    SetTargetOffset = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_SetTargetOffset)
    GetTargetOffset = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_GetTargetOffset)
    SetTargetReachedMode = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_SetTargetReachedMode)
    GetTargetReachedMode = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_GetTargetReachedMode)
    SetTargetReachedModeToNoTargets = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_SetTargetReachedModeToNoTargets)
    SetTargetReachedModeToOneTarget = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_SetTargetReachedModeToOneTarget)
    SetTargetReachedModeToSomeTargets = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_SetTargetReachedModeToSomeTargets)
    SetTargetReachedModeToAllTargets = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_SetTargetReachedModeToAllTargets)
    GetNumberOfTargets = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_GetNumberOfTargets)
    GetTargetValue = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_GetTargetValue)
    NoTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_NoTargets
    
    OneTarget = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_OneTarget
    
    SomeTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_SomeTargets
    
    AllTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_AllTargets
    
    LevelSetDoubleDivisionOperatorsCheck = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_LevelSetDoubleDivisionOperatorsCheck
    
    LevelSetDoubleDivisionAndAssignOperatorsCheck = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_LevelSetDoubleDivisionAndAssignOperatorsCheck
    
    __swig_destroy__ = _itkFastMarchingUpwindGradientImageFilterPython.delete_itkFastMarchingUpwindGradientImageFilterID2ID2
    cast = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingUpwindGradientImageFilterID2ID2

        Create a new object of the class itkFastMarchingUpwindGradientImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingUpwindGradientImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingUpwindGradientImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingUpwindGradientImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingUpwindGradientImageFilterID2ID2 in _itkFastMarchingUpwindGradientImageFilterPython:
_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_swigregister(itkFastMarchingUpwindGradientImageFilterID2ID2)
itkFastMarchingUpwindGradientImageFilterID2ID2___New_orig__ = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2___New_orig__
itkFastMarchingUpwindGradientImageFilterID2ID2_cast = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID2ID2_cast

class itkFastMarchingUpwindGradientImageFilterID3ID3(itkFastMarchingImageFilterPython.itkFastMarchingImageFilterID3ID3):
    r"""Proxy of C++ itkFastMarchingUpwindGradientImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_Clone)
    SetTargetPoints = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_SetTargetPoints)
    GetTargetPoints = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_GetTargetPoints)
    GetReachedTargetPoints = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_GetReachedTargetPoints)
    GetGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_GetGradientImage)
    SetGenerateGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_SetGenerateGradientImage)
    GetGenerateGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_GetGenerateGradientImage)
    GenerateGradientImageOn = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_GenerateGradientImageOn)
    GenerateGradientImageOff = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_GenerateGradientImageOff)
    SetTargetOffset = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_SetTargetOffset)
    GetTargetOffset = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_GetTargetOffset)
    SetTargetReachedMode = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_SetTargetReachedMode)
    GetTargetReachedMode = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_GetTargetReachedMode)
    SetTargetReachedModeToNoTargets = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_SetTargetReachedModeToNoTargets)
    SetTargetReachedModeToOneTarget = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_SetTargetReachedModeToOneTarget)
    SetTargetReachedModeToSomeTargets = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_SetTargetReachedModeToSomeTargets)
    SetTargetReachedModeToAllTargets = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_SetTargetReachedModeToAllTargets)
    GetNumberOfTargets = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_GetNumberOfTargets)
    GetTargetValue = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_GetTargetValue)
    NoTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_NoTargets
    
    OneTarget = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_OneTarget
    
    SomeTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_SomeTargets
    
    AllTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_AllTargets
    
    LevelSetDoubleDivisionOperatorsCheck = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_LevelSetDoubleDivisionOperatorsCheck
    
    LevelSetDoubleDivisionAndAssignOperatorsCheck = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_LevelSetDoubleDivisionAndAssignOperatorsCheck
    
    __swig_destroy__ = _itkFastMarchingUpwindGradientImageFilterPython.delete_itkFastMarchingUpwindGradientImageFilterID3ID3
    cast = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingUpwindGradientImageFilterID3ID3

        Create a new object of the class itkFastMarchingUpwindGradientImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingUpwindGradientImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingUpwindGradientImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingUpwindGradientImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingUpwindGradientImageFilterID3ID3 in _itkFastMarchingUpwindGradientImageFilterPython:
_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_swigregister(itkFastMarchingUpwindGradientImageFilterID3ID3)
itkFastMarchingUpwindGradientImageFilterID3ID3___New_orig__ = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3___New_orig__
itkFastMarchingUpwindGradientImageFilterID3ID3_cast = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterID3ID3_cast

class itkFastMarchingUpwindGradientImageFilterIF2IF2(itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF2IF2):
    r"""Proxy of C++ itkFastMarchingUpwindGradientImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_Clone)
    SetTargetPoints = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetPoints)
    GetTargetPoints = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetTargetPoints)
    GetReachedTargetPoints = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetReachedTargetPoints)
    GetGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetGradientImage)
    SetGenerateGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetGenerateGradientImage)
    GetGenerateGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetGenerateGradientImage)
    GenerateGradientImageOn = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GenerateGradientImageOn)
    GenerateGradientImageOff = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GenerateGradientImageOff)
    SetTargetOffset = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetOffset)
    GetTargetOffset = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetTargetOffset)
    SetTargetReachedMode = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetReachedMode)
    GetTargetReachedMode = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetTargetReachedMode)
    SetTargetReachedModeToNoTargets = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetReachedModeToNoTargets)
    SetTargetReachedModeToOneTarget = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetReachedModeToOneTarget)
    SetTargetReachedModeToSomeTargets = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetReachedModeToSomeTargets)
    SetTargetReachedModeToAllTargets = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SetTargetReachedModeToAllTargets)
    GetNumberOfTargets = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetNumberOfTargets)
    GetTargetValue = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_GetTargetValue)
    NoTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_NoTargets
    
    OneTarget = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_OneTarget
    
    SomeTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_SomeTargets
    
    AllTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_AllTargets
    
    LevelSetDoubleDivisionOperatorsCheck = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_LevelSetDoubleDivisionOperatorsCheck
    
    LevelSetDoubleDivisionAndAssignOperatorsCheck = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_LevelSetDoubleDivisionAndAssignOperatorsCheck
    
    __swig_destroy__ = _itkFastMarchingUpwindGradientImageFilterPython.delete_itkFastMarchingUpwindGradientImageFilterIF2IF2
    cast = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingUpwindGradientImageFilterIF2IF2

        Create a new object of the class itkFastMarchingUpwindGradientImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingUpwindGradientImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingUpwindGradientImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingUpwindGradientImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingUpwindGradientImageFilterIF2IF2 in _itkFastMarchingUpwindGradientImageFilterPython:
_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_swigregister(itkFastMarchingUpwindGradientImageFilterIF2IF2)
itkFastMarchingUpwindGradientImageFilterIF2IF2___New_orig__ = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2___New_orig__
itkFastMarchingUpwindGradientImageFilterIF2IF2_cast = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF2IF2_cast

class itkFastMarchingUpwindGradientImageFilterIF3IF3(itkFastMarchingImageFilterPython.itkFastMarchingImageFilterIF3IF3):
    r"""Proxy of C++ itkFastMarchingUpwindGradientImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_Clone)
    SetTargetPoints = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetPoints)
    GetTargetPoints = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetTargetPoints)
    GetReachedTargetPoints = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetReachedTargetPoints)
    GetGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetGradientImage)
    SetGenerateGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetGenerateGradientImage)
    GetGenerateGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetGenerateGradientImage)
    GenerateGradientImageOn = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GenerateGradientImageOn)
    GenerateGradientImageOff = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GenerateGradientImageOff)
    SetTargetOffset = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetOffset)
    GetTargetOffset = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetTargetOffset)
    SetTargetReachedMode = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetReachedMode)
    GetTargetReachedMode = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetTargetReachedMode)
    SetTargetReachedModeToNoTargets = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetReachedModeToNoTargets)
    SetTargetReachedModeToOneTarget = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetReachedModeToOneTarget)
    SetTargetReachedModeToSomeTargets = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetReachedModeToSomeTargets)
    SetTargetReachedModeToAllTargets = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SetTargetReachedModeToAllTargets)
    GetNumberOfTargets = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetNumberOfTargets)
    GetTargetValue = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_GetTargetValue)
    NoTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_NoTargets
    
    OneTarget = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_OneTarget
    
    SomeTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_SomeTargets
    
    AllTargets = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_AllTargets
    
    LevelSetDoubleDivisionOperatorsCheck = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_LevelSetDoubleDivisionOperatorsCheck
    
    LevelSetDoubleDivisionAndAssignOperatorsCheck = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_LevelSetDoubleDivisionAndAssignOperatorsCheck
    
    __swig_destroy__ = _itkFastMarchingUpwindGradientImageFilterPython.delete_itkFastMarchingUpwindGradientImageFilterIF3IF3
    cast = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingUpwindGradientImageFilterIF3IF3

        Create a new object of the class itkFastMarchingUpwindGradientImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingUpwindGradientImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingUpwindGradientImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingUpwindGradientImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingUpwindGradientImageFilterIF3IF3 in _itkFastMarchingUpwindGradientImageFilterPython:
_itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_swigregister(itkFastMarchingUpwindGradientImageFilterIF3IF3)
itkFastMarchingUpwindGradientImageFilterIF3IF3___New_orig__ = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3___New_orig__
itkFastMarchingUpwindGradientImageFilterIF3IF3_cast = _itkFastMarchingUpwindGradientImageFilterPython.itkFastMarchingUpwindGradientImageFilterIF3IF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def fast_marching_upwind_gradient_image_filter(*args, **kwargs):
    """Procedural interface for FastMarchingUpwindGradientImageFilter"""
    import itk
    instance = itk.FastMarchingUpwindGradientImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def fast_marching_upwind_gradient_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.FastMarchingUpwindGradientImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.FastMarchingUpwindGradientImageFilter.values()[0]
    else:
        filter_object = itk.FastMarchingUpwindGradientImageFilter

    fast_marching_upwind_gradient_image_filter.__doc__ = filter_object.__doc__
    fast_marching_upwind_gradient_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    fast_marching_upwind_gradient_image_filter.__doc__ += "Available Keyword Arguments:\n"
    fast_marching_upwind_gradient_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



