# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkShapeOpeningLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkShapeOpeningLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkShapeOpeningLabelMapFilterPython
            return _itkShapeOpeningLabelMapFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkShapeOpeningLabelMapFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkShapeOpeningLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkShapeOpeningLabelMapFilterPython
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
import itkInPlaceLabelMapFilterPython
import ITKLabelMapBasePython
import itkImageSourcePython
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
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkStatisticsLabelObjectPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkDiffusionTensor3DPython
import itkArray2DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkTransformBasePython
import itkHistogramPython
import itkSamplePython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkLabelMapFilterPython

def itkShapeOpeningLabelMapFilterLM3_New():
  return itkShapeOpeningLabelMapFilterLM3.New()


def itkShapeOpeningLabelMapFilterLM2_New():
  return itkShapeOpeningLabelMapFilterLM2.New()

class itkShapeOpeningLabelMapFilterLM2(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    """


    Remove objects according to the value of their shape attribute.

    ShapeOpeningLabelMapFilter removes objects in a label collection image
    with an attribute value smaller or greater than a threshold called
    Lambda. The attributes are those of the ShapeLabelObject.

    This implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/584 orhttp://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, BinaryShapeOpeningImageFilter,
    LabelStatisticsOpeningImageFilter  \\sphinx
    \\sphinxexample{Filtering/LabelMap/KeepRegionsThatMeetSpecific,Keep
    Regions That Meet Specific Properties} \\endsphinx

    C++ includes: itkShapeOpeningLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapeOpeningLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkShapeOpeningLabelMapFilterLM2_Pointer"""
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapeOpeningLabelMapFilterLM2_Pointer":
        """Clone(itkShapeOpeningLabelMapFilterLM2 self) -> itkShapeOpeningLabelMapFilterLM2_Pointer"""
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_Clone(self)


    def GetLambda(self) -> "double":
        """
        GetLambda(itkShapeOpeningLabelMapFilterLM2 self) -> double

        Set/Get the threshold
        used to keep or remove the objects. 
        """
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_GetLambda(self)


    def SetLambda(self, _arg: 'double const') -> "void":
        """SetLambda(itkShapeOpeningLabelMapFilterLM2 self, double const _arg)"""
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_SetLambda(self, _arg)


    def GetReverseOrdering(self) -> "bool":
        """
        GetReverseOrdering(itkShapeOpeningLabelMapFilterLM2 self) -> bool

        Set/Get the
        ordering of the objects. By default, objects with an attribute value
        smaller than Lamba are removed. Turning ReverseOrdering to true makes
        this filter remove objects with an attribute value greater than Lambda
        instead. 
        """
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_GetReverseOrdering(self)


    def SetReverseOrdering(self, _arg: 'bool const') -> "void":
        """SetReverseOrdering(itkShapeOpeningLabelMapFilterLM2 self, bool const _arg)"""
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_SetReverseOrdering(self, _arg)


    def ReverseOrderingOn(self) -> "void":
        """ReverseOrderingOn(itkShapeOpeningLabelMapFilterLM2 self)"""
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_ReverseOrderingOn(self)


    def ReverseOrderingOff(self) -> "void":
        """ReverseOrderingOff(itkShapeOpeningLabelMapFilterLM2 self)"""
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_ReverseOrderingOff(self)


    def GetAttribute(self) -> "unsigned int":
        """
        GetAttribute(itkShapeOpeningLabelMapFilterLM2 self) -> unsigned int

        Set/Get the attribute
        to use to select the object to remove. The default is "Size". 
        """
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_GetAttribute(self)


    def SetAttribute(self, *args) -> "void":
        """
        SetAttribute(itkShapeOpeningLabelMapFilterLM2 self, unsigned int const _arg)
        SetAttribute(itkShapeOpeningLabelMapFilterLM2 self, std::string const & s)
        """
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_SetAttribute(self, *args)

    __swig_destroy__ = _itkShapeOpeningLabelMapFilterPython.delete_itkShapeOpeningLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkShapeOpeningLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkShapeOpeningLabelMapFilterLM2"""
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkShapeOpeningLabelMapFilterLM2

        Create a new object of the class itkShapeOpeningLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeOpeningLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapeOpeningLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapeOpeningLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapeOpeningLabelMapFilterLM2.Clone = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_Clone, None, itkShapeOpeningLabelMapFilterLM2)
itkShapeOpeningLabelMapFilterLM2.GetLambda = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_GetLambda, None, itkShapeOpeningLabelMapFilterLM2)
itkShapeOpeningLabelMapFilterLM2.SetLambda = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_SetLambda, None, itkShapeOpeningLabelMapFilterLM2)
itkShapeOpeningLabelMapFilterLM2.GetReverseOrdering = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_GetReverseOrdering, None, itkShapeOpeningLabelMapFilterLM2)
itkShapeOpeningLabelMapFilterLM2.SetReverseOrdering = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_SetReverseOrdering, None, itkShapeOpeningLabelMapFilterLM2)
itkShapeOpeningLabelMapFilterLM2.ReverseOrderingOn = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_ReverseOrderingOn, None, itkShapeOpeningLabelMapFilterLM2)
itkShapeOpeningLabelMapFilterLM2.ReverseOrderingOff = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_ReverseOrderingOff, None, itkShapeOpeningLabelMapFilterLM2)
itkShapeOpeningLabelMapFilterLM2.GetAttribute = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_GetAttribute, None, itkShapeOpeningLabelMapFilterLM2)
itkShapeOpeningLabelMapFilterLM2.SetAttribute = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_SetAttribute, None, itkShapeOpeningLabelMapFilterLM2)
itkShapeOpeningLabelMapFilterLM2_swigregister = _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_swigregister
itkShapeOpeningLabelMapFilterLM2_swigregister(itkShapeOpeningLabelMapFilterLM2)

def itkShapeOpeningLabelMapFilterLM2___New_orig__() -> "itkShapeOpeningLabelMapFilterLM2_Pointer":
    """itkShapeOpeningLabelMapFilterLM2___New_orig__() -> itkShapeOpeningLabelMapFilterLM2_Pointer"""
    return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2___New_orig__()

def itkShapeOpeningLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkShapeOpeningLabelMapFilterLM2 *":
    """itkShapeOpeningLabelMapFilterLM2_cast(itkLightObject obj) -> itkShapeOpeningLabelMapFilterLM2"""
    return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_cast(obj)

class itkShapeOpeningLabelMapFilterLM3(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    """


    Remove objects according to the value of their shape attribute.

    ShapeOpeningLabelMapFilter removes objects in a label collection image
    with an attribute value smaller or greater than a threshold called
    Lambda. The attributes are those of the ShapeLabelObject.

    This implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/584 orhttp://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, BinaryShapeOpeningImageFilter,
    LabelStatisticsOpeningImageFilter  \\sphinx
    \\sphinxexample{Filtering/LabelMap/KeepRegionsThatMeetSpecific,Keep
    Regions That Meet Specific Properties} \\endsphinx

    C++ includes: itkShapeOpeningLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShapeOpeningLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkShapeOpeningLabelMapFilterLM3_Pointer"""
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShapeOpeningLabelMapFilterLM3_Pointer":
        """Clone(itkShapeOpeningLabelMapFilterLM3 self) -> itkShapeOpeningLabelMapFilterLM3_Pointer"""
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_Clone(self)


    def GetLambda(self) -> "double":
        """
        GetLambda(itkShapeOpeningLabelMapFilterLM3 self) -> double

        Set/Get the threshold
        used to keep or remove the objects. 
        """
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_GetLambda(self)


    def SetLambda(self, _arg: 'double const') -> "void":
        """SetLambda(itkShapeOpeningLabelMapFilterLM3 self, double const _arg)"""
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_SetLambda(self, _arg)


    def GetReverseOrdering(self) -> "bool":
        """
        GetReverseOrdering(itkShapeOpeningLabelMapFilterLM3 self) -> bool

        Set/Get the
        ordering of the objects. By default, objects with an attribute value
        smaller than Lamba are removed. Turning ReverseOrdering to true makes
        this filter remove objects with an attribute value greater than Lambda
        instead. 
        """
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_GetReverseOrdering(self)


    def SetReverseOrdering(self, _arg: 'bool const') -> "void":
        """SetReverseOrdering(itkShapeOpeningLabelMapFilterLM3 self, bool const _arg)"""
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_SetReverseOrdering(self, _arg)


    def ReverseOrderingOn(self) -> "void":
        """ReverseOrderingOn(itkShapeOpeningLabelMapFilterLM3 self)"""
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_ReverseOrderingOn(self)


    def ReverseOrderingOff(self) -> "void":
        """ReverseOrderingOff(itkShapeOpeningLabelMapFilterLM3 self)"""
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_ReverseOrderingOff(self)


    def GetAttribute(self) -> "unsigned int":
        """
        GetAttribute(itkShapeOpeningLabelMapFilterLM3 self) -> unsigned int

        Set/Get the attribute
        to use to select the object to remove. The default is "Size". 
        """
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_GetAttribute(self)


    def SetAttribute(self, *args) -> "void":
        """
        SetAttribute(itkShapeOpeningLabelMapFilterLM3 self, unsigned int const _arg)
        SetAttribute(itkShapeOpeningLabelMapFilterLM3 self, std::string const & s)
        """
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_SetAttribute(self, *args)

    __swig_destroy__ = _itkShapeOpeningLabelMapFilterPython.delete_itkShapeOpeningLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkShapeOpeningLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkShapeOpeningLabelMapFilterLM3"""
        return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkShapeOpeningLabelMapFilterLM3

        Create a new object of the class itkShapeOpeningLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeOpeningLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapeOpeningLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapeOpeningLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShapeOpeningLabelMapFilterLM3.Clone = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_Clone, None, itkShapeOpeningLabelMapFilterLM3)
itkShapeOpeningLabelMapFilterLM3.GetLambda = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_GetLambda, None, itkShapeOpeningLabelMapFilterLM3)
itkShapeOpeningLabelMapFilterLM3.SetLambda = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_SetLambda, None, itkShapeOpeningLabelMapFilterLM3)
itkShapeOpeningLabelMapFilterLM3.GetReverseOrdering = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_GetReverseOrdering, None, itkShapeOpeningLabelMapFilterLM3)
itkShapeOpeningLabelMapFilterLM3.SetReverseOrdering = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_SetReverseOrdering, None, itkShapeOpeningLabelMapFilterLM3)
itkShapeOpeningLabelMapFilterLM3.ReverseOrderingOn = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_ReverseOrderingOn, None, itkShapeOpeningLabelMapFilterLM3)
itkShapeOpeningLabelMapFilterLM3.ReverseOrderingOff = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_ReverseOrderingOff, None, itkShapeOpeningLabelMapFilterLM3)
itkShapeOpeningLabelMapFilterLM3.GetAttribute = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_GetAttribute, None, itkShapeOpeningLabelMapFilterLM3)
itkShapeOpeningLabelMapFilterLM3.SetAttribute = new_instancemethod(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_SetAttribute, None, itkShapeOpeningLabelMapFilterLM3)
itkShapeOpeningLabelMapFilterLM3_swigregister = _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_swigregister
itkShapeOpeningLabelMapFilterLM3_swigregister(itkShapeOpeningLabelMapFilterLM3)

def itkShapeOpeningLabelMapFilterLM3___New_orig__() -> "itkShapeOpeningLabelMapFilterLM3_Pointer":
    """itkShapeOpeningLabelMapFilterLM3___New_orig__() -> itkShapeOpeningLabelMapFilterLM3_Pointer"""
    return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3___New_orig__()

def itkShapeOpeningLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkShapeOpeningLabelMapFilterLM3 *":
    """itkShapeOpeningLabelMapFilterLM3_cast(itkLightObject obj) -> itkShapeOpeningLabelMapFilterLM3"""
    return _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def shape_opening_label_map_filter(*args, **kwargs):
    """Procedural interface for ShapeOpeningLabelMapFilter"""
    import itk
    instance = itk.ShapeOpeningLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def shape_opening_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ShapeOpeningLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.ShapeOpeningLabelMapFilter.values()[0]
    else:
        filter_object = itk.ShapeOpeningLabelMapFilter

    shape_opening_label_map_filter.__doc__ = filter_object.__doc__
    shape_opening_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    shape_opening_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    shape_opening_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



