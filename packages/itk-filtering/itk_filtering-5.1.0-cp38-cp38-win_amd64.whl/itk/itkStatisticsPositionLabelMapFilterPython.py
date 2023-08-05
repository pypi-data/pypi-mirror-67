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
    from . import _itkStatisticsPositionLabelMapFilterPython
else:
    import _itkStatisticsPositionLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkStatisticsPositionLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkStatisticsPositionLabelMapFilterPython.SWIG_PyStaticMethod_New

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


import itkStatisticsLabelObjectPython
import itkAffineTransformPython
import itkVectorPython
import itkFixedArrayPython
import pyBasePython
import vnl_vector_refPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkCovariantVectorPython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkArrayPython
import itkDiffusionTensor3DPython
import ITKCommonBasePython
import itkOptimizerParametersPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkMatrixOffsetTransformBasePython
import itkHistogramPython
import itkSamplePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkShapeLabelObjectPython
import itkImageRegionPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkShapePositionLabelMapFilterPython
import itkInPlaceLabelMapFilterPython
import itkLabelMapFilterPython
import ITKLabelMapBasePython
import itkImagePython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageSourcePython
import itkVectorImagePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkStatisticsPositionLabelMapFilterLM3_New():
  return itkStatisticsPositionLabelMapFilterLM3.New()


def itkStatisticsPositionLabelMapFilterLM2_New():
  return itkStatisticsPositionLabelMapFilterLM2.New()

class itkStatisticsPositionLabelMapFilterLM2(itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2):
    r"""Proxy of C++ itkStatisticsPositionLabelMapFilterLM2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2_Clone)
    __swig_destroy__ = _itkStatisticsPositionLabelMapFilterPython.delete_itkStatisticsPositionLabelMapFilterLM2
    cast = _swig_new_static_method(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsPositionLabelMapFilterLM2

        Create a new object of the class itkStatisticsPositionLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsPositionLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkStatisticsPositionLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkStatisticsPositionLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStatisticsPositionLabelMapFilterLM2 in _itkStatisticsPositionLabelMapFilterPython:
_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2_swigregister(itkStatisticsPositionLabelMapFilterLM2)
itkStatisticsPositionLabelMapFilterLM2___New_orig__ = _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2___New_orig__
itkStatisticsPositionLabelMapFilterLM2_cast = _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2_cast

class itkStatisticsPositionLabelMapFilterLM3(itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3):
    r"""Proxy of C++ itkStatisticsPositionLabelMapFilterLM3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3_Clone)
    __swig_destroy__ = _itkStatisticsPositionLabelMapFilterPython.delete_itkStatisticsPositionLabelMapFilterLM3
    cast = _swig_new_static_method(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsPositionLabelMapFilterLM3

        Create a new object of the class itkStatisticsPositionLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsPositionLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkStatisticsPositionLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkStatisticsPositionLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStatisticsPositionLabelMapFilterLM3 in _itkStatisticsPositionLabelMapFilterPython:
_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3_swigregister(itkStatisticsPositionLabelMapFilterLM3)
itkStatisticsPositionLabelMapFilterLM3___New_orig__ = _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3___New_orig__
itkStatisticsPositionLabelMapFilterLM3_cast = _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def statistics_position_label_map_filter(*args, **kwargs):
    """Procedural interface for StatisticsPositionLabelMapFilter"""
    import itk
    instance = itk.StatisticsPositionLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def statistics_position_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.StatisticsPositionLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.StatisticsPositionLabelMapFilter.values()[0]
    else:
        filter_object = itk.StatisticsPositionLabelMapFilter

    statistics_position_label_map_filter.__doc__ = filter_object.__doc__
    statistics_position_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    statistics_position_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    statistics_position_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



