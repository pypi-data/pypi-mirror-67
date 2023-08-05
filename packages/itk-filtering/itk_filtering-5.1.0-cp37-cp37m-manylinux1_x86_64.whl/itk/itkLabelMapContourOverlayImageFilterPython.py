# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLabelMapContourOverlayImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLabelMapContourOverlayImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkLabelMapContourOverlayImageFilterPython
            return _itkLabelMapContourOverlayImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkLabelMapContourOverlayImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkLabelMapContourOverlayImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLabelMapContourOverlayImageFilterPython
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


import itkImageRegionPython
import itkIndexPython
import itkSizePython
import pyBasePython
import itkOffsetPython
import ITKCommonBasePython
import ITKLabelMapBasePython
import itkImageToImageFilterCommonPython
import itkImageSourceCommonPython
import itkImagePython
import itkPointPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkVectorPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkStatisticsLabelObjectPython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkDiffusionTensor3DPython
import itkVariableLengthVectorPython
import itkOptimizerParametersPython
import itkArrayPython
import itkTransformBasePython
import itkArray2DPython
import itkHistogramPython
import itkSamplePython
import itkImageSourcePython
import itkVectorImagePython
import itkLabelMapFilterPython

def itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_New():
  return itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.New()


def itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_New():
  return itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.New()

class itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2(itkLabelMapFilterPython.itkLabelMapFilterLM2IRGBUC2):
    """


    Apply a colormap to the contours (outlines) of each object in a label
    map and superimpose it on top of the feature image.

    The feature image is typically the image from which the labeling was
    produced. Use the SetInput function to set the LabelMap, and the
    SetFeatureImage function to set the feature image.

    Apply a colormap to a label map and put it on top of the input image.
    The set of colors is a good selection of distinct colors. The opacity
    of the label map can be defined by the user. A background label
    produce a gray pixel with the same intensity than the input one.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://hdl.handle.net/1926/584
    orhttp://www.insight-journal.org/browse/publication/176

    See:   LabelMapOverlayImageFilter, LabelOverlayImageFilter,
    LabelOverlayFunctor

    See:  LabelMapToBinaryImageFilter, LabelMapToLabelImageFilter,

    C++ includes: itkLabelMapContourOverlayImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    PLAIN = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_PLAIN
    CONTOUR = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_CONTOUR
    SLICE_CONTOUR = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SLICE_CONTOUR
    HIGH_LABEL_ON_TOP = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_HIGH_LABEL_ON_TOP
    LOW_LABEL_ON_TOP = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_LOW_LABEL_ON_TOP

    def __New_orig__() -> "itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_Pointer":
        """__New_orig__() -> itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_Pointer"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_Pointer":
        """Clone(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self) -> itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_Pointer"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_Clone(self)


    def SetFeatureImage(self, input: 'itkImageUC2') -> "void":
        """
        SetFeatureImage(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self, itkImageUC2 input)

        Set the feature
        image 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetFeatureImage(self, input)


    def GetFeatureImage(self) -> "itkImageUC2 *":
        """
        GetFeatureImage(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self) -> itkImageUC2

        Get the feature
        image 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetFeatureImage(self)


    def SetInput1(self, input: 'itkLabelMap2') -> "void":
        """
        SetInput1(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self, itkLabelMap2 input)

        Set the input image 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetInput1(self, input)


    def SetInput2(self, input: 'itkImageUC2') -> "void":
        """
        SetInput2(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self, itkImageUC2 input)

        Set the feature image 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetInput2(self, input)


    def SetOpacity(self, _arg: 'double const') -> "void":
        """
        SetOpacity(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self, double const _arg)

        Set/Get the opacity of
        the colored label image. The value must be between 0 and 1 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetOpacity(self, _arg)


    def GetOpacity(self) -> "double const &":
        """GetOpacity(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self) -> double const &"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetOpacity(self)


    def SetType(self, _arg: 'int const') -> "void":
        """
        SetType(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self, int const _arg)

        Set/Get the overlay type -
        CONTOUR is used by default. 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetType(self, _arg)


    def GetType(self) -> "int const &":
        """GetType(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self) -> int const &"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetType(self)


    def SetPriority(self, _arg: 'int const') -> "void":
        """
        SetPriority(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self, int const _arg)

        Set/Get the object
        priority - HIGH_LABEL_ON_TOP by default. 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetPriority(self, _arg)


    def GetPriority(self) -> "int const &":
        """GetPriority(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self) -> int const &"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetPriority(self)


    def SetDilationRadius(self, _arg: 'itkSize2') -> "void":
        """
        SetDilationRadius(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self, itkSize2 _arg)

        Set/Get the
        object dilation radius - 0 by default. 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetDilationRadius(self, _arg)


    def GetDilationRadius(self) -> "itkSize2 const &":
        """GetDilationRadius(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self) -> itkSize2"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetDilationRadius(self)


    def SetContourThickness(self, _arg: 'itkSize2') -> "void":
        """
        SetContourThickness(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self, itkSize2 _arg)

        Set/Get the
        contour thickness - 1 by default. 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetContourThickness(self, _arg)


    def GetContourThickness(self) -> "itkSize2 const &":
        """GetContourThickness(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self) -> itkSize2"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetContourThickness(self)


    def SetSliceDimension(self, _arg: 'int const') -> "void":
        """
        SetSliceDimension(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self, int const _arg)

        Set/Get the slice
        dimension - defaults to image dimension - 1. 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetSliceDimension(self, _arg)


    def GetSliceDimension(self) -> "int const &":
        """GetSliceDimension(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self) -> int const &"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetSliceDimension(self)


    def SetFunctor(self, functor: 'itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > > const &') -> "void":
        """
        SetFunctor(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self, itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > > const & functor)

        Set/Get the overlay
        functor - defaults to a reasonable set of colors. This can be used to
        apply a different colormap. 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetFunctor(self, functor)


    def GetFunctor(self, *args) -> "itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > > const &":
        """
        GetFunctor(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self) -> itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > >
        GetFunctor(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 self) -> itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > > const &
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetFunctor(self, *args)

    __swig_destroy__ = _itkLabelMapContourOverlayImageFilterPython.delete_itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2

    def cast(obj: 'itkLightObject') -> "itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 *":
        """cast(itkLightObject obj) -> itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2

        Create a new object of the class itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.Clone = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_Clone, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.SetFeatureImage = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetFeatureImage, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.GetFeatureImage = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetFeatureImage, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.SetInput1 = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetInput1, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.SetInput2 = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetInput2, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.SetOpacity = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetOpacity, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.GetOpacity = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetOpacity, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.SetType = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetType, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.GetType = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetType, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.SetPriority = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetPriority, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.GetPriority = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetPriority, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.SetDilationRadius = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetDilationRadius, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.GetDilationRadius = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetDilationRadius, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.SetContourThickness = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetContourThickness, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.GetContourThickness = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetContourThickness, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.SetSliceDimension = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetSliceDimension, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.GetSliceDimension = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetSliceDimension, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.SetFunctor = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetFunctor, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.GetFunctor = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetFunctor, None, itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_swigregister = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_swigregister
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_swigregister(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)

def itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2___New_orig__() -> "itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_Pointer":
    """itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2___New_orig__() -> itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_Pointer"""
    return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2___New_orig__()

def itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_cast(obj: 'itkLightObject') -> "itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 *":
    """itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_cast(itkLightObject obj) -> itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2"""
    return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_cast(obj)

class itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3(itkLabelMapFilterPython.itkLabelMapFilterLM3IRGBUC3):
    """


    Apply a colormap to the contours (outlines) of each object in a label
    map and superimpose it on top of the feature image.

    The feature image is typically the image from which the labeling was
    produced. Use the SetInput function to set the LabelMap, and the
    SetFeatureImage function to set the feature image.

    Apply a colormap to a label map and put it on top of the input image.
    The set of colors is a good selection of distinct colors. The opacity
    of the label map can be defined by the user. A background label
    produce a gray pixel with the same intensity than the input one.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://hdl.handle.net/1926/584
    orhttp://www.insight-journal.org/browse/publication/176

    See:   LabelMapOverlayImageFilter, LabelOverlayImageFilter,
    LabelOverlayFunctor

    See:  LabelMapToBinaryImageFilter, LabelMapToLabelImageFilter,

    C++ includes: itkLabelMapContourOverlayImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    PLAIN = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_PLAIN
    CONTOUR = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_CONTOUR
    SLICE_CONTOUR = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SLICE_CONTOUR
    HIGH_LABEL_ON_TOP = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_HIGH_LABEL_ON_TOP
    LOW_LABEL_ON_TOP = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_LOW_LABEL_ON_TOP

    def __New_orig__() -> "itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_Pointer":
        """__New_orig__() -> itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_Pointer"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_Pointer":
        """Clone(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self) -> itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_Pointer"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_Clone(self)


    def SetFeatureImage(self, input: 'itkImageUC3') -> "void":
        """
        SetFeatureImage(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self, itkImageUC3 input)

        Set the feature
        image 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetFeatureImage(self, input)


    def GetFeatureImage(self) -> "itkImageUC3 *":
        """
        GetFeatureImage(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self) -> itkImageUC3

        Get the feature
        image 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetFeatureImage(self)


    def SetInput1(self, input: 'itkLabelMap3') -> "void":
        """
        SetInput1(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self, itkLabelMap3 input)

        Set the input image 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetInput1(self, input)


    def SetInput2(self, input: 'itkImageUC3') -> "void":
        """
        SetInput2(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self, itkImageUC3 input)

        Set the feature image 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetInput2(self, input)


    def SetOpacity(self, _arg: 'double const') -> "void":
        """
        SetOpacity(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self, double const _arg)

        Set/Get the opacity of
        the colored label image. The value must be between 0 and 1 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetOpacity(self, _arg)


    def GetOpacity(self) -> "double const &":
        """GetOpacity(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self) -> double const &"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetOpacity(self)


    def SetType(self, _arg: 'int const') -> "void":
        """
        SetType(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self, int const _arg)

        Set/Get the overlay type -
        CONTOUR is used by default. 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetType(self, _arg)


    def GetType(self) -> "int const &":
        """GetType(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self) -> int const &"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetType(self)


    def SetPriority(self, _arg: 'int const') -> "void":
        """
        SetPriority(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self, int const _arg)

        Set/Get the object
        priority - HIGH_LABEL_ON_TOP by default. 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetPriority(self, _arg)


    def GetPriority(self) -> "int const &":
        """GetPriority(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self) -> int const &"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetPriority(self)


    def SetDilationRadius(self, _arg: 'itkSize3') -> "void":
        """
        SetDilationRadius(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self, itkSize3 _arg)

        Set/Get the
        object dilation radius - 0 by default. 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetDilationRadius(self, _arg)


    def GetDilationRadius(self) -> "itkSize3 const &":
        """GetDilationRadius(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self) -> itkSize3"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetDilationRadius(self)


    def SetContourThickness(self, _arg: 'itkSize3') -> "void":
        """
        SetContourThickness(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self, itkSize3 _arg)

        Set/Get the
        contour thickness - 1 by default. 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetContourThickness(self, _arg)


    def GetContourThickness(self) -> "itkSize3 const &":
        """GetContourThickness(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self) -> itkSize3"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetContourThickness(self)


    def SetSliceDimension(self, _arg: 'int const') -> "void":
        """
        SetSliceDimension(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self, int const _arg)

        Set/Get the slice
        dimension - defaults to image dimension - 1. 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetSliceDimension(self, _arg)


    def GetSliceDimension(self) -> "int const &":
        """GetSliceDimension(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self) -> int const &"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetSliceDimension(self)


    def SetFunctor(self, functor: 'itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > > const &') -> "void":
        """
        SetFunctor(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self, itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > > const & functor)

        Set/Get the overlay
        functor - defaults to a reasonable set of colors. This can be used to
        apply a different colormap. 
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetFunctor(self, functor)


    def GetFunctor(self, *args) -> "itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > > const &":
        """
        GetFunctor(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self) -> itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > >
        GetFunctor(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 self) -> itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > > const &
        """
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetFunctor(self, *args)

    __swig_destroy__ = _itkLabelMapContourOverlayImageFilterPython.delete_itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3

    def cast(obj: 'itkLightObject') -> "itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 *":
        """cast(itkLightObject obj) -> itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3"""
        return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3

        Create a new object of the class itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.Clone = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_Clone, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.SetFeatureImage = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetFeatureImage, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.GetFeatureImage = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetFeatureImage, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.SetInput1 = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetInput1, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.SetInput2 = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetInput2, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.SetOpacity = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetOpacity, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.GetOpacity = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetOpacity, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.SetType = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetType, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.GetType = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetType, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.SetPriority = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetPriority, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.GetPriority = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetPriority, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.SetDilationRadius = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetDilationRadius, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.GetDilationRadius = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetDilationRadius, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.SetContourThickness = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetContourThickness, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.GetContourThickness = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetContourThickness, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.SetSliceDimension = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetSliceDimension, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.GetSliceDimension = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetSliceDimension, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.SetFunctor = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetFunctor, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.GetFunctor = new_instancemethod(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetFunctor, None, itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_swigregister = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_swigregister
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_swigregister(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)

def itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3___New_orig__() -> "itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_Pointer":
    """itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3___New_orig__() -> itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_Pointer"""
    return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3___New_orig__()

def itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_cast(obj: 'itkLightObject') -> "itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 *":
    """itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_cast(itkLightObject obj) -> itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3"""
    return _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def label_map_contour_overlay_image_filter(*args, **kwargs):
    """Procedural interface for LabelMapContourOverlayImageFilter"""
    import itk
    instance = itk.LabelMapContourOverlayImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def label_map_contour_overlay_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.LabelMapContourOverlayImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.LabelMapContourOverlayImageFilter.values()[0]
    else:
        filter_object = itk.LabelMapContourOverlayImageFilter

    label_map_contour_overlay_image_filter.__doc__ = filter_object.__doc__
    label_map_contour_overlay_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    label_map_contour_overlay_image_filter.__doc__ += "Available Keyword Arguments:\n"
    label_map_contour_overlay_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



