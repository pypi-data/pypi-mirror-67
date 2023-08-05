# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLabelMapToLabelImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLabelMapToLabelImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkLabelMapToLabelImageFilterPython
            return _itkLabelMapToLabelImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkLabelMapToLabelImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkLabelMapToLabelImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLabelMapToLabelImageFilterPython
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
import itkStatisticsLabelObjectPython
import itkMatrixPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkPointPython
import vnl_vector_refPython
import itkVectorPython
import itkFixedArrayPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkDiffusionTensor3DPython
import itkArray2DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkVariableLengthVectorPython
import itkTransformBasePython
import itkHistogramPython
import itkSamplePython
import itkShapeLabelObjectPython
import itkImageRegionPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkLabelMapFilterPython
import ITKLabelMapBasePython
import itkImageSourcePython
import itkImagePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkVectorImagePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkLabelMapToLabelImageFilterLM3IUS3_New():
  return itkLabelMapToLabelImageFilterLM3IUS3.New()


def itkLabelMapToLabelImageFilterLM2IUS2_New():
  return itkLabelMapToLabelImageFilterLM2IUS2.New()


def itkLabelMapToLabelImageFilterLM3IUC3_New():
  return itkLabelMapToLabelImageFilterLM3IUC3.New()


def itkLabelMapToLabelImageFilterLM2IUC2_New():
  return itkLabelMapToLabelImageFilterLM2IUC2.New()

class itkLabelMapToLabelImageFilterLM2IUC2(itkLabelMapFilterPython.itkLabelMapFilterLM2IUC2):
    """


    Converts a LabelMap to a labeled image.

    LabelMapToBinaryImageFilter to a label image.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://hdl.handle.net/1926/584
    orhttp://www.insight-journal.org/browse/publication/176

    See:   LabelMapToBinaryImageFilter, LabelMapMaskImageFilter
    \\sphinx
    \\sphinxexample{Filtering/LabelMap/ConvertLabelMapToImage,Convert
    Label Map To Normal Image} \\endsphinx

    C++ includes: itkLabelMapToLabelImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelMapToLabelImageFilterLM2IUC2_Pointer":
        """__New_orig__() -> itkLabelMapToLabelImageFilterLM2IUC2_Pointer"""
        return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelMapToLabelImageFilterLM2IUC2_Pointer":
        """Clone(itkLabelMapToLabelImageFilterLM2IUC2 self) -> itkLabelMapToLabelImageFilterLM2IUC2_Pointer"""
        return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2_Clone(self)

    SameDimensionCheck = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2_SameDimensionCheck
    __swig_destroy__ = _itkLabelMapToLabelImageFilterPython.delete_itkLabelMapToLabelImageFilterLM2IUC2

    def cast(obj: 'itkLightObject') -> "itkLabelMapToLabelImageFilterLM2IUC2 *":
        """cast(itkLightObject obj) -> itkLabelMapToLabelImageFilterLM2IUC2"""
        return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToLabelImageFilterLM2IUC2

        Create a new object of the class itkLabelMapToLabelImageFilterLM2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToLabelImageFilterLM2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapToLabelImageFilterLM2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapToLabelImageFilterLM2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelMapToLabelImageFilterLM2IUC2.Clone = new_instancemethod(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2_Clone, None, itkLabelMapToLabelImageFilterLM2IUC2)
itkLabelMapToLabelImageFilterLM2IUC2_swigregister = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2_swigregister
itkLabelMapToLabelImageFilterLM2IUC2_swigregister(itkLabelMapToLabelImageFilterLM2IUC2)

def itkLabelMapToLabelImageFilterLM2IUC2___New_orig__() -> "itkLabelMapToLabelImageFilterLM2IUC2_Pointer":
    """itkLabelMapToLabelImageFilterLM2IUC2___New_orig__() -> itkLabelMapToLabelImageFilterLM2IUC2_Pointer"""
    return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2___New_orig__()

def itkLabelMapToLabelImageFilterLM2IUC2_cast(obj: 'itkLightObject') -> "itkLabelMapToLabelImageFilterLM2IUC2 *":
    """itkLabelMapToLabelImageFilterLM2IUC2_cast(itkLightObject obj) -> itkLabelMapToLabelImageFilterLM2IUC2"""
    return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2_cast(obj)

class itkLabelMapToLabelImageFilterLM2IUS2(itkLabelMapFilterPython.itkLabelMapFilterLM2IUS2):
    """


    Converts a LabelMap to a labeled image.

    LabelMapToBinaryImageFilter to a label image.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://hdl.handle.net/1926/584
    orhttp://www.insight-journal.org/browse/publication/176

    See:   LabelMapToBinaryImageFilter, LabelMapMaskImageFilter
    \\sphinx
    \\sphinxexample{Filtering/LabelMap/ConvertLabelMapToImage,Convert
    Label Map To Normal Image} \\endsphinx

    C++ includes: itkLabelMapToLabelImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelMapToLabelImageFilterLM2IUS2_Pointer":
        """__New_orig__() -> itkLabelMapToLabelImageFilterLM2IUS2_Pointer"""
        return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelMapToLabelImageFilterLM2IUS2_Pointer":
        """Clone(itkLabelMapToLabelImageFilterLM2IUS2 self) -> itkLabelMapToLabelImageFilterLM2IUS2_Pointer"""
        return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2_Clone(self)

    SameDimensionCheck = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2_SameDimensionCheck
    __swig_destroy__ = _itkLabelMapToLabelImageFilterPython.delete_itkLabelMapToLabelImageFilterLM2IUS2

    def cast(obj: 'itkLightObject') -> "itkLabelMapToLabelImageFilterLM2IUS2 *":
        """cast(itkLightObject obj) -> itkLabelMapToLabelImageFilterLM2IUS2"""
        return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToLabelImageFilterLM2IUS2

        Create a new object of the class itkLabelMapToLabelImageFilterLM2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToLabelImageFilterLM2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapToLabelImageFilterLM2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapToLabelImageFilterLM2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelMapToLabelImageFilterLM2IUS2.Clone = new_instancemethod(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2_Clone, None, itkLabelMapToLabelImageFilterLM2IUS2)
itkLabelMapToLabelImageFilterLM2IUS2_swigregister = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2_swigregister
itkLabelMapToLabelImageFilterLM2IUS2_swigregister(itkLabelMapToLabelImageFilterLM2IUS2)

def itkLabelMapToLabelImageFilterLM2IUS2___New_orig__() -> "itkLabelMapToLabelImageFilterLM2IUS2_Pointer":
    """itkLabelMapToLabelImageFilterLM2IUS2___New_orig__() -> itkLabelMapToLabelImageFilterLM2IUS2_Pointer"""
    return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2___New_orig__()

def itkLabelMapToLabelImageFilterLM2IUS2_cast(obj: 'itkLightObject') -> "itkLabelMapToLabelImageFilterLM2IUS2 *":
    """itkLabelMapToLabelImageFilterLM2IUS2_cast(itkLightObject obj) -> itkLabelMapToLabelImageFilterLM2IUS2"""
    return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2_cast(obj)

class itkLabelMapToLabelImageFilterLM3IUC3(itkLabelMapFilterPython.itkLabelMapFilterLM3IUC3):
    """


    Converts a LabelMap to a labeled image.

    LabelMapToBinaryImageFilter to a label image.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://hdl.handle.net/1926/584
    orhttp://www.insight-journal.org/browse/publication/176

    See:   LabelMapToBinaryImageFilter, LabelMapMaskImageFilter
    \\sphinx
    \\sphinxexample{Filtering/LabelMap/ConvertLabelMapToImage,Convert
    Label Map To Normal Image} \\endsphinx

    C++ includes: itkLabelMapToLabelImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelMapToLabelImageFilterLM3IUC3_Pointer":
        """__New_orig__() -> itkLabelMapToLabelImageFilterLM3IUC3_Pointer"""
        return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelMapToLabelImageFilterLM3IUC3_Pointer":
        """Clone(itkLabelMapToLabelImageFilterLM3IUC3 self) -> itkLabelMapToLabelImageFilterLM3IUC3_Pointer"""
        return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3_Clone(self)

    SameDimensionCheck = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3_SameDimensionCheck
    __swig_destroy__ = _itkLabelMapToLabelImageFilterPython.delete_itkLabelMapToLabelImageFilterLM3IUC3

    def cast(obj: 'itkLightObject') -> "itkLabelMapToLabelImageFilterLM3IUC3 *":
        """cast(itkLightObject obj) -> itkLabelMapToLabelImageFilterLM3IUC3"""
        return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToLabelImageFilterLM3IUC3

        Create a new object of the class itkLabelMapToLabelImageFilterLM3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToLabelImageFilterLM3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapToLabelImageFilterLM3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapToLabelImageFilterLM3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelMapToLabelImageFilterLM3IUC3.Clone = new_instancemethod(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3_Clone, None, itkLabelMapToLabelImageFilterLM3IUC3)
itkLabelMapToLabelImageFilterLM3IUC3_swigregister = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3_swigregister
itkLabelMapToLabelImageFilterLM3IUC3_swigregister(itkLabelMapToLabelImageFilterLM3IUC3)

def itkLabelMapToLabelImageFilterLM3IUC3___New_orig__() -> "itkLabelMapToLabelImageFilterLM3IUC3_Pointer":
    """itkLabelMapToLabelImageFilterLM3IUC3___New_orig__() -> itkLabelMapToLabelImageFilterLM3IUC3_Pointer"""
    return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3___New_orig__()

def itkLabelMapToLabelImageFilterLM3IUC3_cast(obj: 'itkLightObject') -> "itkLabelMapToLabelImageFilterLM3IUC3 *":
    """itkLabelMapToLabelImageFilterLM3IUC3_cast(itkLightObject obj) -> itkLabelMapToLabelImageFilterLM3IUC3"""
    return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3_cast(obj)

class itkLabelMapToLabelImageFilterLM3IUS3(itkLabelMapFilterPython.itkLabelMapFilterLM3IUS3):
    """


    Converts a LabelMap to a labeled image.

    LabelMapToBinaryImageFilter to a label image.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://hdl.handle.net/1926/584
    orhttp://www.insight-journal.org/browse/publication/176

    See:   LabelMapToBinaryImageFilter, LabelMapMaskImageFilter
    \\sphinx
    \\sphinxexample{Filtering/LabelMap/ConvertLabelMapToImage,Convert
    Label Map To Normal Image} \\endsphinx

    C++ includes: itkLabelMapToLabelImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelMapToLabelImageFilterLM3IUS3_Pointer":
        """__New_orig__() -> itkLabelMapToLabelImageFilterLM3IUS3_Pointer"""
        return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelMapToLabelImageFilterLM3IUS3_Pointer":
        """Clone(itkLabelMapToLabelImageFilterLM3IUS3 self) -> itkLabelMapToLabelImageFilterLM3IUS3_Pointer"""
        return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3_Clone(self)

    SameDimensionCheck = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3_SameDimensionCheck
    __swig_destroy__ = _itkLabelMapToLabelImageFilterPython.delete_itkLabelMapToLabelImageFilterLM3IUS3

    def cast(obj: 'itkLightObject') -> "itkLabelMapToLabelImageFilterLM3IUS3 *":
        """cast(itkLightObject obj) -> itkLabelMapToLabelImageFilterLM3IUS3"""
        return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToLabelImageFilterLM3IUS3

        Create a new object of the class itkLabelMapToLabelImageFilterLM3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToLabelImageFilterLM3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapToLabelImageFilterLM3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapToLabelImageFilterLM3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelMapToLabelImageFilterLM3IUS3.Clone = new_instancemethod(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3_Clone, None, itkLabelMapToLabelImageFilterLM3IUS3)
itkLabelMapToLabelImageFilterLM3IUS3_swigregister = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3_swigregister
itkLabelMapToLabelImageFilterLM3IUS3_swigregister(itkLabelMapToLabelImageFilterLM3IUS3)

def itkLabelMapToLabelImageFilterLM3IUS3___New_orig__() -> "itkLabelMapToLabelImageFilterLM3IUS3_Pointer":
    """itkLabelMapToLabelImageFilterLM3IUS3___New_orig__() -> itkLabelMapToLabelImageFilterLM3IUS3_Pointer"""
    return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3___New_orig__()

def itkLabelMapToLabelImageFilterLM3IUS3_cast(obj: 'itkLightObject') -> "itkLabelMapToLabelImageFilterLM3IUS3 *":
    """itkLabelMapToLabelImageFilterLM3IUS3_cast(itkLightObject obj) -> itkLabelMapToLabelImageFilterLM3IUS3"""
    return _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def label_map_to_label_image_filter(*args, **kwargs):
    """Procedural interface for LabelMapToLabelImageFilter"""
    import itk
    instance = itk.LabelMapToLabelImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def label_map_to_label_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.LabelMapToLabelImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.LabelMapToLabelImageFilter.values()[0]
    else:
        filter_object = itk.LabelMapToLabelImageFilter

    label_map_to_label_image_filter.__doc__ = filter_object.__doc__
    label_map_to_label_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    label_map_to_label_image_filter.__doc__ += "Available Keyword Arguments:\n"
    label_map_to_label_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



