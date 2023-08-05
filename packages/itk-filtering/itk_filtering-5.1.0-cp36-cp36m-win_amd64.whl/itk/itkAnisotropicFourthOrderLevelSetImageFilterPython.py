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
    from . import _itkAnisotropicFourthOrderLevelSetImageFilterPython
else:
    import _itkAnisotropicFourthOrderLevelSetImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkAnisotropicFourthOrderLevelSetImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkAnisotropicFourthOrderLevelSetImageFilterPython.SWIG_PyStaticMethod_New

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


import itkSparseFieldFourthOrderLevelSetImageFilterPython
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
import itkFiniteDifferenceFunctionPython
import itkLevelSetFunctionPython

def itkAnisotropicFourthOrderLevelSetImageFilterID3ID3_New():
  return itkAnisotropicFourthOrderLevelSetImageFilterID3ID3.New()


def itkAnisotropicFourthOrderLevelSetImageFilterID2ID2_New():
  return itkAnisotropicFourthOrderLevelSetImageFilterID2ID2.New()


def itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_New():
  return itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3.New()


def itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_New():
  return itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2.New()

class itkAnisotropicFourthOrderLevelSetImageFilterID2ID2(itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterID2ID2):
    r"""Proxy of C++ itkAnisotropicFourthOrderLevelSetImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterID2ID2_Clone)
    GetMaxFilterIteration = _swig_new_instance_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterID2ID2_GetMaxFilterIteration)
    SetMaxFilterIteration = _swig_new_instance_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterID2ID2_SetMaxFilterIteration)
    __swig_destroy__ = _itkAnisotropicFourthOrderLevelSetImageFilterPython.delete_itkAnisotropicFourthOrderLevelSetImageFilterID2ID2
    cast = _swig_new_static_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkAnisotropicFourthOrderLevelSetImageFilterID2ID2

        Create a new object of the class itkAnisotropicFourthOrderLevelSetImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAnisotropicFourthOrderLevelSetImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAnisotropicFourthOrderLevelSetImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAnisotropicFourthOrderLevelSetImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAnisotropicFourthOrderLevelSetImageFilterID2ID2 in _itkAnisotropicFourthOrderLevelSetImageFilterPython:
_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterID2ID2_swigregister(itkAnisotropicFourthOrderLevelSetImageFilterID2ID2)
itkAnisotropicFourthOrderLevelSetImageFilterID2ID2___New_orig__ = _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterID2ID2___New_orig__
itkAnisotropicFourthOrderLevelSetImageFilterID2ID2_cast = _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterID2ID2_cast

class itkAnisotropicFourthOrderLevelSetImageFilterID3ID3(itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterID3ID3):
    r"""Proxy of C++ itkAnisotropicFourthOrderLevelSetImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterID3ID3_Clone)
    GetMaxFilterIteration = _swig_new_instance_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterID3ID3_GetMaxFilterIteration)
    SetMaxFilterIteration = _swig_new_instance_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterID3ID3_SetMaxFilterIteration)
    __swig_destroy__ = _itkAnisotropicFourthOrderLevelSetImageFilterPython.delete_itkAnisotropicFourthOrderLevelSetImageFilterID3ID3
    cast = _swig_new_static_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkAnisotropicFourthOrderLevelSetImageFilterID3ID3

        Create a new object of the class itkAnisotropicFourthOrderLevelSetImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAnisotropicFourthOrderLevelSetImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAnisotropicFourthOrderLevelSetImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAnisotropicFourthOrderLevelSetImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAnisotropicFourthOrderLevelSetImageFilterID3ID3 in _itkAnisotropicFourthOrderLevelSetImageFilterPython:
_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterID3ID3_swigregister(itkAnisotropicFourthOrderLevelSetImageFilterID3ID3)
itkAnisotropicFourthOrderLevelSetImageFilterID3ID3___New_orig__ = _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterID3ID3___New_orig__
itkAnisotropicFourthOrderLevelSetImageFilterID3ID3_cast = _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterID3ID3_cast

class itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2(itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterIF2IF2):
    r"""Proxy of C++ itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_Clone)
    GetMaxFilterIteration = _swig_new_instance_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_GetMaxFilterIteration)
    SetMaxFilterIteration = _swig_new_instance_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_SetMaxFilterIteration)
    __swig_destroy__ = _itkAnisotropicFourthOrderLevelSetImageFilterPython.delete_itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2
    cast = _swig_new_static_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2

        Create a new object of the class itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2 in _itkAnisotropicFourthOrderLevelSetImageFilterPython:
_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_swigregister(itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2)
itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2___New_orig__ = _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2___New_orig__
itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_cast = _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2_cast

class itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3(itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterIF3IF3):
    r"""Proxy of C++ itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_Clone)
    GetMaxFilterIteration = _swig_new_instance_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_GetMaxFilterIteration)
    SetMaxFilterIteration = _swig_new_instance_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_SetMaxFilterIteration)
    __swig_destroy__ = _itkAnisotropicFourthOrderLevelSetImageFilterPython.delete_itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3
    cast = _swig_new_static_method(_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3

        Create a new object of the class itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3 in _itkAnisotropicFourthOrderLevelSetImageFilterPython:
_itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_swigregister(itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3)
itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3___New_orig__ = _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3___New_orig__
itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_cast = _itkAnisotropicFourthOrderLevelSetImageFilterPython.itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def anisotropic_fourth_order_level_set_image_filter(*args, **kwargs):
    """Procedural interface for AnisotropicFourthOrderLevelSetImageFilter"""
    import itk
    instance = itk.AnisotropicFourthOrderLevelSetImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def anisotropic_fourth_order_level_set_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.AnisotropicFourthOrderLevelSetImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.AnisotropicFourthOrderLevelSetImageFilter.values()[0]
    else:
        filter_object = itk.AnisotropicFourthOrderLevelSetImageFilter

    anisotropic_fourth_order_level_set_image_filter.__doc__ = filter_object.__doc__
    anisotropic_fourth_order_level_set_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    anisotropic_fourth_order_level_set_image_filter.__doc__ += "Available Keyword Arguments:\n"
    anisotropic_fourth_order_level_set_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



