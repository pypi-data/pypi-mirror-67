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
    from . import _itkGeodesicActiveContourLevelSetImageFilterPython
else:
    import _itkGeodesicActiveContourLevelSetImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkGeodesicActiveContourLevelSetImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkGeodesicActiveContourLevelSetImageFilterPython.SWIG_PyStaticMethod_New

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


import itkSegmentationLevelSetImageFilterPython
import ITKCommonBasePython
import pyBasePython
import itkSparseFieldLevelSetImageFilterPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImagePython
import stdcomplexPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkCovariantVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkRGBPixelPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterBPython
import itkFiniteDifferenceFunctionPython
import itkSegmentationLevelSetFunctionPython
import itkLevelSetFunctionPython

def itkGeodesicActiveContourLevelSetImageFilterID3ID3D_New():
  return itkGeodesicActiveContourLevelSetImageFilterID3ID3D.New()


def itkGeodesicActiveContourLevelSetImageFilterIF3IF3F_New():
  return itkGeodesicActiveContourLevelSetImageFilterIF3IF3F.New()


def itkGeodesicActiveContourLevelSetImageFilterID2ID2D_New():
  return itkGeodesicActiveContourLevelSetImageFilterID2ID2D.New()


def itkGeodesicActiveContourLevelSetImageFilterIF2IF2F_New():
  return itkGeodesicActiveContourLevelSetImageFilterIF2IF2F.New()

class itkGeodesicActiveContourLevelSetImageFilterID2ID2D(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterID2ID2D):
    r"""Proxy of C++ itkGeodesicActiveContourLevelSetImageFilterID2ID2D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterID2ID2D___New_orig__)
    Clone = _swig_new_instance_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterID2ID2D_Clone)
    SetDerivativeSigma = _swig_new_instance_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterID2ID2D_SetDerivativeSigma)
    GetDerivativeSigma = _swig_new_instance_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterID2ID2D_GetDerivativeSigma)
    __swig_destroy__ = _itkGeodesicActiveContourLevelSetImageFilterPython.delete_itkGeodesicActiveContourLevelSetImageFilterID2ID2D
    cast = _swig_new_static_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterID2ID2D_cast)

    def New(*args, **kargs):
        """New() -> itkGeodesicActiveContourLevelSetImageFilterID2ID2D

        Create a new object of the class itkGeodesicActiveContourLevelSetImageFilterID2ID2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGeodesicActiveContourLevelSetImageFilterID2ID2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGeodesicActiveContourLevelSetImageFilterID2ID2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGeodesicActiveContourLevelSetImageFilterID2ID2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGeodesicActiveContourLevelSetImageFilterID2ID2D in _itkGeodesicActiveContourLevelSetImageFilterPython:
_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterID2ID2D_swigregister(itkGeodesicActiveContourLevelSetImageFilterID2ID2D)
itkGeodesicActiveContourLevelSetImageFilterID2ID2D___New_orig__ = _itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterID2ID2D___New_orig__
itkGeodesicActiveContourLevelSetImageFilterID2ID2D_cast = _itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterID2ID2D_cast

class itkGeodesicActiveContourLevelSetImageFilterID3ID3D(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterID3ID3D):
    r"""Proxy of C++ itkGeodesicActiveContourLevelSetImageFilterID3ID3D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterID3ID3D___New_orig__)
    Clone = _swig_new_instance_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterID3ID3D_Clone)
    SetDerivativeSigma = _swig_new_instance_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterID3ID3D_SetDerivativeSigma)
    GetDerivativeSigma = _swig_new_instance_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterID3ID3D_GetDerivativeSigma)
    __swig_destroy__ = _itkGeodesicActiveContourLevelSetImageFilterPython.delete_itkGeodesicActiveContourLevelSetImageFilterID3ID3D
    cast = _swig_new_static_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterID3ID3D_cast)

    def New(*args, **kargs):
        """New() -> itkGeodesicActiveContourLevelSetImageFilterID3ID3D

        Create a new object of the class itkGeodesicActiveContourLevelSetImageFilterID3ID3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGeodesicActiveContourLevelSetImageFilterID3ID3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGeodesicActiveContourLevelSetImageFilterID3ID3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGeodesicActiveContourLevelSetImageFilterID3ID3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGeodesicActiveContourLevelSetImageFilterID3ID3D in _itkGeodesicActiveContourLevelSetImageFilterPython:
_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterID3ID3D_swigregister(itkGeodesicActiveContourLevelSetImageFilterID3ID3D)
itkGeodesicActiveContourLevelSetImageFilterID3ID3D___New_orig__ = _itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterID3ID3D___New_orig__
itkGeodesicActiveContourLevelSetImageFilterID3ID3D_cast = _itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterID3ID3D_cast

class itkGeodesicActiveContourLevelSetImageFilterIF2IF2F(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF2IF2F):
    r"""Proxy of C++ itkGeodesicActiveContourLevelSetImageFilterIF2IF2F class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterIF2IF2F___New_orig__)
    Clone = _swig_new_instance_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterIF2IF2F_Clone)
    SetDerivativeSigma = _swig_new_instance_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterIF2IF2F_SetDerivativeSigma)
    GetDerivativeSigma = _swig_new_instance_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterIF2IF2F_GetDerivativeSigma)
    __swig_destroy__ = _itkGeodesicActiveContourLevelSetImageFilterPython.delete_itkGeodesicActiveContourLevelSetImageFilterIF2IF2F
    cast = _swig_new_static_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterIF2IF2F_cast)

    def New(*args, **kargs):
        """New() -> itkGeodesicActiveContourLevelSetImageFilterIF2IF2F

        Create a new object of the class itkGeodesicActiveContourLevelSetImageFilterIF2IF2F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGeodesicActiveContourLevelSetImageFilterIF2IF2F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGeodesicActiveContourLevelSetImageFilterIF2IF2F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGeodesicActiveContourLevelSetImageFilterIF2IF2F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGeodesicActiveContourLevelSetImageFilterIF2IF2F in _itkGeodesicActiveContourLevelSetImageFilterPython:
_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterIF2IF2F_swigregister(itkGeodesicActiveContourLevelSetImageFilterIF2IF2F)
itkGeodesicActiveContourLevelSetImageFilterIF2IF2F___New_orig__ = _itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterIF2IF2F___New_orig__
itkGeodesicActiveContourLevelSetImageFilterIF2IF2F_cast = _itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterIF2IF2F_cast

class itkGeodesicActiveContourLevelSetImageFilterIF3IF3F(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF3IF3F):
    r"""Proxy of C++ itkGeodesicActiveContourLevelSetImageFilterIF3IF3F class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterIF3IF3F___New_orig__)
    Clone = _swig_new_instance_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterIF3IF3F_Clone)
    SetDerivativeSigma = _swig_new_instance_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterIF3IF3F_SetDerivativeSigma)
    GetDerivativeSigma = _swig_new_instance_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterIF3IF3F_GetDerivativeSigma)
    __swig_destroy__ = _itkGeodesicActiveContourLevelSetImageFilterPython.delete_itkGeodesicActiveContourLevelSetImageFilterIF3IF3F
    cast = _swig_new_static_method(_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterIF3IF3F_cast)

    def New(*args, **kargs):
        """New() -> itkGeodesicActiveContourLevelSetImageFilterIF3IF3F

        Create a new object of the class itkGeodesicActiveContourLevelSetImageFilterIF3IF3F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGeodesicActiveContourLevelSetImageFilterIF3IF3F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGeodesicActiveContourLevelSetImageFilterIF3IF3F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGeodesicActiveContourLevelSetImageFilterIF3IF3F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGeodesicActiveContourLevelSetImageFilterIF3IF3F in _itkGeodesicActiveContourLevelSetImageFilterPython:
_itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterIF3IF3F_swigregister(itkGeodesicActiveContourLevelSetImageFilterIF3IF3F)
itkGeodesicActiveContourLevelSetImageFilterIF3IF3F___New_orig__ = _itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterIF3IF3F___New_orig__
itkGeodesicActiveContourLevelSetImageFilterIF3IF3F_cast = _itkGeodesicActiveContourLevelSetImageFilterPython.itkGeodesicActiveContourLevelSetImageFilterIF3IF3F_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def geodesic_active_contour_level_set_image_filter(*args, **kwargs):
    """Procedural interface for GeodesicActiveContourLevelSetImageFilter"""
    import itk
    instance = itk.GeodesicActiveContourLevelSetImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def geodesic_active_contour_level_set_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.GeodesicActiveContourLevelSetImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.GeodesicActiveContourLevelSetImageFilter.values()[0]
    else:
        filter_object = itk.GeodesicActiveContourLevelSetImageFilter

    geodesic_active_contour_level_set_image_filter.__doc__ = filter_object.__doc__
    geodesic_active_contour_level_set_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    geodesic_active_contour_level_set_image_filter.__doc__ += "Available Keyword Arguments:\n"
    geodesic_active_contour_level_set_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



