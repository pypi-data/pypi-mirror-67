# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkHoughTransform2DLinesImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkHoughTransform2DLinesImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkHoughTransform2DLinesImageFilterPython
            return _itkHoughTransform2DLinesImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkHoughTransform2DLinesImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkHoughTransform2DLinesImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkHoughTransform2DLinesImageFilterPython
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


import ITKCommonBasePython
import pyBasePython
import itkImagePython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkRGBPixelPython
import itkPointPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkIndexPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkLineSpatialObjectPython
import itkLineSpatialObjectPointPython
import itkSpatialObjectPointPython
import itkSpatialObjectBasePython
import itkBoundingBoxPython
import itkMapContainerPython
import itkVectorContainerPython
import itkContinuousIndexPython
import itkSpatialObjectPropertyPython
import itkAffineTransformPython
import itkTransformBasePython
import itkArray2DPython
import itkDiffusionTensor3DPython
import itkArrayPython
import itkOptimizerParametersPython
import itkVariableLengthVectorPython
import itkMatrixOffsetTransformBasePython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkImageToImageFilterCommonPython

def itkHoughTransform2DLinesImageFilterDD_New():
  return itkHoughTransform2DLinesImageFilterDD.New()


def itkHoughTransform2DLinesImageFilterFF_New():
  return itkHoughTransform2DLinesImageFilterFF.New()

class itkHoughTransform2DLinesImageFilterDD(itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    """


    Performs the Hough Transform to find 2D straight lines in a 2D image.

    This filter derives from ImageToImageFilter. The input is an image,
    and all pixels above some threshold are those to be extracted. The
    output is the image of the accumulator. GetLines() returns a list of
    LinesSpatialObjects.

    Lines are parameterized in the form:

    $ R = x \\cos(\\theta) + y \\sin(\\theta) $ where $R$ is the
    perpendicular distance from the origin and $\\theta$ the angle with
    the normal.

    The output is the accumulator array: The first dimension (X)
    represents the distance R from the corner to the line.

    The second dimension (Y) represents the angle between the X axis and
    the normal to the line.

    The size of the array depends on the AngleAxisSize that could be set
    (500 by default) for the angle axis. The distance axis depends on the
    size of the diagonal of the input image.

    See:  LineSpatialObject

    C++ includes: itkHoughTransform2DLinesImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkHoughTransform2DLinesImageFilterDD_Pointer":
        """__New_orig__() -> itkHoughTransform2DLinesImageFilterDD_Pointer"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkHoughTransform2DLinesImageFilterDD_Pointer":
        """Clone(itkHoughTransform2DLinesImageFilterDD self) -> itkHoughTransform2DLinesImageFilterDD_Pointer"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_Clone(self)


    def GenerateData(self) -> "void":
        """
        GenerateData(itkHoughTransform2DLinesImageFilterDD self)

        Method for evaluating
        the implicit function over the image. 
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GenerateData(self)


    def SetThreshold(self, _arg: 'double const') -> "void":
        """
        SetThreshold(itkHoughTransform2DLinesImageFilterDD self, double const _arg)

        Set/Get the threshold
        above which the filter should consider the point as a valid point. 
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_SetThreshold(self, _arg)


    def GetThreshold(self) -> "double":
        """GetThreshold(itkHoughTransform2DLinesImageFilterDD self) -> double"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GetThreshold(self)


    def SetAngleResolution(self, _arg: 'double const') -> "void":
        """
        SetAngleResolution(itkHoughTransform2DLinesImageFilterDD self, double const _arg)

        Set/Get the
        resolution angle. The Hough space describes (in the angle direction)
        [-PI,PI[ with a constant step AngleResolution. 
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_SetAngleResolution(self, _arg)


    def GetAngleResolution(self) -> "double":
        """GetAngleResolution(itkHoughTransform2DLinesImageFilterDD self) -> double"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GetAngleResolution(self)


    def Simplify(self) -> "void":
        """
        Simplify(itkHoughTransform2DLinesImageFilterDD self)

        Simplify the accumulator.
        Performs the same iteration process as the Update() method, but finds
        the maximum along the curve and then removes the curve. 
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_Simplify(self)


    def GetModifiableSimplifyAccumulator(self) -> "itkImageD2 *":
        """GetModifiableSimplifyAccumulator(itkHoughTransform2DLinesImageFilterDD self) -> itkImageD2"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GetModifiableSimplifyAccumulator(self)


    def GetSimplifyAccumulator(self, *args) -> "itkImageD2 *":
        """
        GetSimplifyAccumulator(itkHoughTransform2DLinesImageFilterDD self) -> itkImageD2
        GetSimplifyAccumulator(itkHoughTransform2DLinesImageFilterDD self) -> itkImageD2
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GetSimplifyAccumulator(self, *args)


    def GetLines(self) -> "std::list< itkLineSpatialObject2_Pointer,std::allocator< itkLineSpatialObject2_Pointer > > &":
        """
        GetLines(itkHoughTransform2DLinesImageFilterDD self) -> listitkLineSpatialObject2_Pointer

        Get the list of lines.
        This recomputes the lines. 
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GetLines(self)


    def SetNumberOfLines(self, _arg: 'unsigned long const') -> "void":
        """
        SetNumberOfLines(itkHoughTransform2DLinesImageFilterDD self, unsigned long const _arg)

        Set/Get the number
        of lines to extract 
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_SetNumberOfLines(self, _arg)


    def GetNumberOfLines(self) -> "unsigned long":
        """GetNumberOfLines(itkHoughTransform2DLinesImageFilterDD self) -> unsigned long"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GetNumberOfLines(self)


    def SetDiscRadius(self, _arg: 'double const') -> "void":
        """
        SetDiscRadius(itkHoughTransform2DLinesImageFilterDD self, double const _arg)

        Set/Get the radius of
        the disc to remove from the accumulator for each line found. 
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_SetDiscRadius(self, _arg)


    def GetDiscRadius(self) -> "double":
        """GetDiscRadius(itkHoughTransform2DLinesImageFilterDD self) -> double"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GetDiscRadius(self)


    def SetVariance(self, _arg: 'double const') -> "void":
        """
        SetVariance(itkHoughTransform2DLinesImageFilterDD self, double const _arg)

        Set/Get the variance of
        the Gaussian blurring for the accumulator. 
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_SetVariance(self, _arg)


    def GetVariance(self) -> "double":
        """GetVariance(itkHoughTransform2DLinesImageFilterDD self) -> double"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GetVariance(self)

    IntConvertibleToOutputCheck = _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_IntConvertibleToOutputCheck
    InputGreaterThanFloatCheck = _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_InputGreaterThanFloatCheck
    OutputPlusIntCheck = _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_OutputPlusIntCheck
    __swig_destroy__ = _itkHoughTransform2DLinesImageFilterPython.delete_itkHoughTransform2DLinesImageFilterDD

    def cast(obj: 'itkLightObject') -> "itkHoughTransform2DLinesImageFilterDD *":
        """cast(itkLightObject obj) -> itkHoughTransform2DLinesImageFilterDD"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkHoughTransform2DLinesImageFilterDD

        Create a new object of the class itkHoughTransform2DLinesImageFilterDD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHoughTransform2DLinesImageFilterDD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHoughTransform2DLinesImageFilterDD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHoughTransform2DLinesImageFilterDD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkHoughTransform2DLinesImageFilterDD.Clone = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_Clone, None, itkHoughTransform2DLinesImageFilterDD)
itkHoughTransform2DLinesImageFilterDD.GenerateData = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GenerateData, None, itkHoughTransform2DLinesImageFilterDD)
itkHoughTransform2DLinesImageFilterDD.SetThreshold = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_SetThreshold, None, itkHoughTransform2DLinesImageFilterDD)
itkHoughTransform2DLinesImageFilterDD.GetThreshold = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GetThreshold, None, itkHoughTransform2DLinesImageFilterDD)
itkHoughTransform2DLinesImageFilterDD.SetAngleResolution = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_SetAngleResolution, None, itkHoughTransform2DLinesImageFilterDD)
itkHoughTransform2DLinesImageFilterDD.GetAngleResolution = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GetAngleResolution, None, itkHoughTransform2DLinesImageFilterDD)
itkHoughTransform2DLinesImageFilterDD.Simplify = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_Simplify, None, itkHoughTransform2DLinesImageFilterDD)
itkHoughTransform2DLinesImageFilterDD.GetModifiableSimplifyAccumulator = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GetModifiableSimplifyAccumulator, None, itkHoughTransform2DLinesImageFilterDD)
itkHoughTransform2DLinesImageFilterDD.GetSimplifyAccumulator = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GetSimplifyAccumulator, None, itkHoughTransform2DLinesImageFilterDD)
itkHoughTransform2DLinesImageFilterDD.GetLines = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GetLines, None, itkHoughTransform2DLinesImageFilterDD)
itkHoughTransform2DLinesImageFilterDD.SetNumberOfLines = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_SetNumberOfLines, None, itkHoughTransform2DLinesImageFilterDD)
itkHoughTransform2DLinesImageFilterDD.GetNumberOfLines = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GetNumberOfLines, None, itkHoughTransform2DLinesImageFilterDD)
itkHoughTransform2DLinesImageFilterDD.SetDiscRadius = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_SetDiscRadius, None, itkHoughTransform2DLinesImageFilterDD)
itkHoughTransform2DLinesImageFilterDD.GetDiscRadius = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GetDiscRadius, None, itkHoughTransform2DLinesImageFilterDD)
itkHoughTransform2DLinesImageFilterDD.SetVariance = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_SetVariance, None, itkHoughTransform2DLinesImageFilterDD)
itkHoughTransform2DLinesImageFilterDD.GetVariance = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_GetVariance, None, itkHoughTransform2DLinesImageFilterDD)
itkHoughTransform2DLinesImageFilterDD_swigregister = _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_swigregister
itkHoughTransform2DLinesImageFilterDD_swigregister(itkHoughTransform2DLinesImageFilterDD)

def itkHoughTransform2DLinesImageFilterDD___New_orig__() -> "itkHoughTransform2DLinesImageFilterDD_Pointer":
    """itkHoughTransform2DLinesImageFilterDD___New_orig__() -> itkHoughTransform2DLinesImageFilterDD_Pointer"""
    return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD___New_orig__()

def itkHoughTransform2DLinesImageFilterDD_cast(obj: 'itkLightObject') -> "itkHoughTransform2DLinesImageFilterDD *":
    """itkHoughTransform2DLinesImageFilterDD_cast(itkLightObject obj) -> itkHoughTransform2DLinesImageFilterDD"""
    return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterDD_cast(obj)

class itkHoughTransform2DLinesImageFilterFF(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """


    Performs the Hough Transform to find 2D straight lines in a 2D image.

    This filter derives from ImageToImageFilter. The input is an image,
    and all pixels above some threshold are those to be extracted. The
    output is the image of the accumulator. GetLines() returns a list of
    LinesSpatialObjects.

    Lines are parameterized in the form:

    $ R = x \\cos(\\theta) + y \\sin(\\theta) $ where $R$ is the
    perpendicular distance from the origin and $\\theta$ the angle with
    the normal.

    The output is the accumulator array: The first dimension (X)
    represents the distance R from the corner to the line.

    The second dimension (Y) represents the angle between the X axis and
    the normal to the line.

    The size of the array depends on the AngleAxisSize that could be set
    (500 by default) for the angle axis. The distance axis depends on the
    size of the diagonal of the input image.

    See:  LineSpatialObject

    C++ includes: itkHoughTransform2DLinesImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkHoughTransform2DLinesImageFilterFF_Pointer":
        """__New_orig__() -> itkHoughTransform2DLinesImageFilterFF_Pointer"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkHoughTransform2DLinesImageFilterFF_Pointer":
        """Clone(itkHoughTransform2DLinesImageFilterFF self) -> itkHoughTransform2DLinesImageFilterFF_Pointer"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_Clone(self)


    def GenerateData(self) -> "void":
        """
        GenerateData(itkHoughTransform2DLinesImageFilterFF self)

        Method for evaluating
        the implicit function over the image. 
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GenerateData(self)


    def SetThreshold(self, _arg: 'double const') -> "void":
        """
        SetThreshold(itkHoughTransform2DLinesImageFilterFF self, double const _arg)

        Set/Get the threshold
        above which the filter should consider the point as a valid point. 
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetThreshold(self, _arg)


    def GetThreshold(self) -> "double":
        """GetThreshold(itkHoughTransform2DLinesImageFilterFF self) -> double"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetThreshold(self)


    def SetAngleResolution(self, _arg: 'double const') -> "void":
        """
        SetAngleResolution(itkHoughTransform2DLinesImageFilterFF self, double const _arg)

        Set/Get the
        resolution angle. The Hough space describes (in the angle direction)
        [-PI,PI[ with a constant step AngleResolution. 
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetAngleResolution(self, _arg)


    def GetAngleResolution(self) -> "double":
        """GetAngleResolution(itkHoughTransform2DLinesImageFilterFF self) -> double"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetAngleResolution(self)


    def Simplify(self) -> "void":
        """
        Simplify(itkHoughTransform2DLinesImageFilterFF self)

        Simplify the accumulator.
        Performs the same iteration process as the Update() method, but finds
        the maximum along the curve and then removes the curve. 
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_Simplify(self)


    def GetModifiableSimplifyAccumulator(self) -> "itkImageF2 *":
        """GetModifiableSimplifyAccumulator(itkHoughTransform2DLinesImageFilterFF self) -> itkImageF2"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetModifiableSimplifyAccumulator(self)


    def GetSimplifyAccumulator(self, *args) -> "itkImageF2 *":
        """
        GetSimplifyAccumulator(itkHoughTransform2DLinesImageFilterFF self) -> itkImageF2
        GetSimplifyAccumulator(itkHoughTransform2DLinesImageFilterFF self) -> itkImageF2
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetSimplifyAccumulator(self, *args)


    def GetLines(self) -> "std::list< itkLineSpatialObject2_Pointer,std::allocator< itkLineSpatialObject2_Pointer > > &":
        """
        GetLines(itkHoughTransform2DLinesImageFilterFF self) -> listitkLineSpatialObject2_Pointer

        Get the list of lines.
        This recomputes the lines. 
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetLines(self)


    def SetNumberOfLines(self, _arg: 'unsigned long const') -> "void":
        """
        SetNumberOfLines(itkHoughTransform2DLinesImageFilterFF self, unsigned long const _arg)

        Set/Get the number
        of lines to extract 
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetNumberOfLines(self, _arg)


    def GetNumberOfLines(self) -> "unsigned long":
        """GetNumberOfLines(itkHoughTransform2DLinesImageFilterFF self) -> unsigned long"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetNumberOfLines(self)


    def SetDiscRadius(self, _arg: 'double const') -> "void":
        """
        SetDiscRadius(itkHoughTransform2DLinesImageFilterFF self, double const _arg)

        Set/Get the radius of
        the disc to remove from the accumulator for each line found. 
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetDiscRadius(self, _arg)


    def GetDiscRadius(self) -> "double":
        """GetDiscRadius(itkHoughTransform2DLinesImageFilterFF self) -> double"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetDiscRadius(self)


    def SetVariance(self, _arg: 'double const') -> "void":
        """
        SetVariance(itkHoughTransform2DLinesImageFilterFF self, double const _arg)

        Set/Get the variance of
        the Gaussian blurring for the accumulator. 
        """
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetVariance(self, _arg)


    def GetVariance(self) -> "double":
        """GetVariance(itkHoughTransform2DLinesImageFilterFF self) -> double"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetVariance(self)

    IntConvertibleToOutputCheck = _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_IntConvertibleToOutputCheck
    InputGreaterThanFloatCheck = _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_InputGreaterThanFloatCheck
    OutputPlusIntCheck = _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_OutputPlusIntCheck
    __swig_destroy__ = _itkHoughTransform2DLinesImageFilterPython.delete_itkHoughTransform2DLinesImageFilterFF

    def cast(obj: 'itkLightObject') -> "itkHoughTransform2DLinesImageFilterFF *":
        """cast(itkLightObject obj) -> itkHoughTransform2DLinesImageFilterFF"""
        return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkHoughTransform2DLinesImageFilterFF

        Create a new object of the class itkHoughTransform2DLinesImageFilterFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHoughTransform2DLinesImageFilterFF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHoughTransform2DLinesImageFilterFF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHoughTransform2DLinesImageFilterFF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkHoughTransform2DLinesImageFilterFF.Clone = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_Clone, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GenerateData = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GenerateData, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.SetThreshold = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetThreshold, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetThreshold = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetThreshold, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.SetAngleResolution = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetAngleResolution, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetAngleResolution = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetAngleResolution, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.Simplify = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_Simplify, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetModifiableSimplifyAccumulator = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetModifiableSimplifyAccumulator, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetSimplifyAccumulator = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetSimplifyAccumulator, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetLines = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetLines, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.SetNumberOfLines = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetNumberOfLines, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetNumberOfLines = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetNumberOfLines, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.SetDiscRadius = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetDiscRadius, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetDiscRadius = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetDiscRadius, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.SetVariance = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_SetVariance, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF.GetVariance = new_instancemethod(_itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_GetVariance, None, itkHoughTransform2DLinesImageFilterFF)
itkHoughTransform2DLinesImageFilterFF_swigregister = _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_swigregister
itkHoughTransform2DLinesImageFilterFF_swigregister(itkHoughTransform2DLinesImageFilterFF)

def itkHoughTransform2DLinesImageFilterFF___New_orig__() -> "itkHoughTransform2DLinesImageFilterFF_Pointer":
    """itkHoughTransform2DLinesImageFilterFF___New_orig__() -> itkHoughTransform2DLinesImageFilterFF_Pointer"""
    return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF___New_orig__()

def itkHoughTransform2DLinesImageFilterFF_cast(obj: 'itkLightObject') -> "itkHoughTransform2DLinesImageFilterFF *":
    """itkHoughTransform2DLinesImageFilterFF_cast(itkLightObject obj) -> itkHoughTransform2DLinesImageFilterFF"""
    return _itkHoughTransform2DLinesImageFilterPython.itkHoughTransform2DLinesImageFilterFF_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def hough_transform2_d_lines_image_filter(*args, **kwargs):
    """Procedural interface for HoughTransform2DLinesImageFilter"""
    import itk
    instance = itk.HoughTransform2DLinesImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def hough_transform2_d_lines_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.HoughTransform2DLinesImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.HoughTransform2DLinesImageFilter.values()[0]
    else:
        filter_object = itk.HoughTransform2DLinesImageFilter

    hough_transform2_d_lines_image_filter.__doc__ = filter_object.__doc__
    hough_transform2_d_lines_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    hough_transform2_d_lines_image_filter.__doc__ += "Available Keyword Arguments:\n"
    hough_transform2_d_lines_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



