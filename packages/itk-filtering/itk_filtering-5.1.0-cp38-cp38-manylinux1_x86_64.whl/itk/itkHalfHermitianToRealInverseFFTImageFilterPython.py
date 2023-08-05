# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkHalfHermitianToRealInverseFFTImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkHalfHermitianToRealInverseFFTImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkHalfHermitianToRealInverseFFTImageFilterPython
            return _itkHalfHermitianToRealInverseFFTImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkHalfHermitianToRealInverseFFTImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkHalfHermitianToRealInverseFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkHalfHermitianToRealInverseFFTImageFilterPython
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


import itkSimpleDataObjectDecoratorPython
import itkArrayPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import itkRGBAPixelPython
import itkFixedArrayPython
import itkRGBPixelPython
import itkCovariantVectorPython
import vnl_vector_refPython
import itkVectorPython
import ITKCommonBasePython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkVariableLengthVectorPython
import itkImagePython
import itkPointPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython

def itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_New():
  return itkHalfHermitianToRealInverseFFTImageFilterICF3IF3.New()


def itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_New():
  return itkHalfHermitianToRealInverseFFTImageFilterICF2IF2.New()

class itkHalfHermitianToRealInverseFFTImageFilterICF2IF2(itkImageToImageFilterBPython.itkImageToImageFilterICF2IF2):
    """


    Base class for specialized complex-to-real inverse Fast Fourier
    Transform.

    This is a base class for the "inverse" or "reverse" Discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child class available on the
    system when the object is created via the object factory system.

    The input to this filter is assumed to have the same format as the
    output of the RealToHalfHermitianForwardFFTImageFilter. That is, the
    input is assumed to consist of roughly half the full complex image
    resulting from a real-to-complex discrete Fourier transform. This half
    is expected to be the first half of the image in the X-dimension.
    Because this filter assumes that the input stores only about half of
    the non-redundant complex pixels, the output is larger in the
    X-dimension than it is in the input. To determine the actual size of
    the output image, this filter needs additional information in the form
    of a flag indicating whether the output image has an odd size in the
    X-dimension. Use SetActualXDimensionIsOdd() to set this flag.

    See:   ForwardFFTImageFilter, HalfHermitianToRealInverseFFTImageFilter

    C++ includes: itkHalfHermitianToRealInverseFFTImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_Pointer":
        """__New_orig__() -> itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_Pointer"""
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def SetActualXDimensionIsOddInput(self, _arg: 'itkSimpleDataObjectDecoratorB') -> "void":
        """SetActualXDimensionIsOddInput(itkHalfHermitianToRealInverseFFTImageFilterICF2IF2 self, itkSimpleDataObjectDecoratorB _arg)"""
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_SetActualXDimensionIsOddInput(self, _arg)


    def SetActualXDimensionIsOdd(self, *args) -> "void":
        """
        SetActualXDimensionIsOdd(itkHalfHermitianToRealInverseFFTImageFilterICF2IF2 self, itkSimpleDataObjectDecoratorB _arg)
        SetActualXDimensionIsOdd(itkHalfHermitianToRealInverseFFTImageFilterICF2IF2 self, bool const & _arg)
        """
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_SetActualXDimensionIsOdd(self, *args)


    def GetActualXDimensionIsOddInput(self) -> "itkSimpleDataObjectDecoratorB const *":
        """GetActualXDimensionIsOddInput(itkHalfHermitianToRealInverseFFTImageFilterICF2IF2 self) -> itkSimpleDataObjectDecoratorB"""
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_GetActualXDimensionIsOddInput(self)


    def GetActualXDimensionIsOdd(self) -> "bool const &":
        """GetActualXDimensionIsOdd(itkHalfHermitianToRealInverseFFTImageFilterICF2IF2 self) -> bool const &"""
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_GetActualXDimensionIsOdd(self)


    def ActualXDimensionIsOddOn(self) -> "void":
        """ActualXDimensionIsOddOn(itkHalfHermitianToRealInverseFFTImageFilterICF2IF2 self)"""
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_ActualXDimensionIsOddOn(self)


    def ActualXDimensionIsOddOff(self) -> "void":
        """ActualXDimensionIsOddOff(itkHalfHermitianToRealInverseFFTImageFilterICF2IF2 self)"""
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_ActualXDimensionIsOddOff(self)


    def GetSizeGreatestPrimeFactor(self) -> "unsigned long":
        """GetSizeGreatestPrimeFactor(itkHalfHermitianToRealInverseFFTImageFilterICF2IF2 self) -> unsigned long"""
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_GetSizeGreatestPrimeFactor(self)

    __swig_destroy__ = _itkHalfHermitianToRealInverseFFTImageFilterPython.delete_itkHalfHermitianToRealInverseFFTImageFilterICF2IF2

    def cast(obj: 'itkLightObject') -> "itkHalfHermitianToRealInverseFFTImageFilterICF2IF2 *":
        """cast(itkLightObject obj) -> itkHalfHermitianToRealInverseFFTImageFilterICF2IF2"""
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkHalfHermitianToRealInverseFFTImageFilterICF2IF2

        Create a new object of the class itkHalfHermitianToRealInverseFFTImageFilterICF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfHermitianToRealInverseFFTImageFilterICF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHalfHermitianToRealInverseFFTImageFilterICF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHalfHermitianToRealInverseFFTImageFilterICF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkHalfHermitianToRealInverseFFTImageFilterICF2IF2.SetActualXDimensionIsOddInput = new_instancemethod(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_SetActualXDimensionIsOddInput, None, itkHalfHermitianToRealInverseFFTImageFilterICF2IF2)
itkHalfHermitianToRealInverseFFTImageFilterICF2IF2.SetActualXDimensionIsOdd = new_instancemethod(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_SetActualXDimensionIsOdd, None, itkHalfHermitianToRealInverseFFTImageFilterICF2IF2)
itkHalfHermitianToRealInverseFFTImageFilterICF2IF2.GetActualXDimensionIsOddInput = new_instancemethod(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_GetActualXDimensionIsOddInput, None, itkHalfHermitianToRealInverseFFTImageFilterICF2IF2)
itkHalfHermitianToRealInverseFFTImageFilterICF2IF2.GetActualXDimensionIsOdd = new_instancemethod(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_GetActualXDimensionIsOdd, None, itkHalfHermitianToRealInverseFFTImageFilterICF2IF2)
itkHalfHermitianToRealInverseFFTImageFilterICF2IF2.ActualXDimensionIsOddOn = new_instancemethod(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_ActualXDimensionIsOddOn, None, itkHalfHermitianToRealInverseFFTImageFilterICF2IF2)
itkHalfHermitianToRealInverseFFTImageFilterICF2IF2.ActualXDimensionIsOddOff = new_instancemethod(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_ActualXDimensionIsOddOff, None, itkHalfHermitianToRealInverseFFTImageFilterICF2IF2)
itkHalfHermitianToRealInverseFFTImageFilterICF2IF2.GetSizeGreatestPrimeFactor = new_instancemethod(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_GetSizeGreatestPrimeFactor, None, itkHalfHermitianToRealInverseFFTImageFilterICF2IF2)
itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_swigregister = _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_swigregister
itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_swigregister(itkHalfHermitianToRealInverseFFTImageFilterICF2IF2)

def itkHalfHermitianToRealInverseFFTImageFilterICF2IF2___New_orig__() -> "itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_Pointer":
    """itkHalfHermitianToRealInverseFFTImageFilterICF2IF2___New_orig__() -> itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_Pointer"""
    return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2___New_orig__()

def itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_cast(obj: 'itkLightObject') -> "itkHalfHermitianToRealInverseFFTImageFilterICF2IF2 *":
    """itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_cast(itkLightObject obj) -> itkHalfHermitianToRealInverseFFTImageFilterICF2IF2"""
    return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_cast(obj)

class itkHalfHermitianToRealInverseFFTImageFilterICF3IF3(itkImageToImageFilterBPython.itkImageToImageFilterICF3IF3):
    """


    Base class for specialized complex-to-real inverse Fast Fourier
    Transform.

    This is a base class for the "inverse" or "reverse" Discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child class available on the
    system when the object is created via the object factory system.

    The input to this filter is assumed to have the same format as the
    output of the RealToHalfHermitianForwardFFTImageFilter. That is, the
    input is assumed to consist of roughly half the full complex image
    resulting from a real-to-complex discrete Fourier transform. This half
    is expected to be the first half of the image in the X-dimension.
    Because this filter assumes that the input stores only about half of
    the non-redundant complex pixels, the output is larger in the
    X-dimension than it is in the input. To determine the actual size of
    the output image, this filter needs additional information in the form
    of a flag indicating whether the output image has an odd size in the
    X-dimension. Use SetActualXDimensionIsOdd() to set this flag.

    See:   ForwardFFTImageFilter, HalfHermitianToRealInverseFFTImageFilter

    C++ includes: itkHalfHermitianToRealInverseFFTImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_Pointer":
        """__New_orig__() -> itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_Pointer"""
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def SetActualXDimensionIsOddInput(self, _arg: 'itkSimpleDataObjectDecoratorB') -> "void":
        """SetActualXDimensionIsOddInput(itkHalfHermitianToRealInverseFFTImageFilterICF3IF3 self, itkSimpleDataObjectDecoratorB _arg)"""
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_SetActualXDimensionIsOddInput(self, _arg)


    def SetActualXDimensionIsOdd(self, *args) -> "void":
        """
        SetActualXDimensionIsOdd(itkHalfHermitianToRealInverseFFTImageFilterICF3IF3 self, itkSimpleDataObjectDecoratorB _arg)
        SetActualXDimensionIsOdd(itkHalfHermitianToRealInverseFFTImageFilterICF3IF3 self, bool const & _arg)
        """
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_SetActualXDimensionIsOdd(self, *args)


    def GetActualXDimensionIsOddInput(self) -> "itkSimpleDataObjectDecoratorB const *":
        """GetActualXDimensionIsOddInput(itkHalfHermitianToRealInverseFFTImageFilterICF3IF3 self) -> itkSimpleDataObjectDecoratorB"""
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_GetActualXDimensionIsOddInput(self)


    def GetActualXDimensionIsOdd(self) -> "bool const &":
        """GetActualXDimensionIsOdd(itkHalfHermitianToRealInverseFFTImageFilterICF3IF3 self) -> bool const &"""
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_GetActualXDimensionIsOdd(self)


    def ActualXDimensionIsOddOn(self) -> "void":
        """ActualXDimensionIsOddOn(itkHalfHermitianToRealInverseFFTImageFilterICF3IF3 self)"""
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_ActualXDimensionIsOddOn(self)


    def ActualXDimensionIsOddOff(self) -> "void":
        """ActualXDimensionIsOddOff(itkHalfHermitianToRealInverseFFTImageFilterICF3IF3 self)"""
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_ActualXDimensionIsOddOff(self)


    def GetSizeGreatestPrimeFactor(self) -> "unsigned long":
        """GetSizeGreatestPrimeFactor(itkHalfHermitianToRealInverseFFTImageFilterICF3IF3 self) -> unsigned long"""
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_GetSizeGreatestPrimeFactor(self)

    __swig_destroy__ = _itkHalfHermitianToRealInverseFFTImageFilterPython.delete_itkHalfHermitianToRealInverseFFTImageFilterICF3IF3

    def cast(obj: 'itkLightObject') -> "itkHalfHermitianToRealInverseFFTImageFilterICF3IF3 *":
        """cast(itkLightObject obj) -> itkHalfHermitianToRealInverseFFTImageFilterICF3IF3"""
        return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkHalfHermitianToRealInverseFFTImageFilterICF3IF3

        Create a new object of the class itkHalfHermitianToRealInverseFFTImageFilterICF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfHermitianToRealInverseFFTImageFilterICF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHalfHermitianToRealInverseFFTImageFilterICF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHalfHermitianToRealInverseFFTImageFilterICF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkHalfHermitianToRealInverseFFTImageFilterICF3IF3.SetActualXDimensionIsOddInput = new_instancemethod(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_SetActualXDimensionIsOddInput, None, itkHalfHermitianToRealInverseFFTImageFilterICF3IF3)
itkHalfHermitianToRealInverseFFTImageFilterICF3IF3.SetActualXDimensionIsOdd = new_instancemethod(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_SetActualXDimensionIsOdd, None, itkHalfHermitianToRealInverseFFTImageFilterICF3IF3)
itkHalfHermitianToRealInverseFFTImageFilterICF3IF3.GetActualXDimensionIsOddInput = new_instancemethod(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_GetActualXDimensionIsOddInput, None, itkHalfHermitianToRealInverseFFTImageFilterICF3IF3)
itkHalfHermitianToRealInverseFFTImageFilterICF3IF3.GetActualXDimensionIsOdd = new_instancemethod(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_GetActualXDimensionIsOdd, None, itkHalfHermitianToRealInverseFFTImageFilterICF3IF3)
itkHalfHermitianToRealInverseFFTImageFilterICF3IF3.ActualXDimensionIsOddOn = new_instancemethod(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_ActualXDimensionIsOddOn, None, itkHalfHermitianToRealInverseFFTImageFilterICF3IF3)
itkHalfHermitianToRealInverseFFTImageFilterICF3IF3.ActualXDimensionIsOddOff = new_instancemethod(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_ActualXDimensionIsOddOff, None, itkHalfHermitianToRealInverseFFTImageFilterICF3IF3)
itkHalfHermitianToRealInverseFFTImageFilterICF3IF3.GetSizeGreatestPrimeFactor = new_instancemethod(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_GetSizeGreatestPrimeFactor, None, itkHalfHermitianToRealInverseFFTImageFilterICF3IF3)
itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_swigregister = _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_swigregister
itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_swigregister(itkHalfHermitianToRealInverseFFTImageFilterICF3IF3)

def itkHalfHermitianToRealInverseFFTImageFilterICF3IF3___New_orig__() -> "itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_Pointer":
    """itkHalfHermitianToRealInverseFFTImageFilterICF3IF3___New_orig__() -> itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_Pointer"""
    return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3___New_orig__()

def itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_cast(obj: 'itkLightObject') -> "itkHalfHermitianToRealInverseFFTImageFilterICF3IF3 *":
    """itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_cast(itkLightObject obj) -> itkHalfHermitianToRealInverseFFTImageFilterICF3IF3"""
    return _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def half_hermitian_to_real_inverse_fft_image_filter(*args, **kwargs):
    """Procedural interface for HalfHermitianToRealInverseFFTImageFilter"""
    import itk
    instance = itk.HalfHermitianToRealInverseFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def half_hermitian_to_real_inverse_fft_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.HalfHermitianToRealInverseFFTImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.HalfHermitianToRealInverseFFTImageFilter.values()[0]
    else:
        filter_object = itk.HalfHermitianToRealInverseFFTImageFilter

    half_hermitian_to_real_inverse_fft_image_filter.__doc__ = filter_object.__doc__
    half_hermitian_to_real_inverse_fft_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    half_hermitian_to_real_inverse_fft_image_filter.__doc__ += "Available Keyword Arguments:\n"
    half_hermitian_to_real_inverse_fft_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



