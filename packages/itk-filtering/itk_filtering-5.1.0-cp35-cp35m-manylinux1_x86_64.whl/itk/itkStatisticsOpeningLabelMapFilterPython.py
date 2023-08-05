# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkStatisticsOpeningLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkStatisticsOpeningLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkStatisticsOpeningLabelMapFilterPython
            return _itkStatisticsOpeningLabelMapFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkStatisticsOpeningLabelMapFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkStatisticsOpeningLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkStatisticsOpeningLabelMapFilterPython
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
import itkShapeOpeningLabelMapFilterPython
import itkInPlaceLabelMapFilterPython
import ITKLabelMapBasePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImageToImageFilterCommonPython
import itkImageSourceCommonPython
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

def itkStatisticsOpeningLabelMapFilterLM3_New():
  return itkStatisticsOpeningLabelMapFilterLM3.New()


def itkStatisticsOpeningLabelMapFilterLM2_New():
  return itkStatisticsOpeningLabelMapFilterLM2.New()

class itkStatisticsOpeningLabelMapFilterLM2(itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2):
    """


    remove the objects according to the value of their statistics
    attribute

    StatisticsOpeningLabelMapFilter removes the objects in a label
    collection image with an attribute value smaller or greater than a
    threshold called Lambda. The attributes are the ones of the
    StatisticsLabelObject.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://hdl.handle.net/1926/584
    orhttp://www.insight-journal.org/browse/publication/176

    See:   StatisticsLabelObject, BinaryStatisticsOpeningImageFilter,
    LabelShapeOpeningImageFilter

    C++ includes: itkStatisticsOpeningLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkStatisticsOpeningLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkStatisticsOpeningLabelMapFilterLM2_Pointer"""
        return _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkStatisticsOpeningLabelMapFilterLM2_Pointer":
        """Clone(itkStatisticsOpeningLabelMapFilterLM2 self) -> itkStatisticsOpeningLabelMapFilterLM2_Pointer"""
        return _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM2_Clone(self)

    __swig_destroy__ = _itkStatisticsOpeningLabelMapFilterPython.delete_itkStatisticsOpeningLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkStatisticsOpeningLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkStatisticsOpeningLabelMapFilterLM2"""
        return _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsOpeningLabelMapFilterLM2

        Create a new object of the class itkStatisticsOpeningLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsOpeningLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkStatisticsOpeningLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkStatisticsOpeningLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkStatisticsOpeningLabelMapFilterLM2.Clone = new_instancemethod(_itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM2_Clone, None, itkStatisticsOpeningLabelMapFilterLM2)
itkStatisticsOpeningLabelMapFilterLM2_swigregister = _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM2_swigregister
itkStatisticsOpeningLabelMapFilterLM2_swigregister(itkStatisticsOpeningLabelMapFilterLM2)

def itkStatisticsOpeningLabelMapFilterLM2___New_orig__() -> "itkStatisticsOpeningLabelMapFilterLM2_Pointer":
    """itkStatisticsOpeningLabelMapFilterLM2___New_orig__() -> itkStatisticsOpeningLabelMapFilterLM2_Pointer"""
    return _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM2___New_orig__()

def itkStatisticsOpeningLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkStatisticsOpeningLabelMapFilterLM2 *":
    """itkStatisticsOpeningLabelMapFilterLM2_cast(itkLightObject obj) -> itkStatisticsOpeningLabelMapFilterLM2"""
    return _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM2_cast(obj)

class itkStatisticsOpeningLabelMapFilterLM3(itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3):
    """


    remove the objects according to the value of their statistics
    attribute

    StatisticsOpeningLabelMapFilter removes the objects in a label
    collection image with an attribute value smaller or greater than a
    threshold called Lambda. The attributes are the ones of the
    StatisticsLabelObject.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://hdl.handle.net/1926/584
    orhttp://www.insight-journal.org/browse/publication/176

    See:   StatisticsLabelObject, BinaryStatisticsOpeningImageFilter,
    LabelShapeOpeningImageFilter

    C++ includes: itkStatisticsOpeningLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkStatisticsOpeningLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkStatisticsOpeningLabelMapFilterLM3_Pointer"""
        return _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkStatisticsOpeningLabelMapFilterLM3_Pointer":
        """Clone(itkStatisticsOpeningLabelMapFilterLM3 self) -> itkStatisticsOpeningLabelMapFilterLM3_Pointer"""
        return _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM3_Clone(self)

    __swig_destroy__ = _itkStatisticsOpeningLabelMapFilterPython.delete_itkStatisticsOpeningLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkStatisticsOpeningLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkStatisticsOpeningLabelMapFilterLM3"""
        return _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsOpeningLabelMapFilterLM3

        Create a new object of the class itkStatisticsOpeningLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsOpeningLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkStatisticsOpeningLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkStatisticsOpeningLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkStatisticsOpeningLabelMapFilterLM3.Clone = new_instancemethod(_itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM3_Clone, None, itkStatisticsOpeningLabelMapFilterLM3)
itkStatisticsOpeningLabelMapFilterLM3_swigregister = _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM3_swigregister
itkStatisticsOpeningLabelMapFilterLM3_swigregister(itkStatisticsOpeningLabelMapFilterLM3)

def itkStatisticsOpeningLabelMapFilterLM3___New_orig__() -> "itkStatisticsOpeningLabelMapFilterLM3_Pointer":
    """itkStatisticsOpeningLabelMapFilterLM3___New_orig__() -> itkStatisticsOpeningLabelMapFilterLM3_Pointer"""
    return _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM3___New_orig__()

def itkStatisticsOpeningLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkStatisticsOpeningLabelMapFilterLM3 *":
    """itkStatisticsOpeningLabelMapFilterLM3_cast(itkLightObject obj) -> itkStatisticsOpeningLabelMapFilterLM3"""
    return _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def statistics_opening_label_map_filter(*args, **kwargs):
    """Procedural interface for StatisticsOpeningLabelMapFilter"""
    import itk
    instance = itk.StatisticsOpeningLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def statistics_opening_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.StatisticsOpeningLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.StatisticsOpeningLabelMapFilter.values()[0]
    else:
        filter_object = itk.StatisticsOpeningLabelMapFilter

    statistics_opening_label_map_filter.__doc__ = filter_object.__doc__
    statistics_opening_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    statistics_opening_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    statistics_opening_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



