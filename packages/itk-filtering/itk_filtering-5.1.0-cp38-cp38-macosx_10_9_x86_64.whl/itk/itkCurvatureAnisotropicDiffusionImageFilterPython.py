# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkCurvatureAnisotropicDiffusionImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkCurvatureAnisotropicDiffusionImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkCurvatureAnisotropicDiffusionImageFilterPython
            return _itkCurvatureAnisotropicDiffusionImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkCurvatureAnisotropicDiffusionImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkCurvatureAnisotropicDiffusionImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkCurvatureAnisotropicDiffusionImageFilterPython
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
import itkImagePython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkRGBPixelPython
import itkPointPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkIndexPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython
import itkFiniteDifferenceFunctionPython

def itkCurvatureAnisotropicDiffusionImageFilterID3ID3_New():
  return itkCurvatureAnisotropicDiffusionImageFilterID3ID3.New()


def itkCurvatureAnisotropicDiffusionImageFilterID2ID2_New():
  return itkCurvatureAnisotropicDiffusionImageFilterID2ID2.New()


def itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_New():
  return itkCurvatureAnisotropicDiffusionImageFilterIF3IF3.New()


def itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_New():
  return itkCurvatureAnisotropicDiffusionImageFilterIF2IF2.New()

class itkCurvatureAnisotropicDiffusionImageFilterID2ID2(itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterID2ID2):
    """


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the modified curvature diffusion equation (MCDE).

    For detailed information on anisotropic diffusion and the MCDE see
    itkAnisotropicDiffusionFunction and
    itkCurvatureNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input and output to this filter must be a
    scalar itk::Image with numerical pixel types (float or double). A user
    defined type which correctly defines arithmetic operations with
    floating point accuracy should also give correct results. Parameters
    Please first read all the documentation found in
    AnisotropicDiffusionImageFilter and AnisotropicDiffusionFunction. Also
    see CurvatureNDAnisotropicDiffusionFunction.  The default time step
    for this filter is set to the maximum theoretically stable value: 0.5
    / 2^N, where N is the dimensionality of the image. For a 2D image,
    this means valid time steps are below 0.1250. For a 3D image, valid
    time steps are below 0.0625.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  CurvatureNDAnisotropicDiffusionFunction

    C++ includes: itkCurvatureAnisotropicDiffusionImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCurvatureAnisotropicDiffusionImageFilterID2ID2_Pointer":
        """__New_orig__() -> itkCurvatureAnisotropicDiffusionImageFilterID2ID2_Pointer"""
        return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCurvatureAnisotropicDiffusionImageFilterID2ID2_Pointer":
        """Clone(itkCurvatureAnisotropicDiffusionImageFilterID2ID2 self) -> itkCurvatureAnisotropicDiffusionImageFilterID2ID2_Pointer"""
        return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID2ID2_Clone(self)

    OutputHasNumericTraitsCheck = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID2ID2_OutputHasNumericTraitsCheck
    __swig_destroy__ = _itkCurvatureAnisotropicDiffusionImageFilterPython.delete_itkCurvatureAnisotropicDiffusionImageFilterID2ID2

    def cast(obj: 'itkLightObject') -> "itkCurvatureAnisotropicDiffusionImageFilterID2ID2 *":
        """cast(itkLightObject obj) -> itkCurvatureAnisotropicDiffusionImageFilterID2ID2"""
        return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkCurvatureAnisotropicDiffusionImageFilterID2ID2

        Create a new object of the class itkCurvatureAnisotropicDiffusionImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvatureAnisotropicDiffusionImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCurvatureAnisotropicDiffusionImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCurvatureAnisotropicDiffusionImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCurvatureAnisotropicDiffusionImageFilterID2ID2.Clone = new_instancemethod(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID2ID2_Clone, None, itkCurvatureAnisotropicDiffusionImageFilterID2ID2)
itkCurvatureAnisotropicDiffusionImageFilterID2ID2_swigregister = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID2ID2_swigregister
itkCurvatureAnisotropicDiffusionImageFilterID2ID2_swigregister(itkCurvatureAnisotropicDiffusionImageFilterID2ID2)

def itkCurvatureAnisotropicDiffusionImageFilterID2ID2___New_orig__() -> "itkCurvatureAnisotropicDiffusionImageFilterID2ID2_Pointer":
    """itkCurvatureAnisotropicDiffusionImageFilterID2ID2___New_orig__() -> itkCurvatureAnisotropicDiffusionImageFilterID2ID2_Pointer"""
    return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID2ID2___New_orig__()

def itkCurvatureAnisotropicDiffusionImageFilterID2ID2_cast(obj: 'itkLightObject') -> "itkCurvatureAnisotropicDiffusionImageFilterID2ID2 *":
    """itkCurvatureAnisotropicDiffusionImageFilterID2ID2_cast(itkLightObject obj) -> itkCurvatureAnisotropicDiffusionImageFilterID2ID2"""
    return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID2ID2_cast(obj)

class itkCurvatureAnisotropicDiffusionImageFilterID3ID3(itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterID3ID3):
    """


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the modified curvature diffusion equation (MCDE).

    For detailed information on anisotropic diffusion and the MCDE see
    itkAnisotropicDiffusionFunction and
    itkCurvatureNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input and output to this filter must be a
    scalar itk::Image with numerical pixel types (float or double). A user
    defined type which correctly defines arithmetic operations with
    floating point accuracy should also give correct results. Parameters
    Please first read all the documentation found in
    AnisotropicDiffusionImageFilter and AnisotropicDiffusionFunction. Also
    see CurvatureNDAnisotropicDiffusionFunction.  The default time step
    for this filter is set to the maximum theoretically stable value: 0.5
    / 2^N, where N is the dimensionality of the image. For a 2D image,
    this means valid time steps are below 0.1250. For a 3D image, valid
    time steps are below 0.0625.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  CurvatureNDAnisotropicDiffusionFunction

    C++ includes: itkCurvatureAnisotropicDiffusionImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCurvatureAnisotropicDiffusionImageFilterID3ID3_Pointer":
        """__New_orig__() -> itkCurvatureAnisotropicDiffusionImageFilterID3ID3_Pointer"""
        return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCurvatureAnisotropicDiffusionImageFilterID3ID3_Pointer":
        """Clone(itkCurvatureAnisotropicDiffusionImageFilterID3ID3 self) -> itkCurvatureAnisotropicDiffusionImageFilterID3ID3_Pointer"""
        return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID3ID3_Clone(self)

    OutputHasNumericTraitsCheck = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID3ID3_OutputHasNumericTraitsCheck
    __swig_destroy__ = _itkCurvatureAnisotropicDiffusionImageFilterPython.delete_itkCurvatureAnisotropicDiffusionImageFilterID3ID3

    def cast(obj: 'itkLightObject') -> "itkCurvatureAnisotropicDiffusionImageFilterID3ID3 *":
        """cast(itkLightObject obj) -> itkCurvatureAnisotropicDiffusionImageFilterID3ID3"""
        return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkCurvatureAnisotropicDiffusionImageFilterID3ID3

        Create a new object of the class itkCurvatureAnisotropicDiffusionImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvatureAnisotropicDiffusionImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCurvatureAnisotropicDiffusionImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCurvatureAnisotropicDiffusionImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCurvatureAnisotropicDiffusionImageFilterID3ID3.Clone = new_instancemethod(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID3ID3_Clone, None, itkCurvatureAnisotropicDiffusionImageFilterID3ID3)
itkCurvatureAnisotropicDiffusionImageFilterID3ID3_swigregister = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID3ID3_swigregister
itkCurvatureAnisotropicDiffusionImageFilterID3ID3_swigregister(itkCurvatureAnisotropicDiffusionImageFilterID3ID3)

def itkCurvatureAnisotropicDiffusionImageFilterID3ID3___New_orig__() -> "itkCurvatureAnisotropicDiffusionImageFilterID3ID3_Pointer":
    """itkCurvatureAnisotropicDiffusionImageFilterID3ID3___New_orig__() -> itkCurvatureAnisotropicDiffusionImageFilterID3ID3_Pointer"""
    return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID3ID3___New_orig__()

def itkCurvatureAnisotropicDiffusionImageFilterID3ID3_cast(obj: 'itkLightObject') -> "itkCurvatureAnisotropicDiffusionImageFilterID3ID3 *":
    """itkCurvatureAnisotropicDiffusionImageFilterID3ID3_cast(itkLightObject obj) -> itkCurvatureAnisotropicDiffusionImageFilterID3ID3"""
    return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID3ID3_cast(obj)

class itkCurvatureAnisotropicDiffusionImageFilterIF2IF2(itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterIF2IF2):
    """


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the modified curvature diffusion equation (MCDE).

    For detailed information on anisotropic diffusion and the MCDE see
    itkAnisotropicDiffusionFunction and
    itkCurvatureNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input and output to this filter must be a
    scalar itk::Image with numerical pixel types (float or double). A user
    defined type which correctly defines arithmetic operations with
    floating point accuracy should also give correct results. Parameters
    Please first read all the documentation found in
    AnisotropicDiffusionImageFilter and AnisotropicDiffusionFunction. Also
    see CurvatureNDAnisotropicDiffusionFunction.  The default time step
    for this filter is set to the maximum theoretically stable value: 0.5
    / 2^N, where N is the dimensionality of the image. For a 2D image,
    this means valid time steps are below 0.1250. For a 3D image, valid
    time steps are below 0.0625.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  CurvatureNDAnisotropicDiffusionFunction

    C++ includes: itkCurvatureAnisotropicDiffusionImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_Pointer"""
        return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_Pointer":
        """Clone(itkCurvatureAnisotropicDiffusionImageFilterIF2IF2 self) -> itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_Pointer"""
        return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_Clone(self)

    OutputHasNumericTraitsCheck = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_OutputHasNumericTraitsCheck
    __swig_destroy__ = _itkCurvatureAnisotropicDiffusionImageFilterPython.delete_itkCurvatureAnisotropicDiffusionImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkCurvatureAnisotropicDiffusionImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkCurvatureAnisotropicDiffusionImageFilterIF2IF2"""
        return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkCurvatureAnisotropicDiffusionImageFilterIF2IF2

        Create a new object of the class itkCurvatureAnisotropicDiffusionImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvatureAnisotropicDiffusionImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCurvatureAnisotropicDiffusionImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCurvatureAnisotropicDiffusionImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCurvatureAnisotropicDiffusionImageFilterIF2IF2.Clone = new_instancemethod(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_Clone, None, itkCurvatureAnisotropicDiffusionImageFilterIF2IF2)
itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_swigregister = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_swigregister
itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_swigregister(itkCurvatureAnisotropicDiffusionImageFilterIF2IF2)

def itkCurvatureAnisotropicDiffusionImageFilterIF2IF2___New_orig__() -> "itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_Pointer":
    """itkCurvatureAnisotropicDiffusionImageFilterIF2IF2___New_orig__() -> itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_Pointer"""
    return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF2IF2___New_orig__()

def itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkCurvatureAnisotropicDiffusionImageFilterIF2IF2 *":
    """itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_cast(itkLightObject obj) -> itkCurvatureAnisotropicDiffusionImageFilterIF2IF2"""
    return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_cast(obj)

class itkCurvatureAnisotropicDiffusionImageFilterIF3IF3(itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterIF3IF3):
    """


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the modified curvature diffusion equation (MCDE).

    For detailed information on anisotropic diffusion and the MCDE see
    itkAnisotropicDiffusionFunction and
    itkCurvatureNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input and output to this filter must be a
    scalar itk::Image with numerical pixel types (float or double). A user
    defined type which correctly defines arithmetic operations with
    floating point accuracy should also give correct results. Parameters
    Please first read all the documentation found in
    AnisotropicDiffusionImageFilter and AnisotropicDiffusionFunction. Also
    see CurvatureNDAnisotropicDiffusionFunction.  The default time step
    for this filter is set to the maximum theoretically stable value: 0.5
    / 2^N, where N is the dimensionality of the image. For a 2D image,
    this means valid time steps are below 0.1250. For a 3D image, valid
    time steps are below 0.0625.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  CurvatureNDAnisotropicDiffusionFunction

    C++ includes: itkCurvatureAnisotropicDiffusionImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_Pointer"""
        return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_Pointer":
        """Clone(itkCurvatureAnisotropicDiffusionImageFilterIF3IF3 self) -> itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_Pointer"""
        return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_Clone(self)

    OutputHasNumericTraitsCheck = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_OutputHasNumericTraitsCheck
    __swig_destroy__ = _itkCurvatureAnisotropicDiffusionImageFilterPython.delete_itkCurvatureAnisotropicDiffusionImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkCurvatureAnisotropicDiffusionImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkCurvatureAnisotropicDiffusionImageFilterIF3IF3"""
        return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkCurvatureAnisotropicDiffusionImageFilterIF3IF3

        Create a new object of the class itkCurvatureAnisotropicDiffusionImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvatureAnisotropicDiffusionImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCurvatureAnisotropicDiffusionImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCurvatureAnisotropicDiffusionImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCurvatureAnisotropicDiffusionImageFilterIF3IF3.Clone = new_instancemethod(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_Clone, None, itkCurvatureAnisotropicDiffusionImageFilterIF3IF3)
itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_swigregister = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_swigregister
itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_swigregister(itkCurvatureAnisotropicDiffusionImageFilterIF3IF3)

def itkCurvatureAnisotropicDiffusionImageFilterIF3IF3___New_orig__() -> "itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_Pointer":
    """itkCurvatureAnisotropicDiffusionImageFilterIF3IF3___New_orig__() -> itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_Pointer"""
    return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF3IF3___New_orig__()

def itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkCurvatureAnisotropicDiffusionImageFilterIF3IF3 *":
    """itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_cast(itkLightObject obj) -> itkCurvatureAnisotropicDiffusionImageFilterIF3IF3"""
    return _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def curvature_anisotropic_diffusion_image_filter(*args, **kwargs):
    """Procedural interface for CurvatureAnisotropicDiffusionImageFilter"""
    import itk
    instance = itk.CurvatureAnisotropicDiffusionImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def curvature_anisotropic_diffusion_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.CurvatureAnisotropicDiffusionImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.CurvatureAnisotropicDiffusionImageFilter.values()[0]
    else:
        filter_object = itk.CurvatureAnisotropicDiffusionImageFilter

    curvature_anisotropic_diffusion_image_filter.__doc__ = filter_object.__doc__
    curvature_anisotropic_diffusion_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    curvature_anisotropic_diffusion_image_filter.__doc__ += "Available Keyword Arguments:\n"
    curvature_anisotropic_diffusion_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



