# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkForwardFFTImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkForwardFFTImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkForwardFFTImageFilterPython
            return _itkForwardFFTImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkForwardFFTImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkForwardFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkForwardFFTImageFilterPython
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


import itkImageToImageFilterBPython
import itkImagePython
import ITKCommonBasePython
import pyBasePython
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

def itkForwardFFTImageFilterIF3ICF3_New():
  return itkForwardFFTImageFilterIF3ICF3.New()


def itkForwardFFTImageFilterIF2ICF2_New():
  return itkForwardFFTImageFilterIF2ICF2.New()

class itkForwardFFTImageFilterIF2ICF2(itkImageToImageFilterBPython.itkImageToImageFilterIF2ICF2):
    """


    Base class for forward Fast Fourier Transform.

    This is a base class for the "forward" or "direct" discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child class available on the
    system when the object is created via the object factory system.

    This class transforms a real input image into its full complex Fourier
    transform. The Fourier transform of a real input image has Hermitian
    symmetry: $ f(\\mathbf{x}) = f^*(-\\mathbf{x}) $. That is, when
    the result of the transform is split in half along the x-dimension,
    the values in the second half of the transform are the complex
    conjugates of values in the first half reflected about the center of
    the image in each dimension.

    This filter works only for real single-component input image types.

    The output generated from a ForwardFFTImageFilter is in the dual space
    or frequency domain. Refer to
    FrequencyFFTLayoutImageRegionConstIteratorWithIndex for a description
    of the layout of frequencies generated after a forward FFT. Also see
    ITKImageFrequency for a set of filters requiring input images in the
    frequency domain.

    See:   InverseFFTImageFilter, FFTComplexToComplexImageFilter

    C++ includes: itkForwardFFTImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkForwardFFTImageFilterIF2ICF2_Pointer":
        """__New_orig__() -> itkForwardFFTImageFilterIF2ICF2_Pointer"""
        return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def GetSizeGreatestPrimeFactor(self) -> "unsigned long":
        """GetSizeGreatestPrimeFactor(itkForwardFFTImageFilterIF2ICF2 self) -> unsigned long"""
        return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2_GetSizeGreatestPrimeFactor(self)

    __swig_destroy__ = _itkForwardFFTImageFilterPython.delete_itkForwardFFTImageFilterIF2ICF2

    def cast(obj: 'itkLightObject') -> "itkForwardFFTImageFilterIF2ICF2 *":
        """cast(itkLightObject obj) -> itkForwardFFTImageFilterIF2ICF2"""
        return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkForwardFFTImageFilterIF2ICF2

        Create a new object of the class itkForwardFFTImageFilterIF2ICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkForwardFFTImageFilterIF2ICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkForwardFFTImageFilterIF2ICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkForwardFFTImageFilterIF2ICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkForwardFFTImageFilterIF2ICF2.GetSizeGreatestPrimeFactor = new_instancemethod(_itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2_GetSizeGreatestPrimeFactor, None, itkForwardFFTImageFilterIF2ICF2)
itkForwardFFTImageFilterIF2ICF2_swigregister = _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2_swigregister
itkForwardFFTImageFilterIF2ICF2_swigregister(itkForwardFFTImageFilterIF2ICF2)

def itkForwardFFTImageFilterIF2ICF2___New_orig__() -> "itkForwardFFTImageFilterIF2ICF2_Pointer":
    """itkForwardFFTImageFilterIF2ICF2___New_orig__() -> itkForwardFFTImageFilterIF2ICF2_Pointer"""
    return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2___New_orig__()

def itkForwardFFTImageFilterIF2ICF2_cast(obj: 'itkLightObject') -> "itkForwardFFTImageFilterIF2ICF2 *":
    """itkForwardFFTImageFilterIF2ICF2_cast(itkLightObject obj) -> itkForwardFFTImageFilterIF2ICF2"""
    return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2_cast(obj)

class itkForwardFFTImageFilterIF3ICF3(itkImageToImageFilterBPython.itkImageToImageFilterIF3ICF3):
    """


    Base class for forward Fast Fourier Transform.

    This is a base class for the "forward" or "direct" discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child class available on the
    system when the object is created via the object factory system.

    This class transforms a real input image into its full complex Fourier
    transform. The Fourier transform of a real input image has Hermitian
    symmetry: $ f(\\mathbf{x}) = f^*(-\\mathbf{x}) $. That is, when
    the result of the transform is split in half along the x-dimension,
    the values in the second half of the transform are the complex
    conjugates of values in the first half reflected about the center of
    the image in each dimension.

    This filter works only for real single-component input image types.

    The output generated from a ForwardFFTImageFilter is in the dual space
    or frequency domain. Refer to
    FrequencyFFTLayoutImageRegionConstIteratorWithIndex for a description
    of the layout of frequencies generated after a forward FFT. Also see
    ITKImageFrequency for a set of filters requiring input images in the
    frequency domain.

    See:   InverseFFTImageFilter, FFTComplexToComplexImageFilter

    C++ includes: itkForwardFFTImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkForwardFFTImageFilterIF3ICF3_Pointer":
        """__New_orig__() -> itkForwardFFTImageFilterIF3ICF3_Pointer"""
        return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def GetSizeGreatestPrimeFactor(self) -> "unsigned long":
        """GetSizeGreatestPrimeFactor(itkForwardFFTImageFilterIF3ICF3 self) -> unsigned long"""
        return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3_GetSizeGreatestPrimeFactor(self)

    __swig_destroy__ = _itkForwardFFTImageFilterPython.delete_itkForwardFFTImageFilterIF3ICF3

    def cast(obj: 'itkLightObject') -> "itkForwardFFTImageFilterIF3ICF3 *":
        """cast(itkLightObject obj) -> itkForwardFFTImageFilterIF3ICF3"""
        return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkForwardFFTImageFilterIF3ICF3

        Create a new object of the class itkForwardFFTImageFilterIF3ICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkForwardFFTImageFilterIF3ICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkForwardFFTImageFilterIF3ICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkForwardFFTImageFilterIF3ICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkForwardFFTImageFilterIF3ICF3.GetSizeGreatestPrimeFactor = new_instancemethod(_itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3_GetSizeGreatestPrimeFactor, None, itkForwardFFTImageFilterIF3ICF3)
itkForwardFFTImageFilterIF3ICF3_swigregister = _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3_swigregister
itkForwardFFTImageFilterIF3ICF3_swigregister(itkForwardFFTImageFilterIF3ICF3)

def itkForwardFFTImageFilterIF3ICF3___New_orig__() -> "itkForwardFFTImageFilterIF3ICF3_Pointer":
    """itkForwardFFTImageFilterIF3ICF3___New_orig__() -> itkForwardFFTImageFilterIF3ICF3_Pointer"""
    return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3___New_orig__()

def itkForwardFFTImageFilterIF3ICF3_cast(obj: 'itkLightObject') -> "itkForwardFFTImageFilterIF3ICF3 *":
    """itkForwardFFTImageFilterIF3ICF3_cast(itkLightObject obj) -> itkForwardFFTImageFilterIF3ICF3"""
    return _itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def forward_fft_image_filter(*args, **kwargs):
    """Procedural interface for ForwardFFTImageFilter"""
    import itk
    instance = itk.ForwardFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def forward_fft_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ForwardFFTImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.ForwardFFTImageFilter.values()[0]
    else:
        filter_object = itk.ForwardFFTImageFilter

    forward_fft_image_filter.__doc__ = filter_object.__doc__
    forward_fft_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    forward_fft_image_filter.__doc__ += "Available Keyword Arguments:\n"
    forward_fft_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



