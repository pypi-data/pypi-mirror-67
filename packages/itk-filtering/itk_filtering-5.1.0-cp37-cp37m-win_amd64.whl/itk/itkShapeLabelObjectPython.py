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
    from . import _itkShapeLabelObjectPython
else:
    import _itkShapeLabelObjectPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkShapeLabelObjectPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkShapeLabelObjectPython.SWIG_PyStaticMethod_New

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


import itkPointPython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import pyBasePython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkImageRegionPython
import ITKCommonBasePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkArray2DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkTransformBasePython

def itkShapeLabelObjectUL3_New():
  return itkShapeLabelObjectUL3.New()


def itkShapeLabelObjectUL2_New():
  return itkShapeLabelObjectUL2.New()

class itkFixedArrayPD24(object):
    r"""Proxy of C++ itkFixedArrayPD24 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkShapeLabelObjectPython.delete_itkFixedArrayPD24

    def __init__(self, *args):
        r"""
        __init__(itkFixedArrayPD24 self) -> itkFixedArrayPD24
        __init__(itkFixedArrayPD24 self, itkFixedArrayPD24 arg0) -> itkFixedArrayPD24
        __init__(itkFixedArrayPD24 self, itkPointD2 r) -> itkFixedArrayPD24
        __init__(itkFixedArrayPD24 self, itkPointD2 arg0) -> itkFixedArrayPD24
        __init__(itkFixedArrayPD24 self, std::array< itkPointD2,4 > const & stdArray) -> itkFixedArrayPD24
        """
        _itkShapeLabelObjectPython.itkFixedArrayPD24_swiginit(self, _itkShapeLabelObjectPython.new_itkFixedArrayPD24(*args))
    __eq__ = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD24___eq__)
    __ne__ = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD24___ne__)
    SetElement = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD24_SetElement)
    GetElement = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD24_GetElement)
    GetDataPointer = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD24_GetDataPointer)
    cbegin = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD24_cbegin)
    begin = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD24_begin)
    cend = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD24_cend)
    end = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD24_end)
    crbegin = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD24_crbegin)
    rbegin = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD24_rbegin)
    crend = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD24_crend)
    rend = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD24_rend)
    Size = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD24_Size)
    Fill = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD24_Fill)
    swap = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD24_swap)
    Filled = _swig_new_static_method(_itkShapeLabelObjectPython.itkFixedArrayPD24_Filled)

# Register itkFixedArrayPD24 in _itkShapeLabelObjectPython:
_itkShapeLabelObjectPython.itkFixedArrayPD24_swigregister(itkFixedArrayPD24)
itkFixedArrayPD24_Filled = _itkShapeLabelObjectPython.itkFixedArrayPD24_Filled

class itkFixedArrayPD38(object):
    r"""Proxy of C++ itkFixedArrayPD38 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkShapeLabelObjectPython.delete_itkFixedArrayPD38

    def __init__(self, *args):
        r"""
        __init__(itkFixedArrayPD38 self) -> itkFixedArrayPD38
        __init__(itkFixedArrayPD38 self, itkFixedArrayPD38 arg0) -> itkFixedArrayPD38
        __init__(itkFixedArrayPD38 self, itkPointD3 r) -> itkFixedArrayPD38
        __init__(itkFixedArrayPD38 self, itkPointD3 arg0) -> itkFixedArrayPD38
        __init__(itkFixedArrayPD38 self, std::array< itkPointD3,8 > const & stdArray) -> itkFixedArrayPD38
        """
        _itkShapeLabelObjectPython.itkFixedArrayPD38_swiginit(self, _itkShapeLabelObjectPython.new_itkFixedArrayPD38(*args))
    __eq__ = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD38___eq__)
    __ne__ = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD38___ne__)
    SetElement = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD38_SetElement)
    GetElement = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD38_GetElement)
    GetDataPointer = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD38_GetDataPointer)
    cbegin = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD38_cbegin)
    begin = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD38_begin)
    cend = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD38_cend)
    end = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD38_end)
    crbegin = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD38_crbegin)
    rbegin = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD38_rbegin)
    crend = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD38_crend)
    rend = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD38_rend)
    Size = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD38_Size)
    Fill = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD38_Fill)
    swap = _swig_new_instance_method(_itkShapeLabelObjectPython.itkFixedArrayPD38_swap)
    Filled = _swig_new_static_method(_itkShapeLabelObjectPython.itkFixedArrayPD38_Filled)

# Register itkFixedArrayPD38 in _itkShapeLabelObjectPython:
_itkShapeLabelObjectPython.itkFixedArrayPD38_swigregister(itkFixedArrayPD38)
itkFixedArrayPD38_Filled = _itkShapeLabelObjectPython.itkFixedArrayPD38_Filled

class itkShapeLabelObjectUL2(itkLabelObjectPython.itkLabelObjectUL2):
    r"""Proxy of C++ itkShapeLabelObjectUL2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2___New_orig__)
    Clone = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_Clone)
    GetAttributeFromName = _swig_new_static_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetAttributeFromName)
    GetNameFromAttribute = _swig_new_static_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetNameFromAttribute)
    GetBoundingBox = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetBoundingBox)
    SetBoundingBox = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetBoundingBox)
    GetPhysicalSize = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetPhysicalSize)
    SetPhysicalSize = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetPhysicalSize)
    GetNumberOfPixels = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetNumberOfPixels)
    SetNumberOfPixels = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetNumberOfPixels)
    GetCentroid = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetCentroid)
    SetCentroid = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetCentroid)
    GetNumberOfPixelsOnBorder = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetNumberOfPixelsOnBorder)
    SetNumberOfPixelsOnBorder = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetNumberOfPixelsOnBorder)
    GetPerimeterOnBorder = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetPerimeterOnBorder)
    SetPerimeterOnBorder = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetPerimeterOnBorder)
    GetFeretDiameter = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetFeretDiameter)
    SetFeretDiameter = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetFeretDiameter)
    GetPrincipalMoments = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetPrincipalMoments)
    SetPrincipalMoments = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetPrincipalMoments)
    GetPrincipalAxes = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetPrincipalAxes)
    SetPrincipalAxes = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetPrincipalAxes)
    GetElongation = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetElongation)
    SetElongation = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetElongation)
    GetPerimeter = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetPerimeter)
    SetPerimeter = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetPerimeter)
    GetRoundness = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetRoundness)
    SetRoundness = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetRoundness)
    GetEquivalentSphericalRadius = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetEquivalentSphericalRadius)
    SetEquivalentSphericalRadius = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetEquivalentSphericalRadius)
    GetEquivalentSphericalPerimeter = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetEquivalentSphericalPerimeter)
    SetEquivalentSphericalPerimeter = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetEquivalentSphericalPerimeter)
    GetEquivalentEllipsoidDiameter = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetEquivalentEllipsoidDiameter)
    SetEquivalentEllipsoidDiameter = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetEquivalentEllipsoidDiameter)
    GetFlatness = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetFlatness)
    SetFlatness = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetFlatness)
    GetPerimeterOnBorderRatio = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetPerimeterOnBorderRatio)
    SetPerimeterOnBorderRatio = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetPerimeterOnBorderRatio)
    GetOrientedBoundingBoxOrigin = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetOrientedBoundingBoxOrigin)
    SetOrientedBoundingBoxOrigin = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetOrientedBoundingBoxOrigin)
    GetOrientedBoundingBoxSize = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetOrientedBoundingBoxSize)
    SetOrientedBoundingBoxSize = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_SetOrientedBoundingBoxSize)
    GetRegion = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetRegion)
    GetOrientedBoundingBoxDirection = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetOrientedBoundingBoxDirection)
    GetOrientedBoundingBoxVertices = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetOrientedBoundingBoxVertices)
    GetPrincipalAxesToPhysicalAxesTransform = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetPrincipalAxesToPhysicalAxesTransform)
    GetPhysicalAxesToPrincipalAxesTransform = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetPhysicalAxesToPrincipalAxesTransform)
    __swig_destroy__ = _itkShapeLabelObjectPython.delete_itkShapeLabelObjectUL2
    cast = _swig_new_static_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_cast)

    def New(*args, **kargs):
        """New() -> itkShapeLabelObjectUL2

        Create a new object of the class itkShapeLabelObjectUL2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeLabelObjectUL2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapeLabelObjectUL2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapeLabelObjectUL2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapeLabelObjectUL2 in _itkShapeLabelObjectPython:
_itkShapeLabelObjectPython.itkShapeLabelObjectUL2_swigregister(itkShapeLabelObjectUL2)
itkShapeLabelObjectUL2___New_orig__ = _itkShapeLabelObjectPython.itkShapeLabelObjectUL2___New_orig__
itkShapeLabelObjectUL2_GetAttributeFromName = _itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetAttributeFromName
itkShapeLabelObjectUL2_GetNameFromAttribute = _itkShapeLabelObjectPython.itkShapeLabelObjectUL2_GetNameFromAttribute
itkShapeLabelObjectUL2_cast = _itkShapeLabelObjectPython.itkShapeLabelObjectUL2_cast

class itkShapeLabelObjectUL3(itkLabelObjectPython.itkLabelObjectUL3):
    r"""Proxy of C++ itkShapeLabelObjectUL3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3___New_orig__)
    Clone = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_Clone)
    GetAttributeFromName = _swig_new_static_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetAttributeFromName)
    GetNameFromAttribute = _swig_new_static_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetNameFromAttribute)
    GetBoundingBox = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetBoundingBox)
    SetBoundingBox = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetBoundingBox)
    GetPhysicalSize = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetPhysicalSize)
    SetPhysicalSize = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetPhysicalSize)
    GetNumberOfPixels = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetNumberOfPixels)
    SetNumberOfPixels = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetNumberOfPixels)
    GetCentroid = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetCentroid)
    SetCentroid = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetCentroid)
    GetNumberOfPixelsOnBorder = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetNumberOfPixelsOnBorder)
    SetNumberOfPixelsOnBorder = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetNumberOfPixelsOnBorder)
    GetPerimeterOnBorder = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetPerimeterOnBorder)
    SetPerimeterOnBorder = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetPerimeterOnBorder)
    GetFeretDiameter = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetFeretDiameter)
    SetFeretDiameter = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetFeretDiameter)
    GetPrincipalMoments = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetPrincipalMoments)
    SetPrincipalMoments = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetPrincipalMoments)
    GetPrincipalAxes = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetPrincipalAxes)
    SetPrincipalAxes = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetPrincipalAxes)
    GetElongation = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetElongation)
    SetElongation = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetElongation)
    GetPerimeter = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetPerimeter)
    SetPerimeter = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetPerimeter)
    GetRoundness = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetRoundness)
    SetRoundness = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetRoundness)
    GetEquivalentSphericalRadius = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetEquivalentSphericalRadius)
    SetEquivalentSphericalRadius = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetEquivalentSphericalRadius)
    GetEquivalentSphericalPerimeter = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetEquivalentSphericalPerimeter)
    SetEquivalentSphericalPerimeter = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetEquivalentSphericalPerimeter)
    GetEquivalentEllipsoidDiameter = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetEquivalentEllipsoidDiameter)
    SetEquivalentEllipsoidDiameter = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetEquivalentEllipsoidDiameter)
    GetFlatness = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetFlatness)
    SetFlatness = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetFlatness)
    GetPerimeterOnBorderRatio = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetPerimeterOnBorderRatio)
    SetPerimeterOnBorderRatio = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetPerimeterOnBorderRatio)
    GetOrientedBoundingBoxOrigin = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetOrientedBoundingBoxOrigin)
    SetOrientedBoundingBoxOrigin = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetOrientedBoundingBoxOrigin)
    GetOrientedBoundingBoxSize = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetOrientedBoundingBoxSize)
    SetOrientedBoundingBoxSize = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_SetOrientedBoundingBoxSize)
    GetRegion = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetRegion)
    GetOrientedBoundingBoxDirection = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetOrientedBoundingBoxDirection)
    GetOrientedBoundingBoxVertices = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetOrientedBoundingBoxVertices)
    GetPrincipalAxesToPhysicalAxesTransform = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetPrincipalAxesToPhysicalAxesTransform)
    GetPhysicalAxesToPrincipalAxesTransform = _swig_new_instance_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetPhysicalAxesToPrincipalAxesTransform)
    __swig_destroy__ = _itkShapeLabelObjectPython.delete_itkShapeLabelObjectUL3
    cast = _swig_new_static_method(_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_cast)

    def New(*args, **kargs):
        """New() -> itkShapeLabelObjectUL3

        Create a new object of the class itkShapeLabelObjectUL3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeLabelObjectUL3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapeLabelObjectUL3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapeLabelObjectUL3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapeLabelObjectUL3 in _itkShapeLabelObjectPython:
_itkShapeLabelObjectPython.itkShapeLabelObjectUL3_swigregister(itkShapeLabelObjectUL3)
itkShapeLabelObjectUL3___New_orig__ = _itkShapeLabelObjectPython.itkShapeLabelObjectUL3___New_orig__
itkShapeLabelObjectUL3_GetAttributeFromName = _itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetAttributeFromName
itkShapeLabelObjectUL3_GetNameFromAttribute = _itkShapeLabelObjectPython.itkShapeLabelObjectUL3_GetNameFromAttribute
itkShapeLabelObjectUL3_cast = _itkShapeLabelObjectPython.itkShapeLabelObjectUL3_cast



