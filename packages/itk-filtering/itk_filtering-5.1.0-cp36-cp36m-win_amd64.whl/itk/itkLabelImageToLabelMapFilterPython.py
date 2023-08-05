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
    from . import _itkLabelImageToLabelMapFilterPython
else:
    import _itkLabelImageToLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLabelImageToLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLabelImageToLabelMapFilterPython.SWIG_PyStaticMethod_New

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


import ITKLabelMapBasePython
import itkImageSourcePython
import itkImageSourceCommonPython
import ITKCommonBasePython
import pyBasePython
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

def itkLabelImageToLabelMapFilterIUS3LM3_New():
  return itkLabelImageToLabelMapFilterIUS3LM3.New()


def itkLabelImageToLabelMapFilterIUS2LM2_New():
  return itkLabelImageToLabelMapFilterIUS2LM2.New()


def itkLabelImageToLabelMapFilterIUC3LM3_New():
  return itkLabelImageToLabelMapFilterIUC3LM3.New()


def itkLabelImageToLabelMapFilterIUC2LM2_New():
  return itkLabelImageToLabelMapFilterIUC2LM2.New()


def itkScanlineFilterCommonIUS3LM3_New():
  return itkScanlineFilterCommonIUS3LM3.New()


def itkScanlineFilterCommonIUS2LM2_New():
  return itkScanlineFilterCommonIUS2LM2.New()


def itkScanlineFilterCommonIUC3LM3_New():
  return itkScanlineFilterCommonIUC3LM3.New()


def itkScanlineFilterCommonIUC2LM2_New():
  return itkScanlineFilterCommonIUC2LM2.New()

class itkLabelImageToLabelMapFilterIUC2LM2(ITKLabelMapBasePython.itkImageToImageFilterIUC2LM2):
    r"""Proxy of C++ itkLabelImageToLabelMapFilterIUC2LM2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_Clone)
    SetBackgroundValue = _swig_new_instance_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_GetBackgroundValue)
    SameDimensionCheck = _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_SameDimensionCheck
    
    __swig_destroy__ = _itkLabelImageToLabelMapFilterPython.delete_itkLabelImageToLabelMapFilterIUC2LM2
    cast = _swig_new_static_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelImageToLabelMapFilterIUC2LM2

        Create a new object of the class itkLabelImageToLabelMapFilterIUC2LM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageToLabelMapFilterIUC2LM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageToLabelMapFilterIUC2LM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageToLabelMapFilterIUC2LM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelImageToLabelMapFilterIUC2LM2 in _itkLabelImageToLabelMapFilterPython:
_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_swigregister(itkLabelImageToLabelMapFilterIUC2LM2)
itkLabelImageToLabelMapFilterIUC2LM2___New_orig__ = _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2___New_orig__
itkLabelImageToLabelMapFilterIUC2LM2_cast = _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC2LM2_cast

class itkLabelImageToLabelMapFilterIUC3LM3(ITKLabelMapBasePython.itkImageToImageFilterIUC3LM3):
    r"""Proxy of C++ itkLabelImageToLabelMapFilterIUC3LM3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_Clone)
    SetBackgroundValue = _swig_new_instance_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_GetBackgroundValue)
    SameDimensionCheck = _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_SameDimensionCheck
    
    __swig_destroy__ = _itkLabelImageToLabelMapFilterPython.delete_itkLabelImageToLabelMapFilterIUC3LM3
    cast = _swig_new_static_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelImageToLabelMapFilterIUC3LM3

        Create a new object of the class itkLabelImageToLabelMapFilterIUC3LM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageToLabelMapFilterIUC3LM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageToLabelMapFilterIUC3LM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageToLabelMapFilterIUC3LM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelImageToLabelMapFilterIUC3LM3 in _itkLabelImageToLabelMapFilterPython:
_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_swigregister(itkLabelImageToLabelMapFilterIUC3LM3)
itkLabelImageToLabelMapFilterIUC3LM3___New_orig__ = _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3___New_orig__
itkLabelImageToLabelMapFilterIUC3LM3_cast = _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUC3LM3_cast

class itkLabelImageToLabelMapFilterIUS2LM2(ITKLabelMapBasePython.itkImageToImageFilterIUS2LM2):
    r"""Proxy of C++ itkLabelImageToLabelMapFilterIUS2LM2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS2LM2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS2LM2_Clone)
    SetBackgroundValue = _swig_new_instance_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS2LM2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS2LM2_GetBackgroundValue)
    SameDimensionCheck = _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS2LM2_SameDimensionCheck
    
    __swig_destroy__ = _itkLabelImageToLabelMapFilterPython.delete_itkLabelImageToLabelMapFilterIUS2LM2
    cast = _swig_new_static_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS2LM2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelImageToLabelMapFilterIUS2LM2

        Create a new object of the class itkLabelImageToLabelMapFilterIUS2LM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageToLabelMapFilterIUS2LM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageToLabelMapFilterIUS2LM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageToLabelMapFilterIUS2LM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelImageToLabelMapFilterIUS2LM2 in _itkLabelImageToLabelMapFilterPython:
_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS2LM2_swigregister(itkLabelImageToLabelMapFilterIUS2LM2)
itkLabelImageToLabelMapFilterIUS2LM2___New_orig__ = _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS2LM2___New_orig__
itkLabelImageToLabelMapFilterIUS2LM2_cast = _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS2LM2_cast

class itkLabelImageToLabelMapFilterIUS3LM3(ITKLabelMapBasePython.itkImageToImageFilterIUS3LM3):
    r"""Proxy of C++ itkLabelImageToLabelMapFilterIUS3LM3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS3LM3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS3LM3_Clone)
    SetBackgroundValue = _swig_new_instance_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS3LM3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS3LM3_GetBackgroundValue)
    SameDimensionCheck = _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS3LM3_SameDimensionCheck
    
    __swig_destroy__ = _itkLabelImageToLabelMapFilterPython.delete_itkLabelImageToLabelMapFilterIUS3LM3
    cast = _swig_new_static_method(_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS3LM3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelImageToLabelMapFilterIUS3LM3

        Create a new object of the class itkLabelImageToLabelMapFilterIUS3LM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageToLabelMapFilterIUS3LM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageToLabelMapFilterIUS3LM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageToLabelMapFilterIUS3LM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelImageToLabelMapFilterIUS3LM3 in _itkLabelImageToLabelMapFilterPython:
_itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS3LM3_swigregister(itkLabelImageToLabelMapFilterIUS3LM3)
itkLabelImageToLabelMapFilterIUS3LM3___New_orig__ = _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS3LM3___New_orig__
itkLabelImageToLabelMapFilterIUS3LM3_cast = _itkLabelImageToLabelMapFilterPython.itkLabelImageToLabelMapFilterIUS3LM3_cast

class itkScanlineFilterCommonIUC2LM2(object):
    r"""Proxy of C++ itkScanlineFilterCommonIUC2LM2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUC2LM2___New_orig__)
    SameDimension = _itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUC2LM2_SameDimension
    

    def __init__(self, enclosingFilter: "itkImageToImageFilterIUC2LM2"):
        r"""__init__(itkScanlineFilterCommonIUC2LM2 self, itkImageToImageFilterIUC2LM2 enclosingFilter) -> itkScanlineFilterCommonIUC2LM2"""
        _itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUC2LM2_swiginit(self, _itkLabelImageToLabelMapFilterPython.new_itkScanlineFilterCommonIUC2LM2(enclosingFilter))
    __swig_destroy__ = _itkLabelImageToLabelMapFilterPython.delete_itkScanlineFilterCommonIUC2LM2
    cast = _swig_new_static_method(_itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUC2LM2_cast)

    def New(*args, **kargs):
        """New() -> itkScanlineFilterCommonIUC2LM2

        Create a new object of the class itkScanlineFilterCommonIUC2LM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScanlineFilterCommonIUC2LM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkScanlineFilterCommonIUC2LM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkScanlineFilterCommonIUC2LM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkScanlineFilterCommonIUC2LM2 in _itkLabelImageToLabelMapFilterPython:
_itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUC2LM2_swigregister(itkScanlineFilterCommonIUC2LM2)
itkScanlineFilterCommonIUC2LM2___New_orig__ = _itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUC2LM2___New_orig__
itkScanlineFilterCommonIUC2LM2_cast = _itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUC2LM2_cast

class itkScanlineFilterCommonIUC3LM3(object):
    r"""Proxy of C++ itkScanlineFilterCommonIUC3LM3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUC3LM3___New_orig__)
    SameDimension = _itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUC3LM3_SameDimension
    

    def __init__(self, enclosingFilter: "itkImageToImageFilterIUC3LM3"):
        r"""__init__(itkScanlineFilterCommonIUC3LM3 self, itkImageToImageFilterIUC3LM3 enclosingFilter) -> itkScanlineFilterCommonIUC3LM3"""
        _itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUC3LM3_swiginit(self, _itkLabelImageToLabelMapFilterPython.new_itkScanlineFilterCommonIUC3LM3(enclosingFilter))
    __swig_destroy__ = _itkLabelImageToLabelMapFilterPython.delete_itkScanlineFilterCommonIUC3LM3
    cast = _swig_new_static_method(_itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUC3LM3_cast)

    def New(*args, **kargs):
        """New() -> itkScanlineFilterCommonIUC3LM3

        Create a new object of the class itkScanlineFilterCommonIUC3LM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScanlineFilterCommonIUC3LM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkScanlineFilterCommonIUC3LM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkScanlineFilterCommonIUC3LM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkScanlineFilterCommonIUC3LM3 in _itkLabelImageToLabelMapFilterPython:
_itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUC3LM3_swigregister(itkScanlineFilterCommonIUC3LM3)
itkScanlineFilterCommonIUC3LM3___New_orig__ = _itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUC3LM3___New_orig__
itkScanlineFilterCommonIUC3LM3_cast = _itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUC3LM3_cast

class itkScanlineFilterCommonIUS2LM2(object):
    r"""Proxy of C++ itkScanlineFilterCommonIUS2LM2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUS2LM2___New_orig__)
    SameDimension = _itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUS2LM2_SameDimension
    

    def __init__(self, enclosingFilter: "itkImageToImageFilterIUS2LM2"):
        r"""__init__(itkScanlineFilterCommonIUS2LM2 self, itkImageToImageFilterIUS2LM2 enclosingFilter) -> itkScanlineFilterCommonIUS2LM2"""
        _itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUS2LM2_swiginit(self, _itkLabelImageToLabelMapFilterPython.new_itkScanlineFilterCommonIUS2LM2(enclosingFilter))
    __swig_destroy__ = _itkLabelImageToLabelMapFilterPython.delete_itkScanlineFilterCommonIUS2LM2
    cast = _swig_new_static_method(_itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUS2LM2_cast)

    def New(*args, **kargs):
        """New() -> itkScanlineFilterCommonIUS2LM2

        Create a new object of the class itkScanlineFilterCommonIUS2LM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScanlineFilterCommonIUS2LM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkScanlineFilterCommonIUS2LM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkScanlineFilterCommonIUS2LM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkScanlineFilterCommonIUS2LM2 in _itkLabelImageToLabelMapFilterPython:
_itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUS2LM2_swigregister(itkScanlineFilterCommonIUS2LM2)
itkScanlineFilterCommonIUS2LM2___New_orig__ = _itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUS2LM2___New_orig__
itkScanlineFilterCommonIUS2LM2_cast = _itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUS2LM2_cast

class itkScanlineFilterCommonIUS3LM3(object):
    r"""Proxy of C++ itkScanlineFilterCommonIUS3LM3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUS3LM3___New_orig__)
    SameDimension = _itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUS3LM3_SameDimension
    

    def __init__(self, enclosingFilter: "itkImageToImageFilterIUS3LM3"):
        r"""__init__(itkScanlineFilterCommonIUS3LM3 self, itkImageToImageFilterIUS3LM3 enclosingFilter) -> itkScanlineFilterCommonIUS3LM3"""
        _itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUS3LM3_swiginit(self, _itkLabelImageToLabelMapFilterPython.new_itkScanlineFilterCommonIUS3LM3(enclosingFilter))
    __swig_destroy__ = _itkLabelImageToLabelMapFilterPython.delete_itkScanlineFilterCommonIUS3LM3
    cast = _swig_new_static_method(_itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUS3LM3_cast)

    def New(*args, **kargs):
        """New() -> itkScanlineFilterCommonIUS3LM3

        Create a new object of the class itkScanlineFilterCommonIUS3LM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScanlineFilterCommonIUS3LM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkScanlineFilterCommonIUS3LM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkScanlineFilterCommonIUS3LM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkScanlineFilterCommonIUS3LM3 in _itkLabelImageToLabelMapFilterPython:
_itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUS3LM3_swigregister(itkScanlineFilterCommonIUS3LM3)
itkScanlineFilterCommonIUS3LM3___New_orig__ = _itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUS3LM3___New_orig__
itkScanlineFilterCommonIUS3LM3_cast = _itkLabelImageToLabelMapFilterPython.itkScanlineFilterCommonIUS3LM3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def label_image_to_label_map_filter(*args, **kwargs):
    """Procedural interface for LabelImageToLabelMapFilter"""
    import itk
    instance = itk.LabelImageToLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def label_image_to_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.LabelImageToLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.LabelImageToLabelMapFilter.values()[0]
    else:
        filter_object = itk.LabelImageToLabelMapFilter

    label_image_to_label_map_filter.__doc__ = filter_object.__doc__
    label_image_to_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    label_image_to_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    label_image_to_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



