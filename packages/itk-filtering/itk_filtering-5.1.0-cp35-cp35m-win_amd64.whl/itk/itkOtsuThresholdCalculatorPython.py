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
    from . import _itkOtsuThresholdCalculatorPython
else:
    import _itkOtsuThresholdCalculatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkOtsuThresholdCalculatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkOtsuThresholdCalculatorPython.SWIG_PyStaticMethod_New

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

def itkOtsuThresholdCalculatorHFD_New():
  return itkOtsuThresholdCalculatorHFD.New()


def itkOtsuThresholdCalculatorHDD_New():
  return itkOtsuThresholdCalculatorHDD.New()


def itkOtsuThresholdCalculatorHFF_New():
  return itkOtsuThresholdCalculatorHFF.New()


def itkOtsuThresholdCalculatorHDF_New():
  return itkOtsuThresholdCalculatorHDF.New()


def itkOtsuThresholdCalculatorHFUS_New():
  return itkOtsuThresholdCalculatorHFUS.New()


def itkOtsuThresholdCalculatorHDUS_New():
  return itkOtsuThresholdCalculatorHDUS.New()


def itkOtsuThresholdCalculatorHFUC_New():
  return itkOtsuThresholdCalculatorHFUC.New()


def itkOtsuThresholdCalculatorHDUC_New():
  return itkOtsuThresholdCalculatorHDUC.New()


def itkOtsuThresholdCalculatorHFSS_New():
  return itkOtsuThresholdCalculatorHFSS.New()


def itkOtsuThresholdCalculatorHDSS_New():
  return itkOtsuThresholdCalculatorHDSS.New()

class itkOtsuThresholdCalculatorHDD(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD):
    r"""Proxy of C++ itkOtsuThresholdCalculatorHDD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDD___New_orig__)
    Clone = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDD_Clone)
    SetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDD_SetReturnBinMidpoint)
    GetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDD_GetReturnBinMidpoint)
    ReturnBinMidpointOn = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDD_ReturnBinMidpointOn)
    ReturnBinMidpointOff = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDD_ReturnBinMidpointOff)
    Compute = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDD_Compute)
    __swig_destroy__ = _itkOtsuThresholdCalculatorPython.delete_itkOtsuThresholdCalculatorHDD
    cast = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDD_cast)

    def New(*args, **kargs):
        """New() -> itkOtsuThresholdCalculatorHDD

        Create a new object of the class itkOtsuThresholdCalculatorHDD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOtsuThresholdCalculatorHDD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOtsuThresholdCalculatorHDD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOtsuThresholdCalculatorHDD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkOtsuThresholdCalculatorHDD in _itkOtsuThresholdCalculatorPython:
_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDD_swigregister(itkOtsuThresholdCalculatorHDD)
itkOtsuThresholdCalculatorHDD___New_orig__ = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDD___New_orig__
itkOtsuThresholdCalculatorHDD_cast = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDD_cast

class itkOtsuThresholdCalculatorHDF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    r"""Proxy of C++ itkOtsuThresholdCalculatorHDF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF___New_orig__)
    Clone = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_Clone)
    SetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_SetReturnBinMidpoint)
    GetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_GetReturnBinMidpoint)
    ReturnBinMidpointOn = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_ReturnBinMidpointOn)
    ReturnBinMidpointOff = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_ReturnBinMidpointOff)
    Compute = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_Compute)
    __swig_destroy__ = _itkOtsuThresholdCalculatorPython.delete_itkOtsuThresholdCalculatorHDF
    cast = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_cast)

    def New(*args, **kargs):
        """New() -> itkOtsuThresholdCalculatorHDF

        Create a new object of the class itkOtsuThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOtsuThresholdCalculatorHDF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOtsuThresholdCalculatorHDF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOtsuThresholdCalculatorHDF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkOtsuThresholdCalculatorHDF in _itkOtsuThresholdCalculatorPython:
_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_swigregister(itkOtsuThresholdCalculatorHDF)
itkOtsuThresholdCalculatorHDF___New_orig__ = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF___New_orig__
itkOtsuThresholdCalculatorHDF_cast = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDF_cast

class itkOtsuThresholdCalculatorHDSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    r"""Proxy of C++ itkOtsuThresholdCalculatorHDSS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS___New_orig__)
    Clone = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_Clone)
    SetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_SetReturnBinMidpoint)
    GetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_GetReturnBinMidpoint)
    ReturnBinMidpointOn = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_ReturnBinMidpointOn)
    ReturnBinMidpointOff = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_ReturnBinMidpointOff)
    Compute = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_Compute)
    __swig_destroy__ = _itkOtsuThresholdCalculatorPython.delete_itkOtsuThresholdCalculatorHDSS
    cast = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_cast)

    def New(*args, **kargs):
        """New() -> itkOtsuThresholdCalculatorHDSS

        Create a new object of the class itkOtsuThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOtsuThresholdCalculatorHDSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOtsuThresholdCalculatorHDSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOtsuThresholdCalculatorHDSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkOtsuThresholdCalculatorHDSS in _itkOtsuThresholdCalculatorPython:
_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_swigregister(itkOtsuThresholdCalculatorHDSS)
itkOtsuThresholdCalculatorHDSS___New_orig__ = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS___New_orig__
itkOtsuThresholdCalculatorHDSS_cast = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDSS_cast

class itkOtsuThresholdCalculatorHDUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    r"""Proxy of C++ itkOtsuThresholdCalculatorHDUC class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC___New_orig__)
    Clone = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_Clone)
    SetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_SetReturnBinMidpoint)
    GetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_GetReturnBinMidpoint)
    ReturnBinMidpointOn = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_ReturnBinMidpointOn)
    ReturnBinMidpointOff = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_ReturnBinMidpointOff)
    Compute = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_Compute)
    __swig_destroy__ = _itkOtsuThresholdCalculatorPython.delete_itkOtsuThresholdCalculatorHDUC
    cast = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_cast)

    def New(*args, **kargs):
        """New() -> itkOtsuThresholdCalculatorHDUC

        Create a new object of the class itkOtsuThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOtsuThresholdCalculatorHDUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOtsuThresholdCalculatorHDUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOtsuThresholdCalculatorHDUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkOtsuThresholdCalculatorHDUC in _itkOtsuThresholdCalculatorPython:
_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_swigregister(itkOtsuThresholdCalculatorHDUC)
itkOtsuThresholdCalculatorHDUC___New_orig__ = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC___New_orig__
itkOtsuThresholdCalculatorHDUC_cast = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUC_cast

class itkOtsuThresholdCalculatorHDUS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS):
    r"""Proxy of C++ itkOtsuThresholdCalculatorHDUS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUS___New_orig__)
    Clone = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUS_Clone)
    SetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUS_SetReturnBinMidpoint)
    GetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUS_GetReturnBinMidpoint)
    ReturnBinMidpointOn = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUS_ReturnBinMidpointOn)
    ReturnBinMidpointOff = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUS_ReturnBinMidpointOff)
    Compute = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUS_Compute)
    __swig_destroy__ = _itkOtsuThresholdCalculatorPython.delete_itkOtsuThresholdCalculatorHDUS
    cast = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUS_cast)

    def New(*args, **kargs):
        """New() -> itkOtsuThresholdCalculatorHDUS

        Create a new object of the class itkOtsuThresholdCalculatorHDUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOtsuThresholdCalculatorHDUS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOtsuThresholdCalculatorHDUS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOtsuThresholdCalculatorHDUS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkOtsuThresholdCalculatorHDUS in _itkOtsuThresholdCalculatorPython:
_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUS_swigregister(itkOtsuThresholdCalculatorHDUS)
itkOtsuThresholdCalculatorHDUS___New_orig__ = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUS___New_orig__
itkOtsuThresholdCalculatorHDUS_cast = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHDUS_cast

class itkOtsuThresholdCalculatorHFD(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD):
    r"""Proxy of C++ itkOtsuThresholdCalculatorHFD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFD___New_orig__)
    Clone = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFD_Clone)
    SetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFD_SetReturnBinMidpoint)
    GetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFD_GetReturnBinMidpoint)
    ReturnBinMidpointOn = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFD_ReturnBinMidpointOn)
    ReturnBinMidpointOff = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFD_ReturnBinMidpointOff)
    Compute = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFD_Compute)
    __swig_destroy__ = _itkOtsuThresholdCalculatorPython.delete_itkOtsuThresholdCalculatorHFD
    cast = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFD_cast)

    def New(*args, **kargs):
        """New() -> itkOtsuThresholdCalculatorHFD

        Create a new object of the class itkOtsuThresholdCalculatorHFD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOtsuThresholdCalculatorHFD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOtsuThresholdCalculatorHFD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOtsuThresholdCalculatorHFD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkOtsuThresholdCalculatorHFD in _itkOtsuThresholdCalculatorPython:
_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFD_swigregister(itkOtsuThresholdCalculatorHFD)
itkOtsuThresholdCalculatorHFD___New_orig__ = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFD___New_orig__
itkOtsuThresholdCalculatorHFD_cast = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFD_cast

class itkOtsuThresholdCalculatorHFF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    r"""Proxy of C++ itkOtsuThresholdCalculatorHFF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF___New_orig__)
    Clone = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_Clone)
    SetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_SetReturnBinMidpoint)
    GetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_GetReturnBinMidpoint)
    ReturnBinMidpointOn = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_ReturnBinMidpointOn)
    ReturnBinMidpointOff = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_ReturnBinMidpointOff)
    Compute = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_Compute)
    __swig_destroy__ = _itkOtsuThresholdCalculatorPython.delete_itkOtsuThresholdCalculatorHFF
    cast = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_cast)

    def New(*args, **kargs):
        """New() -> itkOtsuThresholdCalculatorHFF

        Create a new object of the class itkOtsuThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOtsuThresholdCalculatorHFF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOtsuThresholdCalculatorHFF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOtsuThresholdCalculatorHFF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkOtsuThresholdCalculatorHFF in _itkOtsuThresholdCalculatorPython:
_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_swigregister(itkOtsuThresholdCalculatorHFF)
itkOtsuThresholdCalculatorHFF___New_orig__ = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF___New_orig__
itkOtsuThresholdCalculatorHFF_cast = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFF_cast

class itkOtsuThresholdCalculatorHFSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    r"""Proxy of C++ itkOtsuThresholdCalculatorHFSS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS___New_orig__)
    Clone = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_Clone)
    SetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_SetReturnBinMidpoint)
    GetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_GetReturnBinMidpoint)
    ReturnBinMidpointOn = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_ReturnBinMidpointOn)
    ReturnBinMidpointOff = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_ReturnBinMidpointOff)
    Compute = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_Compute)
    __swig_destroy__ = _itkOtsuThresholdCalculatorPython.delete_itkOtsuThresholdCalculatorHFSS
    cast = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_cast)

    def New(*args, **kargs):
        """New() -> itkOtsuThresholdCalculatorHFSS

        Create a new object of the class itkOtsuThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOtsuThresholdCalculatorHFSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOtsuThresholdCalculatorHFSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOtsuThresholdCalculatorHFSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkOtsuThresholdCalculatorHFSS in _itkOtsuThresholdCalculatorPython:
_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_swigregister(itkOtsuThresholdCalculatorHFSS)
itkOtsuThresholdCalculatorHFSS___New_orig__ = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS___New_orig__
itkOtsuThresholdCalculatorHFSS_cast = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFSS_cast

class itkOtsuThresholdCalculatorHFUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    r"""Proxy of C++ itkOtsuThresholdCalculatorHFUC class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC___New_orig__)
    Clone = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_Clone)
    SetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_SetReturnBinMidpoint)
    GetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_GetReturnBinMidpoint)
    ReturnBinMidpointOn = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_ReturnBinMidpointOn)
    ReturnBinMidpointOff = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_ReturnBinMidpointOff)
    Compute = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_Compute)
    __swig_destroy__ = _itkOtsuThresholdCalculatorPython.delete_itkOtsuThresholdCalculatorHFUC
    cast = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_cast)

    def New(*args, **kargs):
        """New() -> itkOtsuThresholdCalculatorHFUC

        Create a new object of the class itkOtsuThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOtsuThresholdCalculatorHFUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOtsuThresholdCalculatorHFUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOtsuThresholdCalculatorHFUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkOtsuThresholdCalculatorHFUC in _itkOtsuThresholdCalculatorPython:
_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_swigregister(itkOtsuThresholdCalculatorHFUC)
itkOtsuThresholdCalculatorHFUC___New_orig__ = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC___New_orig__
itkOtsuThresholdCalculatorHFUC_cast = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUC_cast

class itkOtsuThresholdCalculatorHFUS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS):
    r"""Proxy of C++ itkOtsuThresholdCalculatorHFUS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUS___New_orig__)
    Clone = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUS_Clone)
    SetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUS_SetReturnBinMidpoint)
    GetReturnBinMidpoint = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUS_GetReturnBinMidpoint)
    ReturnBinMidpointOn = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUS_ReturnBinMidpointOn)
    ReturnBinMidpointOff = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUS_ReturnBinMidpointOff)
    Compute = _swig_new_instance_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUS_Compute)
    __swig_destroy__ = _itkOtsuThresholdCalculatorPython.delete_itkOtsuThresholdCalculatorHFUS
    cast = _swig_new_static_method(_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUS_cast)

    def New(*args, **kargs):
        """New() -> itkOtsuThresholdCalculatorHFUS

        Create a new object of the class itkOtsuThresholdCalculatorHFUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOtsuThresholdCalculatorHFUS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOtsuThresholdCalculatorHFUS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOtsuThresholdCalculatorHFUS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkOtsuThresholdCalculatorHFUS in _itkOtsuThresholdCalculatorPython:
_itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUS_swigregister(itkOtsuThresholdCalculatorHFUS)
itkOtsuThresholdCalculatorHFUS___New_orig__ = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUS___New_orig__
itkOtsuThresholdCalculatorHFUS_cast = _itkOtsuThresholdCalculatorPython.itkOtsuThresholdCalculatorHFUS_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def otsu_threshold_calculator(*args, **kwargs):
    """Procedural interface for OtsuThresholdCalculator"""
    import itk
    instance = itk.OtsuThresholdCalculator.New(*args, **kwargs)
    return instance.__internal_call__()

def otsu_threshold_calculator_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.OtsuThresholdCalculator, itkTemplate.itkTemplate):
        filter_object = itk.OtsuThresholdCalculator.values()[0]
    else:
        filter_object = itk.OtsuThresholdCalculator

    otsu_threshold_calculator.__doc__ = filter_object.__doc__
    otsu_threshold_calculator.__doc__ += "\n Args are Input(s) to the filter.\n"
    otsu_threshold_calculator.__doc__ += "Available Keyword Arguments:\n"
    otsu_threshold_calculator.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



