# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkInverseFFTImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkInverseFFTImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkInverseFFTImageFilterPython
            return _itkInverseFFTImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkInverseFFTImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkInverseFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkInverseFFTImageFilterPython
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
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
import pyBasePython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import ITKCommonBasePython
import itkImagePython
import itkPointPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkVectorPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkInverseFFTImageFilterICF3IF3_New():
  return itkInverseFFTImageFilterICF3IF3.New()


def itkInverseFFTImageFilterICF2IF2_New():
  return itkInverseFFTImageFilterICF2IF2.New()

class itkInverseFFTImageFilterICF2IF2(itkImageToImageFilterBPython.itkImageToImageFilterICF2IF2):
    """


    Base class for inverse Fast Fourier Transform.

    This is a base class for the "inverse" or "reverse" Discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child available on the system
    when the object is created via the object factory system.

    This class transforms a full complex image with Hermitian symmetry
    into its real spatial domain representation. If the input does not
    have Hermitian symmetry, the imaginary component is discarded.

    See:   ForwardFFTImageFilter, InverseFFTImageFilter

    C++ includes: itkInverseFFTImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkInverseFFTImageFilterICF2IF2_Pointer":
        """__New_orig__() -> itkInverseFFTImageFilterICF2IF2_Pointer"""
        return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def GetSizeGreatestPrimeFactor(self) -> "unsigned long":
        """GetSizeGreatestPrimeFactor(itkInverseFFTImageFilterICF2IF2 self) -> unsigned long"""
        return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_GetSizeGreatestPrimeFactor(self)

    __swig_destroy__ = _itkInverseFFTImageFilterPython.delete_itkInverseFFTImageFilterICF2IF2

    def cast(obj: 'itkLightObject') -> "itkInverseFFTImageFilterICF2IF2 *":
        """cast(itkLightObject obj) -> itkInverseFFTImageFilterICF2IF2"""
        return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkInverseFFTImageFilterICF2IF2

        Create a new object of the class itkInverseFFTImageFilterICF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseFFTImageFilterICF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkInverseFFTImageFilterICF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkInverseFFTImageFilterICF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkInverseFFTImageFilterICF2IF2.GetSizeGreatestPrimeFactor = new_instancemethod(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_GetSizeGreatestPrimeFactor, None, itkInverseFFTImageFilterICF2IF2)
itkInverseFFTImageFilterICF2IF2_swigregister = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_swigregister
itkInverseFFTImageFilterICF2IF2_swigregister(itkInverseFFTImageFilterICF2IF2)

def itkInverseFFTImageFilterICF2IF2___New_orig__() -> "itkInverseFFTImageFilterICF2IF2_Pointer":
    """itkInverseFFTImageFilterICF2IF2___New_orig__() -> itkInverseFFTImageFilterICF2IF2_Pointer"""
    return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2___New_orig__()

def itkInverseFFTImageFilterICF2IF2_cast(obj: 'itkLightObject') -> "itkInverseFFTImageFilterICF2IF2 *":
    """itkInverseFFTImageFilterICF2IF2_cast(itkLightObject obj) -> itkInverseFFTImageFilterICF2IF2"""
    return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_cast(obj)

class itkInverseFFTImageFilterICF3IF3(itkImageToImageFilterBPython.itkImageToImageFilterICF3IF3):
    """


    Base class for inverse Fast Fourier Transform.

    This is a base class for the "inverse" or "reverse" Discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child available on the system
    when the object is created via the object factory system.

    This class transforms a full complex image with Hermitian symmetry
    into its real spatial domain representation. If the input does not
    have Hermitian symmetry, the imaginary component is discarded.

    See:   ForwardFFTImageFilter, InverseFFTImageFilter

    C++ includes: itkInverseFFTImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkInverseFFTImageFilterICF3IF3_Pointer":
        """__New_orig__() -> itkInverseFFTImageFilterICF3IF3_Pointer"""
        return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def GetSizeGreatestPrimeFactor(self) -> "unsigned long":
        """GetSizeGreatestPrimeFactor(itkInverseFFTImageFilterICF3IF3 self) -> unsigned long"""
        return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_GetSizeGreatestPrimeFactor(self)

    __swig_destroy__ = _itkInverseFFTImageFilterPython.delete_itkInverseFFTImageFilterICF3IF3

    def cast(obj: 'itkLightObject') -> "itkInverseFFTImageFilterICF3IF3 *":
        """cast(itkLightObject obj) -> itkInverseFFTImageFilterICF3IF3"""
        return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkInverseFFTImageFilterICF3IF3

        Create a new object of the class itkInverseFFTImageFilterICF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseFFTImageFilterICF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkInverseFFTImageFilterICF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkInverseFFTImageFilterICF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkInverseFFTImageFilterICF3IF3.GetSizeGreatestPrimeFactor = new_instancemethod(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_GetSizeGreatestPrimeFactor, None, itkInverseFFTImageFilterICF3IF3)
itkInverseFFTImageFilterICF3IF3_swigregister = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_swigregister
itkInverseFFTImageFilterICF3IF3_swigregister(itkInverseFFTImageFilterICF3IF3)

def itkInverseFFTImageFilterICF3IF3___New_orig__() -> "itkInverseFFTImageFilterICF3IF3_Pointer":
    """itkInverseFFTImageFilterICF3IF3___New_orig__() -> itkInverseFFTImageFilterICF3IF3_Pointer"""
    return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3___New_orig__()

def itkInverseFFTImageFilterICF3IF3_cast(obj: 'itkLightObject') -> "itkInverseFFTImageFilterICF3IF3 *":
    """itkInverseFFTImageFilterICF3IF3_cast(itkLightObject obj) -> itkInverseFFTImageFilterICF3IF3"""
    return _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def inverse_fft_image_filter(*args, **kwargs):
    """Procedural interface for InverseFFTImageFilter"""
    import itk
    instance = itk.InverseFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def inverse_fft_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.InverseFFTImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.InverseFFTImageFilter.values()[0]
    else:
        filter_object = itk.InverseFFTImageFilter

    inverse_fft_image_filter.__doc__ = filter_object.__doc__
    inverse_fft_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    inverse_fft_image_filter.__doc__ += "Available Keyword Arguments:\n"
    inverse_fft_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



