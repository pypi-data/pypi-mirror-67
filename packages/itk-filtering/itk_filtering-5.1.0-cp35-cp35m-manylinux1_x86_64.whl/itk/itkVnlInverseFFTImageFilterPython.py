# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkVnlInverseFFTImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkVnlInverseFFTImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkVnlInverseFFTImageFilterPython
            return _itkVnlInverseFFTImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkVnlInverseFFTImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkVnlInverseFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkVnlInverseFFTImageFilterPython
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


import itkInverseFFTImageFilterPython
import itkImageToImageFilterBPython
import itkImageSourcePython
import ITKCommonBasePython
import pyBasePython
import itkImagePython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
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
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkVnlInverseFFTImageFilterICF3IF3_New():
  return itkVnlInverseFFTImageFilterICF3IF3.New()


def itkVnlInverseFFTImageFilterICF2IF2_New():
  return itkVnlInverseFFTImageFilterICF2IF2.New()

class itkVnlInverseFFTImageFilterICF2IF2(itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2):
    """


    VNL-based reverse Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   InverseFFTImageFilter

    C++ includes: itkVnlInverseFFTImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVnlInverseFFTImageFilterICF2IF2_Pointer":
        """__New_orig__() -> itkVnlInverseFFTImageFilterICF2IF2_Pointer"""
        return _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVnlInverseFFTImageFilterICF2IF2_Pointer":
        """Clone(itkVnlInverseFFTImageFilterICF2IF2 self) -> itkVnlInverseFFTImageFilterICF2IF2_Pointer"""
        return _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2_Clone(self)

    PixelUnsignedIntDivisionOperatorsCheck = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2_PixelUnsignedIntDivisionOperatorsCheck
    ImageDimensionsMatchCheck = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2_ImageDimensionsMatchCheck
    __swig_destroy__ = _itkVnlInverseFFTImageFilterPython.delete_itkVnlInverseFFTImageFilterICF2IF2

    def cast(obj: 'itkLightObject') -> "itkVnlInverseFFTImageFilterICF2IF2 *":
        """cast(itkLightObject obj) -> itkVnlInverseFFTImageFilterICF2IF2"""
        return _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkVnlInverseFFTImageFilterICF2IF2

        Create a new object of the class itkVnlInverseFFTImageFilterICF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlInverseFFTImageFilterICF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVnlInverseFFTImageFilterICF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVnlInverseFFTImageFilterICF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVnlInverseFFTImageFilterICF2IF2.Clone = new_instancemethod(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2_Clone, None, itkVnlInverseFFTImageFilterICF2IF2)
itkVnlInverseFFTImageFilterICF2IF2_swigregister = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2_swigregister
itkVnlInverseFFTImageFilterICF2IF2_swigregister(itkVnlInverseFFTImageFilterICF2IF2)

def itkVnlInverseFFTImageFilterICF2IF2___New_orig__() -> "itkVnlInverseFFTImageFilterICF2IF2_Pointer":
    """itkVnlInverseFFTImageFilterICF2IF2___New_orig__() -> itkVnlInverseFFTImageFilterICF2IF2_Pointer"""
    return _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2___New_orig__()

def itkVnlInverseFFTImageFilterICF2IF2_cast(obj: 'itkLightObject') -> "itkVnlInverseFFTImageFilterICF2IF2 *":
    """itkVnlInverseFFTImageFilterICF2IF2_cast(itkLightObject obj) -> itkVnlInverseFFTImageFilterICF2IF2"""
    return _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2_cast(obj)

class itkVnlInverseFFTImageFilterICF3IF3(itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3):
    """


    VNL-based reverse Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   InverseFFTImageFilter

    C++ includes: itkVnlInverseFFTImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVnlInverseFFTImageFilterICF3IF3_Pointer":
        """__New_orig__() -> itkVnlInverseFFTImageFilterICF3IF3_Pointer"""
        return _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVnlInverseFFTImageFilterICF3IF3_Pointer":
        """Clone(itkVnlInverseFFTImageFilterICF3IF3 self) -> itkVnlInverseFFTImageFilterICF3IF3_Pointer"""
        return _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3_Clone(self)

    PixelUnsignedIntDivisionOperatorsCheck = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3_PixelUnsignedIntDivisionOperatorsCheck
    ImageDimensionsMatchCheck = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3_ImageDimensionsMatchCheck
    __swig_destroy__ = _itkVnlInverseFFTImageFilterPython.delete_itkVnlInverseFFTImageFilterICF3IF3

    def cast(obj: 'itkLightObject') -> "itkVnlInverseFFTImageFilterICF3IF3 *":
        """cast(itkLightObject obj) -> itkVnlInverseFFTImageFilterICF3IF3"""
        return _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkVnlInverseFFTImageFilterICF3IF3

        Create a new object of the class itkVnlInverseFFTImageFilterICF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlInverseFFTImageFilterICF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVnlInverseFFTImageFilterICF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVnlInverseFFTImageFilterICF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVnlInverseFFTImageFilterICF3IF3.Clone = new_instancemethod(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3_Clone, None, itkVnlInverseFFTImageFilterICF3IF3)
itkVnlInverseFFTImageFilterICF3IF3_swigregister = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3_swigregister
itkVnlInverseFFTImageFilterICF3IF3_swigregister(itkVnlInverseFFTImageFilterICF3IF3)

def itkVnlInverseFFTImageFilterICF3IF3___New_orig__() -> "itkVnlInverseFFTImageFilterICF3IF3_Pointer":
    """itkVnlInverseFFTImageFilterICF3IF3___New_orig__() -> itkVnlInverseFFTImageFilterICF3IF3_Pointer"""
    return _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3___New_orig__()

def itkVnlInverseFFTImageFilterICF3IF3_cast(obj: 'itkLightObject') -> "itkVnlInverseFFTImageFilterICF3IF3 *":
    """itkVnlInverseFFTImageFilterICF3IF3_cast(itkLightObject obj) -> itkVnlInverseFFTImageFilterICF3IF3"""
    return _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def vnl_inverse_fft_image_filter(*args, **kwargs):
    """Procedural interface for VnlInverseFFTImageFilter"""
    import itk
    instance = itk.VnlInverseFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def vnl_inverse_fft_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.VnlInverseFFTImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.VnlInverseFFTImageFilter.values()[0]
    else:
        filter_object = itk.VnlInverseFFTImageFilter

    vnl_inverse_fft_image_filter.__doc__ = filter_object.__doc__
    vnl_inverse_fft_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    vnl_inverse_fft_image_filter.__doc__ += "Available Keyword Arguments:\n"
    vnl_inverse_fft_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



