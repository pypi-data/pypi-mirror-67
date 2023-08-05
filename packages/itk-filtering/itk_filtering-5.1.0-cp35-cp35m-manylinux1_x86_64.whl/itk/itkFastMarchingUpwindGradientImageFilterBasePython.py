# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkFastMarchingUpwindGradientImageFilterBasePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkFastMarchingUpwindGradientImageFilterBasePython', [dirname(__file__)])
        except ImportError:
            import _itkFastMarchingUpwindGradientImageFilterBasePython
            return _itkFastMarchingUpwindGradientImageFilterBasePython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkFastMarchingUpwindGradientImageFilterBasePython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkFastMarchingUpwindGradientImageFilterBasePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkFastMarchingUpwindGradientImageFilterBasePython
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


import itkFastMarchingImageFilterBasePython
import itkMatrixPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkImagePython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import ITKCommonBasePython
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import ITKFastMarchingBasePython
import itkNodePairPython
import itkLevelSetNodePython
import itkFastMarchingStoppingCriterionBasePython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkFastMarchingUpwindGradientImageFilterBaseID3ID3_New():
  return itkFastMarchingUpwindGradientImageFilterBaseID3ID3.New()


def itkFastMarchingUpwindGradientImageFilterBaseID2ID2_New():
  return itkFastMarchingUpwindGradientImageFilterBaseID2ID2.New()


def itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_New():
  return itkFastMarchingUpwindGradientImageFilterBaseIF3IF3.New()


def itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_New():
  return itkFastMarchingUpwindGradientImageFilterBaseIF2IF2.New()

class itkFastMarchingUpwindGradientImageFilterBaseID2ID2(itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2):
    """


    Generates the upwind gradient field of fast marching arrival times.

    This filter adds some extra functionality to its base class. While the
    solution T(x) of the Eikonal equation is being generated by the base
    class with the fast marching method, the filter generates the upwind
    gradient vectors of T(x), storing them in an image.

    Since the Eikonal equation generates the arrival times of a wave
    traveling at a given speed, the generated gradient vectors can be
    interpreted as the slowness (1/velocity) vectors of the front (the
    quantity inside the modulus operator in the Eikonal equation).

    Gradient vectors are computed using upwind finite differences, that
    is, information only propagates from points where the wavefront has
    already passed. This is consistent with how the fast marching method
    works.

    For an alternative implementation, see
    itk::FastMarchingUpwindGradientImageFilter.

    Luca Antiga Ph.D. Biomedical Technologies Laboratory, Bioengineering
    Department, Mario Negri Institute, Italy.

    See:   FastMarchingUpwindGradientImageFilter

    C++ includes: itkFastMarchingUpwindGradientImageFilterBase.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingUpwindGradientImageFilterBaseID2ID2_Pointer":
        """__New_orig__() -> itkFastMarchingUpwindGradientImageFilterBaseID2ID2_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingUpwindGradientImageFilterBaseID2ID2_Pointer":
        """Clone(itkFastMarchingUpwindGradientImageFilterBaseID2ID2 self) -> itkFastMarchingUpwindGradientImageFilterBaseID2ID2_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID2ID2_Clone(self)


    def GetGradientImage(self) -> "itkImageCVD22 *":
        """
        GetGradientImage(itkFastMarchingUpwindGradientImageFilterBaseID2ID2 self) -> itkImageCVD22

        Get the gradient
        image. 
        """
        return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID2ID2_GetGradientImage(self)

    __swig_destroy__ = _itkFastMarchingUpwindGradientImageFilterBasePython.delete_itkFastMarchingUpwindGradientImageFilterBaseID2ID2

    def cast(obj: 'itkLightObject') -> "itkFastMarchingUpwindGradientImageFilterBaseID2ID2 *":
        """cast(itkLightObject obj) -> itkFastMarchingUpwindGradientImageFilterBaseID2ID2"""
        return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingUpwindGradientImageFilterBaseID2ID2

        Create a new object of the class itkFastMarchingUpwindGradientImageFilterBaseID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingUpwindGradientImageFilterBaseID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingUpwindGradientImageFilterBaseID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingUpwindGradientImageFilterBaseID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingUpwindGradientImageFilterBaseID2ID2.Clone = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID2ID2_Clone, None, itkFastMarchingUpwindGradientImageFilterBaseID2ID2)
itkFastMarchingUpwindGradientImageFilterBaseID2ID2.GetGradientImage = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID2ID2_GetGradientImage, None, itkFastMarchingUpwindGradientImageFilterBaseID2ID2)
itkFastMarchingUpwindGradientImageFilterBaseID2ID2_swigregister = _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID2ID2_swigregister
itkFastMarchingUpwindGradientImageFilterBaseID2ID2_swigregister(itkFastMarchingUpwindGradientImageFilterBaseID2ID2)

def itkFastMarchingUpwindGradientImageFilterBaseID2ID2___New_orig__() -> "itkFastMarchingUpwindGradientImageFilterBaseID2ID2_Pointer":
    """itkFastMarchingUpwindGradientImageFilterBaseID2ID2___New_orig__() -> itkFastMarchingUpwindGradientImageFilterBaseID2ID2_Pointer"""
    return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID2ID2___New_orig__()

def itkFastMarchingUpwindGradientImageFilterBaseID2ID2_cast(obj: 'itkLightObject') -> "itkFastMarchingUpwindGradientImageFilterBaseID2ID2 *":
    """itkFastMarchingUpwindGradientImageFilterBaseID2ID2_cast(itkLightObject obj) -> itkFastMarchingUpwindGradientImageFilterBaseID2ID2"""
    return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID2ID2_cast(obj)

class itkFastMarchingUpwindGradientImageFilterBaseID3ID3(itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3):
    """


    Generates the upwind gradient field of fast marching arrival times.

    This filter adds some extra functionality to its base class. While the
    solution T(x) of the Eikonal equation is being generated by the base
    class with the fast marching method, the filter generates the upwind
    gradient vectors of T(x), storing them in an image.

    Since the Eikonal equation generates the arrival times of a wave
    traveling at a given speed, the generated gradient vectors can be
    interpreted as the slowness (1/velocity) vectors of the front (the
    quantity inside the modulus operator in the Eikonal equation).

    Gradient vectors are computed using upwind finite differences, that
    is, information only propagates from points where the wavefront has
    already passed. This is consistent with how the fast marching method
    works.

    For an alternative implementation, see
    itk::FastMarchingUpwindGradientImageFilter.

    Luca Antiga Ph.D. Biomedical Technologies Laboratory, Bioengineering
    Department, Mario Negri Institute, Italy.

    See:   FastMarchingUpwindGradientImageFilter

    C++ includes: itkFastMarchingUpwindGradientImageFilterBase.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingUpwindGradientImageFilterBaseID3ID3_Pointer":
        """__New_orig__() -> itkFastMarchingUpwindGradientImageFilterBaseID3ID3_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingUpwindGradientImageFilterBaseID3ID3_Pointer":
        """Clone(itkFastMarchingUpwindGradientImageFilterBaseID3ID3 self) -> itkFastMarchingUpwindGradientImageFilterBaseID3ID3_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID3ID3_Clone(self)


    def GetGradientImage(self) -> "itkImageCVD33 *":
        """
        GetGradientImage(itkFastMarchingUpwindGradientImageFilterBaseID3ID3 self) -> itkImageCVD33

        Get the gradient
        image. 
        """
        return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID3ID3_GetGradientImage(self)

    __swig_destroy__ = _itkFastMarchingUpwindGradientImageFilterBasePython.delete_itkFastMarchingUpwindGradientImageFilterBaseID3ID3

    def cast(obj: 'itkLightObject') -> "itkFastMarchingUpwindGradientImageFilterBaseID3ID3 *":
        """cast(itkLightObject obj) -> itkFastMarchingUpwindGradientImageFilterBaseID3ID3"""
        return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingUpwindGradientImageFilterBaseID3ID3

        Create a new object of the class itkFastMarchingUpwindGradientImageFilterBaseID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingUpwindGradientImageFilterBaseID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingUpwindGradientImageFilterBaseID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingUpwindGradientImageFilterBaseID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingUpwindGradientImageFilterBaseID3ID3.Clone = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID3ID3_Clone, None, itkFastMarchingUpwindGradientImageFilterBaseID3ID3)
itkFastMarchingUpwindGradientImageFilterBaseID3ID3.GetGradientImage = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID3ID3_GetGradientImage, None, itkFastMarchingUpwindGradientImageFilterBaseID3ID3)
itkFastMarchingUpwindGradientImageFilterBaseID3ID3_swigregister = _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID3ID3_swigregister
itkFastMarchingUpwindGradientImageFilterBaseID3ID3_swigregister(itkFastMarchingUpwindGradientImageFilterBaseID3ID3)

def itkFastMarchingUpwindGradientImageFilterBaseID3ID3___New_orig__() -> "itkFastMarchingUpwindGradientImageFilterBaseID3ID3_Pointer":
    """itkFastMarchingUpwindGradientImageFilterBaseID3ID3___New_orig__() -> itkFastMarchingUpwindGradientImageFilterBaseID3ID3_Pointer"""
    return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID3ID3___New_orig__()

def itkFastMarchingUpwindGradientImageFilterBaseID3ID3_cast(obj: 'itkLightObject') -> "itkFastMarchingUpwindGradientImageFilterBaseID3ID3 *":
    """itkFastMarchingUpwindGradientImageFilterBaseID3ID3_cast(itkLightObject obj) -> itkFastMarchingUpwindGradientImageFilterBaseID3ID3"""
    return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID3ID3_cast(obj)

class itkFastMarchingUpwindGradientImageFilterBaseIF2IF2(itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2):
    """


    Generates the upwind gradient field of fast marching arrival times.

    This filter adds some extra functionality to its base class. While the
    solution T(x) of the Eikonal equation is being generated by the base
    class with the fast marching method, the filter generates the upwind
    gradient vectors of T(x), storing them in an image.

    Since the Eikonal equation generates the arrival times of a wave
    traveling at a given speed, the generated gradient vectors can be
    interpreted as the slowness (1/velocity) vectors of the front (the
    quantity inside the modulus operator in the Eikonal equation).

    Gradient vectors are computed using upwind finite differences, that
    is, information only propagates from points where the wavefront has
    already passed. This is consistent with how the fast marching method
    works.

    For an alternative implementation, see
    itk::FastMarchingUpwindGradientImageFilter.

    Luca Antiga Ph.D. Biomedical Technologies Laboratory, Bioengineering
    Department, Mario Negri Institute, Italy.

    See:   FastMarchingUpwindGradientImageFilter

    C++ includes: itkFastMarchingUpwindGradientImageFilterBase.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_Pointer":
        """__New_orig__() -> itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_Pointer":
        """Clone(itkFastMarchingUpwindGradientImageFilterBaseIF2IF2 self) -> itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_Clone(self)


    def GetGradientImage(self) -> "itkImageCVF22 *":
        """
        GetGradientImage(itkFastMarchingUpwindGradientImageFilterBaseIF2IF2 self) -> itkImageCVF22

        Get the gradient
        image. 
        """
        return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_GetGradientImage(self)

    __swig_destroy__ = _itkFastMarchingUpwindGradientImageFilterBasePython.delete_itkFastMarchingUpwindGradientImageFilterBaseIF2IF2

    def cast(obj: 'itkLightObject') -> "itkFastMarchingUpwindGradientImageFilterBaseIF2IF2 *":
        """cast(itkLightObject obj) -> itkFastMarchingUpwindGradientImageFilterBaseIF2IF2"""
        return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingUpwindGradientImageFilterBaseIF2IF2

        Create a new object of the class itkFastMarchingUpwindGradientImageFilterBaseIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingUpwindGradientImageFilterBaseIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingUpwindGradientImageFilterBaseIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingUpwindGradientImageFilterBaseIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingUpwindGradientImageFilterBaseIF2IF2.Clone = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_Clone, None, itkFastMarchingUpwindGradientImageFilterBaseIF2IF2)
itkFastMarchingUpwindGradientImageFilterBaseIF2IF2.GetGradientImage = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_GetGradientImage, None, itkFastMarchingUpwindGradientImageFilterBaseIF2IF2)
itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_swigregister = _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_swigregister
itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_swigregister(itkFastMarchingUpwindGradientImageFilterBaseIF2IF2)

def itkFastMarchingUpwindGradientImageFilterBaseIF2IF2___New_orig__() -> "itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_Pointer":
    """itkFastMarchingUpwindGradientImageFilterBaseIF2IF2___New_orig__() -> itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_Pointer"""
    return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF2IF2___New_orig__()

def itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_cast(obj: 'itkLightObject') -> "itkFastMarchingUpwindGradientImageFilterBaseIF2IF2 *":
    """itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_cast(itkLightObject obj) -> itkFastMarchingUpwindGradientImageFilterBaseIF2IF2"""
    return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_cast(obj)

class itkFastMarchingUpwindGradientImageFilterBaseIF3IF3(itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3):
    """


    Generates the upwind gradient field of fast marching arrival times.

    This filter adds some extra functionality to its base class. While the
    solution T(x) of the Eikonal equation is being generated by the base
    class with the fast marching method, the filter generates the upwind
    gradient vectors of T(x), storing them in an image.

    Since the Eikonal equation generates the arrival times of a wave
    traveling at a given speed, the generated gradient vectors can be
    interpreted as the slowness (1/velocity) vectors of the front (the
    quantity inside the modulus operator in the Eikonal equation).

    Gradient vectors are computed using upwind finite differences, that
    is, information only propagates from points where the wavefront has
    already passed. This is consistent with how the fast marching method
    works.

    For an alternative implementation, see
    itk::FastMarchingUpwindGradientImageFilter.

    Luca Antiga Ph.D. Biomedical Technologies Laboratory, Bioengineering
    Department, Mario Negri Institute, Italy.

    See:   FastMarchingUpwindGradientImageFilter

    C++ includes: itkFastMarchingUpwindGradientImageFilterBase.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_Pointer":
        """__New_orig__() -> itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_Pointer":
        """Clone(itkFastMarchingUpwindGradientImageFilterBaseIF3IF3 self) -> itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_Pointer"""
        return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_Clone(self)


    def GetGradientImage(self) -> "itkImageCVF33 *":
        """
        GetGradientImage(itkFastMarchingUpwindGradientImageFilterBaseIF3IF3 self) -> itkImageCVF33

        Get the gradient
        image. 
        """
        return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_GetGradientImage(self)

    __swig_destroy__ = _itkFastMarchingUpwindGradientImageFilterBasePython.delete_itkFastMarchingUpwindGradientImageFilterBaseIF3IF3

    def cast(obj: 'itkLightObject') -> "itkFastMarchingUpwindGradientImageFilterBaseIF3IF3 *":
        """cast(itkLightObject obj) -> itkFastMarchingUpwindGradientImageFilterBaseIF3IF3"""
        return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingUpwindGradientImageFilterBaseIF3IF3

        Create a new object of the class itkFastMarchingUpwindGradientImageFilterBaseIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingUpwindGradientImageFilterBaseIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingUpwindGradientImageFilterBaseIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingUpwindGradientImageFilterBaseIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingUpwindGradientImageFilterBaseIF3IF3.Clone = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_Clone, None, itkFastMarchingUpwindGradientImageFilterBaseIF3IF3)
itkFastMarchingUpwindGradientImageFilterBaseIF3IF3.GetGradientImage = new_instancemethod(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_GetGradientImage, None, itkFastMarchingUpwindGradientImageFilterBaseIF3IF3)
itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_swigregister = _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_swigregister
itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_swigregister(itkFastMarchingUpwindGradientImageFilterBaseIF3IF3)

def itkFastMarchingUpwindGradientImageFilterBaseIF3IF3___New_orig__() -> "itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_Pointer":
    """itkFastMarchingUpwindGradientImageFilterBaseIF3IF3___New_orig__() -> itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_Pointer"""
    return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF3IF3___New_orig__()

def itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_cast(obj: 'itkLightObject') -> "itkFastMarchingUpwindGradientImageFilterBaseIF3IF3 *":
    """itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_cast(itkLightObject obj) -> itkFastMarchingUpwindGradientImageFilterBaseIF3IF3"""
    return _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def fast_marching_upwind_gradient_image_filter_base(*args, **kwargs):
    """Procedural interface for FastMarchingUpwindGradientImageFilterBase"""
    import itk
    instance = itk.FastMarchingUpwindGradientImageFilterBase.New(*args, **kwargs)
    return instance.__internal_call__()

def fast_marching_upwind_gradient_image_filter_base_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.FastMarchingUpwindGradientImageFilterBase, itkTemplate.itkTemplate):
        filter_object = itk.FastMarchingUpwindGradientImageFilterBase.values()[0]
    else:
        filter_object = itk.FastMarchingUpwindGradientImageFilterBase

    fast_marching_upwind_gradient_image_filter_base.__doc__ = filter_object.__doc__
    fast_marching_upwind_gradient_image_filter_base.__doc__ += "\n Args are Input(s) to the filter.\n"
    fast_marching_upwind_gradient_image_filter_base.__doc__ += "Available Keyword Arguments:\n"
    fast_marching_upwind_gradient_image_filter_base.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



