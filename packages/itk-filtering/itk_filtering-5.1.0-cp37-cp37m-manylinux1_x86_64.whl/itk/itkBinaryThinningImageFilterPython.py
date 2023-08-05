# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBinaryThinningImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBinaryThinningImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkBinaryThinningImageFilterPython
            return _itkBinaryThinningImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkBinaryThinningImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkBinaryThinningImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBinaryThinningImageFilterPython
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
import itkImageToImageFilterAPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
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

def itkBinaryThinningImageFilterISS2ISS2_New():
  return itkBinaryThinningImageFilterISS2ISS2.New()


def itkBinaryThinningImageFilterIUS2IUS2_New():
  return itkBinaryThinningImageFilterIUS2IUS2.New()


def itkBinaryThinningImageFilterIUC2IUC2_New():
  return itkBinaryThinningImageFilterIUC2IUC2.New()

class itkBinaryThinningImageFilterISS2ISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    """


    This filter computes one-pixel-wide edges of the input image.

    This class is parameterized over the type of the input image and the
    type of the output image.

    The input is assumed to be a binary image. If the foreground pixels of
    the input image do not have a value of 1, they are rescaled to 1
    internally to simplify the computation.

    The filter will produce a skeleton of the object. The output
    background values are 0, and the foreground values are 1.

    This filter is a sequential thinning algorithm and known to be
    computational time dependable on the image size. The algorithm
    corresponds with the 2D implementation described in:

    Rafael C. Gonzales and Richard E. Woods. Digital Image Processing.
    Addison Wesley, 491-494, (1993).

    To do: Make this filter ND.

    See:  MorphologyImageFilter

    C++ includes: itkBinaryThinningImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryThinningImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkBinaryThinningImageFilterISS2ISS2_Pointer"""
        return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryThinningImageFilterISS2ISS2_Pointer":
        """Clone(itkBinaryThinningImageFilterISS2ISS2 self) -> itkBinaryThinningImageFilterISS2ISS2_Pointer"""
        return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_Clone(self)


    def GetThinning(self) -> "itkImageSS2 *":
        """
        GetThinning(itkBinaryThinningImageFilterISS2ISS2 self) -> itkImageSS2

        Get Skelenton by
        thinning image. 
        """
        return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_GetThinning(self)

    SameDimensionCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_SameDimensionCheck
    InputAdditiveOperatorsCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_InputAdditiveOperatorsCheck
    InputConvertibleToIntCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_InputConvertibleToIntCheck
    IntConvertibleToInputCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_IntConvertibleToInputCheck
    SameTypeCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_SameTypeCheck
    __swig_destroy__ = _itkBinaryThinningImageFilterPython.delete_itkBinaryThinningImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkBinaryThinningImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkBinaryThinningImageFilterISS2ISS2"""
        return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBinaryThinningImageFilterISS2ISS2

        Create a new object of the class itkBinaryThinningImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryThinningImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryThinningImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryThinningImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryThinningImageFilterISS2ISS2.Clone = new_instancemethod(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_Clone, None, itkBinaryThinningImageFilterISS2ISS2)
itkBinaryThinningImageFilterISS2ISS2.GetThinning = new_instancemethod(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_GetThinning, None, itkBinaryThinningImageFilterISS2ISS2)
itkBinaryThinningImageFilterISS2ISS2_swigregister = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_swigregister
itkBinaryThinningImageFilterISS2ISS2_swigregister(itkBinaryThinningImageFilterISS2ISS2)

def itkBinaryThinningImageFilterISS2ISS2___New_orig__() -> "itkBinaryThinningImageFilterISS2ISS2_Pointer":
    """itkBinaryThinningImageFilterISS2ISS2___New_orig__() -> itkBinaryThinningImageFilterISS2ISS2_Pointer"""
    return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2___New_orig__()

def itkBinaryThinningImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkBinaryThinningImageFilterISS2ISS2 *":
    """itkBinaryThinningImageFilterISS2ISS2_cast(itkLightObject obj) -> itkBinaryThinningImageFilterISS2ISS2"""
    return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_cast(obj)

class itkBinaryThinningImageFilterIUC2IUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    """


    This filter computes one-pixel-wide edges of the input image.

    This class is parameterized over the type of the input image and the
    type of the output image.

    The input is assumed to be a binary image. If the foreground pixels of
    the input image do not have a value of 1, they are rescaled to 1
    internally to simplify the computation.

    The filter will produce a skeleton of the object. The output
    background values are 0, and the foreground values are 1.

    This filter is a sequential thinning algorithm and known to be
    computational time dependable on the image size. The algorithm
    corresponds with the 2D implementation described in:

    Rafael C. Gonzales and Richard E. Woods. Digital Image Processing.
    Addison Wesley, 491-494, (1993).

    To do: Make this filter ND.

    See:  MorphologyImageFilter

    C++ includes: itkBinaryThinningImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryThinningImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkBinaryThinningImageFilterIUC2IUC2_Pointer"""
        return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryThinningImageFilterIUC2IUC2_Pointer":
        """Clone(itkBinaryThinningImageFilterIUC2IUC2 self) -> itkBinaryThinningImageFilterIUC2IUC2_Pointer"""
        return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_Clone(self)


    def GetThinning(self) -> "itkImageUC2 *":
        """
        GetThinning(itkBinaryThinningImageFilterIUC2IUC2 self) -> itkImageUC2

        Get Skelenton by
        thinning image. 
        """
        return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_GetThinning(self)

    SameDimensionCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_SameDimensionCheck
    InputAdditiveOperatorsCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_InputAdditiveOperatorsCheck
    InputConvertibleToIntCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_InputConvertibleToIntCheck
    IntConvertibleToInputCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_IntConvertibleToInputCheck
    SameTypeCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_SameTypeCheck
    __swig_destroy__ = _itkBinaryThinningImageFilterPython.delete_itkBinaryThinningImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkBinaryThinningImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkBinaryThinningImageFilterIUC2IUC2"""
        return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBinaryThinningImageFilterIUC2IUC2

        Create a new object of the class itkBinaryThinningImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryThinningImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryThinningImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryThinningImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryThinningImageFilterIUC2IUC2.Clone = new_instancemethod(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_Clone, None, itkBinaryThinningImageFilterIUC2IUC2)
itkBinaryThinningImageFilterIUC2IUC2.GetThinning = new_instancemethod(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_GetThinning, None, itkBinaryThinningImageFilterIUC2IUC2)
itkBinaryThinningImageFilterIUC2IUC2_swigregister = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_swigregister
itkBinaryThinningImageFilterIUC2IUC2_swigregister(itkBinaryThinningImageFilterIUC2IUC2)

def itkBinaryThinningImageFilterIUC2IUC2___New_orig__() -> "itkBinaryThinningImageFilterIUC2IUC2_Pointer":
    """itkBinaryThinningImageFilterIUC2IUC2___New_orig__() -> itkBinaryThinningImageFilterIUC2IUC2_Pointer"""
    return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2___New_orig__()

def itkBinaryThinningImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkBinaryThinningImageFilterIUC2IUC2 *":
    """itkBinaryThinningImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkBinaryThinningImageFilterIUC2IUC2"""
    return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_cast(obj)

class itkBinaryThinningImageFilterIUS2IUS2(itkImageToImageFilterAPython.itkImageToImageFilterIUS2IUS2):
    """


    This filter computes one-pixel-wide edges of the input image.

    This class is parameterized over the type of the input image and the
    type of the output image.

    The input is assumed to be a binary image. If the foreground pixels of
    the input image do not have a value of 1, they are rescaled to 1
    internally to simplify the computation.

    The filter will produce a skeleton of the object. The output
    background values are 0, and the foreground values are 1.

    This filter is a sequential thinning algorithm and known to be
    computational time dependable on the image size. The algorithm
    corresponds with the 2D implementation described in:

    Rafael C. Gonzales and Richard E. Woods. Digital Image Processing.
    Addison Wesley, 491-494, (1993).

    To do: Make this filter ND.

    See:  MorphologyImageFilter

    C++ includes: itkBinaryThinningImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryThinningImageFilterIUS2IUS2_Pointer":
        """__New_orig__() -> itkBinaryThinningImageFilterIUS2IUS2_Pointer"""
        return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryThinningImageFilterIUS2IUS2_Pointer":
        """Clone(itkBinaryThinningImageFilterIUS2IUS2 self) -> itkBinaryThinningImageFilterIUS2IUS2_Pointer"""
        return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_Clone(self)


    def GetThinning(self) -> "itkImageUS2 *":
        """
        GetThinning(itkBinaryThinningImageFilterIUS2IUS2 self) -> itkImageUS2

        Get Skelenton by
        thinning image. 
        """
        return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_GetThinning(self)

    SameDimensionCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_SameDimensionCheck
    InputAdditiveOperatorsCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_InputAdditiveOperatorsCheck
    InputConvertibleToIntCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_InputConvertibleToIntCheck
    IntConvertibleToInputCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_IntConvertibleToInputCheck
    SameTypeCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_SameTypeCheck
    __swig_destroy__ = _itkBinaryThinningImageFilterPython.delete_itkBinaryThinningImageFilterIUS2IUS2

    def cast(obj: 'itkLightObject') -> "itkBinaryThinningImageFilterIUS2IUS2 *":
        """cast(itkLightObject obj) -> itkBinaryThinningImageFilterIUS2IUS2"""
        return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBinaryThinningImageFilterIUS2IUS2

        Create a new object of the class itkBinaryThinningImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryThinningImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryThinningImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryThinningImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryThinningImageFilterIUS2IUS2.Clone = new_instancemethod(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_Clone, None, itkBinaryThinningImageFilterIUS2IUS2)
itkBinaryThinningImageFilterIUS2IUS2.GetThinning = new_instancemethod(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_GetThinning, None, itkBinaryThinningImageFilterIUS2IUS2)
itkBinaryThinningImageFilterIUS2IUS2_swigregister = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_swigregister
itkBinaryThinningImageFilterIUS2IUS2_swigregister(itkBinaryThinningImageFilterIUS2IUS2)

def itkBinaryThinningImageFilterIUS2IUS2___New_orig__() -> "itkBinaryThinningImageFilterIUS2IUS2_Pointer":
    """itkBinaryThinningImageFilterIUS2IUS2___New_orig__() -> itkBinaryThinningImageFilterIUS2IUS2_Pointer"""
    return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2___New_orig__()

def itkBinaryThinningImageFilterIUS2IUS2_cast(obj: 'itkLightObject') -> "itkBinaryThinningImageFilterIUS2IUS2 *":
    """itkBinaryThinningImageFilterIUS2IUS2_cast(itkLightObject obj) -> itkBinaryThinningImageFilterIUS2IUS2"""
    return _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def binary_thinning_image_filter(*args, **kwargs):
    """Procedural interface for BinaryThinningImageFilter"""
    import itk
    instance = itk.BinaryThinningImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def binary_thinning_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.BinaryThinningImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.BinaryThinningImageFilter.values()[0]
    else:
        filter_object = itk.BinaryThinningImageFilter

    binary_thinning_image_filter.__doc__ = filter_object.__doc__
    binary_thinning_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    binary_thinning_image_filter.__doc__ += "Available Keyword Arguments:\n"
    binary_thinning_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



