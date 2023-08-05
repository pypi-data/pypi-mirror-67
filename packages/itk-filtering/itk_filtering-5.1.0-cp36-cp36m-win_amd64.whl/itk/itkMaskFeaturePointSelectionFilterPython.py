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
    from . import _itkMaskFeaturePointSelectionFilterPython
else:
    import _itkMaskFeaturePointSelectionFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMaskFeaturePointSelectionFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMaskFeaturePointSelectionFilterPython.SWIG_PyStaticMethod_New

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


import itkPointSetPython
import ITKCommonBasePython
import pyBasePython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkVectorPython
import itkVectorContainerPython
import itkContinuousIndexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkImagePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython

def itkMaskFeaturePointSelectionFilterID3_New():
  return itkMaskFeaturePointSelectionFilterID3.New()


def itkMaskFeaturePointSelectionFilterID3_Superclass_New():
  return itkMaskFeaturePointSelectionFilterID3_Superclass.New()


def itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_New():
  return itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass.New()


def itkMaskFeaturePointSelectionFilterIF3_New():
  return itkMaskFeaturePointSelectionFilterIF3.New()


def itkMaskFeaturePointSelectionFilterIF3_Superclass_New():
  return itkMaskFeaturePointSelectionFilterIF3_Superclass.New()


def itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_New():
  return itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.New()

class itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass(ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_Clone)
    GetOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_GetOutput)
    SetOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_SetOutput)
    GraftOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_GraftOutput)
    GraftNthOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_GraftNthOutput)
    __swig_destroy__ = _itkMaskFeaturePointSelectionFilterPython.delete_itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass
    cast = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass

        Create a new object of the class itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass in _itkMaskFeaturePointSelectionFilterPython:
_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_swigregister(itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass)
itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass___New_orig__ = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass___New_orig__
itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_cast = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_cast

class itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass(ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_Clone)
    GetOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_GetOutput)
    SetOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_SetOutput)
    GraftOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_GraftOutput)
    GraftNthOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_GraftNthOutput)
    __swig_destroy__ = _itkMaskFeaturePointSelectionFilterPython.delete_itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass
    cast = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass

        Create a new object of the class itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass in _itkMaskFeaturePointSelectionFilterPython:
_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_swigregister(itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass)
itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass___New_orig__ = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass___New_orig__
itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_cast = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_cast

class itkMaskFeaturePointSelectionFilterID3_Superclass(itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass):
    r"""Proxy of C++ itkMaskFeaturePointSelectionFilterID3_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_SetInput)
    GetInput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_GetInput)
    GetOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_GetOutput)
    GenerateOutputInformation = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_GenerateOutputInformation)
    __swig_destroy__ = _itkMaskFeaturePointSelectionFilterPython.delete_itkMaskFeaturePointSelectionFilterID3_Superclass
    cast = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkMaskFeaturePointSelectionFilterID3_Superclass

        Create a new object of the class itkMaskFeaturePointSelectionFilterID3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaskFeaturePointSelectionFilterID3_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaskFeaturePointSelectionFilterID3_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaskFeaturePointSelectionFilterID3_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaskFeaturePointSelectionFilterID3_Superclass in _itkMaskFeaturePointSelectionFilterPython:
_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_swigregister(itkMaskFeaturePointSelectionFilterID3_Superclass)
itkMaskFeaturePointSelectionFilterID3_Superclass_cast = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_cast

class itkMaskFeaturePointSelectionFilterIF3_Superclass(itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass):
    r"""Proxy of C++ itkMaskFeaturePointSelectionFilterIF3_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_SetInput)
    GetInput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_GetInput)
    GetOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_GetOutput)
    GenerateOutputInformation = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_GenerateOutputInformation)
    __swig_destroy__ = _itkMaskFeaturePointSelectionFilterPython.delete_itkMaskFeaturePointSelectionFilterIF3_Superclass
    cast = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkMaskFeaturePointSelectionFilterIF3_Superclass

        Create a new object of the class itkMaskFeaturePointSelectionFilterIF3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaskFeaturePointSelectionFilterIF3_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaskFeaturePointSelectionFilterIF3_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaskFeaturePointSelectionFilterIF3_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaskFeaturePointSelectionFilterIF3_Superclass in _itkMaskFeaturePointSelectionFilterPython:
_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_swigregister(itkMaskFeaturePointSelectionFilterIF3_Superclass)
itkMaskFeaturePointSelectionFilterIF3_Superclass_cast = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_cast

class itkMaskFeaturePointSelectionFilterID3(itkMaskFeaturePointSelectionFilterID3_Superclass):
    r"""Proxy of C++ itkMaskFeaturePointSelectionFilterID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3___New_orig__)
    Clone = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Clone)
    VERTEX_CONNECTIVITY = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_VERTEX_CONNECTIVITY
    
    EDGE_CONNECTIVITY = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_EDGE_CONNECTIVITY
    
    FACE_CONNECTIVITY = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_FACE_CONNECTIVITY
    
    SetNonConnectivity = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_SetNonConnectivity)
    GetNonConnectivity = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_GetNonConnectivity)
    SetMaskImage = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_SetMaskImage)
    GetMaskImage = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_GetMaskImage)
    SetBlockRadius = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_SetBlockRadius)
    GetBlockRadius = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_GetBlockRadius)
    SetComputeStructureTensors = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_SetComputeStructureTensors)
    GetComputeStructureTensors = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_GetComputeStructureTensors)
    ComputeStructureTensorsOn = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_ComputeStructureTensorsOn)
    ComputeStructureTensorsOff = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_ComputeStructureTensorsOff)
    SetSelectFraction = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_SetSelectFraction)
    GetSelectFraction = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_GetSelectFraction)
    ImageDimensionShouldBe3 = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_ImageDimensionShouldBe3
    
    MaskDimensionShouldBe3 = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_MaskDimensionShouldBe3
    
    PointDimensionShouldBe3 = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_PointDimensionShouldBe3
    
    __swig_destroy__ = _itkMaskFeaturePointSelectionFilterPython.delete_itkMaskFeaturePointSelectionFilterID3
    cast = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_cast)

    def New(*args, **kargs):
        """New() -> itkMaskFeaturePointSelectionFilterID3

        Create a new object of the class itkMaskFeaturePointSelectionFilterID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaskFeaturePointSelectionFilterID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaskFeaturePointSelectionFilterID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaskFeaturePointSelectionFilterID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaskFeaturePointSelectionFilterID3 in _itkMaskFeaturePointSelectionFilterPython:
_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_swigregister(itkMaskFeaturePointSelectionFilterID3)
itkMaskFeaturePointSelectionFilterID3___New_orig__ = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3___New_orig__
itkMaskFeaturePointSelectionFilterID3_cast = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_cast

class itkMaskFeaturePointSelectionFilterIF3(itkMaskFeaturePointSelectionFilterIF3_Superclass):
    r"""Proxy of C++ itkMaskFeaturePointSelectionFilterIF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3___New_orig__)
    Clone = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Clone)
    VERTEX_CONNECTIVITY = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_VERTEX_CONNECTIVITY
    
    EDGE_CONNECTIVITY = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_EDGE_CONNECTIVITY
    
    FACE_CONNECTIVITY = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_FACE_CONNECTIVITY
    
    SetNonConnectivity = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetNonConnectivity)
    GetNonConnectivity = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetNonConnectivity)
    SetMaskImage = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetMaskImage)
    GetMaskImage = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetMaskImage)
    SetBlockRadius = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetBlockRadius)
    GetBlockRadius = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetBlockRadius)
    SetComputeStructureTensors = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetComputeStructureTensors)
    GetComputeStructureTensors = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetComputeStructureTensors)
    ComputeStructureTensorsOn = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_ComputeStructureTensorsOn)
    ComputeStructureTensorsOff = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_ComputeStructureTensorsOff)
    SetSelectFraction = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetSelectFraction)
    GetSelectFraction = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetSelectFraction)
    ImageDimensionShouldBe3 = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_ImageDimensionShouldBe3
    
    MaskDimensionShouldBe3 = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_MaskDimensionShouldBe3
    
    PointDimensionShouldBe3 = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_PointDimensionShouldBe3
    
    __swig_destroy__ = _itkMaskFeaturePointSelectionFilterPython.delete_itkMaskFeaturePointSelectionFilterIF3
    cast = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_cast)

    def New(*args, **kargs):
        """New() -> itkMaskFeaturePointSelectionFilterIF3

        Create a new object of the class itkMaskFeaturePointSelectionFilterIF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaskFeaturePointSelectionFilterIF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaskFeaturePointSelectionFilterIF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaskFeaturePointSelectionFilterIF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaskFeaturePointSelectionFilterIF3 in _itkMaskFeaturePointSelectionFilterPython:
_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_swigregister(itkMaskFeaturePointSelectionFilterIF3)
itkMaskFeaturePointSelectionFilterIF3___New_orig__ = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3___New_orig__
itkMaskFeaturePointSelectionFilterIF3_cast = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def mask_feature_point_selection_filter(*args, **kwargs):
    """Procedural interface for MaskFeaturePointSelectionFilter"""
    import itk
    instance = itk.MaskFeaturePointSelectionFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def mask_feature_point_selection_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.MaskFeaturePointSelectionFilter, itkTemplate.itkTemplate):
        filter_object = itk.MaskFeaturePointSelectionFilter.values()[0]
    else:
        filter_object = itk.MaskFeaturePointSelectionFilter

    mask_feature_point_selection_filter.__doc__ = filter_object.__doc__
    mask_feature_point_selection_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    mask_feature_point_selection_filter.__doc__ += "Available Keyword Arguments:\n"
    mask_feature_point_selection_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])
import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def mesh_source(*args, **kwargs):
    """Procedural interface for MeshSource"""
    import itk
    instance = itk.MeshSource.New(*args, **kwargs)
    return instance.__internal_call__()

def mesh_source_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.MeshSource, itkTemplate.itkTemplate):
        filter_object = itk.MeshSource.values()[0]
    else:
        filter_object = itk.MeshSource

    mesh_source.__doc__ = filter_object.__doc__
    mesh_source.__doc__ += "\n Args are Input(s) to the filter.\n"
    mesh_source.__doc__ += "Available Keyword Arguments:\n"
    mesh_source.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])
import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def image_to_mesh_filter(*args, **kwargs):
    """Procedural interface for ImageToMeshFilter"""
    import itk
    instance = itk.ImageToMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def image_to_mesh_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ImageToMeshFilter, itkTemplate.itkTemplate):
        filter_object = itk.ImageToMeshFilter.values()[0]
    else:
        filter_object = itk.ImageToMeshFilter

    image_to_mesh_filter.__doc__ = filter_object.__doc__
    image_to_mesh_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    image_to_mesh_filter.__doc__ += "Available Keyword Arguments:\n"
    image_to_mesh_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



