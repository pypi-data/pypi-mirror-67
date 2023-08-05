# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLabelMapOverlayImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLabelMapOverlayImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkLabelMapOverlayImageFilterPython
            return _itkLabelMapOverlayImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkLabelMapOverlayImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkLabelMapOverlayImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLabelMapOverlayImageFilterPython
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
import itkSizePython
import pyBasePython
import itkIndexPython
import itkOffsetPython
import ITKCommonBasePython
import itkLabelMapFilterPython
import ITKLabelMapBasePython
import itkImageToImageFilterCommonPython
import itkImageSourceCommonPython
import itkImagePython
import itkRGBPixelPython
import itkFixedArrayPython
import stdcomplexPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_vectorPython
import vnl_matrixPython
import itkPointPython
import vnl_vector_refPython
import itkVectorPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBAPixelPython
import itkStatisticsLabelObjectPython
import itkAffineTransformPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkVariableLengthVectorPython
import itkArrayPython
import itkArray2DPython
import itkOptimizerParametersPython
import itkMatrixOffsetTransformBasePython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkHistogramPython
import itkSamplePython
import itkImageSourcePython
import itkVectorImagePython

def itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_New():
  return itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3.New()


def itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_New():
  return itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2.New()

class itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2(itkLabelMapFilterPython.itkLabelMapFilterLM2IRGBUC2):
    """


    Apply a colormap to a label map and superimpose it on an image.

    Apply a colormap to a label map and put it on top of the feature
    image. The feature image is typically the image from which the
    labeling was produced. Use the SetInput function to set the LabelMap,
    and the SetFeatureImage function to set the feature image.

    The set of colors is a good selection of distinct colors. The opacity
    of the label map can be defined by the user. A background label
    produce a gray pixel with the same intensity than the input one.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://hdl.handle.net/1926/584
    orhttp://www.insight-journal.org/browse/publication/176

    See:   LabelOverlayImageFilter, LabelOverlayFunctor

    See:   LabelMapToRGBImageFilter, LabelMapToBinaryImageFilter,
    LabelMapToLabelImageFilter

    C++ includes: itkLabelMapOverlayImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_Pointer":
        """__New_orig__() -> itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_Pointer"""
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_Pointer":
        """Clone(itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2 self) -> itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_Pointer"""
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_Clone(self)


    def SetFeatureImage(self, input: 'itkImageUC2') -> "void":
        """
        SetFeatureImage(itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2 self, itkImageUC2 input)

        Set the feature
        image 
        """
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_SetFeatureImage(self, input)


    def GetFeatureImage(self) -> "itkImageUC2 const *":
        """
        GetFeatureImage(itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2 self) -> itkImageUC2

        Get the feature
        image 
        """
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_GetFeatureImage(self)


    def SetInput1(self, input: 'itkLabelMap2') -> "void":
        """
        SetInput1(itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2 self, itkLabelMap2 input)

        Set the input image 
        """
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_SetInput1(self, input)


    def SetInput2(self, input: 'itkImageUC2') -> "void":
        """
        SetInput2(itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2 self, itkImageUC2 input)

        Set the feature image 
        """
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_SetInput2(self, input)


    def SetOpacity(self, _arg: 'double const') -> "void":
        """
        SetOpacity(itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2 self, double const _arg)

        Set/Get the opacity of
        the colored label image. The value must be between 0 and 1 
        """
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_SetOpacity(self, _arg)


    def GetOpacity(self) -> "double const &":
        """GetOpacity(itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2 self) -> double const &"""
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_GetOpacity(self)


    def SetFunctor(self, functor: 'itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > > const &') -> "void":
        """
        SetFunctor(itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2 self, itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > > const & functor)

        Set/Get the overlay
        functor - defaults to a reasonable set of colors. This can be used to
        apply a different colormap. 
        """
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_SetFunctor(self, functor)


    def GetFunctor(self, *args) -> "itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > > const &":
        """
        GetFunctor(itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2 self) -> itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > >
        GetFunctor(itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2 self) -> itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > > const &
        """
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_GetFunctor(self, *args)

    __swig_destroy__ = _itkLabelMapOverlayImageFilterPython.delete_itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2

    def cast(obj: 'itkLightObject') -> "itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2 *":
        """cast(itkLightObject obj) -> itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2"""
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2

        Create a new object of the class itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2.Clone = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_Clone, None, itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2.SetFeatureImage = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_SetFeatureImage, None, itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2.GetFeatureImage = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_GetFeatureImage, None, itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2.SetInput1 = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_SetInput1, None, itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2.SetInput2 = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_SetInput2, None, itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2.SetOpacity = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_SetOpacity, None, itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2.GetOpacity = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_GetOpacity, None, itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2.SetFunctor = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_SetFunctor, None, itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2.GetFunctor = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_GetFunctor, None, itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_swigregister = _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_swigregister
itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_swigregister(itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2)

def itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2___New_orig__() -> "itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_Pointer":
    """itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2___New_orig__() -> itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_Pointer"""
    return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2___New_orig__()

def itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_cast(obj: 'itkLightObject') -> "itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2 *":
    """itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_cast(itkLightObject obj) -> itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2"""
    return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2_cast(obj)

class itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3(itkLabelMapFilterPython.itkLabelMapFilterLM3IRGBUC3):
    """


    Apply a colormap to a label map and superimpose it on an image.

    Apply a colormap to a label map and put it on top of the feature
    image. The feature image is typically the image from which the
    labeling was produced. Use the SetInput function to set the LabelMap,
    and the SetFeatureImage function to set the feature image.

    The set of colors is a good selection of distinct colors. The opacity
    of the label map can be defined by the user. A background label
    produce a gray pixel with the same intensity than the input one.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://hdl.handle.net/1926/584
    orhttp://www.insight-journal.org/browse/publication/176

    See:   LabelOverlayImageFilter, LabelOverlayFunctor

    See:   LabelMapToRGBImageFilter, LabelMapToBinaryImageFilter,
    LabelMapToLabelImageFilter

    C++ includes: itkLabelMapOverlayImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_Pointer":
        """__New_orig__() -> itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_Pointer"""
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_Pointer":
        """Clone(itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3 self) -> itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_Pointer"""
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_Clone(self)


    def SetFeatureImage(self, input: 'itkImageUC3') -> "void":
        """
        SetFeatureImage(itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3 self, itkImageUC3 input)

        Set the feature
        image 
        """
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_SetFeatureImage(self, input)


    def GetFeatureImage(self) -> "itkImageUC3 const *":
        """
        GetFeatureImage(itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3 self) -> itkImageUC3

        Get the feature
        image 
        """
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_GetFeatureImage(self)


    def SetInput1(self, input: 'itkLabelMap3') -> "void":
        """
        SetInput1(itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3 self, itkLabelMap3 input)

        Set the input image 
        """
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_SetInput1(self, input)


    def SetInput2(self, input: 'itkImageUC3') -> "void":
        """
        SetInput2(itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3 self, itkImageUC3 input)

        Set the feature image 
        """
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_SetInput2(self, input)


    def SetOpacity(self, _arg: 'double const') -> "void":
        """
        SetOpacity(itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3 self, double const _arg)

        Set/Get the opacity of
        the colored label image. The value must be between 0 and 1 
        """
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_SetOpacity(self, _arg)


    def GetOpacity(self) -> "double const &":
        """GetOpacity(itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3 self) -> double const &"""
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_GetOpacity(self)


    def SetFunctor(self, functor: 'itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > > const &') -> "void":
        """
        SetFunctor(itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3 self, itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > > const & functor)

        Set/Get the overlay
        functor - defaults to a reasonable set of colors. This can be used to
        apply a different colormap. 
        """
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_SetFunctor(self, functor)


    def GetFunctor(self, *args) -> "itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > > const &":
        """
        GetFunctor(itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3 self) -> itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > >
        GetFunctor(itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3 self) -> itk::Functor::LabelOverlayFunctor< unsigned char,unsigned long,itk::RGBPixel< unsigned char > > const &
        """
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_GetFunctor(self, *args)

    __swig_destroy__ = _itkLabelMapOverlayImageFilterPython.delete_itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3

    def cast(obj: 'itkLightObject') -> "itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3 *":
        """cast(itkLightObject obj) -> itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3"""
        return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3

        Create a new object of the class itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3.Clone = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_Clone, None, itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3.SetFeatureImage = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_SetFeatureImage, None, itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3.GetFeatureImage = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_GetFeatureImage, None, itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3.SetInput1 = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_SetInput1, None, itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3.SetInput2 = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_SetInput2, None, itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3.SetOpacity = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_SetOpacity, None, itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3.GetOpacity = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_GetOpacity, None, itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3.SetFunctor = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_SetFunctor, None, itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3.GetFunctor = new_instancemethod(_itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_GetFunctor, None, itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_swigregister = _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_swigregister
itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_swigregister(itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3)

def itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3___New_orig__() -> "itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_Pointer":
    """itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3___New_orig__() -> itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_Pointer"""
    return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3___New_orig__()

def itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_cast(obj: 'itkLightObject') -> "itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3 *":
    """itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_cast(itkLightObject obj) -> itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3"""
    return _itkLabelMapOverlayImageFilterPython.itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def label_map_overlay_image_filter(*args, **kwargs):
    """Procedural interface for LabelMapOverlayImageFilter"""
    import itk
    instance = itk.LabelMapOverlayImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def label_map_overlay_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.LabelMapOverlayImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.LabelMapOverlayImageFilter.values()[0]
    else:
        filter_object = itk.LabelMapOverlayImageFilter

    label_map_overlay_image_filter.__doc__ = filter_object.__doc__
    label_map_overlay_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    label_map_overlay_image_filter.__doc__ += "Available Keyword Arguments:\n"
    label_map_overlay_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



