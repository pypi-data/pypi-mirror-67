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
    from . import _itkShapePriorMAPCostFunctionBasePython
else:
    import _itkShapePriorMAPCostFunctionBasePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkShapePriorMAPCostFunctionBasePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkShapePriorMAPCostFunctionBasePython.SWIG_PyStaticMethod_New

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
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkOptimizerParametersPython
import itkArrayPython
import ITKCostFunctionsPython
import vnl_least_squares_functionPython
import itkArray2DPython
import vnl_cost_functionPython
import vnl_unary_functionPython
import itkCostFunctionPython
import itkShapeSignedDistanceFunctionPython
import itkSpatialFunctionPython
import itkFunctionBasePython
import itkContinuousIndexPython
import ITKFastMarchingBasePython
import itkNodePairPython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkLevelSetNodePython
import itkFastMarchingStoppingCriterionBasePython

def itkShapePriorMAPCostFunctionBaseID3D_New():
  return itkShapePriorMAPCostFunctionBaseID3D.New()


def itkShapePriorMAPCostFunctionBaseIF3F_New():
  return itkShapePriorMAPCostFunctionBaseIF3F.New()


def itkShapePriorMAPCostFunctionBaseID2D_New():
  return itkShapePriorMAPCostFunctionBaseID2D.New()


def itkShapePriorMAPCostFunctionBaseIF2F_New():
  return itkShapePriorMAPCostFunctionBaseIF2F.New()

class itkShapePriorMAPCostFunctionBaseID2D(ITKCostFunctionsPython.itkSingleValuedCostFunction):
    r"""Proxy of C++ itkShapePriorMAPCostFunctionBaseID2D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_GetShapeFunction)
    SetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_SetActiveRegion)
    GetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_GetActiveRegion)
    SetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_SetFeatureImage)
    GetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_GetFeatureImage)
    ComputeLogInsideTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_ComputeLogInsideTerm)
    ComputeLogGradientTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_ComputeLogGradientTerm)
    ComputeLogShapePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_ComputeLogShapePriorTerm)
    ComputeLogPosePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_ComputeLogPosePriorTerm)
    Initialize = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_Initialize)
    __swig_destroy__ = _itkShapePriorMAPCostFunctionBasePython.delete_itkShapePriorMAPCostFunctionBaseID2D
    cast = _swig_new_static_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_cast)

    def New(*args, **kargs):
        """New() -> itkShapePriorMAPCostFunctionBaseID2D

        Create a new object of the class itkShapePriorMAPCostFunctionBaseID2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePriorMAPCostFunctionBaseID2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapePriorMAPCostFunctionBaseID2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapePriorMAPCostFunctionBaseID2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapePriorMAPCostFunctionBaseID2D in _itkShapePriorMAPCostFunctionBasePython:
_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_swigregister(itkShapePriorMAPCostFunctionBaseID2D)
itkShapePriorMAPCostFunctionBaseID2D_cast = _itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_cast

class itkShapePriorMAPCostFunctionBaseID3D(ITKCostFunctionsPython.itkSingleValuedCostFunction):
    r"""Proxy of C++ itkShapePriorMAPCostFunctionBaseID3D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_GetShapeFunction)
    SetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_SetActiveRegion)
    GetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_GetActiveRegion)
    SetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_SetFeatureImage)
    GetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_GetFeatureImage)
    ComputeLogInsideTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_ComputeLogInsideTerm)
    ComputeLogGradientTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_ComputeLogGradientTerm)
    ComputeLogShapePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_ComputeLogShapePriorTerm)
    ComputeLogPosePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_ComputeLogPosePriorTerm)
    Initialize = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_Initialize)
    __swig_destroy__ = _itkShapePriorMAPCostFunctionBasePython.delete_itkShapePriorMAPCostFunctionBaseID3D
    cast = _swig_new_static_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_cast)

    def New(*args, **kargs):
        """New() -> itkShapePriorMAPCostFunctionBaseID3D

        Create a new object of the class itkShapePriorMAPCostFunctionBaseID3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePriorMAPCostFunctionBaseID3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapePriorMAPCostFunctionBaseID3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapePriorMAPCostFunctionBaseID3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapePriorMAPCostFunctionBaseID3D in _itkShapePriorMAPCostFunctionBasePython:
_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_swigregister(itkShapePriorMAPCostFunctionBaseID3D)
itkShapePriorMAPCostFunctionBaseID3D_cast = _itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_cast

class itkShapePriorMAPCostFunctionBaseIF2F(ITKCostFunctionsPython.itkSingleValuedCostFunction):
    r"""Proxy of C++ itkShapePriorMAPCostFunctionBaseIF2F class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_GetShapeFunction)
    SetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_SetActiveRegion)
    GetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_GetActiveRegion)
    SetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_SetFeatureImage)
    GetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_GetFeatureImage)
    ComputeLogInsideTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_ComputeLogInsideTerm)
    ComputeLogGradientTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_ComputeLogGradientTerm)
    ComputeLogShapePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_ComputeLogShapePriorTerm)
    ComputeLogPosePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_ComputeLogPosePriorTerm)
    Initialize = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_Initialize)
    __swig_destroy__ = _itkShapePriorMAPCostFunctionBasePython.delete_itkShapePriorMAPCostFunctionBaseIF2F
    cast = _swig_new_static_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_cast)

    def New(*args, **kargs):
        """New() -> itkShapePriorMAPCostFunctionBaseIF2F

        Create a new object of the class itkShapePriorMAPCostFunctionBaseIF2F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePriorMAPCostFunctionBaseIF2F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapePriorMAPCostFunctionBaseIF2F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapePriorMAPCostFunctionBaseIF2F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapePriorMAPCostFunctionBaseIF2F in _itkShapePriorMAPCostFunctionBasePython:
_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_swigregister(itkShapePriorMAPCostFunctionBaseIF2F)
itkShapePriorMAPCostFunctionBaseIF2F_cast = _itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_cast

class itkShapePriorMAPCostFunctionBaseIF3F(ITKCostFunctionsPython.itkSingleValuedCostFunction):
    r"""Proxy of C++ itkShapePriorMAPCostFunctionBaseIF3F class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_GetShapeFunction)
    SetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_SetActiveRegion)
    GetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_GetActiveRegion)
    SetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_SetFeatureImage)
    GetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_GetFeatureImage)
    ComputeLogInsideTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_ComputeLogInsideTerm)
    ComputeLogGradientTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_ComputeLogGradientTerm)
    ComputeLogShapePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_ComputeLogShapePriorTerm)
    ComputeLogPosePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_ComputeLogPosePriorTerm)
    Initialize = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_Initialize)
    __swig_destroy__ = _itkShapePriorMAPCostFunctionBasePython.delete_itkShapePriorMAPCostFunctionBaseIF3F
    cast = _swig_new_static_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_cast)

    def New(*args, **kargs):
        """New() -> itkShapePriorMAPCostFunctionBaseIF3F

        Create a new object of the class itkShapePriorMAPCostFunctionBaseIF3F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePriorMAPCostFunctionBaseIF3F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapePriorMAPCostFunctionBaseIF3F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapePriorMAPCostFunctionBaseIF3F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapePriorMAPCostFunctionBaseIF3F in _itkShapePriorMAPCostFunctionBasePython:
_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_swigregister(itkShapePriorMAPCostFunctionBaseIF3F)
itkShapePriorMAPCostFunctionBaseIF3F_cast = _itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_cast



