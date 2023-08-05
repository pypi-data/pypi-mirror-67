# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkStatisticsPositionLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkStatisticsPositionLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkStatisticsPositionLabelMapFilterPython
            return _itkStatisticsPositionLabelMapFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkStatisticsPositionLabelMapFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkStatisticsPositionLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkStatisticsPositionLabelMapFilterPython
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


import itkShapePositionLabelMapFilterPython
import itkStatisticsLabelObjectPython
import itkShapeLabelObjectPython
import ITKCommonBasePython
import pyBasePython
import itkMatrixPython
import vnl_matrixPython
import vnl_vectorPython
import stdcomplexPython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkImageRegionPython
import itkAffineTransformPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkOptimizerParametersPython
import itkArrayPython
import itkArray2DPython
import itkMatrixOffsetTransformBasePython
import itkHistogramPython
import itkSamplePython
import itkInPlaceLabelMapFilterPython
import ITKLabelMapBasePython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImagePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkLabelMapFilterPython

def itkStatisticsPositionLabelMapFilterLM3_New():
  return itkStatisticsPositionLabelMapFilterLM3.New()


def itkStatisticsPositionLabelMapFilterLM2_New():
  return itkStatisticsPositionLabelMapFilterLM2.New()

class itkStatisticsPositionLabelMapFilterLM2(itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2):
    """


    Mark a single pixel in the label object which correspond to a position
    given by an attribute.

    This code was contributed in the Insight Journal paper: "Label object
    representation and manipulation with ITK" by Lehmann
    G.https://hdl.handle.net/1926/584http://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   StatisticsLabelObject, BinaryStatisticsOpeningImageFilter,
    LabelStatisticsOpeningImageFilter

    C++ includes: itkStatisticsPositionLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkStatisticsPositionLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkStatisticsPositionLabelMapFilterLM2_Pointer"""
        return _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkStatisticsPositionLabelMapFilterLM2_Pointer":
        """Clone(itkStatisticsPositionLabelMapFilterLM2 self) -> itkStatisticsPositionLabelMapFilterLM2_Pointer"""
        return _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2_Clone(self)

    __swig_destroy__ = _itkStatisticsPositionLabelMapFilterPython.delete_itkStatisticsPositionLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkStatisticsPositionLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkStatisticsPositionLabelMapFilterLM2"""
        return _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsPositionLabelMapFilterLM2

        Create a new object of the class itkStatisticsPositionLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsPositionLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkStatisticsPositionLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkStatisticsPositionLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkStatisticsPositionLabelMapFilterLM2.Clone = new_instancemethod(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2_Clone, None, itkStatisticsPositionLabelMapFilterLM2)
itkStatisticsPositionLabelMapFilterLM2_swigregister = _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2_swigregister
itkStatisticsPositionLabelMapFilterLM2_swigregister(itkStatisticsPositionLabelMapFilterLM2)

def itkStatisticsPositionLabelMapFilterLM2___New_orig__() -> "itkStatisticsPositionLabelMapFilterLM2_Pointer":
    """itkStatisticsPositionLabelMapFilterLM2___New_orig__() -> itkStatisticsPositionLabelMapFilterLM2_Pointer"""
    return _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2___New_orig__()

def itkStatisticsPositionLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkStatisticsPositionLabelMapFilterLM2 *":
    """itkStatisticsPositionLabelMapFilterLM2_cast(itkLightObject obj) -> itkStatisticsPositionLabelMapFilterLM2"""
    return _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2_cast(obj)

class itkStatisticsPositionLabelMapFilterLM3(itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3):
    """


    Mark a single pixel in the label object which correspond to a position
    given by an attribute.

    This code was contributed in the Insight Journal paper: "Label object
    representation and manipulation with ITK" by Lehmann
    G.https://hdl.handle.net/1926/584http://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   StatisticsLabelObject, BinaryStatisticsOpeningImageFilter,
    LabelStatisticsOpeningImageFilter

    C++ includes: itkStatisticsPositionLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkStatisticsPositionLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkStatisticsPositionLabelMapFilterLM3_Pointer"""
        return _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkStatisticsPositionLabelMapFilterLM3_Pointer":
        """Clone(itkStatisticsPositionLabelMapFilterLM3 self) -> itkStatisticsPositionLabelMapFilterLM3_Pointer"""
        return _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3_Clone(self)

    __swig_destroy__ = _itkStatisticsPositionLabelMapFilterPython.delete_itkStatisticsPositionLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkStatisticsPositionLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkStatisticsPositionLabelMapFilterLM3"""
        return _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsPositionLabelMapFilterLM3

        Create a new object of the class itkStatisticsPositionLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsPositionLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkStatisticsPositionLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkStatisticsPositionLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkStatisticsPositionLabelMapFilterLM3.Clone = new_instancemethod(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3_Clone, None, itkStatisticsPositionLabelMapFilterLM3)
itkStatisticsPositionLabelMapFilterLM3_swigregister = _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3_swigregister
itkStatisticsPositionLabelMapFilterLM3_swigregister(itkStatisticsPositionLabelMapFilterLM3)

def itkStatisticsPositionLabelMapFilterLM3___New_orig__() -> "itkStatisticsPositionLabelMapFilterLM3_Pointer":
    """itkStatisticsPositionLabelMapFilterLM3___New_orig__() -> itkStatisticsPositionLabelMapFilterLM3_Pointer"""
    return _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3___New_orig__()

def itkStatisticsPositionLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkStatisticsPositionLabelMapFilterLM3 *":
    """itkStatisticsPositionLabelMapFilterLM3_cast(itkLightObject obj) -> itkStatisticsPositionLabelMapFilterLM3"""
    return _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def statistics_position_label_map_filter(*args, **kwargs):
    """Procedural interface for StatisticsPositionLabelMapFilter"""
    import itk
    instance = itk.StatisticsPositionLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def statistics_position_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.StatisticsPositionLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.StatisticsPositionLabelMapFilter.values()[0]
    else:
        filter_object = itk.StatisticsPositionLabelMapFilter

    statistics_position_label_map_filter.__doc__ = filter_object.__doc__
    statistics_position_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    statistics_position_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    statistics_position_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



