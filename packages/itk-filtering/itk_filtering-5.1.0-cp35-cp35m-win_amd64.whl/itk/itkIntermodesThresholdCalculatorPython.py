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
    from . import _itkIntermodesThresholdCalculatorPython
else:
    import _itkIntermodesThresholdCalculatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkIntermodesThresholdCalculatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkIntermodesThresholdCalculatorPython.SWIG_PyStaticMethod_New

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
import itkHistogramThresholdCalculatorPython
import itkSimpleDataObjectDecoratorPython
import itkRGBAPixelPython
import itkFixedArrayPython
import itkArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkVectorPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkHistogramPython
import itkSamplePython

def itkIntermodesThresholdCalculatorHFD_New():
  return itkIntermodesThresholdCalculatorHFD.New()


def itkIntermodesThresholdCalculatorHDD_New():
  return itkIntermodesThresholdCalculatorHDD.New()


def itkIntermodesThresholdCalculatorHFF_New():
  return itkIntermodesThresholdCalculatorHFF.New()


def itkIntermodesThresholdCalculatorHDF_New():
  return itkIntermodesThresholdCalculatorHDF.New()


def itkIntermodesThresholdCalculatorHFUS_New():
  return itkIntermodesThresholdCalculatorHFUS.New()


def itkIntermodesThresholdCalculatorHDUS_New():
  return itkIntermodesThresholdCalculatorHDUS.New()


def itkIntermodesThresholdCalculatorHFUC_New():
  return itkIntermodesThresholdCalculatorHFUC.New()


def itkIntermodesThresholdCalculatorHDUC_New():
  return itkIntermodesThresholdCalculatorHDUC.New()


def itkIntermodesThresholdCalculatorHFSS_New():
  return itkIntermodesThresholdCalculatorHFSS.New()


def itkIntermodesThresholdCalculatorHDSS_New():
  return itkIntermodesThresholdCalculatorHDSS.New()

class itkIntermodesThresholdCalculatorHDD(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD):
    r"""Proxy of C++ itkIntermodesThresholdCalculatorHDD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDD___New_orig__)
    Clone = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDD_Clone)
    SetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDD_SetMaximumSmoothingIterations)
    GetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDD_GetMaximumSmoothingIterations)
    SetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDD_SetUseInterMode)
    GetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDD_GetUseInterMode)
    UseInterModeOn = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDD_UseInterModeOn)
    UseInterModeOff = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDD_UseInterModeOff)
    __swig_destroy__ = _itkIntermodesThresholdCalculatorPython.delete_itkIntermodesThresholdCalculatorHDD
    cast = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDD_cast)

    def New(*args, **kargs):
        """New() -> itkIntermodesThresholdCalculatorHDD

        Create a new object of the class itkIntermodesThresholdCalculatorHDD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIntermodesThresholdCalculatorHDD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIntermodesThresholdCalculatorHDD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIntermodesThresholdCalculatorHDD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIntermodesThresholdCalculatorHDD in _itkIntermodesThresholdCalculatorPython:
_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDD_swigregister(itkIntermodesThresholdCalculatorHDD)
itkIntermodesThresholdCalculatorHDD___New_orig__ = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDD___New_orig__
itkIntermodesThresholdCalculatorHDD_cast = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDD_cast

class itkIntermodesThresholdCalculatorHDF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    r"""Proxy of C++ itkIntermodesThresholdCalculatorHDF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDF___New_orig__)
    Clone = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDF_Clone)
    SetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDF_SetMaximumSmoothingIterations)
    GetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDF_GetMaximumSmoothingIterations)
    SetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDF_SetUseInterMode)
    GetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDF_GetUseInterMode)
    UseInterModeOn = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDF_UseInterModeOn)
    UseInterModeOff = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDF_UseInterModeOff)
    __swig_destroy__ = _itkIntermodesThresholdCalculatorPython.delete_itkIntermodesThresholdCalculatorHDF
    cast = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDF_cast)

    def New(*args, **kargs):
        """New() -> itkIntermodesThresholdCalculatorHDF

        Create a new object of the class itkIntermodesThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIntermodesThresholdCalculatorHDF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIntermodesThresholdCalculatorHDF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIntermodesThresholdCalculatorHDF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIntermodesThresholdCalculatorHDF in _itkIntermodesThresholdCalculatorPython:
_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDF_swigregister(itkIntermodesThresholdCalculatorHDF)
itkIntermodesThresholdCalculatorHDF___New_orig__ = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDF___New_orig__
itkIntermodesThresholdCalculatorHDF_cast = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDF_cast

class itkIntermodesThresholdCalculatorHDSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    r"""Proxy of C++ itkIntermodesThresholdCalculatorHDSS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDSS___New_orig__)
    Clone = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDSS_Clone)
    SetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDSS_SetMaximumSmoothingIterations)
    GetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDSS_GetMaximumSmoothingIterations)
    SetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDSS_SetUseInterMode)
    GetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDSS_GetUseInterMode)
    UseInterModeOn = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDSS_UseInterModeOn)
    UseInterModeOff = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDSS_UseInterModeOff)
    __swig_destroy__ = _itkIntermodesThresholdCalculatorPython.delete_itkIntermodesThresholdCalculatorHDSS
    cast = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDSS_cast)

    def New(*args, **kargs):
        """New() -> itkIntermodesThresholdCalculatorHDSS

        Create a new object of the class itkIntermodesThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIntermodesThresholdCalculatorHDSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIntermodesThresholdCalculatorHDSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIntermodesThresholdCalculatorHDSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIntermodesThresholdCalculatorHDSS in _itkIntermodesThresholdCalculatorPython:
_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDSS_swigregister(itkIntermodesThresholdCalculatorHDSS)
itkIntermodesThresholdCalculatorHDSS___New_orig__ = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDSS___New_orig__
itkIntermodesThresholdCalculatorHDSS_cast = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDSS_cast

class itkIntermodesThresholdCalculatorHDUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    r"""Proxy of C++ itkIntermodesThresholdCalculatorHDUC class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUC___New_orig__)
    Clone = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUC_Clone)
    SetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUC_SetMaximumSmoothingIterations)
    GetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUC_GetMaximumSmoothingIterations)
    SetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUC_SetUseInterMode)
    GetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUC_GetUseInterMode)
    UseInterModeOn = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUC_UseInterModeOn)
    UseInterModeOff = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUC_UseInterModeOff)
    __swig_destroy__ = _itkIntermodesThresholdCalculatorPython.delete_itkIntermodesThresholdCalculatorHDUC
    cast = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUC_cast)

    def New(*args, **kargs):
        """New() -> itkIntermodesThresholdCalculatorHDUC

        Create a new object of the class itkIntermodesThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIntermodesThresholdCalculatorHDUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIntermodesThresholdCalculatorHDUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIntermodesThresholdCalculatorHDUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIntermodesThresholdCalculatorHDUC in _itkIntermodesThresholdCalculatorPython:
_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUC_swigregister(itkIntermodesThresholdCalculatorHDUC)
itkIntermodesThresholdCalculatorHDUC___New_orig__ = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUC___New_orig__
itkIntermodesThresholdCalculatorHDUC_cast = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUC_cast

class itkIntermodesThresholdCalculatorHDUS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS):
    r"""Proxy of C++ itkIntermodesThresholdCalculatorHDUS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUS___New_orig__)
    Clone = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUS_Clone)
    SetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUS_SetMaximumSmoothingIterations)
    GetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUS_GetMaximumSmoothingIterations)
    SetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUS_SetUseInterMode)
    GetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUS_GetUseInterMode)
    UseInterModeOn = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUS_UseInterModeOn)
    UseInterModeOff = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUS_UseInterModeOff)
    __swig_destroy__ = _itkIntermodesThresholdCalculatorPython.delete_itkIntermodesThresholdCalculatorHDUS
    cast = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUS_cast)

    def New(*args, **kargs):
        """New() -> itkIntermodesThresholdCalculatorHDUS

        Create a new object of the class itkIntermodesThresholdCalculatorHDUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIntermodesThresholdCalculatorHDUS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIntermodesThresholdCalculatorHDUS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIntermodesThresholdCalculatorHDUS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIntermodesThresholdCalculatorHDUS in _itkIntermodesThresholdCalculatorPython:
_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUS_swigregister(itkIntermodesThresholdCalculatorHDUS)
itkIntermodesThresholdCalculatorHDUS___New_orig__ = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUS___New_orig__
itkIntermodesThresholdCalculatorHDUS_cast = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHDUS_cast

class itkIntermodesThresholdCalculatorHFD(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD):
    r"""Proxy of C++ itkIntermodesThresholdCalculatorHFD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFD___New_orig__)
    Clone = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFD_Clone)
    SetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFD_SetMaximumSmoothingIterations)
    GetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFD_GetMaximumSmoothingIterations)
    SetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFD_SetUseInterMode)
    GetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFD_GetUseInterMode)
    UseInterModeOn = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFD_UseInterModeOn)
    UseInterModeOff = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFD_UseInterModeOff)
    __swig_destroy__ = _itkIntermodesThresholdCalculatorPython.delete_itkIntermodesThresholdCalculatorHFD
    cast = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFD_cast)

    def New(*args, **kargs):
        """New() -> itkIntermodesThresholdCalculatorHFD

        Create a new object of the class itkIntermodesThresholdCalculatorHFD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIntermodesThresholdCalculatorHFD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIntermodesThresholdCalculatorHFD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIntermodesThresholdCalculatorHFD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIntermodesThresholdCalculatorHFD in _itkIntermodesThresholdCalculatorPython:
_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFD_swigregister(itkIntermodesThresholdCalculatorHFD)
itkIntermodesThresholdCalculatorHFD___New_orig__ = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFD___New_orig__
itkIntermodesThresholdCalculatorHFD_cast = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFD_cast

class itkIntermodesThresholdCalculatorHFF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    r"""Proxy of C++ itkIntermodesThresholdCalculatorHFF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFF___New_orig__)
    Clone = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFF_Clone)
    SetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFF_SetMaximumSmoothingIterations)
    GetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFF_GetMaximumSmoothingIterations)
    SetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFF_SetUseInterMode)
    GetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFF_GetUseInterMode)
    UseInterModeOn = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFF_UseInterModeOn)
    UseInterModeOff = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFF_UseInterModeOff)
    __swig_destroy__ = _itkIntermodesThresholdCalculatorPython.delete_itkIntermodesThresholdCalculatorHFF
    cast = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFF_cast)

    def New(*args, **kargs):
        """New() -> itkIntermodesThresholdCalculatorHFF

        Create a new object of the class itkIntermodesThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIntermodesThresholdCalculatorHFF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIntermodesThresholdCalculatorHFF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIntermodesThresholdCalculatorHFF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIntermodesThresholdCalculatorHFF in _itkIntermodesThresholdCalculatorPython:
_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFF_swigregister(itkIntermodesThresholdCalculatorHFF)
itkIntermodesThresholdCalculatorHFF___New_orig__ = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFF___New_orig__
itkIntermodesThresholdCalculatorHFF_cast = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFF_cast

class itkIntermodesThresholdCalculatorHFSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    r"""Proxy of C++ itkIntermodesThresholdCalculatorHFSS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFSS___New_orig__)
    Clone = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFSS_Clone)
    SetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFSS_SetMaximumSmoothingIterations)
    GetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFSS_GetMaximumSmoothingIterations)
    SetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFSS_SetUseInterMode)
    GetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFSS_GetUseInterMode)
    UseInterModeOn = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFSS_UseInterModeOn)
    UseInterModeOff = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFSS_UseInterModeOff)
    __swig_destroy__ = _itkIntermodesThresholdCalculatorPython.delete_itkIntermodesThresholdCalculatorHFSS
    cast = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFSS_cast)

    def New(*args, **kargs):
        """New() -> itkIntermodesThresholdCalculatorHFSS

        Create a new object of the class itkIntermodesThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIntermodesThresholdCalculatorHFSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIntermodesThresholdCalculatorHFSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIntermodesThresholdCalculatorHFSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIntermodesThresholdCalculatorHFSS in _itkIntermodesThresholdCalculatorPython:
_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFSS_swigregister(itkIntermodesThresholdCalculatorHFSS)
itkIntermodesThresholdCalculatorHFSS___New_orig__ = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFSS___New_orig__
itkIntermodesThresholdCalculatorHFSS_cast = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFSS_cast

class itkIntermodesThresholdCalculatorHFUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    r"""Proxy of C++ itkIntermodesThresholdCalculatorHFUC class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUC___New_orig__)
    Clone = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUC_Clone)
    SetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUC_SetMaximumSmoothingIterations)
    GetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUC_GetMaximumSmoothingIterations)
    SetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUC_SetUseInterMode)
    GetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUC_GetUseInterMode)
    UseInterModeOn = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUC_UseInterModeOn)
    UseInterModeOff = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUC_UseInterModeOff)
    __swig_destroy__ = _itkIntermodesThresholdCalculatorPython.delete_itkIntermodesThresholdCalculatorHFUC
    cast = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUC_cast)

    def New(*args, **kargs):
        """New() -> itkIntermodesThresholdCalculatorHFUC

        Create a new object of the class itkIntermodesThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIntermodesThresholdCalculatorHFUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIntermodesThresholdCalculatorHFUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIntermodesThresholdCalculatorHFUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIntermodesThresholdCalculatorHFUC in _itkIntermodesThresholdCalculatorPython:
_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUC_swigregister(itkIntermodesThresholdCalculatorHFUC)
itkIntermodesThresholdCalculatorHFUC___New_orig__ = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUC___New_orig__
itkIntermodesThresholdCalculatorHFUC_cast = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUC_cast

class itkIntermodesThresholdCalculatorHFUS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS):
    r"""Proxy of C++ itkIntermodesThresholdCalculatorHFUS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUS___New_orig__)
    Clone = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUS_Clone)
    SetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUS_SetMaximumSmoothingIterations)
    GetMaximumSmoothingIterations = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUS_GetMaximumSmoothingIterations)
    SetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUS_SetUseInterMode)
    GetUseInterMode = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUS_GetUseInterMode)
    UseInterModeOn = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUS_UseInterModeOn)
    UseInterModeOff = _swig_new_instance_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUS_UseInterModeOff)
    __swig_destroy__ = _itkIntermodesThresholdCalculatorPython.delete_itkIntermodesThresholdCalculatorHFUS
    cast = _swig_new_static_method(_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUS_cast)

    def New(*args, **kargs):
        """New() -> itkIntermodesThresholdCalculatorHFUS

        Create a new object of the class itkIntermodesThresholdCalculatorHFUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIntermodesThresholdCalculatorHFUS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIntermodesThresholdCalculatorHFUS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIntermodesThresholdCalculatorHFUS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIntermodesThresholdCalculatorHFUS in _itkIntermodesThresholdCalculatorPython:
_itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUS_swigregister(itkIntermodesThresholdCalculatorHFUS)
itkIntermodesThresholdCalculatorHFUS___New_orig__ = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUS___New_orig__
itkIntermodesThresholdCalculatorHFUS_cast = _itkIntermodesThresholdCalculatorPython.itkIntermodesThresholdCalculatorHFUS_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def intermodes_threshold_calculator(*args, **kwargs):
    """Procedural interface for IntermodesThresholdCalculator"""
    import itk
    instance = itk.IntermodesThresholdCalculator.New(*args, **kwargs)
    return instance.__internal_call__()

def intermodes_threshold_calculator_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.IntermodesThresholdCalculator, itkTemplate.itkTemplate):
        filter_object = itk.IntermodesThresholdCalculator.values()[0]
    else:
        filter_object = itk.IntermodesThresholdCalculator

    intermodes_threshold_calculator.__doc__ = filter_object.__doc__
    intermodes_threshold_calculator.__doc__ += "\n Args are Input(s) to the filter.\n"
    intermodes_threshold_calculator.__doc__ += "Available Keyword Arguments:\n"
    intermodes_threshold_calculator.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



