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
    from . import _itkShapeRelabelLabelMapFilterPython
else:
    import _itkShapeRelabelLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkShapeRelabelLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkShapeRelabelLabelMapFilterPython.SWIG_PyStaticMethod_New

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


import itkInPlaceLabelMapFilterPython
import ITKCommonBasePython
import pyBasePython
import itkLabelMapFilterPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkStatisticsLabelObjectPython
import itkAffineTransformPython
import itkVectorPython
import itkFixedArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkMatrixPython
import itkPointPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkArray2DPython
import itkArrayPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkOptimizerParametersPython
import itkMatrixOffsetTransformBasePython
import itkHistogramPython
import itkSamplePython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import ITKLabelMapBasePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImagePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkVectorImagePython

def itkShapeRelabelLabelMapFilterLM3_New():
  return itkShapeRelabelLabelMapFilterLM3.New()


def itkShapeRelabelLabelMapFilterLM2_New():
  return itkShapeRelabelLabelMapFilterLM2.New()

class itkShapeRelabelLabelMapFilterLM2(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    r"""Proxy of C++ itkShapeRelabelLabelMapFilterLM2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_Clone)
    SetReverseOrdering = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_SetReverseOrdering)
    GetReverseOrdering = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_GetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_SetAttribute)
    __swig_destroy__ = _itkShapeRelabelLabelMapFilterPython.delete_itkShapeRelabelLabelMapFilterLM2
    cast = _swig_new_static_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkShapeRelabelLabelMapFilterLM2

        Create a new object of the class itkShapeRelabelLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeRelabelLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapeRelabelLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapeRelabelLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapeRelabelLabelMapFilterLM2 in _itkShapeRelabelLabelMapFilterPython:
_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_swigregister(itkShapeRelabelLabelMapFilterLM2)
itkShapeRelabelLabelMapFilterLM2___New_orig__ = _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2___New_orig__
itkShapeRelabelLabelMapFilterLM2_cast = _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_cast

class itkShapeRelabelLabelMapFilterLM3(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    r"""Proxy of C++ itkShapeRelabelLabelMapFilterLM3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_Clone)
    SetReverseOrdering = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_SetReverseOrdering)
    GetReverseOrdering = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_GetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_SetAttribute)
    __swig_destroy__ = _itkShapeRelabelLabelMapFilterPython.delete_itkShapeRelabelLabelMapFilterLM3
    cast = _swig_new_static_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkShapeRelabelLabelMapFilterLM3

        Create a new object of the class itkShapeRelabelLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeRelabelLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShapeRelabelLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShapeRelabelLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapeRelabelLabelMapFilterLM3 in _itkShapeRelabelLabelMapFilterPython:
_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_swigregister(itkShapeRelabelLabelMapFilterLM3)
itkShapeRelabelLabelMapFilterLM3___New_orig__ = _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3___New_orig__
itkShapeRelabelLabelMapFilterLM3_cast = _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def shape_relabel_label_map_filter(*args, **kwargs):
    """Procedural interface for ShapeRelabelLabelMapFilter"""
    import itk
    instance = itk.ShapeRelabelLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def shape_relabel_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ShapeRelabelLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.ShapeRelabelLabelMapFilter.values()[0]
    else:
        filter_object = itk.ShapeRelabelLabelMapFilter

    shape_relabel_label_map_filter.__doc__ = filter_object.__doc__
    shape_relabel_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    shape_relabel_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    shape_relabel_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



