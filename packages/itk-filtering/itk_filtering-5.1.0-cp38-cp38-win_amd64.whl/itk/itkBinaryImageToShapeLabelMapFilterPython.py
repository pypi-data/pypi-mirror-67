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
    from . import _itkBinaryImageToShapeLabelMapFilterPython
else:
    import _itkBinaryImageToShapeLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBinaryImageToShapeLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBinaryImageToShapeLabelMapFilterPython.SWIG_PyStaticMethod_New

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


import ITKLabelMapBasePython
import itkStatisticsLabelObjectPython
import itkAffineTransformPython
import itkVectorPython
import itkFixedArrayPython
import pyBasePython
import vnl_vector_refPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkCovariantVectorPython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkArrayPython
import itkDiffusionTensor3DPython
import ITKCommonBasePython
import itkOptimizerParametersPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkMatrixOffsetTransformBasePython
import itkHistogramPython
import itkSamplePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkShapeLabelObjectPython
import itkImageRegionPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkImagePython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageSourcePython
import itkVectorImagePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkBinaryImageToShapeLabelMapFilterIUS3LM3_New():
  return itkBinaryImageToShapeLabelMapFilterIUS3LM3.New()


def itkBinaryImageToShapeLabelMapFilterIUS2LM2_New():
  return itkBinaryImageToShapeLabelMapFilterIUS2LM2.New()


def itkBinaryImageToShapeLabelMapFilterIUC3LM3_New():
  return itkBinaryImageToShapeLabelMapFilterIUC3LM3.New()


def itkBinaryImageToShapeLabelMapFilterIUC2LM2_New():
  return itkBinaryImageToShapeLabelMapFilterIUC2LM2.New()

class itkBinaryImageToShapeLabelMapFilterIUC2LM2(ITKLabelMapBasePython.itkImageToImageFilterIUC2LM2):
    r"""Proxy of C++ itkBinaryImageToShapeLabelMapFilterIUC2LM2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_FullyConnectedOff)
    InputEqualityComparableCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_InputEqualityComparableCheck
    
    IntConvertibleToInputCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_IntConvertibleToInputCheck
    
    InputOStreamWritableCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_InputOStreamWritableCheck
    
    SetOutputBackgroundValue = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_SetOutputBackgroundValue)
    GetOutputBackgroundValue = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetOutputBackgroundValue)
    SetInputForegroundValue = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_SetInputForegroundValue)
    GetInputForegroundValue = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetInputForegroundValue)
    SetComputeFeretDiameter = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_SetComputeFeretDiameter)
    GetComputeFeretDiameter = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetComputeFeretDiameter)
    ComputeFeretDiameterOn = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_ComputeFeretDiameterOn)
    ComputeFeretDiameterOff = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_ComputeFeretDiameterOff)
    SetComputePerimeter = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_SetComputePerimeter)
    GetComputePerimeter = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetComputePerimeter)
    ComputePerimeterOn = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_ComputePerimeterOn)
    ComputePerimeterOff = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_ComputePerimeterOff)
    SetComputeOrientedBoundingBox = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_SetComputeOrientedBoundingBox)
    GetComputeOrientedBoundingBox = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_GetComputeOrientedBoundingBox)
    ComputeOrientedBoundingBoxOn = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_ComputeOrientedBoundingBoxOn)
    ComputeOrientedBoundingBoxOff = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_ComputeOrientedBoundingBoxOff)
    __swig_destroy__ = _itkBinaryImageToShapeLabelMapFilterPython.delete_itkBinaryImageToShapeLabelMapFilterIUC2LM2
    cast = _swig_new_static_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryImageToShapeLabelMapFilterIUC2LM2

        Create a new object of the class itkBinaryImageToShapeLabelMapFilterIUC2LM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryImageToShapeLabelMapFilterIUC2LM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryImageToShapeLabelMapFilterIUC2LM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryImageToShapeLabelMapFilterIUC2LM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryImageToShapeLabelMapFilterIUC2LM2 in _itkBinaryImageToShapeLabelMapFilterPython:
_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_swigregister(itkBinaryImageToShapeLabelMapFilterIUC2LM2)
itkBinaryImageToShapeLabelMapFilterIUC2LM2___New_orig__ = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2___New_orig__
itkBinaryImageToShapeLabelMapFilterIUC2LM2_cast = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC2LM2_cast

class itkBinaryImageToShapeLabelMapFilterIUC3LM3(ITKLabelMapBasePython.itkImageToImageFilterIUC3LM3):
    r"""Proxy of C++ itkBinaryImageToShapeLabelMapFilterIUC3LM3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_FullyConnectedOff)
    InputEqualityComparableCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_InputEqualityComparableCheck
    
    IntConvertibleToInputCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_IntConvertibleToInputCheck
    
    InputOStreamWritableCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_InputOStreamWritableCheck
    
    SetOutputBackgroundValue = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_SetOutputBackgroundValue)
    GetOutputBackgroundValue = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetOutputBackgroundValue)
    SetInputForegroundValue = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_SetInputForegroundValue)
    GetInputForegroundValue = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetInputForegroundValue)
    SetComputeFeretDiameter = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_SetComputeFeretDiameter)
    GetComputeFeretDiameter = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetComputeFeretDiameter)
    ComputeFeretDiameterOn = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_ComputeFeretDiameterOn)
    ComputeFeretDiameterOff = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_ComputeFeretDiameterOff)
    SetComputePerimeter = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_SetComputePerimeter)
    GetComputePerimeter = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetComputePerimeter)
    ComputePerimeterOn = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_ComputePerimeterOn)
    ComputePerimeterOff = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_ComputePerimeterOff)
    SetComputeOrientedBoundingBox = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_SetComputeOrientedBoundingBox)
    GetComputeOrientedBoundingBox = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_GetComputeOrientedBoundingBox)
    ComputeOrientedBoundingBoxOn = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_ComputeOrientedBoundingBoxOn)
    ComputeOrientedBoundingBoxOff = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_ComputeOrientedBoundingBoxOff)
    __swig_destroy__ = _itkBinaryImageToShapeLabelMapFilterPython.delete_itkBinaryImageToShapeLabelMapFilterIUC3LM3
    cast = _swig_new_static_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryImageToShapeLabelMapFilterIUC3LM3

        Create a new object of the class itkBinaryImageToShapeLabelMapFilterIUC3LM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryImageToShapeLabelMapFilterIUC3LM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryImageToShapeLabelMapFilterIUC3LM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryImageToShapeLabelMapFilterIUC3LM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryImageToShapeLabelMapFilterIUC3LM3 in _itkBinaryImageToShapeLabelMapFilterPython:
_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_swigregister(itkBinaryImageToShapeLabelMapFilterIUC3LM3)
itkBinaryImageToShapeLabelMapFilterIUC3LM3___New_orig__ = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3___New_orig__
itkBinaryImageToShapeLabelMapFilterIUC3LM3_cast = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUC3LM3_cast

class itkBinaryImageToShapeLabelMapFilterIUS2LM2(ITKLabelMapBasePython.itkImageToImageFilterIUS2LM2):
    r"""Proxy of C++ itkBinaryImageToShapeLabelMapFilterIUS2LM2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_FullyConnectedOff)
    InputEqualityComparableCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_InputEqualityComparableCheck
    
    IntConvertibleToInputCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_IntConvertibleToInputCheck
    
    InputOStreamWritableCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_InputOStreamWritableCheck
    
    SetOutputBackgroundValue = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_SetOutputBackgroundValue)
    GetOutputBackgroundValue = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_GetOutputBackgroundValue)
    SetInputForegroundValue = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_SetInputForegroundValue)
    GetInputForegroundValue = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_GetInputForegroundValue)
    SetComputeFeretDiameter = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_SetComputeFeretDiameter)
    GetComputeFeretDiameter = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_GetComputeFeretDiameter)
    ComputeFeretDiameterOn = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_ComputeFeretDiameterOn)
    ComputeFeretDiameterOff = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_ComputeFeretDiameterOff)
    SetComputePerimeter = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_SetComputePerimeter)
    GetComputePerimeter = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_GetComputePerimeter)
    ComputePerimeterOn = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_ComputePerimeterOn)
    ComputePerimeterOff = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_ComputePerimeterOff)
    SetComputeOrientedBoundingBox = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_SetComputeOrientedBoundingBox)
    GetComputeOrientedBoundingBox = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_GetComputeOrientedBoundingBox)
    ComputeOrientedBoundingBoxOn = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_ComputeOrientedBoundingBoxOn)
    ComputeOrientedBoundingBoxOff = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_ComputeOrientedBoundingBoxOff)
    __swig_destroy__ = _itkBinaryImageToShapeLabelMapFilterPython.delete_itkBinaryImageToShapeLabelMapFilterIUS2LM2
    cast = _swig_new_static_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryImageToShapeLabelMapFilterIUS2LM2

        Create a new object of the class itkBinaryImageToShapeLabelMapFilterIUS2LM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryImageToShapeLabelMapFilterIUS2LM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryImageToShapeLabelMapFilterIUS2LM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryImageToShapeLabelMapFilterIUS2LM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryImageToShapeLabelMapFilterIUS2LM2 in _itkBinaryImageToShapeLabelMapFilterPython:
_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_swigregister(itkBinaryImageToShapeLabelMapFilterIUS2LM2)
itkBinaryImageToShapeLabelMapFilterIUS2LM2___New_orig__ = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2___New_orig__
itkBinaryImageToShapeLabelMapFilterIUS2LM2_cast = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS2LM2_cast

class itkBinaryImageToShapeLabelMapFilterIUS3LM3(ITKLabelMapBasePython.itkImageToImageFilterIUS3LM3):
    r"""Proxy of C++ itkBinaryImageToShapeLabelMapFilterIUS3LM3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_Clone)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_FullyConnectedOff)
    InputEqualityComparableCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_InputEqualityComparableCheck
    
    IntConvertibleToInputCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_IntConvertibleToInputCheck
    
    InputOStreamWritableCheck = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_InputOStreamWritableCheck
    
    SetOutputBackgroundValue = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_SetOutputBackgroundValue)
    GetOutputBackgroundValue = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_GetOutputBackgroundValue)
    SetInputForegroundValue = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_SetInputForegroundValue)
    GetInputForegroundValue = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_GetInputForegroundValue)
    SetComputeFeretDiameter = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_SetComputeFeretDiameter)
    GetComputeFeretDiameter = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_GetComputeFeretDiameter)
    ComputeFeretDiameterOn = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_ComputeFeretDiameterOn)
    ComputeFeretDiameterOff = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_ComputeFeretDiameterOff)
    SetComputePerimeter = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_SetComputePerimeter)
    GetComputePerimeter = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_GetComputePerimeter)
    ComputePerimeterOn = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_ComputePerimeterOn)
    ComputePerimeterOff = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_ComputePerimeterOff)
    SetComputeOrientedBoundingBox = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_SetComputeOrientedBoundingBox)
    GetComputeOrientedBoundingBox = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_GetComputeOrientedBoundingBox)
    ComputeOrientedBoundingBoxOn = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_ComputeOrientedBoundingBoxOn)
    ComputeOrientedBoundingBoxOff = _swig_new_instance_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_ComputeOrientedBoundingBoxOff)
    __swig_destroy__ = _itkBinaryImageToShapeLabelMapFilterPython.delete_itkBinaryImageToShapeLabelMapFilterIUS3LM3
    cast = _swig_new_static_method(_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryImageToShapeLabelMapFilterIUS3LM3

        Create a new object of the class itkBinaryImageToShapeLabelMapFilterIUS3LM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryImageToShapeLabelMapFilterIUS3LM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryImageToShapeLabelMapFilterIUS3LM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryImageToShapeLabelMapFilterIUS3LM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryImageToShapeLabelMapFilterIUS3LM3 in _itkBinaryImageToShapeLabelMapFilterPython:
_itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_swigregister(itkBinaryImageToShapeLabelMapFilterIUS3LM3)
itkBinaryImageToShapeLabelMapFilterIUS3LM3___New_orig__ = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3___New_orig__
itkBinaryImageToShapeLabelMapFilterIUS3LM3_cast = _itkBinaryImageToShapeLabelMapFilterPython.itkBinaryImageToShapeLabelMapFilterIUS3LM3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def binary_image_to_shape_label_map_filter(*args, **kwargs):
    """Procedural interface for BinaryImageToShapeLabelMapFilter"""
    import itk
    instance = itk.BinaryImageToShapeLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def binary_image_to_shape_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.BinaryImageToShapeLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.BinaryImageToShapeLabelMapFilter.values()[0]
    else:
        filter_object = itk.BinaryImageToShapeLabelMapFilter

    binary_image_to_shape_label_map_filter.__doc__ = filter_object.__doc__
    binary_image_to_shape_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    binary_image_to_shape_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    binary_image_to_shape_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



