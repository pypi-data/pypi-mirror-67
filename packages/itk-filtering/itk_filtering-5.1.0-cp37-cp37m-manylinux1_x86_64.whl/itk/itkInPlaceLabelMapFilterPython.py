# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkInPlaceLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkInPlaceLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkInPlaceLabelMapFilterPython
            return _itkInPlaceLabelMapFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkInPlaceLabelMapFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkInPlaceLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkInPlaceLabelMapFilterPython
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


import ITKLabelMapBasePython
import ITKCommonBasePython
import pyBasePython
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

def itkInPlaceLabelMapFilterLM3_New():
  return itkInPlaceLabelMapFilterLM3.New()


def itkInPlaceLabelMapFilterLM2_New():
  return itkInPlaceLabelMapFilterLM2.New()

class itkInPlaceLabelMapFilterLM2(itkLabelMapFilterPython.itkLabelMapFilterLM2LM2):
    """


    Base class for filters that takes an image as input and overwrites
    that image as the output.

    InPlaceLabelMapFilter is the base class for all process objects whose
    output image data is constructed by overwriting the input image data.
    In other words, the output bulk data is the same block of memory as
    the input bulk data. This filter provides the mechanisms for in place
    image processing while maintaining general pipeline mechanics.
    InPlaceLabelMapFilters use less memory than standard
    ImageToImageFilters because the input buffer is reused as the output
    buffer. However, this benefit does not come without a cost. Since the
    filter overwrites its input, the ownership of the bulk data is
    transitioned from the input data object to the output data object.
    When a data object has multiple consumers with one of the consumers
    being an in place filter, the in place filter effectively destroys the
    bulk data for the data object. Upstream filters will then have to re-
    execute to regenerate the data object's bulk data for the remaining
    consumers.

    Since an InPlaceLabelMapFilter reuses the input bulk data memory for
    the output bulk data memory, the input image type must match the
    output image type. If the input and output image types are not
    identical, the filter reverts to a traditional ImageToImageFilter
    behaviour where an output image is allocated. In place operation can
    also be controlled (when the input and output image type match) via
    the methods InPlaceOn() and InPlaceOff().

    Subclasses of InPlaceLabelMapFilter must take extra care in how they
    manage memory using (and perhaps overriding) the implementations of
    ReleaseInputs() and AllocateOutputs() provided here.

    This code was contributed in the Insight Journal paper: "Label object
    representation and manipulation with ITK" by Lehmann
    G.https://hdl.handle.net/1926/584http://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   LabelMapToBinaryImageFilter, LabelMapToLabelImageFilter

    C++ includes: itkInPlaceLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkInPlaceLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkInPlaceLabelMapFilterLM2_Pointer"""
        return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkInPlaceLabelMapFilterLM2_Pointer":
        """Clone(itkInPlaceLabelMapFilterLM2 self) -> itkInPlaceLabelMapFilterLM2_Pointer"""
        return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_Clone(self)


    def SetInPlace(self, _arg: 'bool const') -> "void":
        """
        SetInPlace(itkInPlaceLabelMapFilterLM2 self, bool const _arg)

        In place operation can
        be turned on and off. This only has an effect when the input and
        output image type match. 
        """
        return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_SetInPlace(self, _arg)


    def GetInPlace(self) -> "bool":
        """GetInPlace(itkInPlaceLabelMapFilterLM2 self) -> bool"""
        return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_GetInPlace(self)


    def InPlaceOn(self) -> "void":
        """InPlaceOn(itkInPlaceLabelMapFilterLM2 self)"""
        return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_InPlaceOn(self)


    def InPlaceOff(self) -> "void":
        """InPlaceOff(itkInPlaceLabelMapFilterLM2 self)"""
        return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_InPlaceOff(self)


    def CanRunInPlace(self) -> "bool":
        """
        CanRunInPlace(itkInPlaceLabelMapFilterLM2 self) -> bool

        Can the filter run in
        place? To do so, the filter's first input and output must have the
        same dimension and pixel type. This method can be used in conjunction
        with the InPlace ivar to determine whether a particular use of the
        filter is really running in place. Some filters may be able to
        optimize their operation if the InPlace is true and CanRunInPlace is
        true. 
        """
        return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_CanRunInPlace(self)

    __swig_destroy__ = _itkInPlaceLabelMapFilterPython.delete_itkInPlaceLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkInPlaceLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkInPlaceLabelMapFilterLM2"""
        return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkInPlaceLabelMapFilterLM2

        Create a new object of the class itkInPlaceLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInPlaceLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkInPlaceLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkInPlaceLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkInPlaceLabelMapFilterLM2.Clone = new_instancemethod(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_Clone, None, itkInPlaceLabelMapFilterLM2)
itkInPlaceLabelMapFilterLM2.SetInPlace = new_instancemethod(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_SetInPlace, None, itkInPlaceLabelMapFilterLM2)
itkInPlaceLabelMapFilterLM2.GetInPlace = new_instancemethod(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_GetInPlace, None, itkInPlaceLabelMapFilterLM2)
itkInPlaceLabelMapFilterLM2.InPlaceOn = new_instancemethod(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_InPlaceOn, None, itkInPlaceLabelMapFilterLM2)
itkInPlaceLabelMapFilterLM2.InPlaceOff = new_instancemethod(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_InPlaceOff, None, itkInPlaceLabelMapFilterLM2)
itkInPlaceLabelMapFilterLM2.CanRunInPlace = new_instancemethod(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_CanRunInPlace, None, itkInPlaceLabelMapFilterLM2)
itkInPlaceLabelMapFilterLM2_swigregister = _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_swigregister
itkInPlaceLabelMapFilterLM2_swigregister(itkInPlaceLabelMapFilterLM2)

def itkInPlaceLabelMapFilterLM2___New_orig__() -> "itkInPlaceLabelMapFilterLM2_Pointer":
    """itkInPlaceLabelMapFilterLM2___New_orig__() -> itkInPlaceLabelMapFilterLM2_Pointer"""
    return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2___New_orig__()

def itkInPlaceLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkInPlaceLabelMapFilterLM2 *":
    """itkInPlaceLabelMapFilterLM2_cast(itkLightObject obj) -> itkInPlaceLabelMapFilterLM2"""
    return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_cast(obj)

class itkInPlaceLabelMapFilterLM3(itkLabelMapFilterPython.itkLabelMapFilterLM3LM3):
    """


    Base class for filters that takes an image as input and overwrites
    that image as the output.

    InPlaceLabelMapFilter is the base class for all process objects whose
    output image data is constructed by overwriting the input image data.
    In other words, the output bulk data is the same block of memory as
    the input bulk data. This filter provides the mechanisms for in place
    image processing while maintaining general pipeline mechanics.
    InPlaceLabelMapFilters use less memory than standard
    ImageToImageFilters because the input buffer is reused as the output
    buffer. However, this benefit does not come without a cost. Since the
    filter overwrites its input, the ownership of the bulk data is
    transitioned from the input data object to the output data object.
    When a data object has multiple consumers with one of the consumers
    being an in place filter, the in place filter effectively destroys the
    bulk data for the data object. Upstream filters will then have to re-
    execute to regenerate the data object's bulk data for the remaining
    consumers.

    Since an InPlaceLabelMapFilter reuses the input bulk data memory for
    the output bulk data memory, the input image type must match the
    output image type. If the input and output image types are not
    identical, the filter reverts to a traditional ImageToImageFilter
    behaviour where an output image is allocated. In place operation can
    also be controlled (when the input and output image type match) via
    the methods InPlaceOn() and InPlaceOff().

    Subclasses of InPlaceLabelMapFilter must take extra care in how they
    manage memory using (and perhaps overriding) the implementations of
    ReleaseInputs() and AllocateOutputs() provided here.

    This code was contributed in the Insight Journal paper: "Label object
    representation and manipulation with ITK" by Lehmann
    G.https://hdl.handle.net/1926/584http://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   LabelMapToBinaryImageFilter, LabelMapToLabelImageFilter

    C++ includes: itkInPlaceLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkInPlaceLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkInPlaceLabelMapFilterLM3_Pointer"""
        return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkInPlaceLabelMapFilterLM3_Pointer":
        """Clone(itkInPlaceLabelMapFilterLM3 self) -> itkInPlaceLabelMapFilterLM3_Pointer"""
        return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_Clone(self)


    def SetInPlace(self, _arg: 'bool const') -> "void":
        """
        SetInPlace(itkInPlaceLabelMapFilterLM3 self, bool const _arg)

        In place operation can
        be turned on and off. This only has an effect when the input and
        output image type match. 
        """
        return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_SetInPlace(self, _arg)


    def GetInPlace(self) -> "bool":
        """GetInPlace(itkInPlaceLabelMapFilterLM3 self) -> bool"""
        return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_GetInPlace(self)


    def InPlaceOn(self) -> "void":
        """InPlaceOn(itkInPlaceLabelMapFilterLM3 self)"""
        return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_InPlaceOn(self)


    def InPlaceOff(self) -> "void":
        """InPlaceOff(itkInPlaceLabelMapFilterLM3 self)"""
        return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_InPlaceOff(self)


    def CanRunInPlace(self) -> "bool":
        """
        CanRunInPlace(itkInPlaceLabelMapFilterLM3 self) -> bool

        Can the filter run in
        place? To do so, the filter's first input and output must have the
        same dimension and pixel type. This method can be used in conjunction
        with the InPlace ivar to determine whether a particular use of the
        filter is really running in place. Some filters may be able to
        optimize their operation if the InPlace is true and CanRunInPlace is
        true. 
        """
        return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_CanRunInPlace(self)

    __swig_destroy__ = _itkInPlaceLabelMapFilterPython.delete_itkInPlaceLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkInPlaceLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkInPlaceLabelMapFilterLM3"""
        return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkInPlaceLabelMapFilterLM3

        Create a new object of the class itkInPlaceLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInPlaceLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkInPlaceLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkInPlaceLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkInPlaceLabelMapFilterLM3.Clone = new_instancemethod(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_Clone, None, itkInPlaceLabelMapFilterLM3)
itkInPlaceLabelMapFilterLM3.SetInPlace = new_instancemethod(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_SetInPlace, None, itkInPlaceLabelMapFilterLM3)
itkInPlaceLabelMapFilterLM3.GetInPlace = new_instancemethod(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_GetInPlace, None, itkInPlaceLabelMapFilterLM3)
itkInPlaceLabelMapFilterLM3.InPlaceOn = new_instancemethod(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_InPlaceOn, None, itkInPlaceLabelMapFilterLM3)
itkInPlaceLabelMapFilterLM3.InPlaceOff = new_instancemethod(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_InPlaceOff, None, itkInPlaceLabelMapFilterLM3)
itkInPlaceLabelMapFilterLM3.CanRunInPlace = new_instancemethod(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_CanRunInPlace, None, itkInPlaceLabelMapFilterLM3)
itkInPlaceLabelMapFilterLM3_swigregister = _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_swigregister
itkInPlaceLabelMapFilterLM3_swigregister(itkInPlaceLabelMapFilterLM3)

def itkInPlaceLabelMapFilterLM3___New_orig__() -> "itkInPlaceLabelMapFilterLM3_Pointer":
    """itkInPlaceLabelMapFilterLM3___New_orig__() -> itkInPlaceLabelMapFilterLM3_Pointer"""
    return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3___New_orig__()

def itkInPlaceLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkInPlaceLabelMapFilterLM3 *":
    """itkInPlaceLabelMapFilterLM3_cast(itkLightObject obj) -> itkInPlaceLabelMapFilterLM3"""
    return _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def in_place_label_map_filter(*args, **kwargs):
    """Procedural interface for InPlaceLabelMapFilter"""
    import itk
    instance = itk.InPlaceLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def in_place_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.InPlaceLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.InPlaceLabelMapFilter.values()[0]
    else:
        filter_object = itk.InPlaceLabelMapFilter

    in_place_label_map_filter.__doc__ = filter_object.__doc__
    in_place_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    in_place_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    in_place_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



