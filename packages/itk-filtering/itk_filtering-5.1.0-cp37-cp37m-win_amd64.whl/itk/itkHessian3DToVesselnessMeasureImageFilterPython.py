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
    from . import _itkHessian3DToVesselnessMeasureImageFilterPython
else:
    import _itkHessian3DToVesselnessMeasureImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkHessian3DToVesselnessMeasureImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkHessian3DToVesselnessMeasureImageFilterPython.SWIG_PyStaticMethod_New

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
import itkImageToImageFilterBPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImagePython
import stdcomplexPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkOffsetPython
import itkSizePython
import itkCovariantVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkIndexPython
import itkRGBPixelPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkHessian3DToVesselnessMeasureImageFilterD_New():
  return itkHessian3DToVesselnessMeasureImageFilterD.New()


def itkHessian3DToVesselnessMeasureImageFilterF_New():
  return itkHessian3DToVesselnessMeasureImageFilterF.New()


def itkHessian3DToVesselnessMeasureImageFilterUS_New():
  return itkHessian3DToVesselnessMeasureImageFilterUS.New()


def itkHessian3DToVesselnessMeasureImageFilterUC_New():
  return itkHessian3DToVesselnessMeasureImageFilterUC.New()


def itkHessian3DToVesselnessMeasureImageFilterSS_New():
  return itkHessian3DToVesselnessMeasureImageFilterSS.New()

class itkHessian3DToVesselnessMeasureImageFilterD(itkImageToImageFilterBPython.itkImageToImageFilterISSRTD33ID3):
    r"""Proxy of C++ itkHessian3DToVesselnessMeasureImageFilterD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD___New_orig__)
    Clone = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_Clone)
    SetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_SetAlpha1)
    GetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_GetAlpha1)
    SetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_SetAlpha2)
    GetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_GetAlpha2)
    DoubleConvertibleToOutputCheck = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkHessian3DToVesselnessMeasureImageFilterPython.delete_itkHessian3DToVesselnessMeasureImageFilterD
    cast = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_cast)

    def New(*args, **kargs):
        """New() -> itkHessian3DToVesselnessMeasureImageFilterD

        Create a new object of the class itkHessian3DToVesselnessMeasureImageFilterD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHessian3DToVesselnessMeasureImageFilterD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHessian3DToVesselnessMeasureImageFilterD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHessian3DToVesselnessMeasureImageFilterD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHessian3DToVesselnessMeasureImageFilterD in _itkHessian3DToVesselnessMeasureImageFilterPython:
_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_swigregister(itkHessian3DToVesselnessMeasureImageFilterD)
itkHessian3DToVesselnessMeasureImageFilterD___New_orig__ = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD___New_orig__
itkHessian3DToVesselnessMeasureImageFilterD_cast = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_cast

class itkHessian3DToVesselnessMeasureImageFilterF(itkImageToImageFilterBPython.itkImageToImageFilterISSRTD33IF3):
    r"""Proxy of C++ itkHessian3DToVesselnessMeasureImageFilterF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF___New_orig__)
    Clone = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_Clone)
    SetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_SetAlpha1)
    GetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_GetAlpha1)
    SetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_SetAlpha2)
    GetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_GetAlpha2)
    DoubleConvertibleToOutputCheck = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkHessian3DToVesselnessMeasureImageFilterPython.delete_itkHessian3DToVesselnessMeasureImageFilterF
    cast = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_cast)

    def New(*args, **kargs):
        """New() -> itkHessian3DToVesselnessMeasureImageFilterF

        Create a new object of the class itkHessian3DToVesselnessMeasureImageFilterF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHessian3DToVesselnessMeasureImageFilterF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHessian3DToVesselnessMeasureImageFilterF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHessian3DToVesselnessMeasureImageFilterF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHessian3DToVesselnessMeasureImageFilterF in _itkHessian3DToVesselnessMeasureImageFilterPython:
_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_swigregister(itkHessian3DToVesselnessMeasureImageFilterF)
itkHessian3DToVesselnessMeasureImageFilterF___New_orig__ = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF___New_orig__
itkHessian3DToVesselnessMeasureImageFilterF_cast = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_cast

class itkHessian3DToVesselnessMeasureImageFilterSS(itkImageToImageFilterBPython.itkImageToImageFilterISSRTD33ISS3):
    r"""Proxy of C++ itkHessian3DToVesselnessMeasureImageFilterSS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS___New_orig__)
    Clone = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_Clone)
    SetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_SetAlpha1)
    GetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_GetAlpha1)
    SetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_SetAlpha2)
    GetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_GetAlpha2)
    DoubleConvertibleToOutputCheck = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkHessian3DToVesselnessMeasureImageFilterPython.delete_itkHessian3DToVesselnessMeasureImageFilterSS
    cast = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_cast)

    def New(*args, **kargs):
        """New() -> itkHessian3DToVesselnessMeasureImageFilterSS

        Create a new object of the class itkHessian3DToVesselnessMeasureImageFilterSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHessian3DToVesselnessMeasureImageFilterSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHessian3DToVesselnessMeasureImageFilterSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHessian3DToVesselnessMeasureImageFilterSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHessian3DToVesselnessMeasureImageFilterSS in _itkHessian3DToVesselnessMeasureImageFilterPython:
_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_swigregister(itkHessian3DToVesselnessMeasureImageFilterSS)
itkHessian3DToVesselnessMeasureImageFilterSS___New_orig__ = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS___New_orig__
itkHessian3DToVesselnessMeasureImageFilterSS_cast = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_cast

class itkHessian3DToVesselnessMeasureImageFilterUC(itkImageToImageFilterBPython.itkImageToImageFilterISSRTD33IUC3):
    r"""Proxy of C++ itkHessian3DToVesselnessMeasureImageFilterUC class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC___New_orig__)
    Clone = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_Clone)
    SetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_SetAlpha1)
    GetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_GetAlpha1)
    SetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_SetAlpha2)
    GetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_GetAlpha2)
    DoubleConvertibleToOutputCheck = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkHessian3DToVesselnessMeasureImageFilterPython.delete_itkHessian3DToVesselnessMeasureImageFilterUC
    cast = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_cast)

    def New(*args, **kargs):
        """New() -> itkHessian3DToVesselnessMeasureImageFilterUC

        Create a new object of the class itkHessian3DToVesselnessMeasureImageFilterUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHessian3DToVesselnessMeasureImageFilterUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHessian3DToVesselnessMeasureImageFilterUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHessian3DToVesselnessMeasureImageFilterUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHessian3DToVesselnessMeasureImageFilterUC in _itkHessian3DToVesselnessMeasureImageFilterPython:
_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_swigregister(itkHessian3DToVesselnessMeasureImageFilterUC)
itkHessian3DToVesselnessMeasureImageFilterUC___New_orig__ = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC___New_orig__
itkHessian3DToVesselnessMeasureImageFilterUC_cast = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_cast

class itkHessian3DToVesselnessMeasureImageFilterUS(itkImageToImageFilterBPython.itkImageToImageFilterISSRTD33IUS3):
    r"""Proxy of C++ itkHessian3DToVesselnessMeasureImageFilterUS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS___New_orig__)
    Clone = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_Clone)
    SetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_SetAlpha1)
    GetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_GetAlpha1)
    SetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_SetAlpha2)
    GetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_GetAlpha2)
    DoubleConvertibleToOutputCheck = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkHessian3DToVesselnessMeasureImageFilterPython.delete_itkHessian3DToVesselnessMeasureImageFilterUS
    cast = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_cast)

    def New(*args, **kargs):
        """New() -> itkHessian3DToVesselnessMeasureImageFilterUS

        Create a new object of the class itkHessian3DToVesselnessMeasureImageFilterUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHessian3DToVesselnessMeasureImageFilterUS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHessian3DToVesselnessMeasureImageFilterUS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHessian3DToVesselnessMeasureImageFilterUS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHessian3DToVesselnessMeasureImageFilterUS in _itkHessian3DToVesselnessMeasureImageFilterPython:
_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_swigregister(itkHessian3DToVesselnessMeasureImageFilterUS)
itkHessian3DToVesselnessMeasureImageFilterUS___New_orig__ = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS___New_orig__
itkHessian3DToVesselnessMeasureImageFilterUS_cast = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def hessian3_d_to_vesselness_measure_image_filter(*args, **kwargs):
    """Procedural interface for Hessian3DToVesselnessMeasureImageFilter"""
    import itk
    instance = itk.Hessian3DToVesselnessMeasureImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def hessian3_d_to_vesselness_measure_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.Hessian3DToVesselnessMeasureImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.Hessian3DToVesselnessMeasureImageFilter.values()[0]
    else:
        filter_object = itk.Hessian3DToVesselnessMeasureImageFilter

    hessian3_d_to_vesselness_measure_image_filter.__doc__ = filter_object.__doc__
    hessian3_d_to_vesselness_measure_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    hessian3_d_to_vesselness_measure_image_filter.__doc__ += "Available Keyword Arguments:\n"
    hessian3_d_to_vesselness_measure_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



