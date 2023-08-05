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
    from . import _itkRelabelLabelMapFilterPython
else:
    import _itkRelabelLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkRelabelLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkRelabelLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itkInPlaceLabelMapFilterPython
import ITKLabelMapBasePython
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
import itkImagePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkVectorImagePython
import itkLabelMapFilterPython

def itkRelabelLabelMapFilterLM3_New():
  return itkRelabelLabelMapFilterLM3.New()


def itkRelabelLabelMapFilterLM3_Superclass_New():
  return itkRelabelLabelMapFilterLM3_Superclass.New()


def itkRelabelLabelMapFilterLM2_New():
  return itkRelabelLabelMapFilterLM2.New()


def itkRelabelLabelMapFilterLM2_Superclass_New():
  return itkRelabelLabelMapFilterLM2_Superclass.New()

class itkRelabelLabelMapFilterLM2_Superclass(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    r"""Proxy of C++ itkRelabelLabelMapFilterLM2_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_Clone)
    SetReverseOrdering = _swig_new_instance_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_SetReverseOrdering)
    GetReverseOrdering = _swig_new_instance_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_GetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_ReverseOrderingOff)
    __swig_destroy__ = _itkRelabelLabelMapFilterPython.delete_itkRelabelLabelMapFilterLM2_Superclass
    cast = _swig_new_static_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkRelabelLabelMapFilterLM2_Superclass

        Create a new object of the class itkRelabelLabelMapFilterLM2_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRelabelLabelMapFilterLM2_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRelabelLabelMapFilterLM2_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRelabelLabelMapFilterLM2_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRelabelLabelMapFilterLM2_Superclass in _itkRelabelLabelMapFilterPython:
_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_swigregister(itkRelabelLabelMapFilterLM2_Superclass)
itkRelabelLabelMapFilterLM2_Superclass___New_orig__ = _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass___New_orig__
itkRelabelLabelMapFilterLM2_Superclass_cast = _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_cast

class itkRelabelLabelMapFilterLM3_Superclass(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    r"""Proxy of C++ itkRelabelLabelMapFilterLM3_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_Clone)
    SetReverseOrdering = _swig_new_instance_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_SetReverseOrdering)
    GetReverseOrdering = _swig_new_instance_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_GetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_ReverseOrderingOff)
    __swig_destroy__ = _itkRelabelLabelMapFilterPython.delete_itkRelabelLabelMapFilterLM3_Superclass
    cast = _swig_new_static_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkRelabelLabelMapFilterLM3_Superclass

        Create a new object of the class itkRelabelLabelMapFilterLM3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRelabelLabelMapFilterLM3_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRelabelLabelMapFilterLM3_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRelabelLabelMapFilterLM3_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRelabelLabelMapFilterLM3_Superclass in _itkRelabelLabelMapFilterPython:
_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_swigregister(itkRelabelLabelMapFilterLM3_Superclass)
itkRelabelLabelMapFilterLM3_Superclass___New_orig__ = _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass___New_orig__
itkRelabelLabelMapFilterLM3_Superclass_cast = _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_cast

class itkRelabelLabelMapFilterLM2(itkRelabelLabelMapFilterLM2_Superclass):
    r"""Proxy of C++ itkRelabelLabelMapFilterLM2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Clone)
    __swig_destroy__ = _itkRelabelLabelMapFilterPython.delete_itkRelabelLabelMapFilterLM2
    cast = _swig_new_static_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkRelabelLabelMapFilterLM2

        Create a new object of the class itkRelabelLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRelabelLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRelabelLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRelabelLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRelabelLabelMapFilterLM2 in _itkRelabelLabelMapFilterPython:
_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_swigregister(itkRelabelLabelMapFilterLM2)
itkRelabelLabelMapFilterLM2___New_orig__ = _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2___New_orig__
itkRelabelLabelMapFilterLM2_cast = _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_cast

class itkRelabelLabelMapFilterLM3(itkRelabelLabelMapFilterLM3_Superclass):
    r"""Proxy of C++ itkRelabelLabelMapFilterLM3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Clone)
    __swig_destroy__ = _itkRelabelLabelMapFilterPython.delete_itkRelabelLabelMapFilterLM3
    cast = _swig_new_static_method(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkRelabelLabelMapFilterLM3

        Create a new object of the class itkRelabelLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRelabelLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRelabelLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRelabelLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRelabelLabelMapFilterLM3 in _itkRelabelLabelMapFilterPython:
_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_swigregister(itkRelabelLabelMapFilterLM3)
itkRelabelLabelMapFilterLM3___New_orig__ = _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3___New_orig__
itkRelabelLabelMapFilterLM3_cast = _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def attribute_relabel_label_map_filter(*args, **kwargs):
    """Procedural interface for AttributeRelabelLabelMapFilter"""
    import itk
    instance = itk.AttributeRelabelLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def attribute_relabel_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.AttributeRelabelLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.AttributeRelabelLabelMapFilter.values()[0]
    else:
        filter_object = itk.AttributeRelabelLabelMapFilter

    attribute_relabel_label_map_filter.__doc__ = filter_object.__doc__
    attribute_relabel_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    attribute_relabel_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    attribute_relabel_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])
import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def relabel_label_map_filter(*args, **kwargs):
    """Procedural interface for RelabelLabelMapFilter"""
    import itk
    instance = itk.RelabelLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def relabel_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.RelabelLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.RelabelLabelMapFilter.values()[0]
    else:
        filter_object = itk.RelabelLabelMapFilter

    relabel_label_map_filter.__doc__ = filter_object.__doc__
    relabel_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    relabel_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    relabel_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



