# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLaplacianImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLaplacianImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkLaplacianImageFilterPython
            return _itkLaplacianImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkLaplacianImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkLaplacianImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLaplacianImageFilterPython
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
import itkImageToImageFilterAPython
import itkImagePython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkRGBAPixelPython
import itkFixedArrayPython
import stdcomplexPython
import itkRGBPixelPython
import itkMatrixPython
import vnl_matrix_fixedPython
import vnl_matrixPython
import vnl_vectorPython
import itkVectorPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkLaplacianImageFilterID3ID3_New():
  return itkLaplacianImageFilterID3ID3.New()


def itkLaplacianImageFilterID2ID2_New():
  return itkLaplacianImageFilterID2ID2.New()


def itkLaplacianImageFilterIF3IF3_New():
  return itkLaplacianImageFilterIF3IF3.New()


def itkLaplacianImageFilterIF2IF2_New():
  return itkLaplacianImageFilterIF2IF2.New()

class itkLaplacianImageFilterID2ID2(itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    """


    This filter computes the Laplacian of a scalar-valued image.

    The Laplacian is an isotropic measure of the 2nd spatial derivative of
    an image. The Laplacian of an image highlights regions of rapid
    intensity change and is therefore often used for edge detection.
    Often, the Laplacian is applied to an image that has first been
    smoothed with a Gaussian filter in order to reduce its sensitivity to
    noise.

    The Laplacian at each pixel location is computed by convolution with
    the itk::LaplacianOperator. Inputs and Outputs The input to this
    filter is a scalar-valued itk::Image of arbitrary dimension. The
    output is a scalar-valued itk::Image.

    WARNING:  The pixel type of the input and output images must be of
    real type (float or double). ConceptChecking is used here to enforce
    the input pixel type. You will get a compilation error if the pixel
    type of the input and output images is not float or double.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    See:  LaplacianOperator  \\sphinx
    \\sphinxexample{Filtering/ImageFeature/ComputeLaplacian,Compute
    Laplacian} \\endsphinx

    C++ includes: itkLaplacianImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLaplacianImageFilterID2ID2_Pointer":
        """__New_orig__() -> itkLaplacianImageFilterID2ID2_Pointer"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLaplacianImageFilterID2ID2_Pointer":
        """Clone(itkLaplacianImageFilterID2ID2 self) -> itkLaplacianImageFilterID2ID2_Pointer"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_Clone(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """
        GenerateInputRequestedRegion(itkLaplacianImageFilterID2ID2 self)

        LaplacianImageFilter needs a larger input requested region than the
        output requested region (larger in the direction of the derivative).
        As such, LaplacianImageFilter needs to provide an implementation for
        GenerateInputRequestedRegion() in order to inform the pipeline
        execution model.

        See:  ImageToImageFilter::GenerateInputRequestedRegion() 
        """
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_GenerateInputRequestedRegion(self)


    def UseImageSpacingOn(self) -> "void":
        """
        UseImageSpacingOn(itkLaplacianImageFilterID2ID2 self)

        Enable/Disable
        using the image spacing information in calculations. Use this option
        if you want derivatives in physical space. Default is
        UseImageSpacingOn. 
        """
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_UseImageSpacingOn(self)


    def UseImageSpacingOff(self) -> "void":
        """UseImageSpacingOff(itkLaplacianImageFilterID2ID2 self)"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_UseImageSpacingOff(self)


    def SetUseImageSpacing(self, _arg: 'bool const') -> "void":
        """
        SetUseImageSpacing(itkLaplacianImageFilterID2ID2 self, bool const _arg)

        Set/Get whether
        or not the filter will use the spacing of the input image in its
        calculations 
        """
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_SetUseImageSpacing(self, _arg)


    def GetUseImageSpacing(self) -> "bool":
        """GetUseImageSpacing(itkLaplacianImageFilterID2ID2 self) -> bool"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_GetUseImageSpacing(self)

    SameDimensionCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_SameDimensionCheck
    InputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_InputPixelTypeIsFloatingPointCheck
    OutputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_OutputPixelTypeIsFloatingPointCheck
    __swig_destroy__ = _itkLaplacianImageFilterPython.delete_itkLaplacianImageFilterID2ID2

    def cast(obj: 'itkLightObject') -> "itkLaplacianImageFilterID2ID2 *":
        """cast(itkLightObject obj) -> itkLaplacianImageFilterID2ID2"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLaplacianImageFilterID2ID2

        Create a new object of the class itkLaplacianImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLaplacianImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLaplacianImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLaplacianImageFilterID2ID2.Clone = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_Clone, None, itkLaplacianImageFilterID2ID2)
itkLaplacianImageFilterID2ID2.GenerateInputRequestedRegion = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_GenerateInputRequestedRegion, None, itkLaplacianImageFilterID2ID2)
itkLaplacianImageFilterID2ID2.UseImageSpacingOn = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_UseImageSpacingOn, None, itkLaplacianImageFilterID2ID2)
itkLaplacianImageFilterID2ID2.UseImageSpacingOff = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_UseImageSpacingOff, None, itkLaplacianImageFilterID2ID2)
itkLaplacianImageFilterID2ID2.SetUseImageSpacing = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_SetUseImageSpacing, None, itkLaplacianImageFilterID2ID2)
itkLaplacianImageFilterID2ID2.GetUseImageSpacing = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_GetUseImageSpacing, None, itkLaplacianImageFilterID2ID2)
itkLaplacianImageFilterID2ID2_swigregister = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_swigregister
itkLaplacianImageFilterID2ID2_swigregister(itkLaplacianImageFilterID2ID2)

def itkLaplacianImageFilterID2ID2___New_orig__() -> "itkLaplacianImageFilterID2ID2_Pointer":
    """itkLaplacianImageFilterID2ID2___New_orig__() -> itkLaplacianImageFilterID2ID2_Pointer"""
    return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2___New_orig__()

def itkLaplacianImageFilterID2ID2_cast(obj: 'itkLightObject') -> "itkLaplacianImageFilterID2ID2 *":
    """itkLaplacianImageFilterID2ID2_cast(itkLightObject obj) -> itkLaplacianImageFilterID2ID2"""
    return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_cast(obj)

class itkLaplacianImageFilterID3ID3(itkImageToImageFilterAPython.itkImageToImageFilterID3ID3):
    """


    This filter computes the Laplacian of a scalar-valued image.

    The Laplacian is an isotropic measure of the 2nd spatial derivative of
    an image. The Laplacian of an image highlights regions of rapid
    intensity change and is therefore often used for edge detection.
    Often, the Laplacian is applied to an image that has first been
    smoothed with a Gaussian filter in order to reduce its sensitivity to
    noise.

    The Laplacian at each pixel location is computed by convolution with
    the itk::LaplacianOperator. Inputs and Outputs The input to this
    filter is a scalar-valued itk::Image of arbitrary dimension. The
    output is a scalar-valued itk::Image.

    WARNING:  The pixel type of the input and output images must be of
    real type (float or double). ConceptChecking is used here to enforce
    the input pixel type. You will get a compilation error if the pixel
    type of the input and output images is not float or double.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    See:  LaplacianOperator  \\sphinx
    \\sphinxexample{Filtering/ImageFeature/ComputeLaplacian,Compute
    Laplacian} \\endsphinx

    C++ includes: itkLaplacianImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLaplacianImageFilterID3ID3_Pointer":
        """__New_orig__() -> itkLaplacianImageFilterID3ID3_Pointer"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLaplacianImageFilterID3ID3_Pointer":
        """Clone(itkLaplacianImageFilterID3ID3 self) -> itkLaplacianImageFilterID3ID3_Pointer"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_Clone(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """
        GenerateInputRequestedRegion(itkLaplacianImageFilterID3ID3 self)

        LaplacianImageFilter needs a larger input requested region than the
        output requested region (larger in the direction of the derivative).
        As such, LaplacianImageFilter needs to provide an implementation for
        GenerateInputRequestedRegion() in order to inform the pipeline
        execution model.

        See:  ImageToImageFilter::GenerateInputRequestedRegion() 
        """
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_GenerateInputRequestedRegion(self)


    def UseImageSpacingOn(self) -> "void":
        """
        UseImageSpacingOn(itkLaplacianImageFilterID3ID3 self)

        Enable/Disable
        using the image spacing information in calculations. Use this option
        if you want derivatives in physical space. Default is
        UseImageSpacingOn. 
        """
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_UseImageSpacingOn(self)


    def UseImageSpacingOff(self) -> "void":
        """UseImageSpacingOff(itkLaplacianImageFilterID3ID3 self)"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_UseImageSpacingOff(self)


    def SetUseImageSpacing(self, _arg: 'bool const') -> "void":
        """
        SetUseImageSpacing(itkLaplacianImageFilterID3ID3 self, bool const _arg)

        Set/Get whether
        or not the filter will use the spacing of the input image in its
        calculations 
        """
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_SetUseImageSpacing(self, _arg)


    def GetUseImageSpacing(self) -> "bool":
        """GetUseImageSpacing(itkLaplacianImageFilterID3ID3 self) -> bool"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_GetUseImageSpacing(self)

    SameDimensionCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_SameDimensionCheck
    InputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_InputPixelTypeIsFloatingPointCheck
    OutputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_OutputPixelTypeIsFloatingPointCheck
    __swig_destroy__ = _itkLaplacianImageFilterPython.delete_itkLaplacianImageFilterID3ID3

    def cast(obj: 'itkLightObject') -> "itkLaplacianImageFilterID3ID3 *":
        """cast(itkLightObject obj) -> itkLaplacianImageFilterID3ID3"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLaplacianImageFilterID3ID3

        Create a new object of the class itkLaplacianImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLaplacianImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLaplacianImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLaplacianImageFilterID3ID3.Clone = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_Clone, None, itkLaplacianImageFilterID3ID3)
itkLaplacianImageFilterID3ID3.GenerateInputRequestedRegion = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_GenerateInputRequestedRegion, None, itkLaplacianImageFilterID3ID3)
itkLaplacianImageFilterID3ID3.UseImageSpacingOn = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_UseImageSpacingOn, None, itkLaplacianImageFilterID3ID3)
itkLaplacianImageFilterID3ID3.UseImageSpacingOff = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_UseImageSpacingOff, None, itkLaplacianImageFilterID3ID3)
itkLaplacianImageFilterID3ID3.SetUseImageSpacing = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_SetUseImageSpacing, None, itkLaplacianImageFilterID3ID3)
itkLaplacianImageFilterID3ID3.GetUseImageSpacing = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_GetUseImageSpacing, None, itkLaplacianImageFilterID3ID3)
itkLaplacianImageFilterID3ID3_swigregister = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_swigregister
itkLaplacianImageFilterID3ID3_swigregister(itkLaplacianImageFilterID3ID3)

def itkLaplacianImageFilterID3ID3___New_orig__() -> "itkLaplacianImageFilterID3ID3_Pointer":
    """itkLaplacianImageFilterID3ID3___New_orig__() -> itkLaplacianImageFilterID3ID3_Pointer"""
    return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3___New_orig__()

def itkLaplacianImageFilterID3ID3_cast(obj: 'itkLightObject') -> "itkLaplacianImageFilterID3ID3 *":
    """itkLaplacianImageFilterID3ID3_cast(itkLightObject obj) -> itkLaplacianImageFilterID3ID3"""
    return _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_cast(obj)

class itkLaplacianImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """


    This filter computes the Laplacian of a scalar-valued image.

    The Laplacian is an isotropic measure of the 2nd spatial derivative of
    an image. The Laplacian of an image highlights regions of rapid
    intensity change and is therefore often used for edge detection.
    Often, the Laplacian is applied to an image that has first been
    smoothed with a Gaussian filter in order to reduce its sensitivity to
    noise.

    The Laplacian at each pixel location is computed by convolution with
    the itk::LaplacianOperator. Inputs and Outputs The input to this
    filter is a scalar-valued itk::Image of arbitrary dimension. The
    output is a scalar-valued itk::Image.

    WARNING:  The pixel type of the input and output images must be of
    real type (float or double). ConceptChecking is used here to enforce
    the input pixel type. You will get a compilation error if the pixel
    type of the input and output images is not float or double.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    See:  LaplacianOperator  \\sphinx
    \\sphinxexample{Filtering/ImageFeature/ComputeLaplacian,Compute
    Laplacian} \\endsphinx

    C++ includes: itkLaplacianImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLaplacianImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkLaplacianImageFilterIF2IF2_Pointer"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLaplacianImageFilterIF2IF2_Pointer":
        """Clone(itkLaplacianImageFilterIF2IF2 self) -> itkLaplacianImageFilterIF2IF2_Pointer"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_Clone(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """
        GenerateInputRequestedRegion(itkLaplacianImageFilterIF2IF2 self)

        LaplacianImageFilter needs a larger input requested region than the
        output requested region (larger in the direction of the derivative).
        As such, LaplacianImageFilter needs to provide an implementation for
        GenerateInputRequestedRegion() in order to inform the pipeline
        execution model.

        See:  ImageToImageFilter::GenerateInputRequestedRegion() 
        """
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_GenerateInputRequestedRegion(self)


    def UseImageSpacingOn(self) -> "void":
        """
        UseImageSpacingOn(itkLaplacianImageFilterIF2IF2 self)

        Enable/Disable
        using the image spacing information in calculations. Use this option
        if you want derivatives in physical space. Default is
        UseImageSpacingOn. 
        """
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_UseImageSpacingOn(self)


    def UseImageSpacingOff(self) -> "void":
        """UseImageSpacingOff(itkLaplacianImageFilterIF2IF2 self)"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_UseImageSpacingOff(self)


    def SetUseImageSpacing(self, _arg: 'bool const') -> "void":
        """
        SetUseImageSpacing(itkLaplacianImageFilterIF2IF2 self, bool const _arg)

        Set/Get whether
        or not the filter will use the spacing of the input image in its
        calculations 
        """
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_SetUseImageSpacing(self, _arg)


    def GetUseImageSpacing(self) -> "bool":
        """GetUseImageSpacing(itkLaplacianImageFilterIF2IF2 self) -> bool"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_GetUseImageSpacing(self)

    SameDimensionCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_SameDimensionCheck
    InputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_InputPixelTypeIsFloatingPointCheck
    OutputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_OutputPixelTypeIsFloatingPointCheck
    __swig_destroy__ = _itkLaplacianImageFilterPython.delete_itkLaplacianImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkLaplacianImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkLaplacianImageFilterIF2IF2"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLaplacianImageFilterIF2IF2

        Create a new object of the class itkLaplacianImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLaplacianImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLaplacianImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLaplacianImageFilterIF2IF2.Clone = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_Clone, None, itkLaplacianImageFilterIF2IF2)
itkLaplacianImageFilterIF2IF2.GenerateInputRequestedRegion = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_GenerateInputRequestedRegion, None, itkLaplacianImageFilterIF2IF2)
itkLaplacianImageFilterIF2IF2.UseImageSpacingOn = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_UseImageSpacingOn, None, itkLaplacianImageFilterIF2IF2)
itkLaplacianImageFilterIF2IF2.UseImageSpacingOff = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_UseImageSpacingOff, None, itkLaplacianImageFilterIF2IF2)
itkLaplacianImageFilterIF2IF2.SetUseImageSpacing = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_SetUseImageSpacing, None, itkLaplacianImageFilterIF2IF2)
itkLaplacianImageFilterIF2IF2.GetUseImageSpacing = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_GetUseImageSpacing, None, itkLaplacianImageFilterIF2IF2)
itkLaplacianImageFilterIF2IF2_swigregister = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_swigregister
itkLaplacianImageFilterIF2IF2_swigregister(itkLaplacianImageFilterIF2IF2)

def itkLaplacianImageFilterIF2IF2___New_orig__() -> "itkLaplacianImageFilterIF2IF2_Pointer":
    """itkLaplacianImageFilterIF2IF2___New_orig__() -> itkLaplacianImageFilterIF2IF2_Pointer"""
    return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2___New_orig__()

def itkLaplacianImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkLaplacianImageFilterIF2IF2 *":
    """itkLaplacianImageFilterIF2IF2_cast(itkLightObject obj) -> itkLaplacianImageFilterIF2IF2"""
    return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_cast(obj)

class itkLaplacianImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    """


    This filter computes the Laplacian of a scalar-valued image.

    The Laplacian is an isotropic measure of the 2nd spatial derivative of
    an image. The Laplacian of an image highlights regions of rapid
    intensity change and is therefore often used for edge detection.
    Often, the Laplacian is applied to an image that has first been
    smoothed with a Gaussian filter in order to reduce its sensitivity to
    noise.

    The Laplacian at each pixel location is computed by convolution with
    the itk::LaplacianOperator. Inputs and Outputs The input to this
    filter is a scalar-valued itk::Image of arbitrary dimension. The
    output is a scalar-valued itk::Image.

    WARNING:  The pixel type of the input and output images must be of
    real type (float or double). ConceptChecking is used here to enforce
    the input pixel type. You will get a compilation error if the pixel
    type of the input and output images is not float or double.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    See:  LaplacianOperator  \\sphinx
    \\sphinxexample{Filtering/ImageFeature/ComputeLaplacian,Compute
    Laplacian} \\endsphinx

    C++ includes: itkLaplacianImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLaplacianImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkLaplacianImageFilterIF3IF3_Pointer"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLaplacianImageFilterIF3IF3_Pointer":
        """Clone(itkLaplacianImageFilterIF3IF3 self) -> itkLaplacianImageFilterIF3IF3_Pointer"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_Clone(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """
        GenerateInputRequestedRegion(itkLaplacianImageFilterIF3IF3 self)

        LaplacianImageFilter needs a larger input requested region than the
        output requested region (larger in the direction of the derivative).
        As such, LaplacianImageFilter needs to provide an implementation for
        GenerateInputRequestedRegion() in order to inform the pipeline
        execution model.

        See:  ImageToImageFilter::GenerateInputRequestedRegion() 
        """
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_GenerateInputRequestedRegion(self)


    def UseImageSpacingOn(self) -> "void":
        """
        UseImageSpacingOn(itkLaplacianImageFilterIF3IF3 self)

        Enable/Disable
        using the image spacing information in calculations. Use this option
        if you want derivatives in physical space. Default is
        UseImageSpacingOn. 
        """
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_UseImageSpacingOn(self)


    def UseImageSpacingOff(self) -> "void":
        """UseImageSpacingOff(itkLaplacianImageFilterIF3IF3 self)"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_UseImageSpacingOff(self)


    def SetUseImageSpacing(self, _arg: 'bool const') -> "void":
        """
        SetUseImageSpacing(itkLaplacianImageFilterIF3IF3 self, bool const _arg)

        Set/Get whether
        or not the filter will use the spacing of the input image in its
        calculations 
        """
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_SetUseImageSpacing(self, _arg)


    def GetUseImageSpacing(self) -> "bool":
        """GetUseImageSpacing(itkLaplacianImageFilterIF3IF3 self) -> bool"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_GetUseImageSpacing(self)

    SameDimensionCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_SameDimensionCheck
    InputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_InputPixelTypeIsFloatingPointCheck
    OutputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_OutputPixelTypeIsFloatingPointCheck
    __swig_destroy__ = _itkLaplacianImageFilterPython.delete_itkLaplacianImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkLaplacianImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkLaplacianImageFilterIF3IF3"""
        return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLaplacianImageFilterIF3IF3

        Create a new object of the class itkLaplacianImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLaplacianImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLaplacianImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLaplacianImageFilterIF3IF3.Clone = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_Clone, None, itkLaplacianImageFilterIF3IF3)
itkLaplacianImageFilterIF3IF3.GenerateInputRequestedRegion = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_GenerateInputRequestedRegion, None, itkLaplacianImageFilterIF3IF3)
itkLaplacianImageFilterIF3IF3.UseImageSpacingOn = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_UseImageSpacingOn, None, itkLaplacianImageFilterIF3IF3)
itkLaplacianImageFilterIF3IF3.UseImageSpacingOff = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_UseImageSpacingOff, None, itkLaplacianImageFilterIF3IF3)
itkLaplacianImageFilterIF3IF3.SetUseImageSpacing = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_SetUseImageSpacing, None, itkLaplacianImageFilterIF3IF3)
itkLaplacianImageFilterIF3IF3.GetUseImageSpacing = new_instancemethod(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_GetUseImageSpacing, None, itkLaplacianImageFilterIF3IF3)
itkLaplacianImageFilterIF3IF3_swigregister = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_swigregister
itkLaplacianImageFilterIF3IF3_swigregister(itkLaplacianImageFilterIF3IF3)

def itkLaplacianImageFilterIF3IF3___New_orig__() -> "itkLaplacianImageFilterIF3IF3_Pointer":
    """itkLaplacianImageFilterIF3IF3___New_orig__() -> itkLaplacianImageFilterIF3IF3_Pointer"""
    return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3___New_orig__()

def itkLaplacianImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkLaplacianImageFilterIF3IF3 *":
    """itkLaplacianImageFilterIF3IF3_cast(itkLightObject obj) -> itkLaplacianImageFilterIF3IF3"""
    return _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def laplacian_image_filter(*args, **kwargs):
    """Procedural interface for LaplacianImageFilter"""
    import itk
    instance = itk.LaplacianImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def laplacian_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.LaplacianImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.LaplacianImageFilter.values()[0]
    else:
        filter_object = itk.LaplacianImageFilter

    laplacian_image_filter.__doc__ = filter_object.__doc__
    laplacian_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    laplacian_image_filter.__doc__ += "Available Keyword Arguments:\n"
    laplacian_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



