# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLabelMapToRGBImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLabelMapToRGBImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkLabelMapToRGBImageFilterPython
            return _itkLabelMapToRGBImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkLabelMapToRGBImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkLabelMapToRGBImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLabelMapToRGBImageFilterPython
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


import itkLabelMapFilterPython
import ITKCommonBasePython
import pyBasePython
import itkImageRegionPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
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

def itkLabelMapToRGBImageFilterLM3IRGBUC3_New():
  return itkLabelMapToRGBImageFilterLM3IRGBUC3.New()


def itkLabelMapToRGBImageFilterLM2IRGBUC2_New():
  return itkLabelMapToRGBImageFilterLM2IRGBUC2.New()

class itkLabelMapToRGBImageFilterLM2IRGBUC2(itkLabelMapFilterPython.itkLabelMapFilterLM2IRGBUC2):
    """


    Convert a LabelMap to a colored image.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://hdl.handle.net/1926/584
    orhttp://www.insight-journal.org/browse/publication/176

    See:   LabelToRGBImageFilter, LabelToRGBFunctor

    See:   LabelMapOverlayImageFilter, LabelMapToBinaryImageFilter,
    LabelMapMaskImageFilter

    C++ includes: itkLabelMapToRGBImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelMapToRGBImageFilterLM2IRGBUC2_Pointer":
        """__New_orig__() -> itkLabelMapToRGBImageFilterLM2IRGBUC2_Pointer"""
        return _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelMapToRGBImageFilterLM2IRGBUC2_Pointer":
        """Clone(itkLabelMapToRGBImageFilterLM2IRGBUC2 self) -> itkLabelMapToRGBImageFilterLM2IRGBUC2_Pointer"""
        return _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_Clone(self)


    def SetFunctor(self, functor: 'itk::Functor::LabelToRGBFunctor< unsigned long,itk::RGBPixel< unsigned char > > const &') -> "void":
        """
        SetFunctor(itkLabelMapToRGBImageFilterLM2IRGBUC2 self, itk::Functor::LabelToRGBFunctor< unsigned long,itk::RGBPixel< unsigned char > > const & functor)

        Set/Get the rgb functor
        - defaults to a reasonable set of colors. This can be used to apply a
        different colormap. 
        """
        return _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_SetFunctor(self, functor)


    def GetFunctor(self, *args) -> "itk::Functor::LabelToRGBFunctor< unsigned long,itk::RGBPixel< unsigned char > > const &":
        """
        GetFunctor(itkLabelMapToRGBImageFilterLM2IRGBUC2 self) -> itk::Functor::LabelToRGBFunctor< unsigned long,itk::RGBPixel< unsigned char > >
        GetFunctor(itkLabelMapToRGBImageFilterLM2IRGBUC2 self) -> itk::Functor::LabelToRGBFunctor< unsigned long,itk::RGBPixel< unsigned char > > const &
        """
        return _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_GetFunctor(self, *args)

    __swig_destroy__ = _itkLabelMapToRGBImageFilterPython.delete_itkLabelMapToRGBImageFilterLM2IRGBUC2

    def cast(obj: 'itkLightObject') -> "itkLabelMapToRGBImageFilterLM2IRGBUC2 *":
        """cast(itkLightObject obj) -> itkLabelMapToRGBImageFilterLM2IRGBUC2"""
        return _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToRGBImageFilterLM2IRGBUC2

        Create a new object of the class itkLabelMapToRGBImageFilterLM2IRGBUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToRGBImageFilterLM2IRGBUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapToRGBImageFilterLM2IRGBUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapToRGBImageFilterLM2IRGBUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelMapToRGBImageFilterLM2IRGBUC2.Clone = new_instancemethod(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_Clone, None, itkLabelMapToRGBImageFilterLM2IRGBUC2)
itkLabelMapToRGBImageFilterLM2IRGBUC2.SetFunctor = new_instancemethod(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_SetFunctor, None, itkLabelMapToRGBImageFilterLM2IRGBUC2)
itkLabelMapToRGBImageFilterLM2IRGBUC2.GetFunctor = new_instancemethod(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_GetFunctor, None, itkLabelMapToRGBImageFilterLM2IRGBUC2)
itkLabelMapToRGBImageFilterLM2IRGBUC2_swigregister = _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_swigregister
itkLabelMapToRGBImageFilterLM2IRGBUC2_swigregister(itkLabelMapToRGBImageFilterLM2IRGBUC2)

def itkLabelMapToRGBImageFilterLM2IRGBUC2___New_orig__() -> "itkLabelMapToRGBImageFilterLM2IRGBUC2_Pointer":
    """itkLabelMapToRGBImageFilterLM2IRGBUC2___New_orig__() -> itkLabelMapToRGBImageFilterLM2IRGBUC2_Pointer"""
    return _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2___New_orig__()

def itkLabelMapToRGBImageFilterLM2IRGBUC2_cast(obj: 'itkLightObject') -> "itkLabelMapToRGBImageFilterLM2IRGBUC2 *":
    """itkLabelMapToRGBImageFilterLM2IRGBUC2_cast(itkLightObject obj) -> itkLabelMapToRGBImageFilterLM2IRGBUC2"""
    return _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_cast(obj)

class itkLabelMapToRGBImageFilterLM3IRGBUC3(itkLabelMapFilterPython.itkLabelMapFilterLM3IRGBUC3):
    """


    Convert a LabelMap to a colored image.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://hdl.handle.net/1926/584
    orhttp://www.insight-journal.org/browse/publication/176

    See:   LabelToRGBImageFilter, LabelToRGBFunctor

    See:   LabelMapOverlayImageFilter, LabelMapToBinaryImageFilter,
    LabelMapMaskImageFilter

    C++ includes: itkLabelMapToRGBImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelMapToRGBImageFilterLM3IRGBUC3_Pointer":
        """__New_orig__() -> itkLabelMapToRGBImageFilterLM3IRGBUC3_Pointer"""
        return _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelMapToRGBImageFilterLM3IRGBUC3_Pointer":
        """Clone(itkLabelMapToRGBImageFilterLM3IRGBUC3 self) -> itkLabelMapToRGBImageFilterLM3IRGBUC3_Pointer"""
        return _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_Clone(self)


    def SetFunctor(self, functor: 'itk::Functor::LabelToRGBFunctor< unsigned long,itk::RGBPixel< unsigned char > > const &') -> "void":
        """
        SetFunctor(itkLabelMapToRGBImageFilterLM3IRGBUC3 self, itk::Functor::LabelToRGBFunctor< unsigned long,itk::RGBPixel< unsigned char > > const & functor)

        Set/Get the rgb functor
        - defaults to a reasonable set of colors. This can be used to apply a
        different colormap. 
        """
        return _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_SetFunctor(self, functor)


    def GetFunctor(self, *args) -> "itk::Functor::LabelToRGBFunctor< unsigned long,itk::RGBPixel< unsigned char > > const &":
        """
        GetFunctor(itkLabelMapToRGBImageFilterLM3IRGBUC3 self) -> itk::Functor::LabelToRGBFunctor< unsigned long,itk::RGBPixel< unsigned char > >
        GetFunctor(itkLabelMapToRGBImageFilterLM3IRGBUC3 self) -> itk::Functor::LabelToRGBFunctor< unsigned long,itk::RGBPixel< unsigned char > > const &
        """
        return _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_GetFunctor(self, *args)

    __swig_destroy__ = _itkLabelMapToRGBImageFilterPython.delete_itkLabelMapToRGBImageFilterLM3IRGBUC3

    def cast(obj: 'itkLightObject') -> "itkLabelMapToRGBImageFilterLM3IRGBUC3 *":
        """cast(itkLightObject obj) -> itkLabelMapToRGBImageFilterLM3IRGBUC3"""
        return _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToRGBImageFilterLM3IRGBUC3

        Create a new object of the class itkLabelMapToRGBImageFilterLM3IRGBUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToRGBImageFilterLM3IRGBUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapToRGBImageFilterLM3IRGBUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapToRGBImageFilterLM3IRGBUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelMapToRGBImageFilterLM3IRGBUC3.Clone = new_instancemethod(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_Clone, None, itkLabelMapToRGBImageFilterLM3IRGBUC3)
itkLabelMapToRGBImageFilterLM3IRGBUC3.SetFunctor = new_instancemethod(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_SetFunctor, None, itkLabelMapToRGBImageFilterLM3IRGBUC3)
itkLabelMapToRGBImageFilterLM3IRGBUC3.GetFunctor = new_instancemethod(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_GetFunctor, None, itkLabelMapToRGBImageFilterLM3IRGBUC3)
itkLabelMapToRGBImageFilterLM3IRGBUC3_swigregister = _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_swigregister
itkLabelMapToRGBImageFilterLM3IRGBUC3_swigregister(itkLabelMapToRGBImageFilterLM3IRGBUC3)

def itkLabelMapToRGBImageFilterLM3IRGBUC3___New_orig__() -> "itkLabelMapToRGBImageFilterLM3IRGBUC3_Pointer":
    """itkLabelMapToRGBImageFilterLM3IRGBUC3___New_orig__() -> itkLabelMapToRGBImageFilterLM3IRGBUC3_Pointer"""
    return _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3___New_orig__()

def itkLabelMapToRGBImageFilterLM3IRGBUC3_cast(obj: 'itkLightObject') -> "itkLabelMapToRGBImageFilterLM3IRGBUC3 *":
    """itkLabelMapToRGBImageFilterLM3IRGBUC3_cast(itkLightObject obj) -> itkLabelMapToRGBImageFilterLM3IRGBUC3"""
    return _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def label_map_to_rgb_image_filter(*args, **kwargs):
    """Procedural interface for LabelMapToRGBImageFilter"""
    import itk
    instance = itk.LabelMapToRGBImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def label_map_to_rgb_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.LabelMapToRGBImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.LabelMapToRGBImageFilter.values()[0]
    else:
        filter_object = itk.LabelMapToRGBImageFilter

    label_map_to_rgb_image_filter.__doc__ = filter_object.__doc__
    label_map_to_rgb_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    label_map_to_rgb_image_filter.__doc__ += "Available Keyword Arguments:\n"
    label_map_to_rgb_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



