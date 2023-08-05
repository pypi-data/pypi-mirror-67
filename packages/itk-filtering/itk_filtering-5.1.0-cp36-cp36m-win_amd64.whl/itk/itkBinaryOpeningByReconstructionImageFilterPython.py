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
    from . import _itkBinaryOpeningByReconstructionImageFilterPython
else:
    import _itkBinaryOpeningByReconstructionImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBinaryOpeningByReconstructionImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBinaryOpeningByReconstructionImageFilterPython.SWIG_PyStaticMethod_New

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
import itkFlatStructuringElementPython
import itkBoxImageFilterPython
import itkImageToImageFilterAPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkImagePython
import itkFixedArrayPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import itkPointPython
import vnl_matrix_fixedPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkNeighborhoodPython

def itkBinaryOpeningByReconstructionImageFilterIUS3SE3_New():
  return itkBinaryOpeningByReconstructionImageFilterIUS3SE3.New()


def itkBinaryOpeningByReconstructionImageFilterIUC3SE3_New():
  return itkBinaryOpeningByReconstructionImageFilterIUC3SE3.New()


def itkBinaryOpeningByReconstructionImageFilterIUS2SE2_New():
  return itkBinaryOpeningByReconstructionImageFilterIUS2SE2.New()


def itkBinaryOpeningByReconstructionImageFilterIUC2SE2_New():
  return itkBinaryOpeningByReconstructionImageFilterIUC2SE2.New()

class itkBinaryOpeningByReconstructionImageFilterIUC2SE2(itkFlatStructuringElementPython.itkKernelImageFilterIUC2IUC2SE2):
    r"""Proxy of C++ itkBinaryOpeningByReconstructionImageFilterIUC2SE2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_Clone)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_GetForegroundValue)
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_GetBackgroundValue)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_FullyConnectedOff)
    __swig_destroy__ = _itkBinaryOpeningByReconstructionImageFilterPython.delete_itkBinaryOpeningByReconstructionImageFilterIUC2SE2
    cast = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryOpeningByReconstructionImageFilterIUC2SE2

        Create a new object of the class itkBinaryOpeningByReconstructionImageFilterIUC2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryOpeningByReconstructionImageFilterIUC2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryOpeningByReconstructionImageFilterIUC2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryOpeningByReconstructionImageFilterIUC2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryOpeningByReconstructionImageFilterIUC2SE2 in _itkBinaryOpeningByReconstructionImageFilterPython:
_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_swigregister(itkBinaryOpeningByReconstructionImageFilterIUC2SE2)
itkBinaryOpeningByReconstructionImageFilterIUC2SE2___New_orig__ = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2___New_orig__
itkBinaryOpeningByReconstructionImageFilterIUC2SE2_cast = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_cast

class itkBinaryOpeningByReconstructionImageFilterIUC3SE3(itkFlatStructuringElementPython.itkKernelImageFilterIUC3IUC3SE3):
    r"""Proxy of C++ itkBinaryOpeningByReconstructionImageFilterIUC3SE3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_Clone)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_GetForegroundValue)
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_GetBackgroundValue)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_FullyConnectedOff)
    __swig_destroy__ = _itkBinaryOpeningByReconstructionImageFilterPython.delete_itkBinaryOpeningByReconstructionImageFilterIUC3SE3
    cast = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryOpeningByReconstructionImageFilterIUC3SE3

        Create a new object of the class itkBinaryOpeningByReconstructionImageFilterIUC3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryOpeningByReconstructionImageFilterIUC3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryOpeningByReconstructionImageFilterIUC3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryOpeningByReconstructionImageFilterIUC3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryOpeningByReconstructionImageFilterIUC3SE3 in _itkBinaryOpeningByReconstructionImageFilterPython:
_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_swigregister(itkBinaryOpeningByReconstructionImageFilterIUC3SE3)
itkBinaryOpeningByReconstructionImageFilterIUC3SE3___New_orig__ = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3___New_orig__
itkBinaryOpeningByReconstructionImageFilterIUC3SE3_cast = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_cast

class itkBinaryOpeningByReconstructionImageFilterIUS2SE2(itkFlatStructuringElementPython.itkKernelImageFilterIUS2IUS2SE2):
    r"""Proxy of C++ itkBinaryOpeningByReconstructionImageFilterIUS2SE2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_Clone)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_GetForegroundValue)
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_GetBackgroundValue)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_FullyConnectedOff)
    __swig_destroy__ = _itkBinaryOpeningByReconstructionImageFilterPython.delete_itkBinaryOpeningByReconstructionImageFilterIUS2SE2
    cast = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryOpeningByReconstructionImageFilterIUS2SE2

        Create a new object of the class itkBinaryOpeningByReconstructionImageFilterIUS2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryOpeningByReconstructionImageFilterIUS2SE2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryOpeningByReconstructionImageFilterIUS2SE2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryOpeningByReconstructionImageFilterIUS2SE2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryOpeningByReconstructionImageFilterIUS2SE2 in _itkBinaryOpeningByReconstructionImageFilterPython:
_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_swigregister(itkBinaryOpeningByReconstructionImageFilterIUS2SE2)
itkBinaryOpeningByReconstructionImageFilterIUS2SE2___New_orig__ = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2___New_orig__
itkBinaryOpeningByReconstructionImageFilterIUS2SE2_cast = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_cast

class itkBinaryOpeningByReconstructionImageFilterIUS3SE3(itkFlatStructuringElementPython.itkKernelImageFilterIUS3IUS3SE3):
    r"""Proxy of C++ itkBinaryOpeningByReconstructionImageFilterIUS3SE3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_Clone)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_GetForegroundValue)
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_GetBackgroundValue)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_FullyConnectedOff)
    __swig_destroy__ = _itkBinaryOpeningByReconstructionImageFilterPython.delete_itkBinaryOpeningByReconstructionImageFilterIUS3SE3
    cast = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryOpeningByReconstructionImageFilterIUS3SE3

        Create a new object of the class itkBinaryOpeningByReconstructionImageFilterIUS3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryOpeningByReconstructionImageFilterIUS3SE3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryOpeningByReconstructionImageFilterIUS3SE3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryOpeningByReconstructionImageFilterIUS3SE3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryOpeningByReconstructionImageFilterIUS3SE3 in _itkBinaryOpeningByReconstructionImageFilterPython:
_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_swigregister(itkBinaryOpeningByReconstructionImageFilterIUS3SE3)
itkBinaryOpeningByReconstructionImageFilterIUS3SE3___New_orig__ = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3___New_orig__
itkBinaryOpeningByReconstructionImageFilterIUS3SE3_cast = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def binary_opening_by_reconstruction_image_filter(*args, **kwargs):
    """Procedural interface for BinaryOpeningByReconstructionImageFilter"""
    import itk
    instance = itk.BinaryOpeningByReconstructionImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def binary_opening_by_reconstruction_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.BinaryOpeningByReconstructionImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.BinaryOpeningByReconstructionImageFilter.values()[0]
    else:
        filter_object = itk.BinaryOpeningByReconstructionImageFilter

    binary_opening_by_reconstruction_image_filter.__doc__ = filter_object.__doc__
    binary_opening_by_reconstruction_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    binary_opening_by_reconstruction_image_filter.__doc__ += "Available Keyword Arguments:\n"
    binary_opening_by_reconstruction_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



