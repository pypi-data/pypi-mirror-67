# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkNarrowBandCurvesLevelSetImageFilterPython
else:
    import _itkNarrowBandCurvesLevelSetImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkNarrowBandCurvesLevelSetImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkNarrowBandCurvesLevelSetImageFilterPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import ITKCommonBasePython
import pyBasePython
import itkNarrowBandLevelSetImageFilterPython
import itkImagePython
import itkPointPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkRGBAPixelPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkSegmentationLevelSetFunctionPython
import itkLevelSetFunctionPython
import itkFiniteDifferenceFunctionPython
import itkNarrowBandImageFilterBasePython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython
import ITKNarrowBandBasePython

def itkNarrowBandCurvesLevelSetImageFilterID3ID3D_New():
  return itkNarrowBandCurvesLevelSetImageFilterID3ID3D.New()


def itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_New():
  return itkNarrowBandCurvesLevelSetImageFilterIF3IF3F.New()


def itkNarrowBandCurvesLevelSetImageFilterID2ID2D_New():
  return itkNarrowBandCurvesLevelSetImageFilterID2ID2D.New()


def itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_New():
  return itkNarrowBandCurvesLevelSetImageFilterIF2IF2F.New()

class itkNarrowBandCurvesLevelSetImageFilterID2ID2D(itkNarrowBandLevelSetImageFilterPython.itkNarrowBandLevelSetImageFilterID2ID2D):
    r"""Proxy of C++ itkNarrowBandCurvesLevelSetImageFilterID2ID2D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D___New_orig__)
    Clone = _swig_new_instance_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_Clone)
    SetDerivativeSigma = _swig_new_instance_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_SetDerivativeSigma)
    GetDerivativeSigma = _swig_new_instance_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_GetDerivativeSigma)
    OutputHasNumericTraitsCheck = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkNarrowBandCurvesLevelSetImageFilterPython.delete_itkNarrowBandCurvesLevelSetImageFilterID2ID2D
    cast = _swig_new_static_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_cast)

    def New(*args, **kargs):
        """New() -> itkNarrowBandCurvesLevelSetImageFilterID2ID2D

        Create a new object of the class itkNarrowBandCurvesLevelSetImageFilterID2ID2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNarrowBandCurvesLevelSetImageFilterID2ID2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNarrowBandCurvesLevelSetImageFilterID2ID2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNarrowBandCurvesLevelSetImageFilterID2ID2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkNarrowBandCurvesLevelSetImageFilterID2ID2D in _itkNarrowBandCurvesLevelSetImageFilterPython:
_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_swigregister(itkNarrowBandCurvesLevelSetImageFilterID2ID2D)
itkNarrowBandCurvesLevelSetImageFilterID2ID2D___New_orig__ = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D___New_orig__
itkNarrowBandCurvesLevelSetImageFilterID2ID2D_cast = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID2ID2D_cast

class itkNarrowBandCurvesLevelSetImageFilterID3ID3D(itkNarrowBandLevelSetImageFilterPython.itkNarrowBandLevelSetImageFilterID3ID3D):
    r"""Proxy of C++ itkNarrowBandCurvesLevelSetImageFilterID3ID3D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D___New_orig__)
    Clone = _swig_new_instance_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_Clone)
    SetDerivativeSigma = _swig_new_instance_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_SetDerivativeSigma)
    GetDerivativeSigma = _swig_new_instance_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_GetDerivativeSigma)
    OutputHasNumericTraitsCheck = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkNarrowBandCurvesLevelSetImageFilterPython.delete_itkNarrowBandCurvesLevelSetImageFilterID3ID3D
    cast = _swig_new_static_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_cast)

    def New(*args, **kargs):
        """New() -> itkNarrowBandCurvesLevelSetImageFilterID3ID3D

        Create a new object of the class itkNarrowBandCurvesLevelSetImageFilterID3ID3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNarrowBandCurvesLevelSetImageFilterID3ID3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNarrowBandCurvesLevelSetImageFilterID3ID3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNarrowBandCurvesLevelSetImageFilterID3ID3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkNarrowBandCurvesLevelSetImageFilterID3ID3D in _itkNarrowBandCurvesLevelSetImageFilterPython:
_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_swigregister(itkNarrowBandCurvesLevelSetImageFilterID3ID3D)
itkNarrowBandCurvesLevelSetImageFilterID3ID3D___New_orig__ = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D___New_orig__
itkNarrowBandCurvesLevelSetImageFilterID3ID3D_cast = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterID3ID3D_cast

class itkNarrowBandCurvesLevelSetImageFilterIF2IF2F(itkNarrowBandLevelSetImageFilterPython.itkNarrowBandLevelSetImageFilterIF2IF2F):
    r"""Proxy of C++ itkNarrowBandCurvesLevelSetImageFilterIF2IF2F class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F___New_orig__)
    Clone = _swig_new_instance_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_Clone)
    SetDerivativeSigma = _swig_new_instance_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_SetDerivativeSigma)
    GetDerivativeSigma = _swig_new_instance_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_GetDerivativeSigma)
    OutputHasNumericTraitsCheck = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkNarrowBandCurvesLevelSetImageFilterPython.delete_itkNarrowBandCurvesLevelSetImageFilterIF2IF2F
    cast = _swig_new_static_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_cast)

    def New(*args, **kargs):
        """New() -> itkNarrowBandCurvesLevelSetImageFilterIF2IF2F

        Create a new object of the class itkNarrowBandCurvesLevelSetImageFilterIF2IF2F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNarrowBandCurvesLevelSetImageFilterIF2IF2F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNarrowBandCurvesLevelSetImageFilterIF2IF2F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNarrowBandCurvesLevelSetImageFilterIF2IF2F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkNarrowBandCurvesLevelSetImageFilterIF2IF2F in _itkNarrowBandCurvesLevelSetImageFilterPython:
_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_swigregister(itkNarrowBandCurvesLevelSetImageFilterIF2IF2F)
itkNarrowBandCurvesLevelSetImageFilterIF2IF2F___New_orig__ = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F___New_orig__
itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_cast = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF2IF2F_cast

class itkNarrowBandCurvesLevelSetImageFilterIF3IF3F(itkNarrowBandLevelSetImageFilterPython.itkNarrowBandLevelSetImageFilterIF3IF3F):
    r"""Proxy of C++ itkNarrowBandCurvesLevelSetImageFilterIF3IF3F class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F___New_orig__)
    Clone = _swig_new_instance_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_Clone)
    SetDerivativeSigma = _swig_new_instance_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_SetDerivativeSigma)
    GetDerivativeSigma = _swig_new_instance_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_GetDerivativeSigma)
    OutputHasNumericTraitsCheck = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkNarrowBandCurvesLevelSetImageFilterPython.delete_itkNarrowBandCurvesLevelSetImageFilterIF3IF3F
    cast = _swig_new_static_method(_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_cast)

    def New(*args, **kargs):
        """New() -> itkNarrowBandCurvesLevelSetImageFilterIF3IF3F

        Create a new object of the class itkNarrowBandCurvesLevelSetImageFilterIF3IF3F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNarrowBandCurvesLevelSetImageFilterIF3IF3F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNarrowBandCurvesLevelSetImageFilterIF3IF3F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNarrowBandCurvesLevelSetImageFilterIF3IF3F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkNarrowBandCurvesLevelSetImageFilterIF3IF3F in _itkNarrowBandCurvesLevelSetImageFilterPython:
_itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_swigregister(itkNarrowBandCurvesLevelSetImageFilterIF3IF3F)
itkNarrowBandCurvesLevelSetImageFilterIF3IF3F___New_orig__ = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F___New_orig__
itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_cast = _itkNarrowBandCurvesLevelSetImageFilterPython.itkNarrowBandCurvesLevelSetImageFilterIF3IF3F_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def narrow_band_curves_level_set_image_filter(*args, **kwargs):
    """Procedural interface for NarrowBandCurvesLevelSetImageFilter"""
    import itk
    instance = itk.NarrowBandCurvesLevelSetImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def narrow_band_curves_level_set_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.NarrowBandCurvesLevelSetImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.NarrowBandCurvesLevelSetImageFilter.values()[0]
    else:
        filter_object = itk.NarrowBandCurvesLevelSetImageFilter

    narrow_band_curves_level_set_image_filter.__doc__ = filter_object.__doc__
    narrow_band_curves_level_set_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    narrow_band_curves_level_set_image_filter.__doc__ += "Available Keyword Arguments:\n"
    narrow_band_curves_level_set_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



