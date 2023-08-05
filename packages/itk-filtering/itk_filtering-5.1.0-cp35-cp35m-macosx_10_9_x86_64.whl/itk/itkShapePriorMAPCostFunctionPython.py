# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkShapePriorMAPCostFunctionPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkShapePriorMAPCostFunctionPython', [dirname(__file__)])
        except ImportError:
            import _itkShapePriorMAPCostFunctionPython
            return _itkShapePriorMAPCostFunctionPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkShapePriorMAPCostFunctionPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkShapePriorMAPCostFunctionPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkShapePriorMAPCostFunctionPython
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


import itkFixedArrayPython
import pyBasePython
import itkOptimizerParametersPython
import itkArrayPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import ITKCommonBasePython
import itkShapePriorMAPCostFunctionBasePython
import itkImagePython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkVectorPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkShapeSignedDistanceFunctionPython
import itkSpatialFunctionPython
import itkFunctionBasePython
import itkContinuousIndexPython
import ITKFastMarchingBasePython
import itkNodePairPython
import itkFastMarchingStoppingCriterionBasePython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkLevelSetNodePython
import ITKCostFunctionsPython
import vnl_least_squares_functionPython
import vnl_cost_functionPython
import vnl_unary_functionPython
import itkCostFunctionPython
import itkArray2DPython

def itkShapePriorMAPCostFunctionID3D_New():
  return itkShapePriorMAPCostFunctionID3D.New()


def itkShapePriorMAPCostFunctionIF3F_New():
  return itkShapePriorMAPCostFunctionIF3F.New()


def itkShapePriorMAPCostFunctionID2D_New():
  return itkShapePriorMAPCostFunctionID2D.New()


def itkShapePriorMAPCostFunctionIF2F_New():
  return itkShapePriorMAPCostFunctionIF2F.New()

class itkShapePriorMAPCostFunctionID2D(itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D):
    """


    Represents the maximum aprior (MAP) cost function used
    ShapePriorSegmentationLevelSetImageFilter to estimate the shape
    parameters.

    This class follows the shape and pose parameters estimation developed
    in [1]. Note that this class returns the negative log of the MAP
    function. Using the negative function make this cost function
    compatible with generic optimizers which seeks the minimum of a cost
    function.

    This class has two template parameters, the feature image type
    representing the edge potential map and the pixel type used to
    represent the output level set in the
    ShapePriorSegmentationLevelSetImageFilter.

    See:   ShapePriorSegmentationLevelSetImageFilter REFERENCES

    [1] Leventon, M.E. et al. "Statistical Shape Influence in Geodesic
    Active Contours", CVPR 2000.

    C++ includes: itkShapePriorMAPCostFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapePriorMAPCostFunctionID2D_Pointer":
        """__New_orig__() -> itkShapePriorMAPCostFunctionID2D_Pointer"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapePriorMAPCostFunctionID2D_Pointer":
        """Clone(itkShapePriorMAPCostFunctionID2D self) -> itkShapePriorMAPCostFunctionID2D_Pointer"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_Clone(self)


    def SetShapeParameterMeans(self, _arg: 'itkArrayD') -> "void":
        """
        SetShapeParameterMeans(itkShapePriorMAPCostFunctionID2D self, itkArrayD _arg)

        Set/Get the
        array of shape parameters mean. 
        """
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_SetShapeParameterMeans(self, _arg)


    def GetShapeParameterMeans(self) -> "itkArrayD":
        """GetShapeParameterMeans(itkShapePriorMAPCostFunctionID2D self) -> itkArrayD"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_GetShapeParameterMeans(self)


    def SetShapeParameterStandardDeviations(self, _arg: 'itkArrayD') -> "void":
        """
        SetShapeParameterStandardDeviations(itkShapePriorMAPCostFunctionID2D self, itkArrayD _arg)

        Set/Get the array of shape parameters standard deviation. 
        """
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_SetShapeParameterStandardDeviations(self, _arg)


    def GetShapeParameterStandardDeviations(self) -> "itkArrayD":
        """GetShapeParameterStandardDeviations(itkShapePriorMAPCostFunctionID2D self) -> itkArrayD"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_GetShapeParameterStandardDeviations(self)


    def SetWeights(self, _arg: 'itkFixedArrayD4') -> "void":
        """SetWeights(itkShapePriorMAPCostFunctionID2D self, itkFixedArrayD4 _arg)"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_SetWeights(self, _arg)


    def GetWeights(self) -> "itkFixedArrayD4 const &":
        """GetWeights(itkShapePriorMAPCostFunctionID2D self) -> itkFixedArrayD4"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_GetWeights(self)

    __swig_destroy__ = _itkShapePriorMAPCostFunctionPython.delete_itkShapePriorMAPCostFunctionID2D

    def cast(obj: 'itkLightObject') -> "itkShapePriorMAPCostFunctionID2D *":
        """cast(itkLightObject obj) -> itkShapePriorMAPCostFunctionID2D"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkShapePriorMAPCostFunctionID2D

        Create a new object of the class itkShapePriorMAPCostFunctionID2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePriorMAPCostFunctionID2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapePriorMAPCostFunctionID2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapePriorMAPCostFunctionID2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapePriorMAPCostFunctionID2D.Clone = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_Clone, None, itkShapePriorMAPCostFunctionID2D)
itkShapePriorMAPCostFunctionID2D.SetShapeParameterMeans = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_SetShapeParameterMeans, None, itkShapePriorMAPCostFunctionID2D)
itkShapePriorMAPCostFunctionID2D.GetShapeParameterMeans = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_GetShapeParameterMeans, None, itkShapePriorMAPCostFunctionID2D)
itkShapePriorMAPCostFunctionID2D.SetShapeParameterStandardDeviations = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_SetShapeParameterStandardDeviations, None, itkShapePriorMAPCostFunctionID2D)
itkShapePriorMAPCostFunctionID2D.GetShapeParameterStandardDeviations = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_GetShapeParameterStandardDeviations, None, itkShapePriorMAPCostFunctionID2D)
itkShapePriorMAPCostFunctionID2D.SetWeights = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_SetWeights, None, itkShapePriorMAPCostFunctionID2D)
itkShapePriorMAPCostFunctionID2D.GetWeights = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_GetWeights, None, itkShapePriorMAPCostFunctionID2D)
itkShapePriorMAPCostFunctionID2D_swigregister = _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_swigregister
itkShapePriorMAPCostFunctionID2D_swigregister(itkShapePriorMAPCostFunctionID2D)

def itkShapePriorMAPCostFunctionID2D___New_orig__() -> "itkShapePriorMAPCostFunctionID2D_Pointer":
    """itkShapePriorMAPCostFunctionID2D___New_orig__() -> itkShapePriorMAPCostFunctionID2D_Pointer"""
    return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D___New_orig__()

def itkShapePriorMAPCostFunctionID2D_cast(obj: 'itkLightObject') -> "itkShapePriorMAPCostFunctionID2D *":
    """itkShapePriorMAPCostFunctionID2D_cast(itkLightObject obj) -> itkShapePriorMAPCostFunctionID2D"""
    return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID2D_cast(obj)

class itkShapePriorMAPCostFunctionID3D(itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D):
    """


    Represents the maximum aprior (MAP) cost function used
    ShapePriorSegmentationLevelSetImageFilter to estimate the shape
    parameters.

    This class follows the shape and pose parameters estimation developed
    in [1]. Note that this class returns the negative log of the MAP
    function. Using the negative function make this cost function
    compatible with generic optimizers which seeks the minimum of a cost
    function.

    This class has two template parameters, the feature image type
    representing the edge potential map and the pixel type used to
    represent the output level set in the
    ShapePriorSegmentationLevelSetImageFilter.

    See:   ShapePriorSegmentationLevelSetImageFilter REFERENCES

    [1] Leventon, M.E. et al. "Statistical Shape Influence in Geodesic
    Active Contours", CVPR 2000.

    C++ includes: itkShapePriorMAPCostFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapePriorMAPCostFunctionID3D_Pointer":
        """__New_orig__() -> itkShapePriorMAPCostFunctionID3D_Pointer"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapePriorMAPCostFunctionID3D_Pointer":
        """Clone(itkShapePriorMAPCostFunctionID3D self) -> itkShapePriorMAPCostFunctionID3D_Pointer"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_Clone(self)


    def SetShapeParameterMeans(self, _arg: 'itkArrayD') -> "void":
        """
        SetShapeParameterMeans(itkShapePriorMAPCostFunctionID3D self, itkArrayD _arg)

        Set/Get the
        array of shape parameters mean. 
        """
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_SetShapeParameterMeans(self, _arg)


    def GetShapeParameterMeans(self) -> "itkArrayD":
        """GetShapeParameterMeans(itkShapePriorMAPCostFunctionID3D self) -> itkArrayD"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_GetShapeParameterMeans(self)


    def SetShapeParameterStandardDeviations(self, _arg: 'itkArrayD') -> "void":
        """
        SetShapeParameterStandardDeviations(itkShapePriorMAPCostFunctionID3D self, itkArrayD _arg)

        Set/Get the array of shape parameters standard deviation. 
        """
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_SetShapeParameterStandardDeviations(self, _arg)


    def GetShapeParameterStandardDeviations(self) -> "itkArrayD":
        """GetShapeParameterStandardDeviations(itkShapePriorMAPCostFunctionID3D self) -> itkArrayD"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_GetShapeParameterStandardDeviations(self)


    def SetWeights(self, _arg: 'itkFixedArrayD4') -> "void":
        """SetWeights(itkShapePriorMAPCostFunctionID3D self, itkFixedArrayD4 _arg)"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_SetWeights(self, _arg)


    def GetWeights(self) -> "itkFixedArrayD4 const &":
        """GetWeights(itkShapePriorMAPCostFunctionID3D self) -> itkFixedArrayD4"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_GetWeights(self)

    __swig_destroy__ = _itkShapePriorMAPCostFunctionPython.delete_itkShapePriorMAPCostFunctionID3D

    def cast(obj: 'itkLightObject') -> "itkShapePriorMAPCostFunctionID3D *":
        """cast(itkLightObject obj) -> itkShapePriorMAPCostFunctionID3D"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkShapePriorMAPCostFunctionID3D

        Create a new object of the class itkShapePriorMAPCostFunctionID3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePriorMAPCostFunctionID3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapePriorMAPCostFunctionID3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapePriorMAPCostFunctionID3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapePriorMAPCostFunctionID3D.Clone = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_Clone, None, itkShapePriorMAPCostFunctionID3D)
itkShapePriorMAPCostFunctionID3D.SetShapeParameterMeans = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_SetShapeParameterMeans, None, itkShapePriorMAPCostFunctionID3D)
itkShapePriorMAPCostFunctionID3D.GetShapeParameterMeans = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_GetShapeParameterMeans, None, itkShapePriorMAPCostFunctionID3D)
itkShapePriorMAPCostFunctionID3D.SetShapeParameterStandardDeviations = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_SetShapeParameterStandardDeviations, None, itkShapePriorMAPCostFunctionID3D)
itkShapePriorMAPCostFunctionID3D.GetShapeParameterStandardDeviations = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_GetShapeParameterStandardDeviations, None, itkShapePriorMAPCostFunctionID3D)
itkShapePriorMAPCostFunctionID3D.SetWeights = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_SetWeights, None, itkShapePriorMAPCostFunctionID3D)
itkShapePriorMAPCostFunctionID3D.GetWeights = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_GetWeights, None, itkShapePriorMAPCostFunctionID3D)
itkShapePriorMAPCostFunctionID3D_swigregister = _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_swigregister
itkShapePriorMAPCostFunctionID3D_swigregister(itkShapePriorMAPCostFunctionID3D)

def itkShapePriorMAPCostFunctionID3D___New_orig__() -> "itkShapePriorMAPCostFunctionID3D_Pointer":
    """itkShapePriorMAPCostFunctionID3D___New_orig__() -> itkShapePriorMAPCostFunctionID3D_Pointer"""
    return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D___New_orig__()

def itkShapePriorMAPCostFunctionID3D_cast(obj: 'itkLightObject') -> "itkShapePriorMAPCostFunctionID3D *":
    """itkShapePriorMAPCostFunctionID3D_cast(itkLightObject obj) -> itkShapePriorMAPCostFunctionID3D"""
    return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionID3D_cast(obj)

class itkShapePriorMAPCostFunctionIF2F(itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F):
    """


    Represents the maximum aprior (MAP) cost function used
    ShapePriorSegmentationLevelSetImageFilter to estimate the shape
    parameters.

    This class follows the shape and pose parameters estimation developed
    in [1]. Note that this class returns the negative log of the MAP
    function. Using the negative function make this cost function
    compatible with generic optimizers which seeks the minimum of a cost
    function.

    This class has two template parameters, the feature image type
    representing the edge potential map and the pixel type used to
    represent the output level set in the
    ShapePriorSegmentationLevelSetImageFilter.

    See:   ShapePriorSegmentationLevelSetImageFilter REFERENCES

    [1] Leventon, M.E. et al. "Statistical Shape Influence in Geodesic
    Active Contours", CVPR 2000.

    C++ includes: itkShapePriorMAPCostFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapePriorMAPCostFunctionIF2F_Pointer":
        """__New_orig__() -> itkShapePriorMAPCostFunctionIF2F_Pointer"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapePriorMAPCostFunctionIF2F_Pointer":
        """Clone(itkShapePriorMAPCostFunctionIF2F self) -> itkShapePriorMAPCostFunctionIF2F_Pointer"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_Clone(self)


    def SetShapeParameterMeans(self, _arg: 'itkArrayD') -> "void":
        """
        SetShapeParameterMeans(itkShapePriorMAPCostFunctionIF2F self, itkArrayD _arg)

        Set/Get the
        array of shape parameters mean. 
        """
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_SetShapeParameterMeans(self, _arg)


    def GetShapeParameterMeans(self) -> "itkArrayD":
        """GetShapeParameterMeans(itkShapePriorMAPCostFunctionIF2F self) -> itkArrayD"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_GetShapeParameterMeans(self)


    def SetShapeParameterStandardDeviations(self, _arg: 'itkArrayD') -> "void":
        """
        SetShapeParameterStandardDeviations(itkShapePriorMAPCostFunctionIF2F self, itkArrayD _arg)

        Set/Get the array of shape parameters standard deviation. 
        """
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_SetShapeParameterStandardDeviations(self, _arg)


    def GetShapeParameterStandardDeviations(self) -> "itkArrayD":
        """GetShapeParameterStandardDeviations(itkShapePriorMAPCostFunctionIF2F self) -> itkArrayD"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_GetShapeParameterStandardDeviations(self)


    def SetWeights(self, _arg: 'itkFixedArrayD4') -> "void":
        """SetWeights(itkShapePriorMAPCostFunctionIF2F self, itkFixedArrayD4 _arg)"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_SetWeights(self, _arg)


    def GetWeights(self) -> "itkFixedArrayD4 const &":
        """GetWeights(itkShapePriorMAPCostFunctionIF2F self) -> itkFixedArrayD4"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_GetWeights(self)

    __swig_destroy__ = _itkShapePriorMAPCostFunctionPython.delete_itkShapePriorMAPCostFunctionIF2F

    def cast(obj: 'itkLightObject') -> "itkShapePriorMAPCostFunctionIF2F *":
        """cast(itkLightObject obj) -> itkShapePriorMAPCostFunctionIF2F"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkShapePriorMAPCostFunctionIF2F

        Create a new object of the class itkShapePriorMAPCostFunctionIF2F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePriorMAPCostFunctionIF2F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapePriorMAPCostFunctionIF2F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapePriorMAPCostFunctionIF2F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapePriorMAPCostFunctionIF2F.Clone = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_Clone, None, itkShapePriorMAPCostFunctionIF2F)
itkShapePriorMAPCostFunctionIF2F.SetShapeParameterMeans = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_SetShapeParameterMeans, None, itkShapePriorMAPCostFunctionIF2F)
itkShapePriorMAPCostFunctionIF2F.GetShapeParameterMeans = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_GetShapeParameterMeans, None, itkShapePriorMAPCostFunctionIF2F)
itkShapePriorMAPCostFunctionIF2F.SetShapeParameterStandardDeviations = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_SetShapeParameterStandardDeviations, None, itkShapePriorMAPCostFunctionIF2F)
itkShapePriorMAPCostFunctionIF2F.GetShapeParameterStandardDeviations = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_GetShapeParameterStandardDeviations, None, itkShapePriorMAPCostFunctionIF2F)
itkShapePriorMAPCostFunctionIF2F.SetWeights = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_SetWeights, None, itkShapePriorMAPCostFunctionIF2F)
itkShapePriorMAPCostFunctionIF2F.GetWeights = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_GetWeights, None, itkShapePriorMAPCostFunctionIF2F)
itkShapePriorMAPCostFunctionIF2F_swigregister = _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_swigregister
itkShapePriorMAPCostFunctionIF2F_swigregister(itkShapePriorMAPCostFunctionIF2F)

def itkShapePriorMAPCostFunctionIF2F___New_orig__() -> "itkShapePriorMAPCostFunctionIF2F_Pointer":
    """itkShapePriorMAPCostFunctionIF2F___New_orig__() -> itkShapePriorMAPCostFunctionIF2F_Pointer"""
    return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F___New_orig__()

def itkShapePriorMAPCostFunctionIF2F_cast(obj: 'itkLightObject') -> "itkShapePriorMAPCostFunctionIF2F *":
    """itkShapePriorMAPCostFunctionIF2F_cast(itkLightObject obj) -> itkShapePriorMAPCostFunctionIF2F"""
    return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF2F_cast(obj)

class itkShapePriorMAPCostFunctionIF3F(itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F):
    """


    Represents the maximum aprior (MAP) cost function used
    ShapePriorSegmentationLevelSetImageFilter to estimate the shape
    parameters.

    This class follows the shape and pose parameters estimation developed
    in [1]. Note that this class returns the negative log of the MAP
    function. Using the negative function make this cost function
    compatible with generic optimizers which seeks the minimum of a cost
    function.

    This class has two template parameters, the feature image type
    representing the edge potential map and the pixel type used to
    represent the output level set in the
    ShapePriorSegmentationLevelSetImageFilter.

    See:   ShapePriorSegmentationLevelSetImageFilter REFERENCES

    [1] Leventon, M.E. et al. "Statistical Shape Influence in Geodesic
    Active Contours", CVPR 2000.

    C++ includes: itkShapePriorMAPCostFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapePriorMAPCostFunctionIF3F_Pointer":
        """__New_orig__() -> itkShapePriorMAPCostFunctionIF3F_Pointer"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapePriorMAPCostFunctionIF3F_Pointer":
        """Clone(itkShapePriorMAPCostFunctionIF3F self) -> itkShapePriorMAPCostFunctionIF3F_Pointer"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_Clone(self)


    def SetShapeParameterMeans(self, _arg: 'itkArrayD') -> "void":
        """
        SetShapeParameterMeans(itkShapePriorMAPCostFunctionIF3F self, itkArrayD _arg)

        Set/Get the
        array of shape parameters mean. 
        """
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_SetShapeParameterMeans(self, _arg)


    def GetShapeParameterMeans(self) -> "itkArrayD":
        """GetShapeParameterMeans(itkShapePriorMAPCostFunctionIF3F self) -> itkArrayD"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_GetShapeParameterMeans(self)


    def SetShapeParameterStandardDeviations(self, _arg: 'itkArrayD') -> "void":
        """
        SetShapeParameterStandardDeviations(itkShapePriorMAPCostFunctionIF3F self, itkArrayD _arg)

        Set/Get the array of shape parameters standard deviation. 
        """
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_SetShapeParameterStandardDeviations(self, _arg)


    def GetShapeParameterStandardDeviations(self) -> "itkArrayD":
        """GetShapeParameterStandardDeviations(itkShapePriorMAPCostFunctionIF3F self) -> itkArrayD"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_GetShapeParameterStandardDeviations(self)


    def SetWeights(self, _arg: 'itkFixedArrayD4') -> "void":
        """SetWeights(itkShapePriorMAPCostFunctionIF3F self, itkFixedArrayD4 _arg)"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_SetWeights(self, _arg)


    def GetWeights(self) -> "itkFixedArrayD4 const &":
        """GetWeights(itkShapePriorMAPCostFunctionIF3F self) -> itkFixedArrayD4"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_GetWeights(self)

    __swig_destroy__ = _itkShapePriorMAPCostFunctionPython.delete_itkShapePriorMAPCostFunctionIF3F

    def cast(obj: 'itkLightObject') -> "itkShapePriorMAPCostFunctionIF3F *":
        """cast(itkLightObject obj) -> itkShapePriorMAPCostFunctionIF3F"""
        return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkShapePriorMAPCostFunctionIF3F

        Create a new object of the class itkShapePriorMAPCostFunctionIF3F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePriorMAPCostFunctionIF3F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapePriorMAPCostFunctionIF3F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapePriorMAPCostFunctionIF3F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapePriorMAPCostFunctionIF3F.Clone = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_Clone, None, itkShapePriorMAPCostFunctionIF3F)
itkShapePriorMAPCostFunctionIF3F.SetShapeParameterMeans = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_SetShapeParameterMeans, None, itkShapePriorMAPCostFunctionIF3F)
itkShapePriorMAPCostFunctionIF3F.GetShapeParameterMeans = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_GetShapeParameterMeans, None, itkShapePriorMAPCostFunctionIF3F)
itkShapePriorMAPCostFunctionIF3F.SetShapeParameterStandardDeviations = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_SetShapeParameterStandardDeviations, None, itkShapePriorMAPCostFunctionIF3F)
itkShapePriorMAPCostFunctionIF3F.GetShapeParameterStandardDeviations = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_GetShapeParameterStandardDeviations, None, itkShapePriorMAPCostFunctionIF3F)
itkShapePriorMAPCostFunctionIF3F.SetWeights = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_SetWeights, None, itkShapePriorMAPCostFunctionIF3F)
itkShapePriorMAPCostFunctionIF3F.GetWeights = new_instancemethod(_itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_GetWeights, None, itkShapePriorMAPCostFunctionIF3F)
itkShapePriorMAPCostFunctionIF3F_swigregister = _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_swigregister
itkShapePriorMAPCostFunctionIF3F_swigregister(itkShapePriorMAPCostFunctionIF3F)

def itkShapePriorMAPCostFunctionIF3F___New_orig__() -> "itkShapePriorMAPCostFunctionIF3F_Pointer":
    """itkShapePriorMAPCostFunctionIF3F___New_orig__() -> itkShapePriorMAPCostFunctionIF3F_Pointer"""
    return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F___New_orig__()

def itkShapePriorMAPCostFunctionIF3F_cast(obj: 'itkLightObject') -> "itkShapePriorMAPCostFunctionIF3F *":
    """itkShapePriorMAPCostFunctionIF3F_cast(itkLightObject obj) -> itkShapePriorMAPCostFunctionIF3F"""
    return _itkShapePriorMAPCostFunctionPython.itkShapePriorMAPCostFunctionIF3F_cast(obj)



