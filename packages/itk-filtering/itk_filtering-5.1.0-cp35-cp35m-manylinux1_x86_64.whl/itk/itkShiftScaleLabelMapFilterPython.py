# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkShiftScaleLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkShiftScaleLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkShiftScaleLabelMapFilterPython
            return _itkShiftScaleLabelMapFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkShiftScaleLabelMapFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkShiftScaleLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkShiftScaleLabelMapFilterPython
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


import itkInPlaceLabelMapFilterPython
import ITKLabelMapBasePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import itkImageToImageFilterCommonPython
import itkImageSourceCommonPython
import ITKCommonBasePython
import itkImagePython
import itkImageRegionPython
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
import itkLabelMapFilterPython

def itkShiftScaleLabelMapFilterLM3_New():
  return itkShiftScaleLabelMapFilterLM3.New()


def itkShiftScaleLabelMapFilterLM2_New():
  return itkShiftScaleLabelMapFilterLM2.New()

class itkShiftScaleLabelMapFilterLM2(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    """


    Shifts and scales a label map filter, giving the option to change the
    background value.

    This filter takes as input a label map and shift, scale and background
    values to produce, as output, a rescaled and shifted label map with,
    when applicable, a new background.

    This implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/584 orhttp://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, RelabelComponentImageFilter

    C++ includes: itkShiftScaleLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShiftScaleLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkShiftScaleLabelMapFilterLM2_Pointer"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShiftScaleLabelMapFilterLM2_Pointer":
        """Clone(itkShiftScaleLabelMapFilterLM2 self) -> itkShiftScaleLabelMapFilterLM2_Pointer"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_Clone(self)


    def SetShift(self, _arg: 'double const') -> "void":
        """SetShift(itkShiftScaleLabelMapFilterLM2 self, double const _arg)"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_SetShift(self, _arg)


    def GetShift(self) -> "double const &":
        """GetShift(itkShiftScaleLabelMapFilterLM2 self) -> double const &"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_GetShift(self)


    def SetScale(self, _arg: 'double const') -> "void":
        """SetScale(itkShiftScaleLabelMapFilterLM2 self, double const _arg)"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_SetScale(self, _arg)


    def GetScale(self) -> "double const &":
        """GetScale(itkShiftScaleLabelMapFilterLM2 self) -> double const &"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_GetScale(self)


    def SetChangeBackgroundValue(self, _arg: 'bool const') -> "void":
        """SetChangeBackgroundValue(itkShiftScaleLabelMapFilterLM2 self, bool const _arg)"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_SetChangeBackgroundValue(self, _arg)


    def GetChangeBackgroundValue(self) -> "bool":
        """GetChangeBackgroundValue(itkShiftScaleLabelMapFilterLM2 self) -> bool"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_GetChangeBackgroundValue(self)


    def ChangeBackgroundValueOn(self) -> "void":
        """ChangeBackgroundValueOn(itkShiftScaleLabelMapFilterLM2 self)"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_ChangeBackgroundValueOn(self)


    def ChangeBackgroundValueOff(self) -> "void":
        """ChangeBackgroundValueOff(itkShiftScaleLabelMapFilterLM2 self)"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_ChangeBackgroundValueOff(self)

    __swig_destroy__ = _itkShiftScaleLabelMapFilterPython.delete_itkShiftScaleLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkShiftScaleLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkShiftScaleLabelMapFilterLM2"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkShiftScaleLabelMapFilterLM2

        Create a new object of the class itkShiftScaleLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShiftScaleLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShiftScaleLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShiftScaleLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShiftScaleLabelMapFilterLM2.Clone = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_Clone, None, itkShiftScaleLabelMapFilterLM2)
itkShiftScaleLabelMapFilterLM2.SetShift = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_SetShift, None, itkShiftScaleLabelMapFilterLM2)
itkShiftScaleLabelMapFilterLM2.GetShift = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_GetShift, None, itkShiftScaleLabelMapFilterLM2)
itkShiftScaleLabelMapFilterLM2.SetScale = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_SetScale, None, itkShiftScaleLabelMapFilterLM2)
itkShiftScaleLabelMapFilterLM2.GetScale = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_GetScale, None, itkShiftScaleLabelMapFilterLM2)
itkShiftScaleLabelMapFilterLM2.SetChangeBackgroundValue = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_SetChangeBackgroundValue, None, itkShiftScaleLabelMapFilterLM2)
itkShiftScaleLabelMapFilterLM2.GetChangeBackgroundValue = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_GetChangeBackgroundValue, None, itkShiftScaleLabelMapFilterLM2)
itkShiftScaleLabelMapFilterLM2.ChangeBackgroundValueOn = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_ChangeBackgroundValueOn, None, itkShiftScaleLabelMapFilterLM2)
itkShiftScaleLabelMapFilterLM2.ChangeBackgroundValueOff = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_ChangeBackgroundValueOff, None, itkShiftScaleLabelMapFilterLM2)
itkShiftScaleLabelMapFilterLM2_swigregister = _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_swigregister
itkShiftScaleLabelMapFilterLM2_swigregister(itkShiftScaleLabelMapFilterLM2)

def itkShiftScaleLabelMapFilterLM2___New_orig__() -> "itkShiftScaleLabelMapFilterLM2_Pointer":
    """itkShiftScaleLabelMapFilterLM2___New_orig__() -> itkShiftScaleLabelMapFilterLM2_Pointer"""
    return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2___New_orig__()

def itkShiftScaleLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkShiftScaleLabelMapFilterLM2 *":
    """itkShiftScaleLabelMapFilterLM2_cast(itkLightObject obj) -> itkShiftScaleLabelMapFilterLM2"""
    return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM2_cast(obj)

class itkShiftScaleLabelMapFilterLM3(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    """


    Shifts and scales a label map filter, giving the option to change the
    background value.

    This filter takes as input a label map and shift, scale and background
    values to produce, as output, a rescaled and shifted label map with,
    when applicable, a new background.

    This implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/584 orhttp://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, RelabelComponentImageFilter

    C++ includes: itkShiftScaleLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShiftScaleLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkShiftScaleLabelMapFilterLM3_Pointer"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShiftScaleLabelMapFilterLM3_Pointer":
        """Clone(itkShiftScaleLabelMapFilterLM3 self) -> itkShiftScaleLabelMapFilterLM3_Pointer"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_Clone(self)


    def SetShift(self, _arg: 'double const') -> "void":
        """SetShift(itkShiftScaleLabelMapFilterLM3 self, double const _arg)"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_SetShift(self, _arg)


    def GetShift(self) -> "double const &":
        """GetShift(itkShiftScaleLabelMapFilterLM3 self) -> double const &"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_GetShift(self)


    def SetScale(self, _arg: 'double const') -> "void":
        """SetScale(itkShiftScaleLabelMapFilterLM3 self, double const _arg)"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_SetScale(self, _arg)


    def GetScale(self) -> "double const &":
        """GetScale(itkShiftScaleLabelMapFilterLM3 self) -> double const &"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_GetScale(self)


    def SetChangeBackgroundValue(self, _arg: 'bool const') -> "void":
        """SetChangeBackgroundValue(itkShiftScaleLabelMapFilterLM3 self, bool const _arg)"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_SetChangeBackgroundValue(self, _arg)


    def GetChangeBackgroundValue(self) -> "bool":
        """GetChangeBackgroundValue(itkShiftScaleLabelMapFilterLM3 self) -> bool"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_GetChangeBackgroundValue(self)


    def ChangeBackgroundValueOn(self) -> "void":
        """ChangeBackgroundValueOn(itkShiftScaleLabelMapFilterLM3 self)"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_ChangeBackgroundValueOn(self)


    def ChangeBackgroundValueOff(self) -> "void":
        """ChangeBackgroundValueOff(itkShiftScaleLabelMapFilterLM3 self)"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_ChangeBackgroundValueOff(self)

    __swig_destroy__ = _itkShiftScaleLabelMapFilterPython.delete_itkShiftScaleLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkShiftScaleLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkShiftScaleLabelMapFilterLM3"""
        return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkShiftScaleLabelMapFilterLM3

        Create a new object of the class itkShiftScaleLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShiftScaleLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShiftScaleLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShiftScaleLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShiftScaleLabelMapFilterLM3.Clone = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_Clone, None, itkShiftScaleLabelMapFilterLM3)
itkShiftScaleLabelMapFilterLM3.SetShift = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_SetShift, None, itkShiftScaleLabelMapFilterLM3)
itkShiftScaleLabelMapFilterLM3.GetShift = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_GetShift, None, itkShiftScaleLabelMapFilterLM3)
itkShiftScaleLabelMapFilterLM3.SetScale = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_SetScale, None, itkShiftScaleLabelMapFilterLM3)
itkShiftScaleLabelMapFilterLM3.GetScale = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_GetScale, None, itkShiftScaleLabelMapFilterLM3)
itkShiftScaleLabelMapFilterLM3.SetChangeBackgroundValue = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_SetChangeBackgroundValue, None, itkShiftScaleLabelMapFilterLM3)
itkShiftScaleLabelMapFilterLM3.GetChangeBackgroundValue = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_GetChangeBackgroundValue, None, itkShiftScaleLabelMapFilterLM3)
itkShiftScaleLabelMapFilterLM3.ChangeBackgroundValueOn = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_ChangeBackgroundValueOn, None, itkShiftScaleLabelMapFilterLM3)
itkShiftScaleLabelMapFilterLM3.ChangeBackgroundValueOff = new_instancemethod(_itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_ChangeBackgroundValueOff, None, itkShiftScaleLabelMapFilterLM3)
itkShiftScaleLabelMapFilterLM3_swigregister = _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_swigregister
itkShiftScaleLabelMapFilterLM3_swigregister(itkShiftScaleLabelMapFilterLM3)

def itkShiftScaleLabelMapFilterLM3___New_orig__() -> "itkShiftScaleLabelMapFilterLM3_Pointer":
    """itkShiftScaleLabelMapFilterLM3___New_orig__() -> itkShiftScaleLabelMapFilterLM3_Pointer"""
    return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3___New_orig__()

def itkShiftScaleLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkShiftScaleLabelMapFilterLM3 *":
    """itkShiftScaleLabelMapFilterLM3_cast(itkLightObject obj) -> itkShiftScaleLabelMapFilterLM3"""
    return _itkShiftScaleLabelMapFilterPython.itkShiftScaleLabelMapFilterLM3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def shift_scale_label_map_filter(*args, **kwargs):
    """Procedural interface for ShiftScaleLabelMapFilter"""
    import itk
    instance = itk.ShiftScaleLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def shift_scale_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ShiftScaleLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.ShiftScaleLabelMapFilter.values()[0]
    else:
        filter_object = itk.ShiftScaleLabelMapFilter

    shift_scale_label_map_filter.__doc__ = filter_object.__doc__
    shift_scale_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    shift_scale_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    shift_scale_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



