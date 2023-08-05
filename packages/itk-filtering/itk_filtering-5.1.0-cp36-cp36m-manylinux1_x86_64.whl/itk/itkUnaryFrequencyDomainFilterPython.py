# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkUnaryFrequencyDomainFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkUnaryFrequencyDomainFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkUnaryFrequencyDomainFilterPython
            return _itkUnaryFrequencyDomainFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkUnaryFrequencyDomainFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkUnaryFrequencyDomainFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkUnaryFrequencyDomainFilterPython
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
import itkInPlaceImageFilterBPython
import itkImageToImageFilterBPython
import itkImagePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkSizePython
import itkOffsetPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkCovariantVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkIndexPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkUnaryFrequencyDomainFilterICF3_New():
  return itkUnaryFrequencyDomainFilterICF3.New()


def itkUnaryFrequencyDomainFilterICF2_New():
  return itkUnaryFrequencyDomainFilterICF2.New()

class itkUnaryFrequencyDomainFilterICF2(itkInPlaceImageFilterBPython.itkInPlaceImageFilterICF2ICF2):
    """


    Performs a unary operation on a frequency domain image.

    A frequency filtering functor needs to be supplied via one of
    SetFunctor() overloads. The functor should take FrequencyIteratorType
    reference as its only parameter. If functor configurability is
    required, those parameters should be passed directly to the functor at
    the place of definition.

    Filters in the module ITKImageFrequency work with input images in the
    frequency domain. This filter is templated over a TFrequencyIterator
    depending on the frequency layout of the input image.

    Images in the dual space can be acquired experimentally, from
    scattering experiments or other techniques. In that case use
    FrequencyImageRegionIteratorWithIndex because the layout of dual space
    images is the same as spatial domain images.

    Frequency-domain images can be computed from any spatial-domain
    applying a Fourier Transform. If ForwardFFTImageFilter was used,
    template this filter with the
    FrequencyFFTLayoutImageRegionIteratorWithIndex. Please note that
    FrequencyFFTLayoutImageRegionIteratorWithIndex requires a full FFT,
    and is not compatible with the Hermitian optimization.

    To use this filter with Hermitian (halved-frequency) FFTs, use
    FrequencyHalfHermitianFFTLayoutImageRegionIteratorWithIndex or its
    const version.

    use FrequencyShiftedFFTLayoutImageRegionIteratorWithIndex.

    See:  UnaryGeneratorImageFilter

    C++ includes: itkUnaryFrequencyDomainFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkUnaryFrequencyDomainFilterICF2_Pointer":
        """__New_orig__() -> itkUnaryFrequencyDomainFilterICF2_Pointer"""
        return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkUnaryFrequencyDomainFilterICF2_Pointer":
        """Clone(itkUnaryFrequencyDomainFilterICF2 self) -> itkUnaryFrequencyDomainFilterICF2_Pointer"""
        return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_Clone(self)

    ImageTypeHasNumericTraitsCheck = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_ImageTypeHasNumericTraitsCheck

    def SetActualXDimensionIsOdd(self, _arg: 'bool const') -> "void":
        """
        SetActualXDimensionIsOdd(itkUnaryFrequencyDomainFilterICF2 self, bool const _arg)

        Set to
        true when the you are dealing with images in the frequency domain that
        have been computed using RealToHalfHermitianFFT, and the original
        image in the spatial domain was odd. Only needed when using
        HermitianFrequencyIterator and the original image was odd. 
        """
        return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_SetActualXDimensionIsOdd(self, _arg)


    def GetActualXDimensionIsOdd(self) -> "bool const &":
        """GetActualXDimensionIsOdd(itkUnaryFrequencyDomainFilterICF2 self) -> bool const &"""
        return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_GetActualXDimensionIsOdd(self)


    def ActualXDimensionIsOddOn(self) -> "void":
        """ActualXDimensionIsOddOn(itkUnaryFrequencyDomainFilterICF2 self)"""
        return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_ActualXDimensionIsOddOn(self)


    def ActualXDimensionIsOddOff(self) -> "void":
        """ActualXDimensionIsOddOff(itkUnaryFrequencyDomainFilterICF2 self)"""
        return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_ActualXDimensionIsOddOff(self)

    __swig_destroy__ = _itkUnaryFrequencyDomainFilterPython.delete_itkUnaryFrequencyDomainFilterICF2

    def cast(obj: 'itkLightObject') -> "itkUnaryFrequencyDomainFilterICF2 *":
        """cast(itkLightObject obj) -> itkUnaryFrequencyDomainFilterICF2"""
        return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkUnaryFrequencyDomainFilterICF2

        Create a new object of the class itkUnaryFrequencyDomainFilterICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnaryFrequencyDomainFilterICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkUnaryFrequencyDomainFilterICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkUnaryFrequencyDomainFilterICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkUnaryFrequencyDomainFilterICF2.Clone = new_instancemethod(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_Clone, None, itkUnaryFrequencyDomainFilterICF2)
itkUnaryFrequencyDomainFilterICF2.SetActualXDimensionIsOdd = new_instancemethod(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_SetActualXDimensionIsOdd, None, itkUnaryFrequencyDomainFilterICF2)
itkUnaryFrequencyDomainFilterICF2.GetActualXDimensionIsOdd = new_instancemethod(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_GetActualXDimensionIsOdd, None, itkUnaryFrequencyDomainFilterICF2)
itkUnaryFrequencyDomainFilterICF2.ActualXDimensionIsOddOn = new_instancemethod(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_ActualXDimensionIsOddOn, None, itkUnaryFrequencyDomainFilterICF2)
itkUnaryFrequencyDomainFilterICF2.ActualXDimensionIsOddOff = new_instancemethod(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_ActualXDimensionIsOddOff, None, itkUnaryFrequencyDomainFilterICF2)
itkUnaryFrequencyDomainFilterICF2_swigregister = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_swigregister
itkUnaryFrequencyDomainFilterICF2_swigregister(itkUnaryFrequencyDomainFilterICF2)

def itkUnaryFrequencyDomainFilterICF2___New_orig__() -> "itkUnaryFrequencyDomainFilterICF2_Pointer":
    """itkUnaryFrequencyDomainFilterICF2___New_orig__() -> itkUnaryFrequencyDomainFilterICF2_Pointer"""
    return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2___New_orig__()

def itkUnaryFrequencyDomainFilterICF2_cast(obj: 'itkLightObject') -> "itkUnaryFrequencyDomainFilterICF2 *":
    """itkUnaryFrequencyDomainFilterICF2_cast(itkLightObject obj) -> itkUnaryFrequencyDomainFilterICF2"""
    return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_cast(obj)

class itkUnaryFrequencyDomainFilterICF3(itkInPlaceImageFilterBPython.itkInPlaceImageFilterICF3ICF3):
    """


    Performs a unary operation on a frequency domain image.

    A frequency filtering functor needs to be supplied via one of
    SetFunctor() overloads. The functor should take FrequencyIteratorType
    reference as its only parameter. If functor configurability is
    required, those parameters should be passed directly to the functor at
    the place of definition.

    Filters in the module ITKImageFrequency work with input images in the
    frequency domain. This filter is templated over a TFrequencyIterator
    depending on the frequency layout of the input image.

    Images in the dual space can be acquired experimentally, from
    scattering experiments or other techniques. In that case use
    FrequencyImageRegionIteratorWithIndex because the layout of dual space
    images is the same as spatial domain images.

    Frequency-domain images can be computed from any spatial-domain
    applying a Fourier Transform. If ForwardFFTImageFilter was used,
    template this filter with the
    FrequencyFFTLayoutImageRegionIteratorWithIndex. Please note that
    FrequencyFFTLayoutImageRegionIteratorWithIndex requires a full FFT,
    and is not compatible with the Hermitian optimization.

    To use this filter with Hermitian (halved-frequency) FFTs, use
    FrequencyHalfHermitianFFTLayoutImageRegionIteratorWithIndex or its
    const version.

    use FrequencyShiftedFFTLayoutImageRegionIteratorWithIndex.

    See:  UnaryGeneratorImageFilter

    C++ includes: itkUnaryFrequencyDomainFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkUnaryFrequencyDomainFilterICF3_Pointer":
        """__New_orig__() -> itkUnaryFrequencyDomainFilterICF3_Pointer"""
        return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkUnaryFrequencyDomainFilterICF3_Pointer":
        """Clone(itkUnaryFrequencyDomainFilterICF3 self) -> itkUnaryFrequencyDomainFilterICF3_Pointer"""
        return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_Clone(self)

    ImageTypeHasNumericTraitsCheck = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_ImageTypeHasNumericTraitsCheck

    def SetActualXDimensionIsOdd(self, _arg: 'bool const') -> "void":
        """
        SetActualXDimensionIsOdd(itkUnaryFrequencyDomainFilterICF3 self, bool const _arg)

        Set to
        true when the you are dealing with images in the frequency domain that
        have been computed using RealToHalfHermitianFFT, and the original
        image in the spatial domain was odd. Only needed when using
        HermitianFrequencyIterator and the original image was odd. 
        """
        return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_SetActualXDimensionIsOdd(self, _arg)


    def GetActualXDimensionIsOdd(self) -> "bool const &":
        """GetActualXDimensionIsOdd(itkUnaryFrequencyDomainFilterICF3 self) -> bool const &"""
        return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_GetActualXDimensionIsOdd(self)


    def ActualXDimensionIsOddOn(self) -> "void":
        """ActualXDimensionIsOddOn(itkUnaryFrequencyDomainFilterICF3 self)"""
        return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_ActualXDimensionIsOddOn(self)


    def ActualXDimensionIsOddOff(self) -> "void":
        """ActualXDimensionIsOddOff(itkUnaryFrequencyDomainFilterICF3 self)"""
        return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_ActualXDimensionIsOddOff(self)

    __swig_destroy__ = _itkUnaryFrequencyDomainFilterPython.delete_itkUnaryFrequencyDomainFilterICF3

    def cast(obj: 'itkLightObject') -> "itkUnaryFrequencyDomainFilterICF3 *":
        """cast(itkLightObject obj) -> itkUnaryFrequencyDomainFilterICF3"""
        return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkUnaryFrequencyDomainFilterICF3

        Create a new object of the class itkUnaryFrequencyDomainFilterICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnaryFrequencyDomainFilterICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkUnaryFrequencyDomainFilterICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkUnaryFrequencyDomainFilterICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkUnaryFrequencyDomainFilterICF3.Clone = new_instancemethod(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_Clone, None, itkUnaryFrequencyDomainFilterICF3)
itkUnaryFrequencyDomainFilterICF3.SetActualXDimensionIsOdd = new_instancemethod(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_SetActualXDimensionIsOdd, None, itkUnaryFrequencyDomainFilterICF3)
itkUnaryFrequencyDomainFilterICF3.GetActualXDimensionIsOdd = new_instancemethod(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_GetActualXDimensionIsOdd, None, itkUnaryFrequencyDomainFilterICF3)
itkUnaryFrequencyDomainFilterICF3.ActualXDimensionIsOddOn = new_instancemethod(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_ActualXDimensionIsOddOn, None, itkUnaryFrequencyDomainFilterICF3)
itkUnaryFrequencyDomainFilterICF3.ActualXDimensionIsOddOff = new_instancemethod(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_ActualXDimensionIsOddOff, None, itkUnaryFrequencyDomainFilterICF3)
itkUnaryFrequencyDomainFilterICF3_swigregister = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_swigregister
itkUnaryFrequencyDomainFilterICF3_swigregister(itkUnaryFrequencyDomainFilterICF3)

def itkUnaryFrequencyDomainFilterICF3___New_orig__() -> "itkUnaryFrequencyDomainFilterICF3_Pointer":
    """itkUnaryFrequencyDomainFilterICF3___New_orig__() -> itkUnaryFrequencyDomainFilterICF3_Pointer"""
    return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3___New_orig__()

def itkUnaryFrequencyDomainFilterICF3_cast(obj: 'itkLightObject') -> "itkUnaryFrequencyDomainFilterICF3 *":
    """itkUnaryFrequencyDomainFilterICF3_cast(itkLightObject obj) -> itkUnaryFrequencyDomainFilterICF3"""
    return _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def unary_frequency_domain_filter(*args, **kwargs):
    """Procedural interface for UnaryFrequencyDomainFilter"""
    import itk
    instance = itk.UnaryFrequencyDomainFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def unary_frequency_domain_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.UnaryFrequencyDomainFilter, itkTemplate.itkTemplate):
        filter_object = itk.UnaryFrequencyDomainFilter.values()[0]
    else:
        filter_object = itk.UnaryFrequencyDomainFilter

    unary_frequency_domain_filter.__doc__ = filter_object.__doc__
    unary_frequency_domain_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    unary_frequency_domain_filter.__doc__ += "Available Keyword Arguments:\n"
    unary_frequency_domain_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



