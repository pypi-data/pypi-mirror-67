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
    from . import _itkGradientVectorFlowImageFilterPython
else:
    import _itkGradientVectorFlowImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkGradientVectorFlowImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkGradientVectorFlowImageFilterPython.SWIG_PyStaticMethod_New

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


import itkImageToImageFilterAPython
import itkImageToImageFilterCommonPython
import pyBasePython
import ITKCommonBasePython
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
import itkLaplacianImageFilterPython

def itkGradientVectorFlowImageFilterICVF33ICVF33F_New():
  return itkGradientVectorFlowImageFilterICVF33ICVF33F.New()


def itkGradientVectorFlowImageFilterIVF33IVF33F_New():
  return itkGradientVectorFlowImageFilterIVF33IVF33F.New()


def itkGradientVectorFlowImageFilterICVF22ICVF22F_New():
  return itkGradientVectorFlowImageFilterICVF22ICVF22F.New()


def itkGradientVectorFlowImageFilterIVF22IVF22F_New():
  return itkGradientVectorFlowImageFilterIVF22IVF22F.New()

class itkGradientVectorFlowImageFilterICVF22ICVF22F(itkImageToImageFilterAPython.itkImageToImageFilterICVF22ICVF22):
    r"""Proxy of C++ itkGradientVectorFlowImageFilterICVF22ICVF22F class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_Clone)
    SetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_SetLaplacianFilter)
    GetModifiableLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_GetModifiableLaplacianFilter)
    GetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_GetLaplacianFilter)
    SetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_SetTimeStep)
    GetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_GetTimeStep)
    SetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_SetNoiseLevel)
    GetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_GetNoiseLevel)
    SetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_SetIterationNum)
    GetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_GetIterationNum)
    SameDimensionCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_SameDimensionCheck
    
    InputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_InputHasNumericTraitsCheck
    
    OutputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientVectorFlowImageFilterPython.delete_itkGradientVectorFlowImageFilterICVF22ICVF22F
    cast = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_cast)

    def New(*args, **kargs):
        """New() -> itkGradientVectorFlowImageFilterICVF22ICVF22F

        Create a new object of the class itkGradientVectorFlowImageFilterICVF22ICVF22F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientVectorFlowImageFilterICVF22ICVF22F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientVectorFlowImageFilterICVF22ICVF22F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientVectorFlowImageFilterICVF22ICVF22F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientVectorFlowImageFilterICVF22ICVF22F in _itkGradientVectorFlowImageFilterPython:
_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_swigregister(itkGradientVectorFlowImageFilterICVF22ICVF22F)
itkGradientVectorFlowImageFilterICVF22ICVF22F___New_orig__ = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F___New_orig__
itkGradientVectorFlowImageFilterICVF22ICVF22F_cast = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_cast

class itkGradientVectorFlowImageFilterICVF33ICVF33F(itkImageToImageFilterAPython.itkImageToImageFilterICVF33ICVF33):
    r"""Proxy of C++ itkGradientVectorFlowImageFilterICVF33ICVF33F class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_Clone)
    SetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_SetLaplacianFilter)
    GetModifiableLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_GetModifiableLaplacianFilter)
    GetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_GetLaplacianFilter)
    SetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_SetTimeStep)
    GetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_GetTimeStep)
    SetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_SetNoiseLevel)
    GetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_GetNoiseLevel)
    SetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_SetIterationNum)
    GetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_GetIterationNum)
    SameDimensionCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_SameDimensionCheck
    
    InputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_InputHasNumericTraitsCheck
    
    OutputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientVectorFlowImageFilterPython.delete_itkGradientVectorFlowImageFilterICVF33ICVF33F
    cast = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_cast)

    def New(*args, **kargs):
        """New() -> itkGradientVectorFlowImageFilterICVF33ICVF33F

        Create a new object of the class itkGradientVectorFlowImageFilterICVF33ICVF33F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientVectorFlowImageFilterICVF33ICVF33F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientVectorFlowImageFilterICVF33ICVF33F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientVectorFlowImageFilterICVF33ICVF33F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientVectorFlowImageFilterICVF33ICVF33F in _itkGradientVectorFlowImageFilterPython:
_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_swigregister(itkGradientVectorFlowImageFilterICVF33ICVF33F)
itkGradientVectorFlowImageFilterICVF33ICVF33F___New_orig__ = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F___New_orig__
itkGradientVectorFlowImageFilterICVF33ICVF33F_cast = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_cast

class itkGradientVectorFlowImageFilterIVF22IVF22F(itkImageToImageFilterAPython.itkImageToImageFilterIVF22IVF22):
    r"""Proxy of C++ itkGradientVectorFlowImageFilterIVF22IVF22F class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_Clone)
    SetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_SetLaplacianFilter)
    GetModifiableLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_GetModifiableLaplacianFilter)
    GetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_GetLaplacianFilter)
    SetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_SetTimeStep)
    GetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_GetTimeStep)
    SetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_SetNoiseLevel)
    GetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_GetNoiseLevel)
    SetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_SetIterationNum)
    GetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_GetIterationNum)
    SameDimensionCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_SameDimensionCheck
    
    InputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_InputHasNumericTraitsCheck
    
    OutputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientVectorFlowImageFilterPython.delete_itkGradientVectorFlowImageFilterIVF22IVF22F
    cast = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_cast)

    def New(*args, **kargs):
        """New() -> itkGradientVectorFlowImageFilterIVF22IVF22F

        Create a new object of the class itkGradientVectorFlowImageFilterIVF22IVF22F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientVectorFlowImageFilterIVF22IVF22F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientVectorFlowImageFilterIVF22IVF22F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientVectorFlowImageFilterIVF22IVF22F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientVectorFlowImageFilterIVF22IVF22F in _itkGradientVectorFlowImageFilterPython:
_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_swigregister(itkGradientVectorFlowImageFilterIVF22IVF22F)
itkGradientVectorFlowImageFilterIVF22IVF22F___New_orig__ = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F___New_orig__
itkGradientVectorFlowImageFilterIVF22IVF22F_cast = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_cast

class itkGradientVectorFlowImageFilterIVF33IVF33F(itkImageToImageFilterAPython.itkImageToImageFilterIVF33IVF33):
    r"""Proxy of C++ itkGradientVectorFlowImageFilterIVF33IVF33F class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_Clone)
    SetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_SetLaplacianFilter)
    GetModifiableLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_GetModifiableLaplacianFilter)
    GetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_GetLaplacianFilter)
    SetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_SetTimeStep)
    GetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_GetTimeStep)
    SetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_SetNoiseLevel)
    GetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_GetNoiseLevel)
    SetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_SetIterationNum)
    GetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_GetIterationNum)
    SameDimensionCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_SameDimensionCheck
    
    InputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_InputHasNumericTraitsCheck
    
    OutputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientVectorFlowImageFilterPython.delete_itkGradientVectorFlowImageFilterIVF33IVF33F
    cast = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_cast)

    def New(*args, **kargs):
        """New() -> itkGradientVectorFlowImageFilterIVF33IVF33F

        Create a new object of the class itkGradientVectorFlowImageFilterIVF33IVF33F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientVectorFlowImageFilterIVF33IVF33F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientVectorFlowImageFilterIVF33IVF33F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientVectorFlowImageFilterIVF33IVF33F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientVectorFlowImageFilterIVF33IVF33F in _itkGradientVectorFlowImageFilterPython:
_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_swigregister(itkGradientVectorFlowImageFilterIVF33IVF33F)
itkGradientVectorFlowImageFilterIVF33IVF33F___New_orig__ = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F___New_orig__
itkGradientVectorFlowImageFilterIVF33IVF33F_cast = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def gradient_vector_flow_image_filter(*args, **kwargs):
    """Procedural interface for GradientVectorFlowImageFilter"""
    import itk
    instance = itk.GradientVectorFlowImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def gradient_vector_flow_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.GradientVectorFlowImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.GradientVectorFlowImageFilter.values()[0]
    else:
        filter_object = itk.GradientVectorFlowImageFilter

    gradient_vector_flow_image_filter.__doc__ = filter_object.__doc__
    gradient_vector_flow_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    gradient_vector_flow_image_filter.__doc__ += "Available Keyword Arguments:\n"
    gradient_vector_flow_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



