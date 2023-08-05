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
    from . import _itkShapePriorSegmentationLevelSetImageFilterPython
else:
    import _itkShapePriorSegmentationLevelSetImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkShapePriorSegmentationLevelSetImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkShapePriorSegmentationLevelSetImageFilterPython.SWIG_PyStaticMethod_New

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


import itkSegmentationLevelSetImageFilterPython
import ITKCommonBasePython
import pyBasePython
import itkSparseFieldLevelSetImageFilterPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
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
import itkImageRegionPython
import itkRGBPixelPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterBPython
import itkFiniteDifferenceFunctionPython
import itkSegmentationLevelSetFunctionPython
import itkLevelSetFunctionPython
import itkOptimizerParametersPython
import itkArrayPython
import itkShapePriorMAPCostFunctionBasePython
import ITKCostFunctionsPython
import vnl_least_squares_functionPython
import vnl_cost_functionPython
import vnl_unary_functionPython
import itkArray2DPython
import itkCostFunctionPython
import itkShapeSignedDistanceFunctionPython
import itkSpatialFunctionPython
import itkFunctionBasePython
import itkContinuousIndexPython
import ITKFastMarchingBasePython
import itkNodePairPython
import itkFastMarchingStoppingCriterionBasePython
import itkLevelSetNodePython
import ITKOptimizersBasePython

def itkShapePriorSegmentationLevelSetImageFilterID3ID3D_New():
  return itkShapePriorSegmentationLevelSetImageFilterID3ID3D.New()


def itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_New():
  return itkShapePriorSegmentationLevelSetImageFilterIF3IF3F.New()


def itkShapePriorSegmentationLevelSetImageFilterID2ID2D_New():
  return itkShapePriorSegmentationLevelSetImageFilterID2ID2D.New()


def itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_New():
  return itkShapePriorSegmentationLevelSetImageFilterIF2IF2F.New()

class itkShapePriorSegmentationLevelSetImageFilterID2ID2D(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterID2ID2D):
    r"""Proxy of C++ itkShapePriorSegmentationLevelSetImageFilterID2ID2D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetShapeFunction)
    SetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_SetCostFunction)
    GetModifiableCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetModifiableCostFunction)
    GetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetCostFunction)
    SetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_SetOptimizer)
    GetModifiableOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetModifiableOptimizer)
    GetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetOptimizer)
    SetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_SetInitialParameters)
    GetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetInitialParameters)
    SetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_SetShapePriorScaling)
    GetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetShapePriorScaling)
    SetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_SetShapePriorSegmentationFunction)
    GetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetShapePriorSegmentationFunction)
    GetCurrentParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetCurrentParameters)
    __swig_destroy__ = _itkShapePriorSegmentationLevelSetImageFilterPython.delete_itkShapePriorSegmentationLevelSetImageFilterID2ID2D
    cast = _swig_new_static_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_cast)

    def New(*args, **kargs):
        """New() -> itkShapePriorSegmentationLevelSetImageFilterID2ID2D

        Create a new object of the class itkShapePriorSegmentationLevelSetImageFilterID2ID2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePriorSegmentationLevelSetImageFilterID2ID2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapePriorSegmentationLevelSetImageFilterID2ID2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapePriorSegmentationLevelSetImageFilterID2ID2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapePriorSegmentationLevelSetImageFilterID2ID2D in _itkShapePriorSegmentationLevelSetImageFilterPython:
_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_swigregister(itkShapePriorSegmentationLevelSetImageFilterID2ID2D)
itkShapePriorSegmentationLevelSetImageFilterID2ID2D_cast = _itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_cast

class itkShapePriorSegmentationLevelSetImageFilterID3ID3D(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterID3ID3D):
    r"""Proxy of C++ itkShapePriorSegmentationLevelSetImageFilterID3ID3D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetShapeFunction)
    SetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_SetCostFunction)
    GetModifiableCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetModifiableCostFunction)
    GetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetCostFunction)
    SetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_SetOptimizer)
    GetModifiableOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetModifiableOptimizer)
    GetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetOptimizer)
    SetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_SetInitialParameters)
    GetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetInitialParameters)
    SetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_SetShapePriorScaling)
    GetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetShapePriorScaling)
    SetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_SetShapePriorSegmentationFunction)
    GetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetShapePriorSegmentationFunction)
    GetCurrentParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetCurrentParameters)
    __swig_destroy__ = _itkShapePriorSegmentationLevelSetImageFilterPython.delete_itkShapePriorSegmentationLevelSetImageFilterID3ID3D
    cast = _swig_new_static_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_cast)

    def New(*args, **kargs):
        """New() -> itkShapePriorSegmentationLevelSetImageFilterID3ID3D

        Create a new object of the class itkShapePriorSegmentationLevelSetImageFilterID3ID3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePriorSegmentationLevelSetImageFilterID3ID3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapePriorSegmentationLevelSetImageFilterID3ID3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapePriorSegmentationLevelSetImageFilterID3ID3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapePriorSegmentationLevelSetImageFilterID3ID3D in _itkShapePriorSegmentationLevelSetImageFilterPython:
_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_swigregister(itkShapePriorSegmentationLevelSetImageFilterID3ID3D)
itkShapePriorSegmentationLevelSetImageFilterID3ID3D_cast = _itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_cast

class itkShapePriorSegmentationLevelSetImageFilterIF2IF2F(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF2IF2F):
    r"""Proxy of C++ itkShapePriorSegmentationLevelSetImageFilterIF2IF2F class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetShapeFunction)
    SetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_SetCostFunction)
    GetModifiableCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetModifiableCostFunction)
    GetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetCostFunction)
    SetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_SetOptimizer)
    GetModifiableOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetModifiableOptimizer)
    GetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetOptimizer)
    SetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_SetInitialParameters)
    GetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetInitialParameters)
    SetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_SetShapePriorScaling)
    GetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetShapePriorScaling)
    SetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_SetShapePriorSegmentationFunction)
    GetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetShapePriorSegmentationFunction)
    GetCurrentParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetCurrentParameters)
    __swig_destroy__ = _itkShapePriorSegmentationLevelSetImageFilterPython.delete_itkShapePriorSegmentationLevelSetImageFilterIF2IF2F
    cast = _swig_new_static_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_cast)

    def New(*args, **kargs):
        """New() -> itkShapePriorSegmentationLevelSetImageFilterIF2IF2F

        Create a new object of the class itkShapePriorSegmentationLevelSetImageFilterIF2IF2F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePriorSegmentationLevelSetImageFilterIF2IF2F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapePriorSegmentationLevelSetImageFilterIF2IF2F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapePriorSegmentationLevelSetImageFilterIF2IF2F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapePriorSegmentationLevelSetImageFilterIF2IF2F in _itkShapePriorSegmentationLevelSetImageFilterPython:
_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_swigregister(itkShapePriorSegmentationLevelSetImageFilterIF2IF2F)
itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_cast = _itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_cast

class itkShapePriorSegmentationLevelSetImageFilterIF3IF3F(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF3IF3F):
    r"""Proxy of C++ itkShapePriorSegmentationLevelSetImageFilterIF3IF3F class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetShapeFunction)
    SetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_SetCostFunction)
    GetModifiableCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetModifiableCostFunction)
    GetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetCostFunction)
    SetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_SetOptimizer)
    GetModifiableOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetModifiableOptimizer)
    GetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetOptimizer)
    SetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_SetInitialParameters)
    GetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetInitialParameters)
    SetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_SetShapePriorScaling)
    GetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetShapePriorScaling)
    SetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_SetShapePriorSegmentationFunction)
    GetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetShapePriorSegmentationFunction)
    GetCurrentParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetCurrentParameters)
    __swig_destroy__ = _itkShapePriorSegmentationLevelSetImageFilterPython.delete_itkShapePriorSegmentationLevelSetImageFilterIF3IF3F
    cast = _swig_new_static_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_cast)

    def New(*args, **kargs):
        """New() -> itkShapePriorSegmentationLevelSetImageFilterIF3IF3F

        Create a new object of the class itkShapePriorSegmentationLevelSetImageFilterIF3IF3F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePriorSegmentationLevelSetImageFilterIF3IF3F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapePriorSegmentationLevelSetImageFilterIF3IF3F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapePriorSegmentationLevelSetImageFilterIF3IF3F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapePriorSegmentationLevelSetImageFilterIF3IF3F in _itkShapePriorSegmentationLevelSetImageFilterPython:
_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_swigregister(itkShapePriorSegmentationLevelSetImageFilterIF3IF3F)
itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_cast = _itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def shape_prior_segmentation_level_set_image_filter(*args, **kwargs):
    """Procedural interface for ShapePriorSegmentationLevelSetImageFilter"""
    import itk
    instance = itk.ShapePriorSegmentationLevelSetImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def shape_prior_segmentation_level_set_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ShapePriorSegmentationLevelSetImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.ShapePriorSegmentationLevelSetImageFilter.values()[0]
    else:
        filter_object = itk.ShapePriorSegmentationLevelSetImageFilter

    shape_prior_segmentation_level_set_image_filter.__doc__ = filter_object.__doc__
    shape_prior_segmentation_level_set_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    shape_prior_segmentation_level_set_image_filter.__doc__ += "Available Keyword Arguments:\n"
    shape_prior_segmentation_level_set_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



