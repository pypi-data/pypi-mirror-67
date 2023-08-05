# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkGradientAnisotropicDiffusionImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkGradientAnisotropicDiffusionImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkGradientAnisotropicDiffusionImageFilterPython
            return _itkGradientAnisotropicDiffusionImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkGradientAnisotropicDiffusionImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkGradientAnisotropicDiffusionImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkGradientAnisotropicDiffusionImageFilterPython
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
import itkAnisotropicDiffusionImageFilterPython
import itkDenseFiniteDifferenceImageFilterPython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkFiniteDifferenceImageFilterPython
import itkFiniteDifferenceFunctionPython
import itkVectorPython
import itkFixedArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkImagePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython

def itkGradientAnisotropicDiffusionImageFilterID3ID3_New():
  return itkGradientAnisotropicDiffusionImageFilterID3ID3.New()


def itkGradientAnisotropicDiffusionImageFilterID2ID2_New():
  return itkGradientAnisotropicDiffusionImageFilterID2ID2.New()


def itkGradientAnisotropicDiffusionImageFilterIF3IF3_New():
  return itkGradientAnisotropicDiffusionImageFilterIF3IF3.New()


def itkGradientAnisotropicDiffusionImageFilterIF2IF2_New():
  return itkGradientAnisotropicDiffusionImageFilterIF2IF2.New()

class itkGradientAnisotropicDiffusionImageFilterID2ID2(itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterID2ID2):
    """


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the classic Perona-Malik, gradient magnitude based equation.

    For detailed information on anisotropic diffusion, see
    itkAnisotropicDiffusionFunction and
    itkGradientNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input to this filter should be a scalar
    itk::Image of any dimensionality. The output image will be a diffused
    copy of the input. Parameters Please see the description of parameters
    given in itkAnisotropicDiffusionImageFilter.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  GradientAnisotropicDiffusionFunction

    C++ includes: itkGradientAnisotropicDiffusionImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGradientAnisotropicDiffusionImageFilterID2ID2_Pointer":
        """__New_orig__() -> itkGradientAnisotropicDiffusionImageFilterID2ID2_Pointer"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGradientAnisotropicDiffusionImageFilterID2ID2_Pointer":
        """Clone(itkGradientAnisotropicDiffusionImageFilterID2ID2 self) -> itkGradientAnisotropicDiffusionImageFilterID2ID2_Pointer"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID2ID2_Clone(self)

    UpdateBufferHasNumericTraitsCheck = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID2ID2_UpdateBufferHasNumericTraitsCheck
    __swig_destroy__ = _itkGradientAnisotropicDiffusionImageFilterPython.delete_itkGradientAnisotropicDiffusionImageFilterID2ID2

    def cast(obj: 'itkLightObject') -> "itkGradientAnisotropicDiffusionImageFilterID2ID2 *":
        """cast(itkLightObject obj) -> itkGradientAnisotropicDiffusionImageFilterID2ID2"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkGradientAnisotropicDiffusionImageFilterID2ID2

        Create a new object of the class itkGradientAnisotropicDiffusionImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientAnisotropicDiffusionImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientAnisotropicDiffusionImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientAnisotropicDiffusionImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGradientAnisotropicDiffusionImageFilterID2ID2.Clone = new_instancemethod(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID2ID2_Clone, None, itkGradientAnisotropicDiffusionImageFilterID2ID2)
itkGradientAnisotropicDiffusionImageFilterID2ID2_swigregister = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID2ID2_swigregister
itkGradientAnisotropicDiffusionImageFilterID2ID2_swigregister(itkGradientAnisotropicDiffusionImageFilterID2ID2)

def itkGradientAnisotropicDiffusionImageFilterID2ID2___New_orig__() -> "itkGradientAnisotropicDiffusionImageFilterID2ID2_Pointer":
    """itkGradientAnisotropicDiffusionImageFilterID2ID2___New_orig__() -> itkGradientAnisotropicDiffusionImageFilterID2ID2_Pointer"""
    return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID2ID2___New_orig__()

def itkGradientAnisotropicDiffusionImageFilterID2ID2_cast(obj: 'itkLightObject') -> "itkGradientAnisotropicDiffusionImageFilterID2ID2 *":
    """itkGradientAnisotropicDiffusionImageFilterID2ID2_cast(itkLightObject obj) -> itkGradientAnisotropicDiffusionImageFilterID2ID2"""
    return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID2ID2_cast(obj)

class itkGradientAnisotropicDiffusionImageFilterID3ID3(itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterID3ID3):
    """


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the classic Perona-Malik, gradient magnitude based equation.

    For detailed information on anisotropic diffusion, see
    itkAnisotropicDiffusionFunction and
    itkGradientNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input to this filter should be a scalar
    itk::Image of any dimensionality. The output image will be a diffused
    copy of the input. Parameters Please see the description of parameters
    given in itkAnisotropicDiffusionImageFilter.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  GradientAnisotropicDiffusionFunction

    C++ includes: itkGradientAnisotropicDiffusionImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGradientAnisotropicDiffusionImageFilterID3ID3_Pointer":
        """__New_orig__() -> itkGradientAnisotropicDiffusionImageFilterID3ID3_Pointer"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGradientAnisotropicDiffusionImageFilterID3ID3_Pointer":
        """Clone(itkGradientAnisotropicDiffusionImageFilterID3ID3 self) -> itkGradientAnisotropicDiffusionImageFilterID3ID3_Pointer"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID3ID3_Clone(self)

    UpdateBufferHasNumericTraitsCheck = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID3ID3_UpdateBufferHasNumericTraitsCheck
    __swig_destroy__ = _itkGradientAnisotropicDiffusionImageFilterPython.delete_itkGradientAnisotropicDiffusionImageFilterID3ID3

    def cast(obj: 'itkLightObject') -> "itkGradientAnisotropicDiffusionImageFilterID3ID3 *":
        """cast(itkLightObject obj) -> itkGradientAnisotropicDiffusionImageFilterID3ID3"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkGradientAnisotropicDiffusionImageFilterID3ID3

        Create a new object of the class itkGradientAnisotropicDiffusionImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientAnisotropicDiffusionImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientAnisotropicDiffusionImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientAnisotropicDiffusionImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGradientAnisotropicDiffusionImageFilterID3ID3.Clone = new_instancemethod(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID3ID3_Clone, None, itkGradientAnisotropicDiffusionImageFilterID3ID3)
itkGradientAnisotropicDiffusionImageFilterID3ID3_swigregister = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID3ID3_swigregister
itkGradientAnisotropicDiffusionImageFilterID3ID3_swigregister(itkGradientAnisotropicDiffusionImageFilterID3ID3)

def itkGradientAnisotropicDiffusionImageFilterID3ID3___New_orig__() -> "itkGradientAnisotropicDiffusionImageFilterID3ID3_Pointer":
    """itkGradientAnisotropicDiffusionImageFilterID3ID3___New_orig__() -> itkGradientAnisotropicDiffusionImageFilterID3ID3_Pointer"""
    return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID3ID3___New_orig__()

def itkGradientAnisotropicDiffusionImageFilterID3ID3_cast(obj: 'itkLightObject') -> "itkGradientAnisotropicDiffusionImageFilterID3ID3 *":
    """itkGradientAnisotropicDiffusionImageFilterID3ID3_cast(itkLightObject obj) -> itkGradientAnisotropicDiffusionImageFilterID3ID3"""
    return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID3ID3_cast(obj)

class itkGradientAnisotropicDiffusionImageFilterIF2IF2(itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterIF2IF2):
    """


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the classic Perona-Malik, gradient magnitude based equation.

    For detailed information on anisotropic diffusion, see
    itkAnisotropicDiffusionFunction and
    itkGradientNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input to this filter should be a scalar
    itk::Image of any dimensionality. The output image will be a diffused
    copy of the input. Parameters Please see the description of parameters
    given in itkAnisotropicDiffusionImageFilter.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  GradientAnisotropicDiffusionFunction

    C++ includes: itkGradientAnisotropicDiffusionImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGradientAnisotropicDiffusionImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkGradientAnisotropicDiffusionImageFilterIF2IF2_Pointer"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGradientAnisotropicDiffusionImageFilterIF2IF2_Pointer":
        """Clone(itkGradientAnisotropicDiffusionImageFilterIF2IF2 self) -> itkGradientAnisotropicDiffusionImageFilterIF2IF2_Pointer"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_Clone(self)

    UpdateBufferHasNumericTraitsCheck = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_UpdateBufferHasNumericTraitsCheck
    __swig_destroy__ = _itkGradientAnisotropicDiffusionImageFilterPython.delete_itkGradientAnisotropicDiffusionImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkGradientAnisotropicDiffusionImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkGradientAnisotropicDiffusionImageFilterIF2IF2"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkGradientAnisotropicDiffusionImageFilterIF2IF2

        Create a new object of the class itkGradientAnisotropicDiffusionImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientAnisotropicDiffusionImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientAnisotropicDiffusionImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientAnisotropicDiffusionImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGradientAnisotropicDiffusionImageFilterIF2IF2.Clone = new_instancemethod(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_Clone, None, itkGradientAnisotropicDiffusionImageFilterIF2IF2)
itkGradientAnisotropicDiffusionImageFilterIF2IF2_swigregister = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_swigregister
itkGradientAnisotropicDiffusionImageFilterIF2IF2_swigregister(itkGradientAnisotropicDiffusionImageFilterIF2IF2)

def itkGradientAnisotropicDiffusionImageFilterIF2IF2___New_orig__() -> "itkGradientAnisotropicDiffusionImageFilterIF2IF2_Pointer":
    """itkGradientAnisotropicDiffusionImageFilterIF2IF2___New_orig__() -> itkGradientAnisotropicDiffusionImageFilterIF2IF2_Pointer"""
    return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2___New_orig__()

def itkGradientAnisotropicDiffusionImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkGradientAnisotropicDiffusionImageFilterIF2IF2 *":
    """itkGradientAnisotropicDiffusionImageFilterIF2IF2_cast(itkLightObject obj) -> itkGradientAnisotropicDiffusionImageFilterIF2IF2"""
    return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_cast(obj)

class itkGradientAnisotropicDiffusionImageFilterIF3IF3(itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterIF3IF3):
    """


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the classic Perona-Malik, gradient magnitude based equation.

    For detailed information on anisotropic diffusion, see
    itkAnisotropicDiffusionFunction and
    itkGradientNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input to this filter should be a scalar
    itk::Image of any dimensionality. The output image will be a diffused
    copy of the input. Parameters Please see the description of parameters
    given in itkAnisotropicDiffusionImageFilter.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  GradientAnisotropicDiffusionFunction

    C++ includes: itkGradientAnisotropicDiffusionImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGradientAnisotropicDiffusionImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkGradientAnisotropicDiffusionImageFilterIF3IF3_Pointer"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGradientAnisotropicDiffusionImageFilterIF3IF3_Pointer":
        """Clone(itkGradientAnisotropicDiffusionImageFilterIF3IF3 self) -> itkGradientAnisotropicDiffusionImageFilterIF3IF3_Pointer"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_Clone(self)

    UpdateBufferHasNumericTraitsCheck = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_UpdateBufferHasNumericTraitsCheck
    __swig_destroy__ = _itkGradientAnisotropicDiffusionImageFilterPython.delete_itkGradientAnisotropicDiffusionImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkGradientAnisotropicDiffusionImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkGradientAnisotropicDiffusionImageFilterIF3IF3"""
        return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkGradientAnisotropicDiffusionImageFilterIF3IF3

        Create a new object of the class itkGradientAnisotropicDiffusionImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientAnisotropicDiffusionImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientAnisotropicDiffusionImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientAnisotropicDiffusionImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGradientAnisotropicDiffusionImageFilterIF3IF3.Clone = new_instancemethod(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_Clone, None, itkGradientAnisotropicDiffusionImageFilterIF3IF3)
itkGradientAnisotropicDiffusionImageFilterIF3IF3_swigregister = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_swigregister
itkGradientAnisotropicDiffusionImageFilterIF3IF3_swigregister(itkGradientAnisotropicDiffusionImageFilterIF3IF3)

def itkGradientAnisotropicDiffusionImageFilterIF3IF3___New_orig__() -> "itkGradientAnisotropicDiffusionImageFilterIF3IF3_Pointer":
    """itkGradientAnisotropicDiffusionImageFilterIF3IF3___New_orig__() -> itkGradientAnisotropicDiffusionImageFilterIF3IF3_Pointer"""
    return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3___New_orig__()

def itkGradientAnisotropicDiffusionImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkGradientAnisotropicDiffusionImageFilterIF3IF3 *":
    """itkGradientAnisotropicDiffusionImageFilterIF3IF3_cast(itkLightObject obj) -> itkGradientAnisotropicDiffusionImageFilterIF3IF3"""
    return _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def gradient_anisotropic_diffusion_image_filter(*args, **kwargs):
    """Procedural interface for GradientAnisotropicDiffusionImageFilter"""
    import itk
    instance = itk.GradientAnisotropicDiffusionImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def gradient_anisotropic_diffusion_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.GradientAnisotropicDiffusionImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.GradientAnisotropicDiffusionImageFilter.values()[0]
    else:
        filter_object = itk.GradientAnisotropicDiffusionImageFilter

    gradient_anisotropic_diffusion_image_filter.__doc__ = filter_object.__doc__
    gradient_anisotropic_diffusion_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    gradient_anisotropic_diffusion_image_filter.__doc__ += "Available Keyword Arguments:\n"
    gradient_anisotropic_diffusion_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



