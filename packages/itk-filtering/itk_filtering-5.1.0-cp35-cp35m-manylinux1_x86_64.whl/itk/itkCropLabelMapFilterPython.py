# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkCropLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkCropLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkCropLabelMapFilterPython
            return _itkCropLabelMapFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkCropLabelMapFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkCropLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkCropLabelMapFilterPython
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


import itkChangeRegionLabelMapFilterPython
import ITKCommonBasePython
import pyBasePython
import itkStatisticsLabelObjectPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkAffineTransformPython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkDiffusionTensor3DPython
import itkVariableLengthVectorPython
import itkArrayPython
import itkArray2DPython
import itkOptimizerParametersPython
import itkMatrixOffsetTransformBasePython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkImageRegionPython
import itkHistogramPython
import itkSamplePython
import itkInPlaceLabelMapFilterPython
import ITKLabelMapBasePython
import itkImageToImageFilterCommonPython
import itkImageSourceCommonPython
import itkImagePython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageSourcePython
import itkVectorImagePython
import itkLabelMapFilterPython

def itkCropLabelMapFilterLM3_New():
  return itkCropLabelMapFilterLM3.New()


def itkCropLabelMapFilterLM2_New():
  return itkCropLabelMapFilterLM2.New()

class itkCropLabelMapFilterLM2(itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2):
    """


    Crop a LabelMap image.

    Crop a label map. If the output cannot contain some lines of the
    objects, they are truncated or removed. All objects fully outside the
    output region are removed.

    The SetCropSize() method can be used to set the crop size of the lower
    and the upper boundaries in a single call. By default, the filter does
    not crop anything.

    This implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/584 orhttp://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   PadLabelMapFilter

    C++ includes: itkCropLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCropLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkCropLabelMapFilterLM2_Pointer"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCropLabelMapFilterLM2_Pointer":
        """Clone(itkCropLabelMapFilterLM2 self) -> itkCropLabelMapFilterLM2_Pointer"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_Clone(self)


    def SetUpperBoundaryCropSize(self, _arg: 'itkSize2') -> "void":
        """
        SetUpperBoundaryCropSize(itkCropLabelMapFilterLM2 self, itkSize2 _arg)

        Set/Get
        the cropping sizes for the upper and lower boundaries. 
        """
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_SetUpperBoundaryCropSize(self, _arg)


    def GetUpperBoundaryCropSize(self) -> "itkSize2":
        """GetUpperBoundaryCropSize(itkCropLabelMapFilterLM2 self) -> itkSize2"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_GetUpperBoundaryCropSize(self)


    def SetLowerBoundaryCropSize(self, _arg: 'itkSize2') -> "void":
        """SetLowerBoundaryCropSize(itkCropLabelMapFilterLM2 self, itkSize2 _arg)"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_SetLowerBoundaryCropSize(self, _arg)


    def GetLowerBoundaryCropSize(self) -> "itkSize2":
        """GetLowerBoundaryCropSize(itkCropLabelMapFilterLM2 self) -> itkSize2"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_GetLowerBoundaryCropSize(self)


    def SetCropSize(self, size: 'itkSize2') -> "void":
        """SetCropSize(itkCropLabelMapFilterLM2 self, itkSize2 size)"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_SetCropSize(self, size)

    __swig_destroy__ = _itkCropLabelMapFilterPython.delete_itkCropLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkCropLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkCropLabelMapFilterLM2"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkCropLabelMapFilterLM2

        Create a new object of the class itkCropLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCropLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCropLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCropLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCropLabelMapFilterLM2.Clone = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_Clone, None, itkCropLabelMapFilterLM2)
itkCropLabelMapFilterLM2.SetUpperBoundaryCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_SetUpperBoundaryCropSize, None, itkCropLabelMapFilterLM2)
itkCropLabelMapFilterLM2.GetUpperBoundaryCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_GetUpperBoundaryCropSize, None, itkCropLabelMapFilterLM2)
itkCropLabelMapFilterLM2.SetLowerBoundaryCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_SetLowerBoundaryCropSize, None, itkCropLabelMapFilterLM2)
itkCropLabelMapFilterLM2.GetLowerBoundaryCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_GetLowerBoundaryCropSize, None, itkCropLabelMapFilterLM2)
itkCropLabelMapFilterLM2.SetCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_SetCropSize, None, itkCropLabelMapFilterLM2)
itkCropLabelMapFilterLM2_swigregister = _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_swigregister
itkCropLabelMapFilterLM2_swigregister(itkCropLabelMapFilterLM2)

def itkCropLabelMapFilterLM2___New_orig__() -> "itkCropLabelMapFilterLM2_Pointer":
    """itkCropLabelMapFilterLM2___New_orig__() -> itkCropLabelMapFilterLM2_Pointer"""
    return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2___New_orig__()

def itkCropLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkCropLabelMapFilterLM2 *":
    """itkCropLabelMapFilterLM2_cast(itkLightObject obj) -> itkCropLabelMapFilterLM2"""
    return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM2_cast(obj)

class itkCropLabelMapFilterLM3(itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3):
    """


    Crop a LabelMap image.

    Crop a label map. If the output cannot contain some lines of the
    objects, they are truncated or removed. All objects fully outside the
    output region are removed.

    The SetCropSize() method can be used to set the crop size of the lower
    and the upper boundaries in a single call. By default, the filter does
    not crop anything.

    This implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/584 orhttp://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   PadLabelMapFilter

    C++ includes: itkCropLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCropLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkCropLabelMapFilterLM3_Pointer"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCropLabelMapFilterLM3_Pointer":
        """Clone(itkCropLabelMapFilterLM3 self) -> itkCropLabelMapFilterLM3_Pointer"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_Clone(self)


    def SetUpperBoundaryCropSize(self, _arg: 'itkSize3') -> "void":
        """
        SetUpperBoundaryCropSize(itkCropLabelMapFilterLM3 self, itkSize3 _arg)

        Set/Get
        the cropping sizes for the upper and lower boundaries. 
        """
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_SetUpperBoundaryCropSize(self, _arg)


    def GetUpperBoundaryCropSize(self) -> "itkSize3":
        """GetUpperBoundaryCropSize(itkCropLabelMapFilterLM3 self) -> itkSize3"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_GetUpperBoundaryCropSize(self)


    def SetLowerBoundaryCropSize(self, _arg: 'itkSize3') -> "void":
        """SetLowerBoundaryCropSize(itkCropLabelMapFilterLM3 self, itkSize3 _arg)"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_SetLowerBoundaryCropSize(self, _arg)


    def GetLowerBoundaryCropSize(self) -> "itkSize3":
        """GetLowerBoundaryCropSize(itkCropLabelMapFilterLM3 self) -> itkSize3"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_GetLowerBoundaryCropSize(self)


    def SetCropSize(self, size: 'itkSize3') -> "void":
        """SetCropSize(itkCropLabelMapFilterLM3 self, itkSize3 size)"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_SetCropSize(self, size)

    __swig_destroy__ = _itkCropLabelMapFilterPython.delete_itkCropLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkCropLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkCropLabelMapFilterLM3"""
        return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkCropLabelMapFilterLM3

        Create a new object of the class itkCropLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCropLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCropLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCropLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCropLabelMapFilterLM3.Clone = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_Clone, None, itkCropLabelMapFilterLM3)
itkCropLabelMapFilterLM3.SetUpperBoundaryCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_SetUpperBoundaryCropSize, None, itkCropLabelMapFilterLM3)
itkCropLabelMapFilterLM3.GetUpperBoundaryCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_GetUpperBoundaryCropSize, None, itkCropLabelMapFilterLM3)
itkCropLabelMapFilterLM3.SetLowerBoundaryCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_SetLowerBoundaryCropSize, None, itkCropLabelMapFilterLM3)
itkCropLabelMapFilterLM3.GetLowerBoundaryCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_GetLowerBoundaryCropSize, None, itkCropLabelMapFilterLM3)
itkCropLabelMapFilterLM3.SetCropSize = new_instancemethod(_itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_SetCropSize, None, itkCropLabelMapFilterLM3)
itkCropLabelMapFilterLM3_swigregister = _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_swigregister
itkCropLabelMapFilterLM3_swigregister(itkCropLabelMapFilterLM3)

def itkCropLabelMapFilterLM3___New_orig__() -> "itkCropLabelMapFilterLM3_Pointer":
    """itkCropLabelMapFilterLM3___New_orig__() -> itkCropLabelMapFilterLM3_Pointer"""
    return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3___New_orig__()

def itkCropLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkCropLabelMapFilterLM3 *":
    """itkCropLabelMapFilterLM3_cast(itkLightObject obj) -> itkCropLabelMapFilterLM3"""
    return _itkCropLabelMapFilterPython.itkCropLabelMapFilterLM3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def crop_label_map_filter(*args, **kwargs):
    """Procedural interface for CropLabelMapFilter"""
    import itk
    instance = itk.CropLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def crop_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.CropLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.CropLabelMapFilter.values()[0]
    else:
        filter_object = itk.CropLabelMapFilter

    crop_label_map_filter.__doc__ = filter_object.__doc__
    crop_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    crop_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    crop_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



