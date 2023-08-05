# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkShapeLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkShapeLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkShapeLabelMapFilterPython
            return _itkShapeLabelMapFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkShapeLabelMapFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkShapeLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkShapeLabelMapFilterPython
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


import itkOffsetPython
import itkSizePython
import pyBasePython
import ITKCommonBasePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkImagePython
import itkIndexPython
import itkRGBAPixelPython
import itkPointPython
import itkRGBPixelPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkStatisticsLabelObjectPython
import itkHistogramPython
import itkSamplePython
import itkArrayPython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkTransformBasePython
import itkOptimizerParametersPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkInPlaceLabelMapFilterPython
import ITKLabelMapBasePython
import itkImageSourcePython
import itkVectorImagePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkLabelMapFilterPython

def itkShapeLabelMapFilterLM3_New():
  return itkShapeLabelMapFilterLM3.New()


def itkShapeLabelMapFilterLM2_New():
  return itkShapeLabelMapFilterLM2.New()

class itkShapeLabelMapFilterLM2(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    """


    The valuator class for the ShapeLabelObject.

    ShapeLabelMapFilter can be used to set the attributes values of the
    ShapeLabelObject in a LabelMap.

    ShapeLabelMapFilter takes an optional parameter, used only to optimize
    the computation time and the memory usage when the perimeter or the
    feret diameter is used: the exact copy of the input LabelMap is stored
    in an Image. It can be set with SetLabelImage(). It is cleared at the
    end of the computation, so must be reset before running Update()
    again. It is not part of the pipeline management design, to let the
    subclasses of ShapeLabelMapFilter use the pipeline design to specify
    truly required inputs.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://hdl.handle.net/1926/584
    orhttp://www.insight-journal.org/browse/publication/176

    C++ includes: itkShapeLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapeLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkShapeLabelMapFilterLM2_Pointer"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapeLabelMapFilterLM2_Pointer":
        """Clone(itkShapeLabelMapFilterLM2 self) -> itkShapeLabelMapFilterLM2_Pointer"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_Clone(self)


    def SetComputeFeretDiameter(self, _arg: 'bool const') -> "void":
        """
        SetComputeFeretDiameter(itkShapeLabelMapFilterLM2 self, bool const _arg)

        Set/Get
        whether the maximum Feret diameter should be computed or not. Default
        value is false because of the high computation time required. 
        """
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_SetComputeFeretDiameter(self, _arg)


    def GetComputeFeretDiameter(self) -> "bool const &":
        """GetComputeFeretDiameter(itkShapeLabelMapFilterLM2 self) -> bool const &"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_GetComputeFeretDiameter(self)


    def ComputeFeretDiameterOn(self) -> "void":
        """ComputeFeretDiameterOn(itkShapeLabelMapFilterLM2 self)"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_ComputeFeretDiameterOn(self)


    def ComputeFeretDiameterOff(self) -> "void":
        """ComputeFeretDiameterOff(itkShapeLabelMapFilterLM2 self)"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_ComputeFeretDiameterOff(self)


    def SetComputePerimeter(self, _arg: 'bool const') -> "void":
        """
        SetComputePerimeter(itkShapeLabelMapFilterLM2 self, bool const _arg)

        Set/Get whether
        the perimeter should be computed or not. Default value is true; 
        """
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_SetComputePerimeter(self, _arg)


    def GetComputePerimeter(self) -> "bool const &":
        """GetComputePerimeter(itkShapeLabelMapFilterLM2 self) -> bool const &"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_GetComputePerimeter(self)


    def ComputePerimeterOn(self) -> "void":
        """ComputePerimeterOn(itkShapeLabelMapFilterLM2 self)"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_ComputePerimeterOn(self)


    def ComputePerimeterOff(self) -> "void":
        """ComputePerimeterOff(itkShapeLabelMapFilterLM2 self)"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_ComputePerimeterOff(self)


    def SetComputeOrientedBoundingBox(self, _arg: 'bool const') -> "void":
        """
        SetComputeOrientedBoundingBox(itkShapeLabelMapFilterLM2 self, bool const _arg)

        Set/Get whether the oriented bounding box should be computed or not.
        Default value is false because of potential memory consumption issues
        with sparse labels. 
        """
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_SetComputeOrientedBoundingBox(self, _arg)


    def GetComputeOrientedBoundingBox(self) -> "bool const &":
        """GetComputeOrientedBoundingBox(itkShapeLabelMapFilterLM2 self) -> bool const &"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_GetComputeOrientedBoundingBox(self)


    def ComputeOrientedBoundingBoxOn(self) -> "void":
        """ComputeOrientedBoundingBoxOn(itkShapeLabelMapFilterLM2 self)"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_ComputeOrientedBoundingBoxOn(self)


    def ComputeOrientedBoundingBoxOff(self) -> "void":
        """ComputeOrientedBoundingBoxOff(itkShapeLabelMapFilterLM2 self)"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_ComputeOrientedBoundingBoxOff(self)


    def SetLabelImage(self, input: 'itkImageUL2') -> "void":
        """
        SetLabelImage(itkShapeLabelMapFilterLM2 self, itkImageUL2 input)

        Set the label image

        """
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_SetLabelImage(self, input)

    __swig_destroy__ = _itkShapeLabelMapFilterPython.delete_itkShapeLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkShapeLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkShapeLabelMapFilterLM2"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkShapeLabelMapFilterLM2

        Create a new object of the class itkShapeLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapeLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapeLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapeLabelMapFilterLM2.Clone = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_Clone, None, itkShapeLabelMapFilterLM2)
itkShapeLabelMapFilterLM2.SetComputeFeretDiameter = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_SetComputeFeretDiameter, None, itkShapeLabelMapFilterLM2)
itkShapeLabelMapFilterLM2.GetComputeFeretDiameter = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_GetComputeFeretDiameter, None, itkShapeLabelMapFilterLM2)
itkShapeLabelMapFilterLM2.ComputeFeretDiameterOn = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_ComputeFeretDiameterOn, None, itkShapeLabelMapFilterLM2)
itkShapeLabelMapFilterLM2.ComputeFeretDiameterOff = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_ComputeFeretDiameterOff, None, itkShapeLabelMapFilterLM2)
itkShapeLabelMapFilterLM2.SetComputePerimeter = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_SetComputePerimeter, None, itkShapeLabelMapFilterLM2)
itkShapeLabelMapFilterLM2.GetComputePerimeter = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_GetComputePerimeter, None, itkShapeLabelMapFilterLM2)
itkShapeLabelMapFilterLM2.ComputePerimeterOn = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_ComputePerimeterOn, None, itkShapeLabelMapFilterLM2)
itkShapeLabelMapFilterLM2.ComputePerimeterOff = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_ComputePerimeterOff, None, itkShapeLabelMapFilterLM2)
itkShapeLabelMapFilterLM2.SetComputeOrientedBoundingBox = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_SetComputeOrientedBoundingBox, None, itkShapeLabelMapFilterLM2)
itkShapeLabelMapFilterLM2.GetComputeOrientedBoundingBox = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_GetComputeOrientedBoundingBox, None, itkShapeLabelMapFilterLM2)
itkShapeLabelMapFilterLM2.ComputeOrientedBoundingBoxOn = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_ComputeOrientedBoundingBoxOn, None, itkShapeLabelMapFilterLM2)
itkShapeLabelMapFilterLM2.ComputeOrientedBoundingBoxOff = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_ComputeOrientedBoundingBoxOff, None, itkShapeLabelMapFilterLM2)
itkShapeLabelMapFilterLM2.SetLabelImage = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_SetLabelImage, None, itkShapeLabelMapFilterLM2)
itkShapeLabelMapFilterLM2_swigregister = _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_swigregister
itkShapeLabelMapFilterLM2_swigregister(itkShapeLabelMapFilterLM2)

def itkShapeLabelMapFilterLM2___New_orig__() -> "itkShapeLabelMapFilterLM2_Pointer":
    """itkShapeLabelMapFilterLM2___New_orig__() -> itkShapeLabelMapFilterLM2_Pointer"""
    return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2___New_orig__()

def itkShapeLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkShapeLabelMapFilterLM2 *":
    """itkShapeLabelMapFilterLM2_cast(itkLightObject obj) -> itkShapeLabelMapFilterLM2"""
    return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM2_cast(obj)

class itkShapeLabelMapFilterLM3(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    """


    The valuator class for the ShapeLabelObject.

    ShapeLabelMapFilter can be used to set the attributes values of the
    ShapeLabelObject in a LabelMap.

    ShapeLabelMapFilter takes an optional parameter, used only to optimize
    the computation time and the memory usage when the perimeter or the
    feret diameter is used: the exact copy of the input LabelMap is stored
    in an Image. It can be set with SetLabelImage(). It is cleared at the
    end of the computation, so must be reset before running Update()
    again. It is not part of the pipeline management design, to let the
    subclasses of ShapeLabelMapFilter use the pipeline design to specify
    truly required inputs.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://hdl.handle.net/1926/584
    orhttp://www.insight-journal.org/browse/publication/176

    C++ includes: itkShapeLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapeLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkShapeLabelMapFilterLM3_Pointer"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapeLabelMapFilterLM3_Pointer":
        """Clone(itkShapeLabelMapFilterLM3 self) -> itkShapeLabelMapFilterLM3_Pointer"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_Clone(self)


    def SetComputeFeretDiameter(self, _arg: 'bool const') -> "void":
        """
        SetComputeFeretDiameter(itkShapeLabelMapFilterLM3 self, bool const _arg)

        Set/Get
        whether the maximum Feret diameter should be computed or not. Default
        value is false because of the high computation time required. 
        """
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_SetComputeFeretDiameter(self, _arg)


    def GetComputeFeretDiameter(self) -> "bool const &":
        """GetComputeFeretDiameter(itkShapeLabelMapFilterLM3 self) -> bool const &"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_GetComputeFeretDiameter(self)


    def ComputeFeretDiameterOn(self) -> "void":
        """ComputeFeretDiameterOn(itkShapeLabelMapFilterLM3 self)"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_ComputeFeretDiameterOn(self)


    def ComputeFeretDiameterOff(self) -> "void":
        """ComputeFeretDiameterOff(itkShapeLabelMapFilterLM3 self)"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_ComputeFeretDiameterOff(self)


    def SetComputePerimeter(self, _arg: 'bool const') -> "void":
        """
        SetComputePerimeter(itkShapeLabelMapFilterLM3 self, bool const _arg)

        Set/Get whether
        the perimeter should be computed or not. Default value is true; 
        """
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_SetComputePerimeter(self, _arg)


    def GetComputePerimeter(self) -> "bool const &":
        """GetComputePerimeter(itkShapeLabelMapFilterLM3 self) -> bool const &"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_GetComputePerimeter(self)


    def ComputePerimeterOn(self) -> "void":
        """ComputePerimeterOn(itkShapeLabelMapFilterLM3 self)"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_ComputePerimeterOn(self)


    def ComputePerimeterOff(self) -> "void":
        """ComputePerimeterOff(itkShapeLabelMapFilterLM3 self)"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_ComputePerimeterOff(self)


    def SetComputeOrientedBoundingBox(self, _arg: 'bool const') -> "void":
        """
        SetComputeOrientedBoundingBox(itkShapeLabelMapFilterLM3 self, bool const _arg)

        Set/Get whether the oriented bounding box should be computed or not.
        Default value is false because of potential memory consumption issues
        with sparse labels. 
        """
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_SetComputeOrientedBoundingBox(self, _arg)


    def GetComputeOrientedBoundingBox(self) -> "bool const &":
        """GetComputeOrientedBoundingBox(itkShapeLabelMapFilterLM3 self) -> bool const &"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_GetComputeOrientedBoundingBox(self)


    def ComputeOrientedBoundingBoxOn(self) -> "void":
        """ComputeOrientedBoundingBoxOn(itkShapeLabelMapFilterLM3 self)"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_ComputeOrientedBoundingBoxOn(self)


    def ComputeOrientedBoundingBoxOff(self) -> "void":
        """ComputeOrientedBoundingBoxOff(itkShapeLabelMapFilterLM3 self)"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_ComputeOrientedBoundingBoxOff(self)


    def SetLabelImage(self, input: 'itkImageUL3') -> "void":
        """
        SetLabelImage(itkShapeLabelMapFilterLM3 self, itkImageUL3 input)

        Set the label image

        """
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_SetLabelImage(self, input)

    __swig_destroy__ = _itkShapeLabelMapFilterPython.delete_itkShapeLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkShapeLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkShapeLabelMapFilterLM3"""
        return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkShapeLabelMapFilterLM3

        Create a new object of the class itkShapeLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapeLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapeLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapeLabelMapFilterLM3.Clone = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_Clone, None, itkShapeLabelMapFilterLM3)
itkShapeLabelMapFilterLM3.SetComputeFeretDiameter = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_SetComputeFeretDiameter, None, itkShapeLabelMapFilterLM3)
itkShapeLabelMapFilterLM3.GetComputeFeretDiameter = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_GetComputeFeretDiameter, None, itkShapeLabelMapFilterLM3)
itkShapeLabelMapFilterLM3.ComputeFeretDiameterOn = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_ComputeFeretDiameterOn, None, itkShapeLabelMapFilterLM3)
itkShapeLabelMapFilterLM3.ComputeFeretDiameterOff = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_ComputeFeretDiameterOff, None, itkShapeLabelMapFilterLM3)
itkShapeLabelMapFilterLM3.SetComputePerimeter = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_SetComputePerimeter, None, itkShapeLabelMapFilterLM3)
itkShapeLabelMapFilterLM3.GetComputePerimeter = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_GetComputePerimeter, None, itkShapeLabelMapFilterLM3)
itkShapeLabelMapFilterLM3.ComputePerimeterOn = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_ComputePerimeterOn, None, itkShapeLabelMapFilterLM3)
itkShapeLabelMapFilterLM3.ComputePerimeterOff = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_ComputePerimeterOff, None, itkShapeLabelMapFilterLM3)
itkShapeLabelMapFilterLM3.SetComputeOrientedBoundingBox = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_SetComputeOrientedBoundingBox, None, itkShapeLabelMapFilterLM3)
itkShapeLabelMapFilterLM3.GetComputeOrientedBoundingBox = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_GetComputeOrientedBoundingBox, None, itkShapeLabelMapFilterLM3)
itkShapeLabelMapFilterLM3.ComputeOrientedBoundingBoxOn = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_ComputeOrientedBoundingBoxOn, None, itkShapeLabelMapFilterLM3)
itkShapeLabelMapFilterLM3.ComputeOrientedBoundingBoxOff = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_ComputeOrientedBoundingBoxOff, None, itkShapeLabelMapFilterLM3)
itkShapeLabelMapFilterLM3.SetLabelImage = new_instancemethod(_itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_SetLabelImage, None, itkShapeLabelMapFilterLM3)
itkShapeLabelMapFilterLM3_swigregister = _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_swigregister
itkShapeLabelMapFilterLM3_swigregister(itkShapeLabelMapFilterLM3)

def itkShapeLabelMapFilterLM3___New_orig__() -> "itkShapeLabelMapFilterLM3_Pointer":
    """itkShapeLabelMapFilterLM3___New_orig__() -> itkShapeLabelMapFilterLM3_Pointer"""
    return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3___New_orig__()

def itkShapeLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkShapeLabelMapFilterLM3 *":
    """itkShapeLabelMapFilterLM3_cast(itkLightObject obj) -> itkShapeLabelMapFilterLM3"""
    return _itkShapeLabelMapFilterPython.itkShapeLabelMapFilterLM3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def shape_label_map_filter(*args, **kwargs):
    """Procedural interface for ShapeLabelMapFilter"""
    import itk
    instance = itk.ShapeLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def shape_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ShapeLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.ShapeLabelMapFilter.values()[0]
    else:
        filter_object = itk.ShapeLabelMapFilter

    shape_label_map_filter.__doc__ = filter_object.__doc__
    shape_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    shape_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    shape_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



