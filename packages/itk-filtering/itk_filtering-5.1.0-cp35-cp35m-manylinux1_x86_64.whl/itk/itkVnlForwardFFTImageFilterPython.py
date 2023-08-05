# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkVnlForwardFFTImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkVnlForwardFFTImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkVnlForwardFFTImageFilterPython
            return _itkVnlForwardFFTImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkVnlForwardFFTImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkVnlForwardFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkVnlForwardFFTImageFilterPython
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
import itkForwardFFTImageFilterPython
import itkImageToImageFilterBPython
import itkImageSourcePython
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

def itkVnlForwardFFTImageFilterIF3ICF3_New():
  return itkVnlForwardFFTImageFilterIF3ICF3.New()


def itkVnlForwardFFTImageFilterIF2ICF2_New():
  return itkVnlForwardFFTImageFilterIF2ICF2.New()

class itkVnlForwardFFTImageFilterIF2ICF2(itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2):
    """


    VNL based forward Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   ForwardFFTImageFilter

    C++ includes: itkVnlForwardFFTImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVnlForwardFFTImageFilterIF2ICF2_Pointer":
        """__New_orig__() -> itkVnlForwardFFTImageFilterIF2ICF2_Pointer"""
        return _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF2ICF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVnlForwardFFTImageFilterIF2ICF2_Pointer":
        """Clone(itkVnlForwardFFTImageFilterIF2ICF2 self) -> itkVnlForwardFFTImageFilterIF2ICF2_Pointer"""
        return _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF2ICF2_Clone(self)

    ImageDimensionsMatchCheck = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF2ICF2_ImageDimensionsMatchCheck
    __swig_destroy__ = _itkVnlForwardFFTImageFilterPython.delete_itkVnlForwardFFTImageFilterIF2ICF2

    def cast(obj: 'itkLightObject') -> "itkVnlForwardFFTImageFilterIF2ICF2 *":
        """cast(itkLightObject obj) -> itkVnlForwardFFTImageFilterIF2ICF2"""
        return _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF2ICF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkVnlForwardFFTImageFilterIF2ICF2

        Create a new object of the class itkVnlForwardFFTImageFilterIF2ICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlForwardFFTImageFilterIF2ICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVnlForwardFFTImageFilterIF2ICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVnlForwardFFTImageFilterIF2ICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVnlForwardFFTImageFilterIF2ICF2.Clone = new_instancemethod(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF2ICF2_Clone, None, itkVnlForwardFFTImageFilterIF2ICF2)
itkVnlForwardFFTImageFilterIF2ICF2_swigregister = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF2ICF2_swigregister
itkVnlForwardFFTImageFilterIF2ICF2_swigregister(itkVnlForwardFFTImageFilterIF2ICF2)

def itkVnlForwardFFTImageFilterIF2ICF2___New_orig__() -> "itkVnlForwardFFTImageFilterIF2ICF2_Pointer":
    """itkVnlForwardFFTImageFilterIF2ICF2___New_orig__() -> itkVnlForwardFFTImageFilterIF2ICF2_Pointer"""
    return _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF2ICF2___New_orig__()

def itkVnlForwardFFTImageFilterIF2ICF2_cast(obj: 'itkLightObject') -> "itkVnlForwardFFTImageFilterIF2ICF2 *":
    """itkVnlForwardFFTImageFilterIF2ICF2_cast(itkLightObject obj) -> itkVnlForwardFFTImageFilterIF2ICF2"""
    return _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF2ICF2_cast(obj)

class itkVnlForwardFFTImageFilterIF3ICF3(itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3):
    """


    VNL based forward Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   ForwardFFTImageFilter

    C++ includes: itkVnlForwardFFTImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVnlForwardFFTImageFilterIF3ICF3_Pointer":
        """__New_orig__() -> itkVnlForwardFFTImageFilterIF3ICF3_Pointer"""
        return _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF3ICF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVnlForwardFFTImageFilterIF3ICF3_Pointer":
        """Clone(itkVnlForwardFFTImageFilterIF3ICF3 self) -> itkVnlForwardFFTImageFilterIF3ICF3_Pointer"""
        return _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF3ICF3_Clone(self)

    ImageDimensionsMatchCheck = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF3ICF3_ImageDimensionsMatchCheck
    __swig_destroy__ = _itkVnlForwardFFTImageFilterPython.delete_itkVnlForwardFFTImageFilterIF3ICF3

    def cast(obj: 'itkLightObject') -> "itkVnlForwardFFTImageFilterIF3ICF3 *":
        """cast(itkLightObject obj) -> itkVnlForwardFFTImageFilterIF3ICF3"""
        return _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF3ICF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkVnlForwardFFTImageFilterIF3ICF3

        Create a new object of the class itkVnlForwardFFTImageFilterIF3ICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlForwardFFTImageFilterIF3ICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVnlForwardFFTImageFilterIF3ICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVnlForwardFFTImageFilterIF3ICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVnlForwardFFTImageFilterIF3ICF3.Clone = new_instancemethod(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF3ICF3_Clone, None, itkVnlForwardFFTImageFilterIF3ICF3)
itkVnlForwardFFTImageFilterIF3ICF3_swigregister = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF3ICF3_swigregister
itkVnlForwardFFTImageFilterIF3ICF3_swigregister(itkVnlForwardFFTImageFilterIF3ICF3)

def itkVnlForwardFFTImageFilterIF3ICF3___New_orig__() -> "itkVnlForwardFFTImageFilterIF3ICF3_Pointer":
    """itkVnlForwardFFTImageFilterIF3ICF3___New_orig__() -> itkVnlForwardFFTImageFilterIF3ICF3_Pointer"""
    return _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF3ICF3___New_orig__()

def itkVnlForwardFFTImageFilterIF3ICF3_cast(obj: 'itkLightObject') -> "itkVnlForwardFFTImageFilterIF3ICF3 *":
    """itkVnlForwardFFTImageFilterIF3ICF3_cast(itkLightObject obj) -> itkVnlForwardFFTImageFilterIF3ICF3"""
    return _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF3ICF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def vnl_forward_fft_image_filter(*args, **kwargs):
    """Procedural interface for VnlForwardFFTImageFilter"""
    import itk
    instance = itk.VnlForwardFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def vnl_forward_fft_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.VnlForwardFFTImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.VnlForwardFFTImageFilter.values()[0]
    else:
        filter_object = itk.VnlForwardFFTImageFilter

    vnl_forward_fft_image_filter.__doc__ = filter_object.__doc__
    vnl_forward_fft_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    vnl_forward_fft_image_filter.__doc__ += "Available Keyword Arguments:\n"
    vnl_forward_fft_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



