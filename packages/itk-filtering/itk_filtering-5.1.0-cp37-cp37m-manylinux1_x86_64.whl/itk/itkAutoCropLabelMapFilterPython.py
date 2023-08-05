# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkAutoCropLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkAutoCropLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkAutoCropLabelMapFilterPython
            return _itkAutoCropLabelMapFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkAutoCropLabelMapFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkAutoCropLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkAutoCropLabelMapFilterPython
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
import itkChangeRegionLabelMapFilterPython
import itkInPlaceLabelMapFilterPython
import ITKLabelMapBasePython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkImageToImageFilterCommonPython
import itkImageRegionPython
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

def itkAutoCropLabelMapFilterLM3_New():
  return itkAutoCropLabelMapFilterLM3.New()


def itkAutoCropLabelMapFilterLM2_New():
  return itkAutoCropLabelMapFilterLM2.New()

class itkAutoCropLabelMapFilterLM2(itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2):
    """


    Crop a LabelMap image to fit exactly the objects in the LabelMap.

    The CropBorder can be used to add a border which will never be larger
    than the input image. To add a border of size independent of the input
    image, PadLabelMapFilter can be used.

    This implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/584 orhttp://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   PadLabelMapFilter

    C++ includes: itkAutoCropLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAutoCropLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkAutoCropLabelMapFilterLM2_Pointer"""
        return _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAutoCropLabelMapFilterLM2_Pointer":
        """Clone(itkAutoCropLabelMapFilterLM2 self) -> itkAutoCropLabelMapFilterLM2_Pointer"""
        return _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2_Clone(self)


    def SetCropBorder(self, _arg: 'itkSize2') -> "void":
        """
        SetCropBorder(itkAutoCropLabelMapFilterLM2 self, itkSize2 _arg)

        Set/Get the border
        added to the mask before the crop. The default is 0 on * all the axis.

        """
        return _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2_SetCropBorder(self, _arg)


    def GetCropBorder(self) -> "itkSize2 const &":
        """GetCropBorder(itkAutoCropLabelMapFilterLM2 self) -> itkSize2"""
        return _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2_GetCropBorder(self)

    __swig_destroy__ = _itkAutoCropLabelMapFilterPython.delete_itkAutoCropLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkAutoCropLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkAutoCropLabelMapFilterLM2"""
        return _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAutoCropLabelMapFilterLM2

        Create a new object of the class itkAutoCropLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAutoCropLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAutoCropLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAutoCropLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAutoCropLabelMapFilterLM2.Clone = new_instancemethod(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2_Clone, None, itkAutoCropLabelMapFilterLM2)
itkAutoCropLabelMapFilterLM2.SetCropBorder = new_instancemethod(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2_SetCropBorder, None, itkAutoCropLabelMapFilterLM2)
itkAutoCropLabelMapFilterLM2.GetCropBorder = new_instancemethod(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2_GetCropBorder, None, itkAutoCropLabelMapFilterLM2)
itkAutoCropLabelMapFilterLM2_swigregister = _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2_swigregister
itkAutoCropLabelMapFilterLM2_swigregister(itkAutoCropLabelMapFilterLM2)

def itkAutoCropLabelMapFilterLM2___New_orig__() -> "itkAutoCropLabelMapFilterLM2_Pointer":
    """itkAutoCropLabelMapFilterLM2___New_orig__() -> itkAutoCropLabelMapFilterLM2_Pointer"""
    return _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2___New_orig__()

def itkAutoCropLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkAutoCropLabelMapFilterLM2 *":
    """itkAutoCropLabelMapFilterLM2_cast(itkLightObject obj) -> itkAutoCropLabelMapFilterLM2"""
    return _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2_cast(obj)

class itkAutoCropLabelMapFilterLM3(itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3):
    """


    Crop a LabelMap image to fit exactly the objects in the LabelMap.

    The CropBorder can be used to add a border which will never be larger
    than the input image. To add a border of size independent of the input
    image, PadLabelMapFilter can be used.

    This implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/584 orhttp://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   PadLabelMapFilter

    C++ includes: itkAutoCropLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAutoCropLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkAutoCropLabelMapFilterLM3_Pointer"""
        return _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAutoCropLabelMapFilterLM3_Pointer":
        """Clone(itkAutoCropLabelMapFilterLM3 self) -> itkAutoCropLabelMapFilterLM3_Pointer"""
        return _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3_Clone(self)


    def SetCropBorder(self, _arg: 'itkSize3') -> "void":
        """
        SetCropBorder(itkAutoCropLabelMapFilterLM3 self, itkSize3 _arg)

        Set/Get the border
        added to the mask before the crop. The default is 0 on * all the axis.

        """
        return _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3_SetCropBorder(self, _arg)


    def GetCropBorder(self) -> "itkSize3 const &":
        """GetCropBorder(itkAutoCropLabelMapFilterLM3 self) -> itkSize3"""
        return _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3_GetCropBorder(self)

    __swig_destroy__ = _itkAutoCropLabelMapFilterPython.delete_itkAutoCropLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkAutoCropLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkAutoCropLabelMapFilterLM3"""
        return _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAutoCropLabelMapFilterLM3

        Create a new object of the class itkAutoCropLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAutoCropLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAutoCropLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAutoCropLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAutoCropLabelMapFilterLM3.Clone = new_instancemethod(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3_Clone, None, itkAutoCropLabelMapFilterLM3)
itkAutoCropLabelMapFilterLM3.SetCropBorder = new_instancemethod(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3_SetCropBorder, None, itkAutoCropLabelMapFilterLM3)
itkAutoCropLabelMapFilterLM3.GetCropBorder = new_instancemethod(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3_GetCropBorder, None, itkAutoCropLabelMapFilterLM3)
itkAutoCropLabelMapFilterLM3_swigregister = _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3_swigregister
itkAutoCropLabelMapFilterLM3_swigregister(itkAutoCropLabelMapFilterLM3)

def itkAutoCropLabelMapFilterLM3___New_orig__() -> "itkAutoCropLabelMapFilterLM3_Pointer":
    """itkAutoCropLabelMapFilterLM3___New_orig__() -> itkAutoCropLabelMapFilterLM3_Pointer"""
    return _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3___New_orig__()

def itkAutoCropLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkAutoCropLabelMapFilterLM3 *":
    """itkAutoCropLabelMapFilterLM3_cast(itkLightObject obj) -> itkAutoCropLabelMapFilterLM3"""
    return _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def auto_crop_label_map_filter(*args, **kwargs):
    """Procedural interface for AutoCropLabelMapFilter"""
    import itk
    instance = itk.AutoCropLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def auto_crop_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.AutoCropLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.AutoCropLabelMapFilter.values()[0]
    else:
        filter_object = itk.AutoCropLabelMapFilter

    auto_crop_label_map_filter.__doc__ = filter_object.__doc__
    auto_crop_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    auto_crop_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    auto_crop_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



