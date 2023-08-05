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
    from . import _itkCollidingFrontsImageFilterPython
else:
    import _itkCollidingFrontsImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkCollidingFrontsImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkCollidingFrontsImageFilterPython.SWIG_PyStaticMethod_New

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
import ITKCommonBasePython
import pyBasePython
import itkVectorImagePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkVariableLengthVectorPython
import stdcomplexPython
import itkImagePython
import itkMatrixPython
import vnl_matrixPython
import vnl_vectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkSymmetricSecondRankTensorPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import ITKFastMarchingBasePython
import itkNodePairPython
import itkLevelSetNodePython
import itkFastMarchingStoppingCriterionBasePython

def itkCollidingFrontsImageFilterID3ID3_New():
  return itkCollidingFrontsImageFilterID3ID3.New()


def itkCollidingFrontsImageFilterID2ID2_New():
  return itkCollidingFrontsImageFilterID2ID2.New()


def itkCollidingFrontsImageFilterIF3IF3_New():
  return itkCollidingFrontsImageFilterIF3IF3.New()


def itkCollidingFrontsImageFilterIF2IF2_New():
  return itkCollidingFrontsImageFilterIF2IF2.New()

class itkCollidingFrontsImageFilterID2ID2(itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    r"""Proxy of C++ itkCollidingFrontsImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_Clone)
    SetSeedPoints1 = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_SetSeedPoints1)
    GetSeedPoints1 = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_GetSeedPoints1)
    SetSeedPoints2 = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_SetSeedPoints2)
    GetSeedPoints2 = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_GetSeedPoints2)
    SetNegativeEpsilon = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_SetNegativeEpsilon)
    GetNegativeEpsilon = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_GetNegativeEpsilon)
    SetApplyConnectivity = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_SetApplyConnectivity)
    GetApplyConnectivity = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_GetApplyConnectivity)
    ApplyConnectivityOn = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_ApplyConnectivityOn)
    ApplyConnectivityOff = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_ApplyConnectivityOff)
    SetStopOnTargets = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_SetStopOnTargets)
    GetStopOnTargets = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_GetStopOnTargets)
    StopOnTargetsOn = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_StopOnTargetsOn)
    StopOnTargetsOff = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_StopOnTargetsOff)
    InputHasNumericTraitsCheck = _itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkCollidingFrontsImageFilterPython.delete_itkCollidingFrontsImageFilterID2ID2
    cast = _swig_new_static_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkCollidingFrontsImageFilterID2ID2

        Create a new object of the class itkCollidingFrontsImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCollidingFrontsImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCollidingFrontsImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCollidingFrontsImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCollidingFrontsImageFilterID2ID2 in _itkCollidingFrontsImageFilterPython:
_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_swigregister(itkCollidingFrontsImageFilterID2ID2)
itkCollidingFrontsImageFilterID2ID2___New_orig__ = _itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2___New_orig__
itkCollidingFrontsImageFilterID2ID2_cast = _itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID2ID2_cast

class itkCollidingFrontsImageFilterID3ID3(itkImageToImageFilterAPython.itkImageToImageFilterID3ID3):
    r"""Proxy of C++ itkCollidingFrontsImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_Clone)
    SetSeedPoints1 = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_SetSeedPoints1)
    GetSeedPoints1 = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_GetSeedPoints1)
    SetSeedPoints2 = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_SetSeedPoints2)
    GetSeedPoints2 = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_GetSeedPoints2)
    SetNegativeEpsilon = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_SetNegativeEpsilon)
    GetNegativeEpsilon = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_GetNegativeEpsilon)
    SetApplyConnectivity = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_SetApplyConnectivity)
    GetApplyConnectivity = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_GetApplyConnectivity)
    ApplyConnectivityOn = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_ApplyConnectivityOn)
    ApplyConnectivityOff = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_ApplyConnectivityOff)
    SetStopOnTargets = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_SetStopOnTargets)
    GetStopOnTargets = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_GetStopOnTargets)
    StopOnTargetsOn = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_StopOnTargetsOn)
    StopOnTargetsOff = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_StopOnTargetsOff)
    InputHasNumericTraitsCheck = _itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkCollidingFrontsImageFilterPython.delete_itkCollidingFrontsImageFilterID3ID3
    cast = _swig_new_static_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkCollidingFrontsImageFilterID3ID3

        Create a new object of the class itkCollidingFrontsImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCollidingFrontsImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCollidingFrontsImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCollidingFrontsImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCollidingFrontsImageFilterID3ID3 in _itkCollidingFrontsImageFilterPython:
_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_swigregister(itkCollidingFrontsImageFilterID3ID3)
itkCollidingFrontsImageFilterID3ID3___New_orig__ = _itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3___New_orig__
itkCollidingFrontsImageFilterID3ID3_cast = _itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterID3ID3_cast

class itkCollidingFrontsImageFilterIF2IF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    r"""Proxy of C++ itkCollidingFrontsImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_Clone)
    SetSeedPoints1 = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_SetSeedPoints1)
    GetSeedPoints1 = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_GetSeedPoints1)
    SetSeedPoints2 = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_SetSeedPoints2)
    GetSeedPoints2 = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_GetSeedPoints2)
    SetNegativeEpsilon = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_SetNegativeEpsilon)
    GetNegativeEpsilon = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_GetNegativeEpsilon)
    SetApplyConnectivity = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_SetApplyConnectivity)
    GetApplyConnectivity = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_GetApplyConnectivity)
    ApplyConnectivityOn = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_ApplyConnectivityOn)
    ApplyConnectivityOff = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_ApplyConnectivityOff)
    SetStopOnTargets = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_SetStopOnTargets)
    GetStopOnTargets = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_GetStopOnTargets)
    StopOnTargetsOn = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_StopOnTargetsOn)
    StopOnTargetsOff = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_StopOnTargetsOff)
    InputHasNumericTraitsCheck = _itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkCollidingFrontsImageFilterPython.delete_itkCollidingFrontsImageFilterIF2IF2
    cast = _swig_new_static_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkCollidingFrontsImageFilterIF2IF2

        Create a new object of the class itkCollidingFrontsImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCollidingFrontsImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCollidingFrontsImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCollidingFrontsImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCollidingFrontsImageFilterIF2IF2 in _itkCollidingFrontsImageFilterPython:
_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_swigregister(itkCollidingFrontsImageFilterIF2IF2)
itkCollidingFrontsImageFilterIF2IF2___New_orig__ = _itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2___New_orig__
itkCollidingFrontsImageFilterIF2IF2_cast = _itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF2IF2_cast

class itkCollidingFrontsImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    r"""Proxy of C++ itkCollidingFrontsImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_Clone)
    SetSeedPoints1 = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_SetSeedPoints1)
    GetSeedPoints1 = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_GetSeedPoints1)
    SetSeedPoints2 = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_SetSeedPoints2)
    GetSeedPoints2 = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_GetSeedPoints2)
    SetNegativeEpsilon = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_SetNegativeEpsilon)
    GetNegativeEpsilon = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_GetNegativeEpsilon)
    SetApplyConnectivity = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_SetApplyConnectivity)
    GetApplyConnectivity = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_GetApplyConnectivity)
    ApplyConnectivityOn = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_ApplyConnectivityOn)
    ApplyConnectivityOff = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_ApplyConnectivityOff)
    SetStopOnTargets = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_SetStopOnTargets)
    GetStopOnTargets = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_GetStopOnTargets)
    StopOnTargetsOn = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_StopOnTargetsOn)
    StopOnTargetsOff = _swig_new_instance_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_StopOnTargetsOff)
    InputHasNumericTraitsCheck = _itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkCollidingFrontsImageFilterPython.delete_itkCollidingFrontsImageFilterIF3IF3
    cast = _swig_new_static_method(_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkCollidingFrontsImageFilterIF3IF3

        Create a new object of the class itkCollidingFrontsImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCollidingFrontsImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCollidingFrontsImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCollidingFrontsImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCollidingFrontsImageFilterIF3IF3 in _itkCollidingFrontsImageFilterPython:
_itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_swigregister(itkCollidingFrontsImageFilterIF3IF3)
itkCollidingFrontsImageFilterIF3IF3___New_orig__ = _itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3___New_orig__
itkCollidingFrontsImageFilterIF3IF3_cast = _itkCollidingFrontsImageFilterPython.itkCollidingFrontsImageFilterIF3IF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def colliding_fronts_image_filter(*args, **kwargs):
    """Procedural interface for CollidingFrontsImageFilter"""
    import itk
    instance = itk.CollidingFrontsImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def colliding_fronts_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.CollidingFrontsImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.CollidingFrontsImageFilter.values()[0]
    else:
        filter_object = itk.CollidingFrontsImageFilter

    colliding_fronts_image_filter.__doc__ = filter_object.__doc__
    colliding_fronts_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    colliding_fronts_image_filter.__doc__ += "Available Keyword Arguments:\n"
    colliding_fronts_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



