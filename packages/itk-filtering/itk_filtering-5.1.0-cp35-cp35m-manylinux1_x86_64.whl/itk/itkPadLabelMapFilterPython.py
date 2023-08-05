# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkPadLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkPadLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkPadLabelMapFilterPython
            return _itkPadLabelMapFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkPadLabelMapFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkPadLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkPadLabelMapFilterPython
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

def itkPadLabelMapFilterLM3_New():
  return itkPadLabelMapFilterLM3.New()


def itkPadLabelMapFilterLM2_New():
  return itkPadLabelMapFilterLM2.New()

class itkPadLabelMapFilterLM2(itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2):
    """


    Pad a LabelMap image.

    This filter pads a label map.

    The SetPadSize() method can be used to set the pad size of the lower
    and the upper boundaries in a single call. By default, the filter
    doesn't pad anything.

    This implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/584 orhttp://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   CropLabelMapFilter

    C++ includes: itkPadLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkPadLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkPadLabelMapFilterLM2_Pointer"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkPadLabelMapFilterLM2_Pointer":
        """Clone(itkPadLabelMapFilterLM2 self) -> itkPadLabelMapFilterLM2_Pointer"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_Clone(self)


    def SetUpperBoundaryPadSize(self, _arg: 'itkSize2') -> "void":
        """
        SetUpperBoundaryPadSize(itkPadLabelMapFilterLM2 self, itkSize2 _arg)

        Set/Get the
        cropping sizes for the upper and lower boundaries. 
        """
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_SetUpperBoundaryPadSize(self, _arg)


    def GetUpperBoundaryPadSize(self) -> "itkSize2":
        """GetUpperBoundaryPadSize(itkPadLabelMapFilterLM2 self) -> itkSize2"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_GetUpperBoundaryPadSize(self)


    def SetLowerBoundaryPadSize(self, _arg: 'itkSize2') -> "void":
        """SetLowerBoundaryPadSize(itkPadLabelMapFilterLM2 self, itkSize2 _arg)"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_SetLowerBoundaryPadSize(self, _arg)


    def GetLowerBoundaryPadSize(self) -> "itkSize2":
        """GetLowerBoundaryPadSize(itkPadLabelMapFilterLM2 self) -> itkSize2"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_GetLowerBoundaryPadSize(self)


    def SetPadSize(self, size: 'itkSize2') -> "void":
        """SetPadSize(itkPadLabelMapFilterLM2 self, itkSize2 size)"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_SetPadSize(self, size)

    __swig_destroy__ = _itkPadLabelMapFilterPython.delete_itkPadLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkPadLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkPadLabelMapFilterLM2"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkPadLabelMapFilterLM2

        Create a new object of the class itkPadLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPadLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPadLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPadLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPadLabelMapFilterLM2.Clone = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_Clone, None, itkPadLabelMapFilterLM2)
itkPadLabelMapFilterLM2.SetUpperBoundaryPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_SetUpperBoundaryPadSize, None, itkPadLabelMapFilterLM2)
itkPadLabelMapFilterLM2.GetUpperBoundaryPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_GetUpperBoundaryPadSize, None, itkPadLabelMapFilterLM2)
itkPadLabelMapFilterLM2.SetLowerBoundaryPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_SetLowerBoundaryPadSize, None, itkPadLabelMapFilterLM2)
itkPadLabelMapFilterLM2.GetLowerBoundaryPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_GetLowerBoundaryPadSize, None, itkPadLabelMapFilterLM2)
itkPadLabelMapFilterLM2.SetPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_SetPadSize, None, itkPadLabelMapFilterLM2)
itkPadLabelMapFilterLM2_swigregister = _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_swigregister
itkPadLabelMapFilterLM2_swigregister(itkPadLabelMapFilterLM2)

def itkPadLabelMapFilterLM2___New_orig__() -> "itkPadLabelMapFilterLM2_Pointer":
    """itkPadLabelMapFilterLM2___New_orig__() -> itkPadLabelMapFilterLM2_Pointer"""
    return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2___New_orig__()

def itkPadLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkPadLabelMapFilterLM2 *":
    """itkPadLabelMapFilterLM2_cast(itkLightObject obj) -> itkPadLabelMapFilterLM2"""
    return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_cast(obj)

class itkPadLabelMapFilterLM3(itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3):
    """


    Pad a LabelMap image.

    This filter pads a label map.

    The SetPadSize() method can be used to set the pad size of the lower
    and the upper boundaries in a single call. By default, the filter
    doesn't pad anything.

    This implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/584 orhttp://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   CropLabelMapFilter

    C++ includes: itkPadLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkPadLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkPadLabelMapFilterLM3_Pointer"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkPadLabelMapFilterLM3_Pointer":
        """Clone(itkPadLabelMapFilterLM3 self) -> itkPadLabelMapFilterLM3_Pointer"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_Clone(self)


    def SetUpperBoundaryPadSize(self, _arg: 'itkSize3') -> "void":
        """
        SetUpperBoundaryPadSize(itkPadLabelMapFilterLM3 self, itkSize3 _arg)

        Set/Get the
        cropping sizes for the upper and lower boundaries. 
        """
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_SetUpperBoundaryPadSize(self, _arg)


    def GetUpperBoundaryPadSize(self) -> "itkSize3":
        """GetUpperBoundaryPadSize(itkPadLabelMapFilterLM3 self) -> itkSize3"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_GetUpperBoundaryPadSize(self)


    def SetLowerBoundaryPadSize(self, _arg: 'itkSize3') -> "void":
        """SetLowerBoundaryPadSize(itkPadLabelMapFilterLM3 self, itkSize3 _arg)"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_SetLowerBoundaryPadSize(self, _arg)


    def GetLowerBoundaryPadSize(self) -> "itkSize3":
        """GetLowerBoundaryPadSize(itkPadLabelMapFilterLM3 self) -> itkSize3"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_GetLowerBoundaryPadSize(self)


    def SetPadSize(self, size: 'itkSize3') -> "void":
        """SetPadSize(itkPadLabelMapFilterLM3 self, itkSize3 size)"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_SetPadSize(self, size)

    __swig_destroy__ = _itkPadLabelMapFilterPython.delete_itkPadLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkPadLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkPadLabelMapFilterLM3"""
        return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkPadLabelMapFilterLM3

        Create a new object of the class itkPadLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPadLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPadLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPadLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPadLabelMapFilterLM3.Clone = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_Clone, None, itkPadLabelMapFilterLM3)
itkPadLabelMapFilterLM3.SetUpperBoundaryPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_SetUpperBoundaryPadSize, None, itkPadLabelMapFilterLM3)
itkPadLabelMapFilterLM3.GetUpperBoundaryPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_GetUpperBoundaryPadSize, None, itkPadLabelMapFilterLM3)
itkPadLabelMapFilterLM3.SetLowerBoundaryPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_SetLowerBoundaryPadSize, None, itkPadLabelMapFilterLM3)
itkPadLabelMapFilterLM3.GetLowerBoundaryPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_GetLowerBoundaryPadSize, None, itkPadLabelMapFilterLM3)
itkPadLabelMapFilterLM3.SetPadSize = new_instancemethod(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_SetPadSize, None, itkPadLabelMapFilterLM3)
itkPadLabelMapFilterLM3_swigregister = _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_swigregister
itkPadLabelMapFilterLM3_swigregister(itkPadLabelMapFilterLM3)

def itkPadLabelMapFilterLM3___New_orig__() -> "itkPadLabelMapFilterLM3_Pointer":
    """itkPadLabelMapFilterLM3___New_orig__() -> itkPadLabelMapFilterLM3_Pointer"""
    return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3___New_orig__()

def itkPadLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkPadLabelMapFilterLM3 *":
    """itkPadLabelMapFilterLM3_cast(itkLightObject obj) -> itkPadLabelMapFilterLM3"""
    return _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def pad_label_map_filter(*args, **kwargs):
    """Procedural interface for PadLabelMapFilter"""
    import itk
    instance = itk.PadLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def pad_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.PadLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.PadLabelMapFilter.values()[0]
    else:
        filter_object = itk.PadLabelMapFilter

    pad_label_map_filter.__doc__ = filter_object.__doc__
    pad_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    pad_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    pad_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



