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
    from . import _itkLabelMapToRGBImageFilterPython
else:
    import _itkLabelMapToRGBImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLabelMapToRGBImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLabelMapToRGBImageFilterPython.SWIG_PyStaticMethod_New

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
import itkLabelMapFilterPython
import ITKLabelMapBasePython
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
import itkStatisticsLabelObjectPython
import itkHistogramPython
import itkArrayPython
import itkSamplePython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkAffineTransformPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkArray2DPython
import itkOptimizerParametersPython
import itkMatrixOffsetTransformBasePython
import itkImageToImageFilterCommonPython

def itkLabelMapToRGBImageFilterLM3IRGBUC3_New():
  return itkLabelMapToRGBImageFilterLM3IRGBUC3.New()


def itkLabelMapToRGBImageFilterLM2IRGBUC2_New():
  return itkLabelMapToRGBImageFilterLM2IRGBUC2.New()

class itkLabelMapToRGBImageFilterLM2IRGBUC2(itkLabelMapFilterPython.itkLabelMapFilterLM2IRGBUC2):
    r"""Proxy of C++ itkLabelMapToRGBImageFilterLM2IRGBUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_Clone)
    SetFunctor = _swig_new_instance_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_SetFunctor)
    GetFunctor = _swig_new_instance_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_GetFunctor)
    __swig_destroy__ = _itkLabelMapToRGBImageFilterPython.delete_itkLabelMapToRGBImageFilterLM2IRGBUC2
    cast = _swig_new_static_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToRGBImageFilterLM2IRGBUC2

        Create a new object of the class itkLabelMapToRGBImageFilterLM2IRGBUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToRGBImageFilterLM2IRGBUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapToRGBImageFilterLM2IRGBUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapToRGBImageFilterLM2IRGBUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToRGBImageFilterLM2IRGBUC2 in _itkLabelMapToRGBImageFilterPython:
_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_swigregister(itkLabelMapToRGBImageFilterLM2IRGBUC2)
itkLabelMapToRGBImageFilterLM2IRGBUC2___New_orig__ = _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2___New_orig__
itkLabelMapToRGBImageFilterLM2IRGBUC2_cast = _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_cast

class itkLabelMapToRGBImageFilterLM3IRGBUC3(itkLabelMapFilterPython.itkLabelMapFilterLM3IRGBUC3):
    r"""Proxy of C++ itkLabelMapToRGBImageFilterLM3IRGBUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_Clone)
    SetFunctor = _swig_new_instance_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_SetFunctor)
    GetFunctor = _swig_new_instance_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_GetFunctor)
    __swig_destroy__ = _itkLabelMapToRGBImageFilterPython.delete_itkLabelMapToRGBImageFilterLM3IRGBUC3
    cast = _swig_new_static_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToRGBImageFilterLM3IRGBUC3

        Create a new object of the class itkLabelMapToRGBImageFilterLM3IRGBUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToRGBImageFilterLM3IRGBUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapToRGBImageFilterLM3IRGBUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapToRGBImageFilterLM3IRGBUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToRGBImageFilterLM3IRGBUC3 in _itkLabelMapToRGBImageFilterPython:
_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_swigregister(itkLabelMapToRGBImageFilterLM3IRGBUC3)
itkLabelMapToRGBImageFilterLM3IRGBUC3___New_orig__ = _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3___New_orig__
itkLabelMapToRGBImageFilterLM3IRGBUC3_cast = _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def label_map_to_rgb_image_filter(*args, **kwargs):
    """Procedural interface for LabelMapToRGBImageFilter"""
    import itk
    instance = itk.LabelMapToRGBImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def label_map_to_rgb_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.LabelMapToRGBImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.LabelMapToRGBImageFilter.values()[0]
    else:
        filter_object = itk.LabelMapToRGBImageFilter

    label_map_to_rgb_image_filter.__doc__ = filter_object.__doc__
    label_map_to_rgb_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    label_map_to_rgb_image_filter.__doc__ += "Available Keyword Arguments:\n"
    label_map_to_rgb_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



