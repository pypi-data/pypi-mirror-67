# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLaplacianSegmentationLevelSetImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLaplacianSegmentationLevelSetImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkLaplacianSegmentationLevelSetImageFilterPython
            return _itkLaplacianSegmentationLevelSetImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkLaplacianSegmentationLevelSetImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkLaplacianSegmentationLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLaplacianSegmentationLevelSetImageFilterPython
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
import itkSegmentationLevelSetImageFilterPython
import itkSparseFieldLevelSetImageFilterPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkFiniteDifferenceImageFilterPython
import itkFiniteDifferenceFunctionPython
import itkVectorPython
import itkFixedArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkImagePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython
import itkSegmentationLevelSetFunctionPython
import itkLevelSetFunctionPython

def itkLaplacianSegmentationLevelSetImageFilterID3ID3D_New():
  return itkLaplacianSegmentationLevelSetImageFilterID3ID3D.New()


def itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_New():
  return itkLaplacianSegmentationLevelSetImageFilterIF3IF3F.New()


def itkLaplacianSegmentationLevelSetImageFilterID2ID2D_New():
  return itkLaplacianSegmentationLevelSetImageFilterID2ID2D.New()


def itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_New():
  return itkLaplacianSegmentationLevelSetImageFilterIF2IF2F.New()

class itkLaplacianSegmentationLevelSetImageFilterID2ID2D(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterID2ID2D):
    """


    Segments structures in images based on a second derivative image
    features.

    IMPORTANT The SegmentationLevelSetImageFilter class and the
    LaplacianSegmentationLevelSetFunction class contain additional
    information necessary to the full understanding of how to use this
    filter. OVERVIEW This class is a level set method segmentation filter.
    It constructs a speed function which is zero at image edges as
    detected by a Laplacian filter. The evolving level set front will
    therefore tend to lock onto zero crossings in the image. The level set
    front moves fastest near edges.

    The Laplacian segmentation filter is intended primarily as a tool for
    refining existing segmentations. The initial isosurface (as given in
    the seed input image) should ideally be very close to the segmentation
    boundary of interest. The idea is that a rough segmentation can be
    refined by allowing the isosurface to deform slightly to achieve a
    better is to refine the output of a hand segmented image.

    Because values in the Laplacian feature image will tend to be low
    except near edge features, this filter is not effective for segmenting
    large image regions from small seed surfaces. INPUTS This filter
    requires two inputs. The first input is a seed image. This seed image
    must contain an isosurface that you want to use as the seed for your
    segmentation. It can be a binary, graylevel, or floating point image.
    The only requirement is that it contain a closed isosurface that you
    will identify as the seed by setting the IsosurfaceValue parameter of
    the filter. For a binary image you will want to set your isosurface
    value halfway between your on and off values (i.e. for 0's and 1's,
    use an isosurface value of 0.5).

    The second input is the feature image. This is the image from which
    the speed function will be calculated. For most applications, this is
    the image that you want to segment. The desired isosurface in your
    seed image should lie within the region of your feature image that you
    are trying to segment.  Note that this filter does no preprocessing of
    the feature image before thresholding. Because second derivative
    calculations are highly sensitive to noise, isotropic or anisotropic
    smoothing of the feature image can dramatically improve the results.

    See SegmentationLevelSetImageFilter for more information on Inputs.
    OUTPUTS The filter outputs a single, scalar, real-valued image.
    Positive *values in the output image are inside the segmented region
    and negative *values in the image are outside of the inside region.
    The zero crossings of *the image correspond to the position of the
    level set front.

    See SparseFieldLevelSetImageFilter and SegmentationLevelSetImageFilter
    for more information. PARAMETERS This filter has no parameters other
    than those described in SegmentationLevelSetImageFilter.

    See:   SegmentationLevelSetImageFilter

    See:  LaplacianSegmentationLevelSetFunction,

    See:   SparseFieldLevelSetImageFilter

    C++ includes: itkLaplacianSegmentationLevelSetImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLaplacianSegmentationLevelSetImageFilterID2ID2D_Pointer":
        """__New_orig__() -> itkLaplacianSegmentationLevelSetImageFilterID2ID2D_Pointer"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterID2ID2D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLaplacianSegmentationLevelSetImageFilterID2ID2D_Pointer":
        """Clone(itkLaplacianSegmentationLevelSetImageFilterID2ID2D self) -> itkLaplacianSegmentationLevelSetImageFilterID2ID2D_Pointer"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterID2ID2D_Clone(self)

    __swig_destroy__ = _itkLaplacianSegmentationLevelSetImageFilterPython.delete_itkLaplacianSegmentationLevelSetImageFilterID2ID2D

    def cast(obj: 'itkLightObject') -> "itkLaplacianSegmentationLevelSetImageFilterID2ID2D *":
        """cast(itkLightObject obj) -> itkLaplacianSegmentationLevelSetImageFilterID2ID2D"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterID2ID2D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLaplacianSegmentationLevelSetImageFilterID2ID2D

        Create a new object of the class itkLaplacianSegmentationLevelSetImageFilterID2ID2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianSegmentationLevelSetImageFilterID2ID2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLaplacianSegmentationLevelSetImageFilterID2ID2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLaplacianSegmentationLevelSetImageFilterID2ID2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLaplacianSegmentationLevelSetImageFilterID2ID2D.Clone = new_instancemethod(_itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterID2ID2D_Clone, None, itkLaplacianSegmentationLevelSetImageFilterID2ID2D)
itkLaplacianSegmentationLevelSetImageFilterID2ID2D_swigregister = _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterID2ID2D_swigregister
itkLaplacianSegmentationLevelSetImageFilterID2ID2D_swigregister(itkLaplacianSegmentationLevelSetImageFilterID2ID2D)

def itkLaplacianSegmentationLevelSetImageFilterID2ID2D___New_orig__() -> "itkLaplacianSegmentationLevelSetImageFilterID2ID2D_Pointer":
    """itkLaplacianSegmentationLevelSetImageFilterID2ID2D___New_orig__() -> itkLaplacianSegmentationLevelSetImageFilterID2ID2D_Pointer"""
    return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterID2ID2D___New_orig__()

def itkLaplacianSegmentationLevelSetImageFilterID2ID2D_cast(obj: 'itkLightObject') -> "itkLaplacianSegmentationLevelSetImageFilterID2ID2D *":
    """itkLaplacianSegmentationLevelSetImageFilterID2ID2D_cast(itkLightObject obj) -> itkLaplacianSegmentationLevelSetImageFilterID2ID2D"""
    return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterID2ID2D_cast(obj)

class itkLaplacianSegmentationLevelSetImageFilterID3ID3D(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterID3ID3D):
    """


    Segments structures in images based on a second derivative image
    features.

    IMPORTANT The SegmentationLevelSetImageFilter class and the
    LaplacianSegmentationLevelSetFunction class contain additional
    information necessary to the full understanding of how to use this
    filter. OVERVIEW This class is a level set method segmentation filter.
    It constructs a speed function which is zero at image edges as
    detected by a Laplacian filter. The evolving level set front will
    therefore tend to lock onto zero crossings in the image. The level set
    front moves fastest near edges.

    The Laplacian segmentation filter is intended primarily as a tool for
    refining existing segmentations. The initial isosurface (as given in
    the seed input image) should ideally be very close to the segmentation
    boundary of interest. The idea is that a rough segmentation can be
    refined by allowing the isosurface to deform slightly to achieve a
    better is to refine the output of a hand segmented image.

    Because values in the Laplacian feature image will tend to be low
    except near edge features, this filter is not effective for segmenting
    large image regions from small seed surfaces. INPUTS This filter
    requires two inputs. The first input is a seed image. This seed image
    must contain an isosurface that you want to use as the seed for your
    segmentation. It can be a binary, graylevel, or floating point image.
    The only requirement is that it contain a closed isosurface that you
    will identify as the seed by setting the IsosurfaceValue parameter of
    the filter. For a binary image you will want to set your isosurface
    value halfway between your on and off values (i.e. for 0's and 1's,
    use an isosurface value of 0.5).

    The second input is the feature image. This is the image from which
    the speed function will be calculated. For most applications, this is
    the image that you want to segment. The desired isosurface in your
    seed image should lie within the region of your feature image that you
    are trying to segment.  Note that this filter does no preprocessing of
    the feature image before thresholding. Because second derivative
    calculations are highly sensitive to noise, isotropic or anisotropic
    smoothing of the feature image can dramatically improve the results.

    See SegmentationLevelSetImageFilter for more information on Inputs.
    OUTPUTS The filter outputs a single, scalar, real-valued image.
    Positive *values in the output image are inside the segmented region
    and negative *values in the image are outside of the inside region.
    The zero crossings of *the image correspond to the position of the
    level set front.

    See SparseFieldLevelSetImageFilter and SegmentationLevelSetImageFilter
    for more information. PARAMETERS This filter has no parameters other
    than those described in SegmentationLevelSetImageFilter.

    See:   SegmentationLevelSetImageFilter

    See:  LaplacianSegmentationLevelSetFunction,

    See:   SparseFieldLevelSetImageFilter

    C++ includes: itkLaplacianSegmentationLevelSetImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLaplacianSegmentationLevelSetImageFilterID3ID3D_Pointer":
        """__New_orig__() -> itkLaplacianSegmentationLevelSetImageFilterID3ID3D_Pointer"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterID3ID3D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLaplacianSegmentationLevelSetImageFilterID3ID3D_Pointer":
        """Clone(itkLaplacianSegmentationLevelSetImageFilterID3ID3D self) -> itkLaplacianSegmentationLevelSetImageFilterID3ID3D_Pointer"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterID3ID3D_Clone(self)

    __swig_destroy__ = _itkLaplacianSegmentationLevelSetImageFilterPython.delete_itkLaplacianSegmentationLevelSetImageFilterID3ID3D

    def cast(obj: 'itkLightObject') -> "itkLaplacianSegmentationLevelSetImageFilterID3ID3D *":
        """cast(itkLightObject obj) -> itkLaplacianSegmentationLevelSetImageFilterID3ID3D"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterID3ID3D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLaplacianSegmentationLevelSetImageFilterID3ID3D

        Create a new object of the class itkLaplacianSegmentationLevelSetImageFilterID3ID3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianSegmentationLevelSetImageFilterID3ID3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLaplacianSegmentationLevelSetImageFilterID3ID3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLaplacianSegmentationLevelSetImageFilterID3ID3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLaplacianSegmentationLevelSetImageFilterID3ID3D.Clone = new_instancemethod(_itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterID3ID3D_Clone, None, itkLaplacianSegmentationLevelSetImageFilterID3ID3D)
itkLaplacianSegmentationLevelSetImageFilterID3ID3D_swigregister = _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterID3ID3D_swigregister
itkLaplacianSegmentationLevelSetImageFilterID3ID3D_swigregister(itkLaplacianSegmentationLevelSetImageFilterID3ID3D)

def itkLaplacianSegmentationLevelSetImageFilterID3ID3D___New_orig__() -> "itkLaplacianSegmentationLevelSetImageFilterID3ID3D_Pointer":
    """itkLaplacianSegmentationLevelSetImageFilterID3ID3D___New_orig__() -> itkLaplacianSegmentationLevelSetImageFilterID3ID3D_Pointer"""
    return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterID3ID3D___New_orig__()

def itkLaplacianSegmentationLevelSetImageFilterID3ID3D_cast(obj: 'itkLightObject') -> "itkLaplacianSegmentationLevelSetImageFilterID3ID3D *":
    """itkLaplacianSegmentationLevelSetImageFilterID3ID3D_cast(itkLightObject obj) -> itkLaplacianSegmentationLevelSetImageFilterID3ID3D"""
    return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterID3ID3D_cast(obj)

class itkLaplacianSegmentationLevelSetImageFilterIF2IF2F(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF2IF2F):
    """


    Segments structures in images based on a second derivative image
    features.

    IMPORTANT The SegmentationLevelSetImageFilter class and the
    LaplacianSegmentationLevelSetFunction class contain additional
    information necessary to the full understanding of how to use this
    filter. OVERVIEW This class is a level set method segmentation filter.
    It constructs a speed function which is zero at image edges as
    detected by a Laplacian filter. The evolving level set front will
    therefore tend to lock onto zero crossings in the image. The level set
    front moves fastest near edges.

    The Laplacian segmentation filter is intended primarily as a tool for
    refining existing segmentations. The initial isosurface (as given in
    the seed input image) should ideally be very close to the segmentation
    boundary of interest. The idea is that a rough segmentation can be
    refined by allowing the isosurface to deform slightly to achieve a
    better is to refine the output of a hand segmented image.

    Because values in the Laplacian feature image will tend to be low
    except near edge features, this filter is not effective for segmenting
    large image regions from small seed surfaces. INPUTS This filter
    requires two inputs. The first input is a seed image. This seed image
    must contain an isosurface that you want to use as the seed for your
    segmentation. It can be a binary, graylevel, or floating point image.
    The only requirement is that it contain a closed isosurface that you
    will identify as the seed by setting the IsosurfaceValue parameter of
    the filter. For a binary image you will want to set your isosurface
    value halfway between your on and off values (i.e. for 0's and 1's,
    use an isosurface value of 0.5).

    The second input is the feature image. This is the image from which
    the speed function will be calculated. For most applications, this is
    the image that you want to segment. The desired isosurface in your
    seed image should lie within the region of your feature image that you
    are trying to segment.  Note that this filter does no preprocessing of
    the feature image before thresholding. Because second derivative
    calculations are highly sensitive to noise, isotropic or anisotropic
    smoothing of the feature image can dramatically improve the results.

    See SegmentationLevelSetImageFilter for more information on Inputs.
    OUTPUTS The filter outputs a single, scalar, real-valued image.
    Positive *values in the output image are inside the segmented region
    and negative *values in the image are outside of the inside region.
    The zero crossings of *the image correspond to the position of the
    level set front.

    See SparseFieldLevelSetImageFilter and SegmentationLevelSetImageFilter
    for more information. PARAMETERS This filter has no parameters other
    than those described in SegmentationLevelSetImageFilter.

    See:   SegmentationLevelSetImageFilter

    See:  LaplacianSegmentationLevelSetFunction,

    See:   SparseFieldLevelSetImageFilter

    C++ includes: itkLaplacianSegmentationLevelSetImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_Pointer":
        """__New_orig__() -> itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_Pointer"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF2IF2F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_Pointer":
        """Clone(itkLaplacianSegmentationLevelSetImageFilterIF2IF2F self) -> itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_Pointer"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_Clone(self)

    __swig_destroy__ = _itkLaplacianSegmentationLevelSetImageFilterPython.delete_itkLaplacianSegmentationLevelSetImageFilterIF2IF2F

    def cast(obj: 'itkLightObject') -> "itkLaplacianSegmentationLevelSetImageFilterIF2IF2F *":
        """cast(itkLightObject obj) -> itkLaplacianSegmentationLevelSetImageFilterIF2IF2F"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLaplacianSegmentationLevelSetImageFilterIF2IF2F

        Create a new object of the class itkLaplacianSegmentationLevelSetImageFilterIF2IF2F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianSegmentationLevelSetImageFilterIF2IF2F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLaplacianSegmentationLevelSetImageFilterIF2IF2F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLaplacianSegmentationLevelSetImageFilterIF2IF2F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLaplacianSegmentationLevelSetImageFilterIF2IF2F.Clone = new_instancemethod(_itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_Clone, None, itkLaplacianSegmentationLevelSetImageFilterIF2IF2F)
itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_swigregister = _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_swigregister
itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_swigregister(itkLaplacianSegmentationLevelSetImageFilterIF2IF2F)

def itkLaplacianSegmentationLevelSetImageFilterIF2IF2F___New_orig__() -> "itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_Pointer":
    """itkLaplacianSegmentationLevelSetImageFilterIF2IF2F___New_orig__() -> itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_Pointer"""
    return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF2IF2F___New_orig__()

def itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_cast(obj: 'itkLightObject') -> "itkLaplacianSegmentationLevelSetImageFilterIF2IF2F *":
    """itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_cast(itkLightObject obj) -> itkLaplacianSegmentationLevelSetImageFilterIF2IF2F"""
    return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF2IF2F_cast(obj)

class itkLaplacianSegmentationLevelSetImageFilterIF3IF3F(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF3IF3F):
    """


    Segments structures in images based on a second derivative image
    features.

    IMPORTANT The SegmentationLevelSetImageFilter class and the
    LaplacianSegmentationLevelSetFunction class contain additional
    information necessary to the full understanding of how to use this
    filter. OVERVIEW This class is a level set method segmentation filter.
    It constructs a speed function which is zero at image edges as
    detected by a Laplacian filter. The evolving level set front will
    therefore tend to lock onto zero crossings in the image. The level set
    front moves fastest near edges.

    The Laplacian segmentation filter is intended primarily as a tool for
    refining existing segmentations. The initial isosurface (as given in
    the seed input image) should ideally be very close to the segmentation
    boundary of interest. The idea is that a rough segmentation can be
    refined by allowing the isosurface to deform slightly to achieve a
    better is to refine the output of a hand segmented image.

    Because values in the Laplacian feature image will tend to be low
    except near edge features, this filter is not effective for segmenting
    large image regions from small seed surfaces. INPUTS This filter
    requires two inputs. The first input is a seed image. This seed image
    must contain an isosurface that you want to use as the seed for your
    segmentation. It can be a binary, graylevel, or floating point image.
    The only requirement is that it contain a closed isosurface that you
    will identify as the seed by setting the IsosurfaceValue parameter of
    the filter. For a binary image you will want to set your isosurface
    value halfway between your on and off values (i.e. for 0's and 1's,
    use an isosurface value of 0.5).

    The second input is the feature image. This is the image from which
    the speed function will be calculated. For most applications, this is
    the image that you want to segment. The desired isosurface in your
    seed image should lie within the region of your feature image that you
    are trying to segment.  Note that this filter does no preprocessing of
    the feature image before thresholding. Because second derivative
    calculations are highly sensitive to noise, isotropic or anisotropic
    smoothing of the feature image can dramatically improve the results.

    See SegmentationLevelSetImageFilter for more information on Inputs.
    OUTPUTS The filter outputs a single, scalar, real-valued image.
    Positive *values in the output image are inside the segmented region
    and negative *values in the image are outside of the inside region.
    The zero crossings of *the image correspond to the position of the
    level set front.

    See SparseFieldLevelSetImageFilter and SegmentationLevelSetImageFilter
    for more information. PARAMETERS This filter has no parameters other
    than those described in SegmentationLevelSetImageFilter.

    See:   SegmentationLevelSetImageFilter

    See:  LaplacianSegmentationLevelSetFunction,

    See:   SparseFieldLevelSetImageFilter

    C++ includes: itkLaplacianSegmentationLevelSetImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_Pointer":
        """__New_orig__() -> itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_Pointer"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF3IF3F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_Pointer":
        """Clone(itkLaplacianSegmentationLevelSetImageFilterIF3IF3F self) -> itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_Pointer"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_Clone(self)

    __swig_destroy__ = _itkLaplacianSegmentationLevelSetImageFilterPython.delete_itkLaplacianSegmentationLevelSetImageFilterIF3IF3F

    def cast(obj: 'itkLightObject') -> "itkLaplacianSegmentationLevelSetImageFilterIF3IF3F *":
        """cast(itkLightObject obj) -> itkLaplacianSegmentationLevelSetImageFilterIF3IF3F"""
        return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLaplacianSegmentationLevelSetImageFilterIF3IF3F

        Create a new object of the class itkLaplacianSegmentationLevelSetImageFilterIF3IF3F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianSegmentationLevelSetImageFilterIF3IF3F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLaplacianSegmentationLevelSetImageFilterIF3IF3F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLaplacianSegmentationLevelSetImageFilterIF3IF3F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLaplacianSegmentationLevelSetImageFilterIF3IF3F.Clone = new_instancemethod(_itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_Clone, None, itkLaplacianSegmentationLevelSetImageFilterIF3IF3F)
itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_swigregister = _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_swigregister
itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_swigregister(itkLaplacianSegmentationLevelSetImageFilterIF3IF3F)

def itkLaplacianSegmentationLevelSetImageFilterIF3IF3F___New_orig__() -> "itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_Pointer":
    """itkLaplacianSegmentationLevelSetImageFilterIF3IF3F___New_orig__() -> itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_Pointer"""
    return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF3IF3F___New_orig__()

def itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_cast(obj: 'itkLightObject') -> "itkLaplacianSegmentationLevelSetImageFilterIF3IF3F *":
    """itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_cast(itkLightObject obj) -> itkLaplacianSegmentationLevelSetImageFilterIF3IF3F"""
    return _itkLaplacianSegmentationLevelSetImageFilterPython.itkLaplacianSegmentationLevelSetImageFilterIF3IF3F_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def laplacian_segmentation_level_set_image_filter(*args, **kwargs):
    """Procedural interface for LaplacianSegmentationLevelSetImageFilter"""
    import itk
    instance = itk.LaplacianSegmentationLevelSetImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def laplacian_segmentation_level_set_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.LaplacianSegmentationLevelSetImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.LaplacianSegmentationLevelSetImageFilter.values()[0]
    else:
        filter_object = itk.LaplacianSegmentationLevelSetImageFilter

    laplacian_segmentation_level_set_image_filter.__doc__ = filter_object.__doc__
    laplacian_segmentation_level_set_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    laplacian_segmentation_level_set_image_filter.__doc__ += "Available Keyword Arguments:\n"
    laplacian_segmentation_level_set_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



