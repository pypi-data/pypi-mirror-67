# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBinaryPruningImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBinaryPruningImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkBinaryPruningImageFilterPython
            return _itkBinaryPruningImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkBinaryPruningImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkBinaryPruningImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBinaryPruningImageFilterPython
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


import itkImagePython
import itkImageRegionPython
import itkSizePython
import pyBasePython
import itkIndexPython
import itkOffsetPython
import ITKCommonBasePython
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
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkBinaryPruningImageFilterID2ID2_New():
  return itkBinaryPruningImageFilterID2ID2.New()


def itkBinaryPruningImageFilterIF2IF2_New():
  return itkBinaryPruningImageFilterIF2IF2.New()


def itkBinaryPruningImageFilterIUS2IUS2_New():
  return itkBinaryPruningImageFilterIUS2IUS2.New()


def itkBinaryPruningImageFilterIUC2IUC2_New():
  return itkBinaryPruningImageFilterIUC2IUC2.New()

class itkBinaryPruningImageFilterID2ID2(itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    """


    This filter removes "spurs" of less than a certain length in the
    input image.

    This class is parameterized over the type of the input image and the
    type of the output image.

    The input is assumed to be a binary image.

    This filter is a sequential pruning algorithm and known to be
    computational time dependable of the image size. The algorithm is the
    N-dimensional version of that given for two dimensions in:

    Rafael C. Gonzales and Richard E. Woods. Digital Image Processing.
    Addison Wesley, 491-494, (1993).

    See:  MorphologyImageFilter

    See:   BinaryErodeImageFilter

    See:   BinaryDilateImageFilter

    See:   BinaryThinningImageFilter

    C++ includes: itkBinaryPruningImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryPruningImageFilterID2ID2_Pointer":
        """__New_orig__() -> itkBinaryPruningImageFilterID2ID2_Pointer"""
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryPruningImageFilterID2ID2_Pointer":
        """Clone(itkBinaryPruningImageFilterID2ID2 self) -> itkBinaryPruningImageFilterID2ID2_Pointer"""
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_Clone(self)


    def GetPruning(self) -> "itkImageD2 *":
        """
        GetPruning(itkBinaryPruningImageFilterID2ID2 self) -> itkImageD2

        Get Skelenton by
        thinning image. 
        """
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_GetPruning(self)


    def SetIteration(self, _arg: 'unsigned int const') -> "void":
        """
        SetIteration(itkBinaryPruningImageFilterID2ID2 self, unsigned int const _arg)

        Set/Get the iteration
        value 
        """
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_SetIteration(self, _arg)


    def GetIteration(self) -> "unsigned int":
        """GetIteration(itkBinaryPruningImageFilterID2ID2 self) -> unsigned int"""
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_GetIteration(self)

    SameDimensionCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_SameDimensionCheck
    SameTypeCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_SameTypeCheck
    AdditiveOperatorsCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_AdditiveOperatorsCheck
    IntConvertibleToPixelTypeCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_IntConvertibleToPixelTypeCheck
    PixelLessThanIntCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_PixelLessThanIntCheck
    __swig_destroy__ = _itkBinaryPruningImageFilterPython.delete_itkBinaryPruningImageFilterID2ID2

    def cast(obj: 'itkLightObject') -> "itkBinaryPruningImageFilterID2ID2 *":
        """cast(itkLightObject obj) -> itkBinaryPruningImageFilterID2ID2"""
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBinaryPruningImageFilterID2ID2

        Create a new object of the class itkBinaryPruningImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryPruningImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryPruningImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryPruningImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryPruningImageFilterID2ID2.Clone = new_instancemethod(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_Clone, None, itkBinaryPruningImageFilterID2ID2)
itkBinaryPruningImageFilterID2ID2.GetPruning = new_instancemethod(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_GetPruning, None, itkBinaryPruningImageFilterID2ID2)
itkBinaryPruningImageFilterID2ID2.SetIteration = new_instancemethod(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_SetIteration, None, itkBinaryPruningImageFilterID2ID2)
itkBinaryPruningImageFilterID2ID2.GetIteration = new_instancemethod(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_GetIteration, None, itkBinaryPruningImageFilterID2ID2)
itkBinaryPruningImageFilterID2ID2_swigregister = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_swigregister
itkBinaryPruningImageFilterID2ID2_swigregister(itkBinaryPruningImageFilterID2ID2)

def itkBinaryPruningImageFilterID2ID2___New_orig__() -> "itkBinaryPruningImageFilterID2ID2_Pointer":
    """itkBinaryPruningImageFilterID2ID2___New_orig__() -> itkBinaryPruningImageFilterID2ID2_Pointer"""
    return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2___New_orig__()

def itkBinaryPruningImageFilterID2ID2_cast(obj: 'itkLightObject') -> "itkBinaryPruningImageFilterID2ID2 *":
    """itkBinaryPruningImageFilterID2ID2_cast(itkLightObject obj) -> itkBinaryPruningImageFilterID2ID2"""
    return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_cast(obj)

class itkBinaryPruningImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    """


    This filter removes "spurs" of less than a certain length in the
    input image.

    This class is parameterized over the type of the input image and the
    type of the output image.

    The input is assumed to be a binary image.

    This filter is a sequential pruning algorithm and known to be
    computational time dependable of the image size. The algorithm is the
    N-dimensional version of that given for two dimensions in:

    Rafael C. Gonzales and Richard E. Woods. Digital Image Processing.
    Addison Wesley, 491-494, (1993).

    See:  MorphologyImageFilter

    See:   BinaryErodeImageFilter

    See:   BinaryDilateImageFilter

    See:   BinaryThinningImageFilter

    C++ includes: itkBinaryPruningImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryPruningImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkBinaryPruningImageFilterIF2IF2_Pointer"""
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryPruningImageFilterIF2IF2_Pointer":
        """Clone(itkBinaryPruningImageFilterIF2IF2 self) -> itkBinaryPruningImageFilterIF2IF2_Pointer"""
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_Clone(self)


    def GetPruning(self) -> "itkImageF2 *":
        """
        GetPruning(itkBinaryPruningImageFilterIF2IF2 self) -> itkImageF2

        Get Skelenton by
        thinning image. 
        """
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_GetPruning(self)


    def SetIteration(self, _arg: 'unsigned int const') -> "void":
        """
        SetIteration(itkBinaryPruningImageFilterIF2IF2 self, unsigned int const _arg)

        Set/Get the iteration
        value 
        """
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_SetIteration(self, _arg)


    def GetIteration(self) -> "unsigned int":
        """GetIteration(itkBinaryPruningImageFilterIF2IF2 self) -> unsigned int"""
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_GetIteration(self)

    SameDimensionCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_SameDimensionCheck
    SameTypeCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_SameTypeCheck
    AdditiveOperatorsCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_AdditiveOperatorsCheck
    IntConvertibleToPixelTypeCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_IntConvertibleToPixelTypeCheck
    PixelLessThanIntCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_PixelLessThanIntCheck
    __swig_destroy__ = _itkBinaryPruningImageFilterPython.delete_itkBinaryPruningImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkBinaryPruningImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkBinaryPruningImageFilterIF2IF2"""
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBinaryPruningImageFilterIF2IF2

        Create a new object of the class itkBinaryPruningImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryPruningImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryPruningImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryPruningImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryPruningImageFilterIF2IF2.Clone = new_instancemethod(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_Clone, None, itkBinaryPruningImageFilterIF2IF2)
itkBinaryPruningImageFilterIF2IF2.GetPruning = new_instancemethod(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_GetPruning, None, itkBinaryPruningImageFilterIF2IF2)
itkBinaryPruningImageFilterIF2IF2.SetIteration = new_instancemethod(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_SetIteration, None, itkBinaryPruningImageFilterIF2IF2)
itkBinaryPruningImageFilterIF2IF2.GetIteration = new_instancemethod(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_GetIteration, None, itkBinaryPruningImageFilterIF2IF2)
itkBinaryPruningImageFilterIF2IF2_swigregister = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_swigregister
itkBinaryPruningImageFilterIF2IF2_swigregister(itkBinaryPruningImageFilterIF2IF2)

def itkBinaryPruningImageFilterIF2IF2___New_orig__() -> "itkBinaryPruningImageFilterIF2IF2_Pointer":
    """itkBinaryPruningImageFilterIF2IF2___New_orig__() -> itkBinaryPruningImageFilterIF2IF2_Pointer"""
    return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2___New_orig__()

def itkBinaryPruningImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkBinaryPruningImageFilterIF2IF2 *":
    """itkBinaryPruningImageFilterIF2IF2_cast(itkLightObject obj) -> itkBinaryPruningImageFilterIF2IF2"""
    return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_cast(obj)

class itkBinaryPruningImageFilterIUC2IUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    """


    This filter removes "spurs" of less than a certain length in the
    input image.

    This class is parameterized over the type of the input image and the
    type of the output image.

    The input is assumed to be a binary image.

    This filter is a sequential pruning algorithm and known to be
    computational time dependable of the image size. The algorithm is the
    N-dimensional version of that given for two dimensions in:

    Rafael C. Gonzales and Richard E. Woods. Digital Image Processing.
    Addison Wesley, 491-494, (1993).

    See:  MorphologyImageFilter

    See:   BinaryErodeImageFilter

    See:   BinaryDilateImageFilter

    See:   BinaryThinningImageFilter

    C++ includes: itkBinaryPruningImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryPruningImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkBinaryPruningImageFilterIUC2IUC2_Pointer"""
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryPruningImageFilterIUC2IUC2_Pointer":
        """Clone(itkBinaryPruningImageFilterIUC2IUC2 self) -> itkBinaryPruningImageFilterIUC2IUC2_Pointer"""
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_Clone(self)


    def GetPruning(self) -> "itkImageUC2 *":
        """
        GetPruning(itkBinaryPruningImageFilterIUC2IUC2 self) -> itkImageUC2

        Get Skelenton by
        thinning image. 
        """
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_GetPruning(self)


    def SetIteration(self, _arg: 'unsigned int const') -> "void":
        """
        SetIteration(itkBinaryPruningImageFilterIUC2IUC2 self, unsigned int const _arg)

        Set/Get the iteration
        value 
        """
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_SetIteration(self, _arg)


    def GetIteration(self) -> "unsigned int":
        """GetIteration(itkBinaryPruningImageFilterIUC2IUC2 self) -> unsigned int"""
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_GetIteration(self)

    SameDimensionCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_SameDimensionCheck
    SameTypeCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_SameTypeCheck
    AdditiveOperatorsCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_AdditiveOperatorsCheck
    IntConvertibleToPixelTypeCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_IntConvertibleToPixelTypeCheck
    PixelLessThanIntCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_PixelLessThanIntCheck
    __swig_destroy__ = _itkBinaryPruningImageFilterPython.delete_itkBinaryPruningImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkBinaryPruningImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkBinaryPruningImageFilterIUC2IUC2"""
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBinaryPruningImageFilterIUC2IUC2

        Create a new object of the class itkBinaryPruningImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryPruningImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryPruningImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryPruningImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryPruningImageFilterIUC2IUC2.Clone = new_instancemethod(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_Clone, None, itkBinaryPruningImageFilterIUC2IUC2)
itkBinaryPruningImageFilterIUC2IUC2.GetPruning = new_instancemethod(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_GetPruning, None, itkBinaryPruningImageFilterIUC2IUC2)
itkBinaryPruningImageFilterIUC2IUC2.SetIteration = new_instancemethod(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_SetIteration, None, itkBinaryPruningImageFilterIUC2IUC2)
itkBinaryPruningImageFilterIUC2IUC2.GetIteration = new_instancemethod(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_GetIteration, None, itkBinaryPruningImageFilterIUC2IUC2)
itkBinaryPruningImageFilterIUC2IUC2_swigregister = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_swigregister
itkBinaryPruningImageFilterIUC2IUC2_swigregister(itkBinaryPruningImageFilterIUC2IUC2)

def itkBinaryPruningImageFilterIUC2IUC2___New_orig__() -> "itkBinaryPruningImageFilterIUC2IUC2_Pointer":
    """itkBinaryPruningImageFilterIUC2IUC2___New_orig__() -> itkBinaryPruningImageFilterIUC2IUC2_Pointer"""
    return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2___New_orig__()

def itkBinaryPruningImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkBinaryPruningImageFilterIUC2IUC2 *":
    """itkBinaryPruningImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkBinaryPruningImageFilterIUC2IUC2"""
    return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_cast(obj)

class itkBinaryPruningImageFilterIUS2IUS2(itkImageToImageFilterAPython.itkImageToImageFilterIUS2IUS2):
    """


    This filter removes "spurs" of less than a certain length in the
    input image.

    This class is parameterized over the type of the input image and the
    type of the output image.

    The input is assumed to be a binary image.

    This filter is a sequential pruning algorithm and known to be
    computational time dependable of the image size. The algorithm is the
    N-dimensional version of that given for two dimensions in:

    Rafael C. Gonzales and Richard E. Woods. Digital Image Processing.
    Addison Wesley, 491-494, (1993).

    See:  MorphologyImageFilter

    See:   BinaryErodeImageFilter

    See:   BinaryDilateImageFilter

    See:   BinaryThinningImageFilter

    C++ includes: itkBinaryPruningImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryPruningImageFilterIUS2IUS2_Pointer":
        """__New_orig__() -> itkBinaryPruningImageFilterIUS2IUS2_Pointer"""
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryPruningImageFilterIUS2IUS2_Pointer":
        """Clone(itkBinaryPruningImageFilterIUS2IUS2 self) -> itkBinaryPruningImageFilterIUS2IUS2_Pointer"""
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_Clone(self)


    def GetPruning(self) -> "itkImageUS2 *":
        """
        GetPruning(itkBinaryPruningImageFilterIUS2IUS2 self) -> itkImageUS2

        Get Skelenton by
        thinning image. 
        """
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_GetPruning(self)


    def SetIteration(self, _arg: 'unsigned int const') -> "void":
        """
        SetIteration(itkBinaryPruningImageFilterIUS2IUS2 self, unsigned int const _arg)

        Set/Get the iteration
        value 
        """
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_SetIteration(self, _arg)


    def GetIteration(self) -> "unsigned int":
        """GetIteration(itkBinaryPruningImageFilterIUS2IUS2 self) -> unsigned int"""
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_GetIteration(self)

    SameDimensionCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_SameDimensionCheck
    SameTypeCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_SameTypeCheck
    AdditiveOperatorsCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_AdditiveOperatorsCheck
    IntConvertibleToPixelTypeCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_IntConvertibleToPixelTypeCheck
    PixelLessThanIntCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_PixelLessThanIntCheck
    __swig_destroy__ = _itkBinaryPruningImageFilterPython.delete_itkBinaryPruningImageFilterIUS2IUS2

    def cast(obj: 'itkLightObject') -> "itkBinaryPruningImageFilterIUS2IUS2 *":
        """cast(itkLightObject obj) -> itkBinaryPruningImageFilterIUS2IUS2"""
        return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBinaryPruningImageFilterIUS2IUS2

        Create a new object of the class itkBinaryPruningImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryPruningImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryPruningImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryPruningImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryPruningImageFilterIUS2IUS2.Clone = new_instancemethod(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_Clone, None, itkBinaryPruningImageFilterIUS2IUS2)
itkBinaryPruningImageFilterIUS2IUS2.GetPruning = new_instancemethod(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_GetPruning, None, itkBinaryPruningImageFilterIUS2IUS2)
itkBinaryPruningImageFilterIUS2IUS2.SetIteration = new_instancemethod(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_SetIteration, None, itkBinaryPruningImageFilterIUS2IUS2)
itkBinaryPruningImageFilterIUS2IUS2.GetIteration = new_instancemethod(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_GetIteration, None, itkBinaryPruningImageFilterIUS2IUS2)
itkBinaryPruningImageFilterIUS2IUS2_swigregister = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_swigregister
itkBinaryPruningImageFilterIUS2IUS2_swigregister(itkBinaryPruningImageFilterIUS2IUS2)

def itkBinaryPruningImageFilterIUS2IUS2___New_orig__() -> "itkBinaryPruningImageFilterIUS2IUS2_Pointer":
    """itkBinaryPruningImageFilterIUS2IUS2___New_orig__() -> itkBinaryPruningImageFilterIUS2IUS2_Pointer"""
    return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2___New_orig__()

def itkBinaryPruningImageFilterIUS2IUS2_cast(obj: 'itkLightObject') -> "itkBinaryPruningImageFilterIUS2IUS2 *":
    """itkBinaryPruningImageFilterIUS2IUS2_cast(itkLightObject obj) -> itkBinaryPruningImageFilterIUS2IUS2"""
    return _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def binary_pruning_image_filter(*args, **kwargs):
    """Procedural interface for BinaryPruningImageFilter"""
    import itk
    instance = itk.BinaryPruningImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def binary_pruning_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.BinaryPruningImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.BinaryPruningImageFilter.values()[0]
    else:
        filter_object = itk.BinaryPruningImageFilter

    binary_pruning_image_filter.__doc__ = filter_object.__doc__
    binary_pruning_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    binary_pruning_image_filter.__doc__ += "Available Keyword Arguments:\n"
    binary_pruning_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



