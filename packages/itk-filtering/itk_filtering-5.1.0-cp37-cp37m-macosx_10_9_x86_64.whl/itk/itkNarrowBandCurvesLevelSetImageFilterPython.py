# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkNarrowBandCurvesLevelSetImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkNarrowBandCurvesLevelSetImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkNarrowBandCurvesLevelSetImageFilterPython
            return _itkNarrowBandCurvesLevelSetImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkNarrowBandCurvesLevelSetImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkNarrowBandCurvesLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkNarrowBandCurvesLevelSetImageFilterPython
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
import itkNarrowBandLevelSetImageFilterPython
import itkImagePython
import itkSymmetricSecondRankTensorPython
import itkFixedArrayPython
import itkMatrixPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkPointPython
import vnl_vector_refPython
import itkVectorPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkImageRegionPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkSegmentationLevelSetFunctionPython
import itkLevelSetFunctionPython
import itkFiniteDifferenceFunctionPython
import itkNarrowBandImageFilterBasePython
import ITKNarrowBandBasePython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython
import itkImageToImageFilterCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterBPython

def itkNarrowBandCurvesLevelSetImageFilterID3ID3D_New():
  return itkNarrowBandCurvesLevelSetImageFilterID3ID3D.New()


def itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_New():
  return itkNarrowBandCurvesLevelSetImageFilterIF3IF3F.New()


def itkNarrowBandCurvesLevelSetImageFilterID2ID2D_New():
  return itkNarrowBandCurvesLevelSetImageFilterID2ID2D.New()


def itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_New():
  return itkNarrowBandCurvesLevelSetImageFilterIF2IF2F.New()

class itkNarrowBandCurvesLevelSetImageFilterID2ID2D(itkNarrowBandLevelSetImageFilterPython.itkNarrowBandLevelSetImageFilterID2ID2D):
    """


    Segments structures in images based on user supplied edge potential
    map.

    IMPORTANT The NarrowBandLevelSetImageFilter class and the
    CurvesLevelSetFunction class contain additional information necessary
    to the full understanding of how to use this filter. OVERVIEW This
    class is a level set method segmentation filter. An initial contour is
    propagated outwards (or inwards) until it sticks to the shape
    boundaries. This is done by using a level set speed function based on
    a user supplied edge potential map. INPUTS This filter requires two
    inputs. The first input is a initial level set. The initial level set
    is a real image which contains the initial contour/surface as the zero
    level set. For example, a signed distance function from the initial
    contour/surface is typically used. Unlike the simpler
    ShapeDetectionLevelSetImageFilter the initial contour does not have to
    lie wholly within the shape to be segmented. The initial contour is
    allow to overlap the shape boundary. The extra advection term in the
    update equation behaves like a doublet and attracts the contour to the
    boundary. This approach for segmentation follows that of Lorigo et al
    (2001).

    The second input is the feature image. For this filter, this is the
    edge potential map. General characteristics of an edge potential map
    is that it has values close to zero in regions near the edges and
    values close to one inside the shape itself. Typically, the edge
    potential map is compute from the image gradient, for example:  \\[
    g(I) = 1 / ( 1 + | (\\nabla * G)(I)| ) \\] \\[ g(I) =
    \\exp^{-|(\\nabla * G)(I)|} \\]

    where $ I $ is image intensity and $ (\\nabla * G) $ is the
    derivative of Gaussian operator.

    See NarrowBandLevelSetImageFilter and NarrowBandImageFilterBase for
    more information on Inputs. PARAMETERS The method
    SetUseNegatiiveFeatures() can be used to switch from propagating
    inwards (false) versus propagating outwards (true).  This
    implementation allows the user to set the weights between the
    propagation, advection and curvature term using methods
    SetPropagationScaling(), SetAdvectionScaling(), SetCurvatureScaling().
    In general, the larger the CurvatureScaling, the smoother the
    resulting contour. To follow the implementation in Caselles's paper,
    set the PropagationScaling to $ c $ (the inflation or ballon force)
    and AdvectionScaling and CurvatureScaling both to 1.0.

    OUTPUTS The filter outputs a single, scalar, real-valued image.
    Negative values in the output image are inside the segmented region
    and positive values in the image are outside of the inside region. The
    zero crossings of the image correspond to the position of the level
    set front. REFERENCES L. Lorigo, O. Faugeras, W.E.L. Grimson, R.
    Keriven, R. Kikinis, A. Nabavi, and C.-F. Westin, Curves: Curve
    evolution for vessel segmentation. Medical Image Analysis, 5:195-206,
    2001.

    See NarrowBandImageFilterBase and NarrowBandLevelSetImageFilter for
    more information.

    See:   NarrowBandLevelSetImageFilter

    See:  CurvesLevelSetFunction

    C++ includes: itkNarrowBandCurvesLevelSetImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNarrowBandCurvesLevelSetImageFilterID2ID2D_Pointer":
        """__New_orig__() -> itkNarrowBandCurvesLevelSetImageFilterID2ID2D_Pointer"""
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNarrowBandCurvesLevelSetImageFilterID2ID2D_Pointer":
        """Clone(itkNarrowBandCurvesLevelSetImageFilterID2ID2D self) -> itkNarrowBandCurvesLevelSetImageFilterID2ID2D_Pointer"""
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_Clone(self)


    def SetDerivativeSigma(self, value: 'float') -> "void":
        """
        SetDerivativeSigma(itkNarrowBandCurvesLevelSetImageFilterID2ID2D self, float value)

        Set the value of
        sigma used to compute derivatives 
        """
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_SetDerivativeSigma(self, value)


    def GetDerivativeSigma(self) -> "float":
        """GetDerivativeSigma(itkNarrowBandCurvesLevelSetImageFilterID2ID2D self) -> float"""
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_GetDerivativeSigma(self)

    OutputHasNumericTraitsCheck = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_OutputHasNumericTraitsCheck
    __swig_destroy__ = _itkNarrowBandCurvesLevelSetImageFilterPython.delete_itkNarrowBandCurvesLevelSetImageFilterID2ID2D

    def cast(obj: 'itkLightObject') -> "itkNarrowBandCurvesLevelSetImageFilterID2ID2D *":
        """cast(itkLightObject obj) -> itkNarrowBandCurvesLevelSetImageFilterID2ID2D"""
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkNarrowBandCurvesLevelSetImageFilterID2ID2D

        Create a new object of the class itkNarrowBandCurvesLevelSetImageFilterID2ID2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNarrowBandCurvesLevelSetImageFilterID2ID2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNarrowBandCurvesLevelSetImageFilterID2ID2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNarrowBandCurvesLevelSetImageFilterID2ID2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNarrowBandCurvesLevelSetImageFilterID2ID2D.Clone = new_instancemethod(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_Clone, None, itkNarrowBandCurvesLevelSetImageFilterID2ID2D)
itkNarrowBandCurvesLevelSetImageFilterID2ID2D.SetDerivativeSigma = new_instancemethod(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_SetDerivativeSigma, None, itkNarrowBandCurvesLevelSetImageFilterID2ID2D)
itkNarrowBandCurvesLevelSetImageFilterID2ID2D.GetDerivativeSigma = new_instancemethod(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_GetDerivativeSigma, None, itkNarrowBandCurvesLevelSetImageFilterID2ID2D)
itkNarrowBandCurvesLevelSetImageFilterID2ID2D_swigregister = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_swigregister
itkNarrowBandCurvesLevelSetImageFilterID2ID2D_swigregister(itkNarrowBandCurvesLevelSetImageFilterID2ID2D)

def itkNarrowBandCurvesLevelSetImageFilterID2ID2D___New_orig__() -> "itkNarrowBandCurvesLevelSetImageFilterID2ID2D_Pointer":
    """itkNarrowBandCurvesLevelSetImageFilterID2ID2D___New_orig__() -> itkNarrowBandCurvesLevelSetImageFilterID2ID2D_Pointer"""
    return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D___New_orig__()

def itkNarrowBandCurvesLevelSetImageFilterID2ID2D_cast(obj: 'itkLightObject') -> "itkNarrowBandCurvesLevelSetImageFilterID2ID2D *":
    """itkNarrowBandCurvesLevelSetImageFilterID2ID2D_cast(itkLightObject obj) -> itkNarrowBandCurvesLevelSetImageFilterID2ID2D"""
    return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_cast(obj)

class itkNarrowBandCurvesLevelSetImageFilterID3ID3D(itkNarrowBandLevelSetImageFilterPython.itkNarrowBandLevelSetImageFilterID3ID3D):
    """


    Segments structures in images based on user supplied edge potential
    map.

    IMPORTANT The NarrowBandLevelSetImageFilter class and the
    CurvesLevelSetFunction class contain additional information necessary
    to the full understanding of how to use this filter. OVERVIEW This
    class is a level set method segmentation filter. An initial contour is
    propagated outwards (or inwards) until it sticks to the shape
    boundaries. This is done by using a level set speed function based on
    a user supplied edge potential map. INPUTS This filter requires two
    inputs. The first input is a initial level set. The initial level set
    is a real image which contains the initial contour/surface as the zero
    level set. For example, a signed distance function from the initial
    contour/surface is typically used. Unlike the simpler
    ShapeDetectionLevelSetImageFilter the initial contour does not have to
    lie wholly within the shape to be segmented. The initial contour is
    allow to overlap the shape boundary. The extra advection term in the
    update equation behaves like a doublet and attracts the contour to the
    boundary. This approach for segmentation follows that of Lorigo et al
    (2001).

    The second input is the feature image. For this filter, this is the
    edge potential map. General characteristics of an edge potential map
    is that it has values close to zero in regions near the edges and
    values close to one inside the shape itself. Typically, the edge
    potential map is compute from the image gradient, for example:  \\[
    g(I) = 1 / ( 1 + | (\\nabla * G)(I)| ) \\] \\[ g(I) =
    \\exp^{-|(\\nabla * G)(I)|} \\]

    where $ I $ is image intensity and $ (\\nabla * G) $ is the
    derivative of Gaussian operator.

    See NarrowBandLevelSetImageFilter and NarrowBandImageFilterBase for
    more information on Inputs. PARAMETERS The method
    SetUseNegatiiveFeatures() can be used to switch from propagating
    inwards (false) versus propagating outwards (true).  This
    implementation allows the user to set the weights between the
    propagation, advection and curvature term using methods
    SetPropagationScaling(), SetAdvectionScaling(), SetCurvatureScaling().
    In general, the larger the CurvatureScaling, the smoother the
    resulting contour. To follow the implementation in Caselles's paper,
    set the PropagationScaling to $ c $ (the inflation or ballon force)
    and AdvectionScaling and CurvatureScaling both to 1.0.

    OUTPUTS The filter outputs a single, scalar, real-valued image.
    Negative values in the output image are inside the segmented region
    and positive values in the image are outside of the inside region. The
    zero crossings of the image correspond to the position of the level
    set front. REFERENCES L. Lorigo, O. Faugeras, W.E.L. Grimson, R.
    Keriven, R. Kikinis, A. Nabavi, and C.-F. Westin, Curves: Curve
    evolution for vessel segmentation. Medical Image Analysis, 5:195-206,
    2001.

    See NarrowBandImageFilterBase and NarrowBandLevelSetImageFilter for
    more information.

    See:   NarrowBandLevelSetImageFilter

    See:  CurvesLevelSetFunction

    C++ includes: itkNarrowBandCurvesLevelSetImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNarrowBandCurvesLevelSetImageFilterID3ID3D_Pointer":
        """__New_orig__() -> itkNarrowBandCurvesLevelSetImageFilterID3ID3D_Pointer"""
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNarrowBandCurvesLevelSetImageFilterID3ID3D_Pointer":
        """Clone(itkNarrowBandCurvesLevelSetImageFilterID3ID3D self) -> itkNarrowBandCurvesLevelSetImageFilterID3ID3D_Pointer"""
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_Clone(self)


    def SetDerivativeSigma(self, value: 'float') -> "void":
        """
        SetDerivativeSigma(itkNarrowBandCurvesLevelSetImageFilterID3ID3D self, float value)

        Set the value of
        sigma used to compute derivatives 
        """
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_SetDerivativeSigma(self, value)


    def GetDerivativeSigma(self) -> "float":
        """GetDerivativeSigma(itkNarrowBandCurvesLevelSetImageFilterID3ID3D self) -> float"""
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_GetDerivativeSigma(self)

    OutputHasNumericTraitsCheck = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_OutputHasNumericTraitsCheck
    __swig_destroy__ = _itkNarrowBandCurvesLevelSetImageFilterPython.delete_itkNarrowBandCurvesLevelSetImageFilterID3ID3D

    def cast(obj: 'itkLightObject') -> "itkNarrowBandCurvesLevelSetImageFilterID3ID3D *":
        """cast(itkLightObject obj) -> itkNarrowBandCurvesLevelSetImageFilterID3ID3D"""
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkNarrowBandCurvesLevelSetImageFilterID3ID3D

        Create a new object of the class itkNarrowBandCurvesLevelSetImageFilterID3ID3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNarrowBandCurvesLevelSetImageFilterID3ID3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNarrowBandCurvesLevelSetImageFilterID3ID3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNarrowBandCurvesLevelSetImageFilterID3ID3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNarrowBandCurvesLevelSetImageFilterID3ID3D.Clone = new_instancemethod(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_Clone, None, itkNarrowBandCurvesLevelSetImageFilterID3ID3D)
itkNarrowBandCurvesLevelSetImageFilterID3ID3D.SetDerivativeSigma = new_instancemethod(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_SetDerivativeSigma, None, itkNarrowBandCurvesLevelSetImageFilterID3ID3D)
itkNarrowBandCurvesLevelSetImageFilterID3ID3D.GetDerivativeSigma = new_instancemethod(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_GetDerivativeSigma, None, itkNarrowBandCurvesLevelSetImageFilterID3ID3D)
itkNarrowBandCurvesLevelSetImageFilterID3ID3D_swigregister = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_swigregister
itkNarrowBandCurvesLevelSetImageFilterID3ID3D_swigregister(itkNarrowBandCurvesLevelSetImageFilterID3ID3D)

def itkNarrowBandCurvesLevelSetImageFilterID3ID3D___New_orig__() -> "itkNarrowBandCurvesLevelSetImageFilterID3ID3D_Pointer":
    """itkNarrowBandCurvesLevelSetImageFilterID3ID3D___New_orig__() -> itkNarrowBandCurvesLevelSetImageFilterID3ID3D_Pointer"""
    return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D___New_orig__()

def itkNarrowBandCurvesLevelSetImageFilterID3ID3D_cast(obj: 'itkLightObject') -> "itkNarrowBandCurvesLevelSetImageFilterID3ID3D *":
    """itkNarrowBandCurvesLevelSetImageFilterID3ID3D_cast(itkLightObject obj) -> itkNarrowBandCurvesLevelSetImageFilterID3ID3D"""
    return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_cast(obj)

class itkNarrowBandCurvesLevelSetImageFilterIF2IF2F(itkNarrowBandLevelSetImageFilterPython.itkNarrowBandLevelSetImageFilterIF2IF2F):
    """


    Segments structures in images based on user supplied edge potential
    map.

    IMPORTANT The NarrowBandLevelSetImageFilter class and the
    CurvesLevelSetFunction class contain additional information necessary
    to the full understanding of how to use this filter. OVERVIEW This
    class is a level set method segmentation filter. An initial contour is
    propagated outwards (or inwards) until it sticks to the shape
    boundaries. This is done by using a level set speed function based on
    a user supplied edge potential map. INPUTS This filter requires two
    inputs. The first input is a initial level set. The initial level set
    is a real image which contains the initial contour/surface as the zero
    level set. For example, a signed distance function from the initial
    contour/surface is typically used. Unlike the simpler
    ShapeDetectionLevelSetImageFilter the initial contour does not have to
    lie wholly within the shape to be segmented. The initial contour is
    allow to overlap the shape boundary. The extra advection term in the
    update equation behaves like a doublet and attracts the contour to the
    boundary. This approach for segmentation follows that of Lorigo et al
    (2001).

    The second input is the feature image. For this filter, this is the
    edge potential map. General characteristics of an edge potential map
    is that it has values close to zero in regions near the edges and
    values close to one inside the shape itself. Typically, the edge
    potential map is compute from the image gradient, for example:  \\[
    g(I) = 1 / ( 1 + | (\\nabla * G)(I)| ) \\] \\[ g(I) =
    \\exp^{-|(\\nabla * G)(I)|} \\]

    where $ I $ is image intensity and $ (\\nabla * G) $ is the
    derivative of Gaussian operator.

    See NarrowBandLevelSetImageFilter and NarrowBandImageFilterBase for
    more information on Inputs. PARAMETERS The method
    SetUseNegatiiveFeatures() can be used to switch from propagating
    inwards (false) versus propagating outwards (true).  This
    implementation allows the user to set the weights between the
    propagation, advection and curvature term using methods
    SetPropagationScaling(), SetAdvectionScaling(), SetCurvatureScaling().
    In general, the larger the CurvatureScaling, the smoother the
    resulting contour. To follow the implementation in Caselles's paper,
    set the PropagationScaling to $ c $ (the inflation or ballon force)
    and AdvectionScaling and CurvatureScaling both to 1.0.

    OUTPUTS The filter outputs a single, scalar, real-valued image.
    Negative values in the output image are inside the segmented region
    and positive values in the image are outside of the inside region. The
    zero crossings of the image correspond to the position of the level
    set front. REFERENCES L. Lorigo, O. Faugeras, W.E.L. Grimson, R.
    Keriven, R. Kikinis, A. Nabavi, and C.-F. Westin, Curves: Curve
    evolution for vessel segmentation. Medical Image Analysis, 5:195-206,
    2001.

    See NarrowBandImageFilterBase and NarrowBandLevelSetImageFilter for
    more information.

    See:   NarrowBandLevelSetImageFilter

    See:  CurvesLevelSetFunction

    C++ includes: itkNarrowBandCurvesLevelSetImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_Pointer":
        """__New_orig__() -> itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_Pointer"""
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_Pointer":
        """Clone(itkNarrowBandCurvesLevelSetImageFilterIF2IF2F self) -> itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_Pointer"""
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_Clone(self)


    def SetDerivativeSigma(self, value: 'float') -> "void":
        """
        SetDerivativeSigma(itkNarrowBandCurvesLevelSetImageFilterIF2IF2F self, float value)

        Set the value of
        sigma used to compute derivatives 
        """
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_SetDerivativeSigma(self, value)


    def GetDerivativeSigma(self) -> "float":
        """GetDerivativeSigma(itkNarrowBandCurvesLevelSetImageFilterIF2IF2F self) -> float"""
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_GetDerivativeSigma(self)

    OutputHasNumericTraitsCheck = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_OutputHasNumericTraitsCheck
    __swig_destroy__ = _itkNarrowBandCurvesLevelSetImageFilterPython.delete_itkNarrowBandCurvesLevelSetImageFilterIF2IF2F

    def cast(obj: 'itkLightObject') -> "itkNarrowBandCurvesLevelSetImageFilterIF2IF2F *":
        """cast(itkLightObject obj) -> itkNarrowBandCurvesLevelSetImageFilterIF2IF2F"""
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkNarrowBandCurvesLevelSetImageFilterIF2IF2F

        Create a new object of the class itkNarrowBandCurvesLevelSetImageFilterIF2IF2F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNarrowBandCurvesLevelSetImageFilterIF2IF2F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNarrowBandCurvesLevelSetImageFilterIF2IF2F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNarrowBandCurvesLevelSetImageFilterIF2IF2F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNarrowBandCurvesLevelSetImageFilterIF2IF2F.Clone = new_instancemethod(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_Clone, None, itkNarrowBandCurvesLevelSetImageFilterIF2IF2F)
itkNarrowBandCurvesLevelSetImageFilterIF2IF2F.SetDerivativeSigma = new_instancemethod(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_SetDerivativeSigma, None, itkNarrowBandCurvesLevelSetImageFilterIF2IF2F)
itkNarrowBandCurvesLevelSetImageFilterIF2IF2F.GetDerivativeSigma = new_instancemethod(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_GetDerivativeSigma, None, itkNarrowBandCurvesLevelSetImageFilterIF2IF2F)
itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_swigregister = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_swigregister
itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_swigregister(itkNarrowBandCurvesLevelSetImageFilterIF2IF2F)

def itkNarrowBandCurvesLevelSetImageFilterIF2IF2F___New_orig__() -> "itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_Pointer":
    """itkNarrowBandCurvesLevelSetImageFilterIF2IF2F___New_orig__() -> itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_Pointer"""
    return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F___New_orig__()

def itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_cast(obj: 'itkLightObject') -> "itkNarrowBandCurvesLevelSetImageFilterIF2IF2F *":
    """itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_cast(itkLightObject obj) -> itkNarrowBandCurvesLevelSetImageFilterIF2IF2F"""
    return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_cast(obj)

class itkNarrowBandCurvesLevelSetImageFilterIF3IF3F(itkNarrowBandLevelSetImageFilterPython.itkNarrowBandLevelSetImageFilterIF3IF3F):
    """


    Segments structures in images based on user supplied edge potential
    map.

    IMPORTANT The NarrowBandLevelSetImageFilter class and the
    CurvesLevelSetFunction class contain additional information necessary
    to the full understanding of how to use this filter. OVERVIEW This
    class is a level set method segmentation filter. An initial contour is
    propagated outwards (or inwards) until it sticks to the shape
    boundaries. This is done by using a level set speed function based on
    a user supplied edge potential map. INPUTS This filter requires two
    inputs. The first input is a initial level set. The initial level set
    is a real image which contains the initial contour/surface as the zero
    level set. For example, a signed distance function from the initial
    contour/surface is typically used. Unlike the simpler
    ShapeDetectionLevelSetImageFilter the initial contour does not have to
    lie wholly within the shape to be segmented. The initial contour is
    allow to overlap the shape boundary. The extra advection term in the
    update equation behaves like a doublet and attracts the contour to the
    boundary. This approach for segmentation follows that of Lorigo et al
    (2001).

    The second input is the feature image. For this filter, this is the
    edge potential map. General characteristics of an edge potential map
    is that it has values close to zero in regions near the edges and
    values close to one inside the shape itself. Typically, the edge
    potential map is compute from the image gradient, for example:  \\[
    g(I) = 1 / ( 1 + | (\\nabla * G)(I)| ) \\] \\[ g(I) =
    \\exp^{-|(\\nabla * G)(I)|} \\]

    where $ I $ is image intensity and $ (\\nabla * G) $ is the
    derivative of Gaussian operator.

    See NarrowBandLevelSetImageFilter and NarrowBandImageFilterBase for
    more information on Inputs. PARAMETERS The method
    SetUseNegatiiveFeatures() can be used to switch from propagating
    inwards (false) versus propagating outwards (true).  This
    implementation allows the user to set the weights between the
    propagation, advection and curvature term using methods
    SetPropagationScaling(), SetAdvectionScaling(), SetCurvatureScaling().
    In general, the larger the CurvatureScaling, the smoother the
    resulting contour. To follow the implementation in Caselles's paper,
    set the PropagationScaling to $ c $ (the inflation or ballon force)
    and AdvectionScaling and CurvatureScaling both to 1.0.

    OUTPUTS The filter outputs a single, scalar, real-valued image.
    Negative values in the output image are inside the segmented region
    and positive values in the image are outside of the inside region. The
    zero crossings of the image correspond to the position of the level
    set front. REFERENCES L. Lorigo, O. Faugeras, W.E.L. Grimson, R.
    Keriven, R. Kikinis, A. Nabavi, and C.-F. Westin, Curves: Curve
    evolution for vessel segmentation. Medical Image Analysis, 5:195-206,
    2001.

    See NarrowBandImageFilterBase and NarrowBandLevelSetImageFilter for
    more information.

    See:   NarrowBandLevelSetImageFilter

    See:  CurvesLevelSetFunction

    C++ includes: itkNarrowBandCurvesLevelSetImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_Pointer":
        """__New_orig__() -> itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_Pointer"""
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_Pointer":
        """Clone(itkNarrowBandCurvesLevelSetImageFilterIF3IF3F self) -> itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_Pointer"""
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_Clone(self)


    def SetDerivativeSigma(self, value: 'float') -> "void":
        """
        SetDerivativeSigma(itkNarrowBandCurvesLevelSetImageFilterIF3IF3F self, float value)

        Set the value of
        sigma used to compute derivatives 
        """
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_SetDerivativeSigma(self, value)


    def GetDerivativeSigma(self) -> "float":
        """GetDerivativeSigma(itkNarrowBandCurvesLevelSetImageFilterIF3IF3F self) -> float"""
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_GetDerivativeSigma(self)

    OutputHasNumericTraitsCheck = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_OutputHasNumericTraitsCheck
    __swig_destroy__ = _itkNarrowBandCurvesLevelSetImageFilterPython.delete_itkNarrowBandCurvesLevelSetImageFilterIF3IF3F

    def cast(obj: 'itkLightObject') -> "itkNarrowBandCurvesLevelSetImageFilterIF3IF3F *":
        """cast(itkLightObject obj) -> itkNarrowBandCurvesLevelSetImageFilterIF3IF3F"""
        return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkNarrowBandCurvesLevelSetImageFilterIF3IF3F

        Create a new object of the class itkNarrowBandCurvesLevelSetImageFilterIF3IF3F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNarrowBandCurvesLevelSetImageFilterIF3IF3F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNarrowBandCurvesLevelSetImageFilterIF3IF3F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNarrowBandCurvesLevelSetImageFilterIF3IF3F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNarrowBandCurvesLevelSetImageFilterIF3IF3F.Clone = new_instancemethod(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_Clone, None, itkNarrowBandCurvesLevelSetImageFilterIF3IF3F)
itkNarrowBandCurvesLevelSetImageFilterIF3IF3F.SetDerivativeSigma = new_instancemethod(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_SetDerivativeSigma, None, itkNarrowBandCurvesLevelSetImageFilterIF3IF3F)
itkNarrowBandCurvesLevelSetImageFilterIF3IF3F.GetDerivativeSigma = new_instancemethod(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_GetDerivativeSigma, None, itkNarrowBandCurvesLevelSetImageFilterIF3IF3F)
itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_swigregister = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_swigregister
itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_swigregister(itkNarrowBandCurvesLevelSetImageFilterIF3IF3F)

def itkNarrowBandCurvesLevelSetImageFilterIF3IF3F___New_orig__() -> "itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_Pointer":
    """itkNarrowBandCurvesLevelSetImageFilterIF3IF3F___New_orig__() -> itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_Pointer"""
    return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F___New_orig__()

def itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_cast(obj: 'itkLightObject') -> "itkNarrowBandCurvesLevelSetImageFilterIF3IF3F *":
    """itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_cast(itkLightObject obj) -> itkNarrowBandCurvesLevelSetImageFilterIF3IF3F"""
    return _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def narrow_band_curves_level_set_image_filter(*args, **kwargs):
    """Procedural interface for NarrowBandCurvesLevelSetImageFilter"""
    import itk
    instance = itk.NarrowBandCurvesLevelSetImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def narrow_band_curves_level_set_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.NarrowBandCurvesLevelSetImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.NarrowBandCurvesLevelSetImageFilter.values()[0]
    else:
        filter_object = itk.NarrowBandCurvesLevelSetImageFilter

    narrow_band_curves_level_set_image_filter.__doc__ = filter_object.__doc__
    narrow_band_curves_level_set_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    narrow_band_curves_level_set_image_filter.__doc__ += "Available Keyword Arguments:\n"
    narrow_band_curves_level_set_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



