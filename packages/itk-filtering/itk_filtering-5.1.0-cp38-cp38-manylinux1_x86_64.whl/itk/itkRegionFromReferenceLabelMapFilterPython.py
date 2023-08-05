# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkRegionFromReferenceLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkRegionFromReferenceLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkRegionFromReferenceLabelMapFilterPython
            return _itkRegionFromReferenceLabelMapFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkRegionFromReferenceLabelMapFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkRegionFromReferenceLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkRegionFromReferenceLabelMapFilterPython
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
import itkMatrixPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vectorPython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkHistogramPython
import itkSamplePython
import itkArrayPython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkOptimizerParametersPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkImageRegionPython
import itkInPlaceLabelMapFilterPython
import ITKLabelMapBasePython
import itkImageSourcePython
import itkVectorImagePython
import itkImagePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkLabelMapFilterPython

def itkRegionFromReferenceLabelMapFilterLM3_New():
  return itkRegionFromReferenceLabelMapFilterLM3.New()


def itkRegionFromReferenceLabelMapFilterLM2_New():
  return itkRegionFromReferenceLabelMapFilterLM2.New()

class itkRegionFromReferenceLabelMapFilterLM2(itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2):
    """


    Set the region from a reference image.

    Change the region of a label map to be the same as one of a reference
    image. This filter implements the same feature as its superclass, but
    with the input region well integrated in the pipeline architecture. If
    the output cannot contain some of the objects' lines, they are
    truncated or removed. All objects fully outside the output region are
    removed.

    This implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/584 orhttp://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    C++ includes: itkRegionFromReferenceLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRegionFromReferenceLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkRegionFromReferenceLabelMapFilterLM2_Pointer"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRegionFromReferenceLabelMapFilterLM2_Pointer":
        """Clone(itkRegionFromReferenceLabelMapFilterLM2 self) -> itkRegionFromReferenceLabelMapFilterLM2_Pointer"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_Clone(self)


    def SetReferenceImage(self, image: 'itkImageBase2') -> "void":
        """
        SetReferenceImage(itkRegionFromReferenceLabelMapFilterLM2 self, itkImageBase2 image)

        Copy the output
        information from another Image. 
        """
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_SetReferenceImage(self, image)


    def GetReferenceImage(self) -> "itkImageBase2 const *":
        """GetReferenceImage(itkRegionFromReferenceLabelMapFilterLM2 self) -> itkImageBase2"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_GetReferenceImage(self)


    def SetInput1(self, input: 'itkLabelMap2') -> "void":
        """
        SetInput1(itkRegionFromReferenceLabelMapFilterLM2 self, itkLabelMap2 input)

        Set the input image 
        """
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_SetInput1(self, input)


    def SetInput2(self, input: 'itkImageBase2') -> "void":
        """
        SetInput2(itkRegionFromReferenceLabelMapFilterLM2 self, itkImageBase2 input)

        Set the reference image

        """
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_SetInput2(self, input)

    __swig_destroy__ = _itkRegionFromReferenceLabelMapFilterPython.delete_itkRegionFromReferenceLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkRegionFromReferenceLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkRegionFromReferenceLabelMapFilterLM2"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkRegionFromReferenceLabelMapFilterLM2

        Create a new object of the class itkRegionFromReferenceLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRegionFromReferenceLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRegionFromReferenceLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRegionFromReferenceLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRegionFromReferenceLabelMapFilterLM2.Clone = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_Clone, None, itkRegionFromReferenceLabelMapFilterLM2)
itkRegionFromReferenceLabelMapFilterLM2.SetReferenceImage = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_SetReferenceImage, None, itkRegionFromReferenceLabelMapFilterLM2)
itkRegionFromReferenceLabelMapFilterLM2.GetReferenceImage = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_GetReferenceImage, None, itkRegionFromReferenceLabelMapFilterLM2)
itkRegionFromReferenceLabelMapFilterLM2.SetInput1 = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_SetInput1, None, itkRegionFromReferenceLabelMapFilterLM2)
itkRegionFromReferenceLabelMapFilterLM2.SetInput2 = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_SetInput2, None, itkRegionFromReferenceLabelMapFilterLM2)
itkRegionFromReferenceLabelMapFilterLM2_swigregister = _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_swigregister
itkRegionFromReferenceLabelMapFilterLM2_swigregister(itkRegionFromReferenceLabelMapFilterLM2)

def itkRegionFromReferenceLabelMapFilterLM2___New_orig__() -> "itkRegionFromReferenceLabelMapFilterLM2_Pointer":
    """itkRegionFromReferenceLabelMapFilterLM2___New_orig__() -> itkRegionFromReferenceLabelMapFilterLM2_Pointer"""
    return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2___New_orig__()

def itkRegionFromReferenceLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkRegionFromReferenceLabelMapFilterLM2 *":
    """itkRegionFromReferenceLabelMapFilterLM2_cast(itkLightObject obj) -> itkRegionFromReferenceLabelMapFilterLM2"""
    return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_cast(obj)

class itkRegionFromReferenceLabelMapFilterLM3(itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3):
    """


    Set the region from a reference image.

    Change the region of a label map to be the same as one of a reference
    image. This filter implements the same feature as its superclass, but
    with the input region well integrated in the pipeline architecture. If
    the output cannot contain some of the objects' lines, they are
    truncated or removed. All objects fully outside the output region are
    removed.

    This implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/584 orhttp://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    C++ includes: itkRegionFromReferenceLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRegionFromReferenceLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkRegionFromReferenceLabelMapFilterLM3_Pointer"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRegionFromReferenceLabelMapFilterLM3_Pointer":
        """Clone(itkRegionFromReferenceLabelMapFilterLM3 self) -> itkRegionFromReferenceLabelMapFilterLM3_Pointer"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_Clone(self)


    def SetReferenceImage(self, image: 'itkImageBase3') -> "void":
        """
        SetReferenceImage(itkRegionFromReferenceLabelMapFilterLM3 self, itkImageBase3 image)

        Copy the output
        information from another Image. 
        """
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_SetReferenceImage(self, image)


    def GetReferenceImage(self) -> "itkImageBase3 const *":
        """GetReferenceImage(itkRegionFromReferenceLabelMapFilterLM3 self) -> itkImageBase3"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_GetReferenceImage(self)


    def SetInput1(self, input: 'itkLabelMap3') -> "void":
        """
        SetInput1(itkRegionFromReferenceLabelMapFilterLM3 self, itkLabelMap3 input)

        Set the input image 
        """
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_SetInput1(self, input)


    def SetInput2(self, input: 'itkImageBase3') -> "void":
        """
        SetInput2(itkRegionFromReferenceLabelMapFilterLM3 self, itkImageBase3 input)

        Set the reference image

        """
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_SetInput2(self, input)

    __swig_destroy__ = _itkRegionFromReferenceLabelMapFilterPython.delete_itkRegionFromReferenceLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkRegionFromReferenceLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkRegionFromReferenceLabelMapFilterLM3"""
        return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkRegionFromReferenceLabelMapFilterLM3

        Create a new object of the class itkRegionFromReferenceLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRegionFromReferenceLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRegionFromReferenceLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRegionFromReferenceLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRegionFromReferenceLabelMapFilterLM3.Clone = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_Clone, None, itkRegionFromReferenceLabelMapFilterLM3)
itkRegionFromReferenceLabelMapFilterLM3.SetReferenceImage = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_SetReferenceImage, None, itkRegionFromReferenceLabelMapFilterLM3)
itkRegionFromReferenceLabelMapFilterLM3.GetReferenceImage = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_GetReferenceImage, None, itkRegionFromReferenceLabelMapFilterLM3)
itkRegionFromReferenceLabelMapFilterLM3.SetInput1 = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_SetInput1, None, itkRegionFromReferenceLabelMapFilterLM3)
itkRegionFromReferenceLabelMapFilterLM3.SetInput2 = new_instancemethod(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_SetInput2, None, itkRegionFromReferenceLabelMapFilterLM3)
itkRegionFromReferenceLabelMapFilterLM3_swigregister = _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_swigregister
itkRegionFromReferenceLabelMapFilterLM3_swigregister(itkRegionFromReferenceLabelMapFilterLM3)

def itkRegionFromReferenceLabelMapFilterLM3___New_orig__() -> "itkRegionFromReferenceLabelMapFilterLM3_Pointer":
    """itkRegionFromReferenceLabelMapFilterLM3___New_orig__() -> itkRegionFromReferenceLabelMapFilterLM3_Pointer"""
    return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3___New_orig__()

def itkRegionFromReferenceLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkRegionFromReferenceLabelMapFilterLM3 *":
    """itkRegionFromReferenceLabelMapFilterLM3_cast(itkLightObject obj) -> itkRegionFromReferenceLabelMapFilterLM3"""
    return _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def region_from_reference_label_map_filter(*args, **kwargs):
    """Procedural interface for RegionFromReferenceLabelMapFilter"""
    import itk
    instance = itk.RegionFromReferenceLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def region_from_reference_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.RegionFromReferenceLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.RegionFromReferenceLabelMapFilter.values()[0]
    else:
        filter_object = itk.RegionFromReferenceLabelMapFilter

    region_from_reference_label_map_filter.__doc__ = filter_object.__doc__
    region_from_reference_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    region_from_reference_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    region_from_reference_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



