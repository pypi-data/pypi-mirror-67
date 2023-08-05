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
    from . import _itkObjectByObjectLabelMapFilterPython
else:
    import _itkObjectByObjectLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkObjectByObjectLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkObjectByObjectLabelMapFilterPython.SWIG_PyStaticMethod_New

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


import itkSizePython
import pyBasePython
import itkImageToImageFilterAPython
import ITKCommonBasePython
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
import itkLabelMapFilterPython
import itkStatisticsLabelObjectPython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkArray2DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkDiffusionTensor3DPython
import itkTransformBasePython
import itkHistogramPython
import itkSamplePython
import ITKLabelMapBasePython

def itkObjectByObjectLabelMapFilterLM3_New():
  return itkObjectByObjectLabelMapFilterLM3.New()


def itkObjectByObjectLabelMapFilterLM2_New():
  return itkObjectByObjectLabelMapFilterLM2.New()

class itkObjectByObjectLabelMapFilterLM2(itkLabelMapFilterPython.itkLabelMapFilterLM2LM2):
    r"""Proxy of C++ itkObjectByObjectLabelMapFilterLM2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_Clone)
    SetFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetFilter)
    GetFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetFilter)
    SetInputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetInputFilter)
    GetModifiableInputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetModifiableInputFilter)
    GetInputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetInputFilter)
    SetOutputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetOutputFilter)
    GetModifiableOutputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetModifiableOutputFilter)
    GetOutputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetOutputFilter)
    SetKeepLabels = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetKeepLabels)
    GetKeepLabels = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetKeepLabels)
    KeepLabelsOn = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_KeepLabelsOn)
    KeepLabelsOff = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_KeepLabelsOff)
    SetPadSize = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetPadSize)
    GetPadSize = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetPadSize)
    SetConstrainPaddingToImage = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetConstrainPaddingToImage)
    GetConstrainPaddingToImage = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetConstrainPaddingToImage)
    ConstrainPaddingToImageOn = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_ConstrainPaddingToImageOn)
    ConstrainPaddingToImageOff = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_ConstrainPaddingToImageOff)
    SetBinaryInternalOutput = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetBinaryInternalOutput)
    GetBinaryInternalOutput = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetBinaryInternalOutput)
    BinaryInternalOutputOn = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_BinaryInternalOutputOn)
    BinaryInternalOutputOff = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_BinaryInternalOutputOff)
    SetInternalForegroundValue = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetInternalForegroundValue)
    GetInternalForegroundValue = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetInternalForegroundValue)
    GetLabel = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetLabel)
    __swig_destroy__ = _itkObjectByObjectLabelMapFilterPython.delete_itkObjectByObjectLabelMapFilterLM2
    cast = _swig_new_static_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkObjectByObjectLabelMapFilterLM2

        Create a new object of the class itkObjectByObjectLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkObjectByObjectLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkObjectByObjectLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkObjectByObjectLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkObjectByObjectLabelMapFilterLM2 in _itkObjectByObjectLabelMapFilterPython:
_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_swigregister(itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2___New_orig__ = _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2___New_orig__
itkObjectByObjectLabelMapFilterLM2_cast = _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_cast

class itkObjectByObjectLabelMapFilterLM3(itkLabelMapFilterPython.itkLabelMapFilterLM3LM3):
    r"""Proxy of C++ itkObjectByObjectLabelMapFilterLM3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_Clone)
    SetFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetFilter)
    GetFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetFilter)
    SetInputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetInputFilter)
    GetModifiableInputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetModifiableInputFilter)
    GetInputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetInputFilter)
    SetOutputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetOutputFilter)
    GetModifiableOutputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetModifiableOutputFilter)
    GetOutputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetOutputFilter)
    SetKeepLabels = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetKeepLabels)
    GetKeepLabels = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetKeepLabels)
    KeepLabelsOn = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_KeepLabelsOn)
    KeepLabelsOff = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_KeepLabelsOff)
    SetPadSize = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetPadSize)
    GetPadSize = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetPadSize)
    SetConstrainPaddingToImage = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetConstrainPaddingToImage)
    GetConstrainPaddingToImage = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetConstrainPaddingToImage)
    ConstrainPaddingToImageOn = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_ConstrainPaddingToImageOn)
    ConstrainPaddingToImageOff = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_ConstrainPaddingToImageOff)
    SetBinaryInternalOutput = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetBinaryInternalOutput)
    GetBinaryInternalOutput = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetBinaryInternalOutput)
    BinaryInternalOutputOn = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_BinaryInternalOutputOn)
    BinaryInternalOutputOff = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_BinaryInternalOutputOff)
    SetInternalForegroundValue = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetInternalForegroundValue)
    GetInternalForegroundValue = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetInternalForegroundValue)
    GetLabel = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetLabel)
    __swig_destroy__ = _itkObjectByObjectLabelMapFilterPython.delete_itkObjectByObjectLabelMapFilterLM3
    cast = _swig_new_static_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkObjectByObjectLabelMapFilterLM3

        Create a new object of the class itkObjectByObjectLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkObjectByObjectLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkObjectByObjectLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkObjectByObjectLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkObjectByObjectLabelMapFilterLM3 in _itkObjectByObjectLabelMapFilterPython:
_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_swigregister(itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3___New_orig__ = _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3___New_orig__
itkObjectByObjectLabelMapFilterLM3_cast = _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def object_by_object_label_map_filter(*args, **kwargs):
    """Procedural interface for ObjectByObjectLabelMapFilter"""
    import itk
    instance = itk.ObjectByObjectLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def object_by_object_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ObjectByObjectLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.ObjectByObjectLabelMapFilter.values()[0]
    else:
        filter_object = itk.ObjectByObjectLabelMapFilter

    object_by_object_label_map_filter.__doc__ = filter_object.__doc__
    object_by_object_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    object_by_object_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    object_by_object_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



