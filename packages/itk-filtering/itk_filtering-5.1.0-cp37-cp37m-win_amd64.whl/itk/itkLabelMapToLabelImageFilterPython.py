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
    from . import _itkLabelMapToLabelImageFilterPython
else:
    import _itkLabelMapToLabelImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLabelMapToLabelImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLabelMapToLabelImageFilterPython.SWIG_PyStaticMethod_New

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
import itkStatisticsLabelObjectPython
import itkShapeLabelObjectPython
import itkPointPython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkArray2DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkTransformBasePython
import itkHistogramPython
import itkSamplePython
import itkLabelMapFilterPython
import ITKLabelMapBasePython
import itkImagePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkVectorImagePython

def itkLabelMapToLabelImageFilterLM3IUS3_New():
  return itkLabelMapToLabelImageFilterLM3IUS3.New()


def itkLabelMapToLabelImageFilterLM2IUS2_New():
  return itkLabelMapToLabelImageFilterLM2IUS2.New()


def itkLabelMapToLabelImageFilterLM3IUC3_New():
  return itkLabelMapToLabelImageFilterLM3IUC3.New()


def itkLabelMapToLabelImageFilterLM2IUC2_New():
  return itkLabelMapToLabelImageFilterLM2IUC2.New()

class itkLabelMapToLabelImageFilterLM2IUC2(itkLabelMapFilterPython.itkLabelMapFilterLM2IUC2):
    r"""Proxy of C++ itkLabelMapToLabelImageFilterLM2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2_Clone)
    SameDimensionCheck = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2_SameDimensionCheck
    
    __swig_destroy__ = _itkLabelMapToLabelImageFilterPython.delete_itkLabelMapToLabelImageFilterLM2IUC2
    cast = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToLabelImageFilterLM2IUC2

        Create a new object of the class itkLabelMapToLabelImageFilterLM2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToLabelImageFilterLM2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapToLabelImageFilterLM2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapToLabelImageFilterLM2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToLabelImageFilterLM2IUC2 in _itkLabelMapToLabelImageFilterPython:
_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2_swigregister(itkLabelMapToLabelImageFilterLM2IUC2)
itkLabelMapToLabelImageFilterLM2IUC2___New_orig__ = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2___New_orig__
itkLabelMapToLabelImageFilterLM2IUC2_cast = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2_cast

class itkLabelMapToLabelImageFilterLM2IUS2(itkLabelMapFilterPython.itkLabelMapFilterLM2IUS2):
    r"""Proxy of C++ itkLabelMapToLabelImageFilterLM2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2_Clone)
    SameDimensionCheck = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2_SameDimensionCheck
    
    __swig_destroy__ = _itkLabelMapToLabelImageFilterPython.delete_itkLabelMapToLabelImageFilterLM2IUS2
    cast = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToLabelImageFilterLM2IUS2

        Create a new object of the class itkLabelMapToLabelImageFilterLM2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToLabelImageFilterLM2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapToLabelImageFilterLM2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapToLabelImageFilterLM2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToLabelImageFilterLM2IUS2 in _itkLabelMapToLabelImageFilterPython:
_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2_swigregister(itkLabelMapToLabelImageFilterLM2IUS2)
itkLabelMapToLabelImageFilterLM2IUS2___New_orig__ = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2___New_orig__
itkLabelMapToLabelImageFilterLM2IUS2_cast = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2_cast

class itkLabelMapToLabelImageFilterLM3IUC3(itkLabelMapFilterPython.itkLabelMapFilterLM3IUC3):
    r"""Proxy of C++ itkLabelMapToLabelImageFilterLM3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3_Clone)
    SameDimensionCheck = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3_SameDimensionCheck
    
    __swig_destroy__ = _itkLabelMapToLabelImageFilterPython.delete_itkLabelMapToLabelImageFilterLM3IUC3
    cast = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToLabelImageFilterLM3IUC3

        Create a new object of the class itkLabelMapToLabelImageFilterLM3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToLabelImageFilterLM3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapToLabelImageFilterLM3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapToLabelImageFilterLM3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToLabelImageFilterLM3IUC3 in _itkLabelMapToLabelImageFilterPython:
_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3_swigregister(itkLabelMapToLabelImageFilterLM3IUC3)
itkLabelMapToLabelImageFilterLM3IUC3___New_orig__ = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3___New_orig__
itkLabelMapToLabelImageFilterLM3IUC3_cast = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3_cast

class itkLabelMapToLabelImageFilterLM3IUS3(itkLabelMapFilterPython.itkLabelMapFilterLM3IUS3):
    r"""Proxy of C++ itkLabelMapToLabelImageFilterLM3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3_Clone)
    SameDimensionCheck = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3_SameDimensionCheck
    
    __swig_destroy__ = _itkLabelMapToLabelImageFilterPython.delete_itkLabelMapToLabelImageFilterLM3IUS3
    cast = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToLabelImageFilterLM3IUS3

        Create a new object of the class itkLabelMapToLabelImageFilterLM3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToLabelImageFilterLM3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelMapToLabelImageFilterLM3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelMapToLabelImageFilterLM3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToLabelImageFilterLM3IUS3 in _itkLabelMapToLabelImageFilterPython:
_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3_swigregister(itkLabelMapToLabelImageFilterLM3IUS3)
itkLabelMapToLabelImageFilterLM3IUS3___New_orig__ = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3___New_orig__
itkLabelMapToLabelImageFilterLM3IUS3_cast = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def label_map_to_label_image_filter(*args, **kwargs):
    """Procedural interface for LabelMapToLabelImageFilter"""
    import itk
    instance = itk.LabelMapToLabelImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def label_map_to_label_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.LabelMapToLabelImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.LabelMapToLabelImageFilter.values()[0]
    else:
        filter_object = itk.LabelMapToLabelImageFilter

    label_map_to_label_image_filter.__doc__ = filter_object.__doc__
    label_map_to_label_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    label_map_to_label_image_filter.__doc__ += "Available Keyword Arguments:\n"
    label_map_to_label_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



