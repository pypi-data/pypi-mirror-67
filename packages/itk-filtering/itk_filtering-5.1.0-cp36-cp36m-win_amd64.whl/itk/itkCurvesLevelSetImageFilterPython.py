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
    from . import _itkCurvesLevelSetImageFilterPython
else:
    import _itkCurvesLevelSetImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkCurvesLevelSetImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkCurvesLevelSetImageFilterPython.SWIG_PyStaticMethod_New

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
import itkImagePython
import itkFixedArrayPython
import pyBasePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkSizePython
import ITKCommonBasePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import itkPointPython
import vnl_matrix_fixedPython
import itkIndexPython
import itkOffsetPython
import itkImageRegionPython
import itkSegmentationLevelSetFunctionPython
import itkLevelSetFunctionPython
import itkFiniteDifferenceFunctionPython
import itkSparseFieldLevelSetImageFilterPython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterAPython

def itkCurvesLevelSetImageFilterID3ID3D_New():
  return itkCurvesLevelSetImageFilterID3ID3D.New()


def itkCurvesLevelSetImageFilterIF3IF3F_New():
  return itkCurvesLevelSetImageFilterIF3IF3F.New()


def itkCurvesLevelSetImageFilterID2ID2D_New():
  return itkCurvesLevelSetImageFilterID2ID2D.New()


def itkCurvesLevelSetImageFilterIF2IF2F_New():
  return itkCurvesLevelSetImageFilterIF2IF2F.New()

class itkCurvesLevelSetImageFilterID2ID2D(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterID2ID2D):
    r"""Proxy of C++ itkCurvesLevelSetImageFilterID2ID2D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID2ID2D___New_orig__)
    Clone = _swig_new_instance_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID2ID2D_Clone)
    SetDerivativeSigma = _swig_new_instance_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID2ID2D_SetDerivativeSigma)
    GetDerivativeSigma = _swig_new_instance_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID2ID2D_GetDerivativeSigma)
    OutputHasNumericTraitsCheck = _itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID2ID2D_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkCurvesLevelSetImageFilterPython.delete_itkCurvesLevelSetImageFilterID2ID2D
    cast = _swig_new_static_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID2ID2D_cast)

    def New(*args, **kargs):
        """New() -> itkCurvesLevelSetImageFilterID2ID2D

        Create a new object of the class itkCurvesLevelSetImageFilterID2ID2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvesLevelSetImageFilterID2ID2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCurvesLevelSetImageFilterID2ID2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCurvesLevelSetImageFilterID2ID2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCurvesLevelSetImageFilterID2ID2D in _itkCurvesLevelSetImageFilterPython:
_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID2ID2D_swigregister(itkCurvesLevelSetImageFilterID2ID2D)
itkCurvesLevelSetImageFilterID2ID2D___New_orig__ = _itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID2ID2D___New_orig__
itkCurvesLevelSetImageFilterID2ID2D_cast = _itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID2ID2D_cast

class itkCurvesLevelSetImageFilterID3ID3D(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterID3ID3D):
    r"""Proxy of C++ itkCurvesLevelSetImageFilterID3ID3D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID3ID3D___New_orig__)
    Clone = _swig_new_instance_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID3ID3D_Clone)
    SetDerivativeSigma = _swig_new_instance_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID3ID3D_SetDerivativeSigma)
    GetDerivativeSigma = _swig_new_instance_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID3ID3D_GetDerivativeSigma)
    OutputHasNumericTraitsCheck = _itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID3ID3D_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkCurvesLevelSetImageFilterPython.delete_itkCurvesLevelSetImageFilterID3ID3D
    cast = _swig_new_static_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID3ID3D_cast)

    def New(*args, **kargs):
        """New() -> itkCurvesLevelSetImageFilterID3ID3D

        Create a new object of the class itkCurvesLevelSetImageFilterID3ID3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvesLevelSetImageFilterID3ID3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCurvesLevelSetImageFilterID3ID3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCurvesLevelSetImageFilterID3ID3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCurvesLevelSetImageFilterID3ID3D in _itkCurvesLevelSetImageFilterPython:
_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID3ID3D_swigregister(itkCurvesLevelSetImageFilterID3ID3D)
itkCurvesLevelSetImageFilterID3ID3D___New_orig__ = _itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID3ID3D___New_orig__
itkCurvesLevelSetImageFilterID3ID3D_cast = _itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterID3ID3D_cast

class itkCurvesLevelSetImageFilterIF2IF2F(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF2IF2F):
    r"""Proxy of C++ itkCurvesLevelSetImageFilterIF2IF2F class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF2IF2F___New_orig__)
    Clone = _swig_new_instance_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF2IF2F_Clone)
    SetDerivativeSigma = _swig_new_instance_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF2IF2F_SetDerivativeSigma)
    GetDerivativeSigma = _swig_new_instance_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF2IF2F_GetDerivativeSigma)
    OutputHasNumericTraitsCheck = _itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF2IF2F_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkCurvesLevelSetImageFilterPython.delete_itkCurvesLevelSetImageFilterIF2IF2F
    cast = _swig_new_static_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF2IF2F_cast)

    def New(*args, **kargs):
        """New() -> itkCurvesLevelSetImageFilterIF2IF2F

        Create a new object of the class itkCurvesLevelSetImageFilterIF2IF2F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvesLevelSetImageFilterIF2IF2F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCurvesLevelSetImageFilterIF2IF2F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCurvesLevelSetImageFilterIF2IF2F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCurvesLevelSetImageFilterIF2IF2F in _itkCurvesLevelSetImageFilterPython:
_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF2IF2F_swigregister(itkCurvesLevelSetImageFilterIF2IF2F)
itkCurvesLevelSetImageFilterIF2IF2F___New_orig__ = _itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF2IF2F___New_orig__
itkCurvesLevelSetImageFilterIF2IF2F_cast = _itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF2IF2F_cast

class itkCurvesLevelSetImageFilterIF3IF3F(itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF3IF3F):
    r"""Proxy of C++ itkCurvesLevelSetImageFilterIF3IF3F class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF3IF3F___New_orig__)
    Clone = _swig_new_instance_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF3IF3F_Clone)
    SetDerivativeSigma = _swig_new_instance_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF3IF3F_SetDerivativeSigma)
    GetDerivativeSigma = _swig_new_instance_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF3IF3F_GetDerivativeSigma)
    OutputHasNumericTraitsCheck = _itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF3IF3F_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkCurvesLevelSetImageFilterPython.delete_itkCurvesLevelSetImageFilterIF3IF3F
    cast = _swig_new_static_method(_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF3IF3F_cast)

    def New(*args, **kargs):
        """New() -> itkCurvesLevelSetImageFilterIF3IF3F

        Create a new object of the class itkCurvesLevelSetImageFilterIF3IF3F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvesLevelSetImageFilterIF3IF3F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCurvesLevelSetImageFilterIF3IF3F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCurvesLevelSetImageFilterIF3IF3F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCurvesLevelSetImageFilterIF3IF3F in _itkCurvesLevelSetImageFilterPython:
_itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF3IF3F_swigregister(itkCurvesLevelSetImageFilterIF3IF3F)
itkCurvesLevelSetImageFilterIF3IF3F___New_orig__ = _itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF3IF3F___New_orig__
itkCurvesLevelSetImageFilterIF3IF3F_cast = _itkCurvesLevelSetImageFilterPython.itkCurvesLevelSetImageFilterIF3IF3F_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def curves_level_set_image_filter(*args, **kwargs):
    """Procedural interface for CurvesLevelSetImageFilter"""
    import itk
    instance = itk.CurvesLevelSetImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def curves_level_set_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.CurvesLevelSetImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.CurvesLevelSetImageFilter.values()[0]
    else:
        filter_object = itk.CurvesLevelSetImageFilter

    curves_level_set_image_filter.__doc__ = filter_object.__doc__
    curves_level_set_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    curves_level_set_image_filter.__doc__ += "Available Keyword Arguments:\n"
    curves_level_set_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



