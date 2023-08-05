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
    from . import _itkIsoDataThresholdCalculatorPython
else:
    import _itkIsoDataThresholdCalculatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkIsoDataThresholdCalculatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkIsoDataThresholdCalculatorPython.SWIG_PyStaticMethod_New

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
import stdcomplexPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkCovariantVectorPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkArrayPython
import itkHistogramPython
import itkSamplePython

def itkIsoDataThresholdCalculatorHFD_New():
  return itkIsoDataThresholdCalculatorHFD.New()


def itkIsoDataThresholdCalculatorHDD_New():
  return itkIsoDataThresholdCalculatorHDD.New()


def itkIsoDataThresholdCalculatorHFF_New():
  return itkIsoDataThresholdCalculatorHFF.New()


def itkIsoDataThresholdCalculatorHDF_New():
  return itkIsoDataThresholdCalculatorHDF.New()


def itkIsoDataThresholdCalculatorHFUS_New():
  return itkIsoDataThresholdCalculatorHFUS.New()


def itkIsoDataThresholdCalculatorHDUS_New():
  return itkIsoDataThresholdCalculatorHDUS.New()


def itkIsoDataThresholdCalculatorHFUC_New():
  return itkIsoDataThresholdCalculatorHFUC.New()


def itkIsoDataThresholdCalculatorHDUC_New():
  return itkIsoDataThresholdCalculatorHDUC.New()


def itkIsoDataThresholdCalculatorHFSS_New():
  return itkIsoDataThresholdCalculatorHFSS.New()


def itkIsoDataThresholdCalculatorHDSS_New():
  return itkIsoDataThresholdCalculatorHDSS.New()

class itkIsoDataThresholdCalculatorHDD(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD):
    r"""Proxy of C++ itkIsoDataThresholdCalculatorHDD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDD___New_orig__)
    Clone = _swig_new_instance_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDD_Clone)
    __swig_destroy__ = _itkIsoDataThresholdCalculatorPython.delete_itkIsoDataThresholdCalculatorHDD
    cast = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDD_cast)

    def New(*args, **kargs):
        """New() -> itkIsoDataThresholdCalculatorHDD

        Create a new object of the class itkIsoDataThresholdCalculatorHDD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoDataThresholdCalculatorHDD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoDataThresholdCalculatorHDD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoDataThresholdCalculatorHDD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIsoDataThresholdCalculatorHDD in _itkIsoDataThresholdCalculatorPython:
_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDD_swigregister(itkIsoDataThresholdCalculatorHDD)
itkIsoDataThresholdCalculatorHDD___New_orig__ = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDD___New_orig__
itkIsoDataThresholdCalculatorHDD_cast = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDD_cast

class itkIsoDataThresholdCalculatorHDF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    r"""Proxy of C++ itkIsoDataThresholdCalculatorHDF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDF___New_orig__)
    Clone = _swig_new_instance_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDF_Clone)
    __swig_destroy__ = _itkIsoDataThresholdCalculatorPython.delete_itkIsoDataThresholdCalculatorHDF
    cast = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDF_cast)

    def New(*args, **kargs):
        """New() -> itkIsoDataThresholdCalculatorHDF

        Create a new object of the class itkIsoDataThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoDataThresholdCalculatorHDF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoDataThresholdCalculatorHDF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoDataThresholdCalculatorHDF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIsoDataThresholdCalculatorHDF in _itkIsoDataThresholdCalculatorPython:
_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDF_swigregister(itkIsoDataThresholdCalculatorHDF)
itkIsoDataThresholdCalculatorHDF___New_orig__ = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDF___New_orig__
itkIsoDataThresholdCalculatorHDF_cast = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDF_cast

class itkIsoDataThresholdCalculatorHDSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    r"""Proxy of C++ itkIsoDataThresholdCalculatorHDSS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDSS___New_orig__)
    Clone = _swig_new_instance_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDSS_Clone)
    __swig_destroy__ = _itkIsoDataThresholdCalculatorPython.delete_itkIsoDataThresholdCalculatorHDSS
    cast = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDSS_cast)

    def New(*args, **kargs):
        """New() -> itkIsoDataThresholdCalculatorHDSS

        Create a new object of the class itkIsoDataThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoDataThresholdCalculatorHDSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoDataThresholdCalculatorHDSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoDataThresholdCalculatorHDSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIsoDataThresholdCalculatorHDSS in _itkIsoDataThresholdCalculatorPython:
_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDSS_swigregister(itkIsoDataThresholdCalculatorHDSS)
itkIsoDataThresholdCalculatorHDSS___New_orig__ = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDSS___New_orig__
itkIsoDataThresholdCalculatorHDSS_cast = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDSS_cast

class itkIsoDataThresholdCalculatorHDUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    r"""Proxy of C++ itkIsoDataThresholdCalculatorHDUC class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUC___New_orig__)
    Clone = _swig_new_instance_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUC_Clone)
    __swig_destroy__ = _itkIsoDataThresholdCalculatorPython.delete_itkIsoDataThresholdCalculatorHDUC
    cast = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUC_cast)

    def New(*args, **kargs):
        """New() -> itkIsoDataThresholdCalculatorHDUC

        Create a new object of the class itkIsoDataThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoDataThresholdCalculatorHDUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoDataThresholdCalculatorHDUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoDataThresholdCalculatorHDUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIsoDataThresholdCalculatorHDUC in _itkIsoDataThresholdCalculatorPython:
_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUC_swigregister(itkIsoDataThresholdCalculatorHDUC)
itkIsoDataThresholdCalculatorHDUC___New_orig__ = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUC___New_orig__
itkIsoDataThresholdCalculatorHDUC_cast = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUC_cast

class itkIsoDataThresholdCalculatorHDUS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS):
    r"""Proxy of C++ itkIsoDataThresholdCalculatorHDUS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUS___New_orig__)
    Clone = _swig_new_instance_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUS_Clone)
    __swig_destroy__ = _itkIsoDataThresholdCalculatorPython.delete_itkIsoDataThresholdCalculatorHDUS
    cast = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUS_cast)

    def New(*args, **kargs):
        """New() -> itkIsoDataThresholdCalculatorHDUS

        Create a new object of the class itkIsoDataThresholdCalculatorHDUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoDataThresholdCalculatorHDUS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoDataThresholdCalculatorHDUS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoDataThresholdCalculatorHDUS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIsoDataThresholdCalculatorHDUS in _itkIsoDataThresholdCalculatorPython:
_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUS_swigregister(itkIsoDataThresholdCalculatorHDUS)
itkIsoDataThresholdCalculatorHDUS___New_orig__ = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUS___New_orig__
itkIsoDataThresholdCalculatorHDUS_cast = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHDUS_cast

class itkIsoDataThresholdCalculatorHFD(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD):
    r"""Proxy of C++ itkIsoDataThresholdCalculatorHFD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFD___New_orig__)
    Clone = _swig_new_instance_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFD_Clone)
    __swig_destroy__ = _itkIsoDataThresholdCalculatorPython.delete_itkIsoDataThresholdCalculatorHFD
    cast = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFD_cast)

    def New(*args, **kargs):
        """New() -> itkIsoDataThresholdCalculatorHFD

        Create a new object of the class itkIsoDataThresholdCalculatorHFD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoDataThresholdCalculatorHFD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoDataThresholdCalculatorHFD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoDataThresholdCalculatorHFD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIsoDataThresholdCalculatorHFD in _itkIsoDataThresholdCalculatorPython:
_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFD_swigregister(itkIsoDataThresholdCalculatorHFD)
itkIsoDataThresholdCalculatorHFD___New_orig__ = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFD___New_orig__
itkIsoDataThresholdCalculatorHFD_cast = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFD_cast

class itkIsoDataThresholdCalculatorHFF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    r"""Proxy of C++ itkIsoDataThresholdCalculatorHFF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFF___New_orig__)
    Clone = _swig_new_instance_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFF_Clone)
    __swig_destroy__ = _itkIsoDataThresholdCalculatorPython.delete_itkIsoDataThresholdCalculatorHFF
    cast = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFF_cast)

    def New(*args, **kargs):
        """New() -> itkIsoDataThresholdCalculatorHFF

        Create a new object of the class itkIsoDataThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoDataThresholdCalculatorHFF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoDataThresholdCalculatorHFF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoDataThresholdCalculatorHFF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIsoDataThresholdCalculatorHFF in _itkIsoDataThresholdCalculatorPython:
_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFF_swigregister(itkIsoDataThresholdCalculatorHFF)
itkIsoDataThresholdCalculatorHFF___New_orig__ = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFF___New_orig__
itkIsoDataThresholdCalculatorHFF_cast = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFF_cast

class itkIsoDataThresholdCalculatorHFSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    r"""Proxy of C++ itkIsoDataThresholdCalculatorHFSS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFSS___New_orig__)
    Clone = _swig_new_instance_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFSS_Clone)
    __swig_destroy__ = _itkIsoDataThresholdCalculatorPython.delete_itkIsoDataThresholdCalculatorHFSS
    cast = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFSS_cast)

    def New(*args, **kargs):
        """New() -> itkIsoDataThresholdCalculatorHFSS

        Create a new object of the class itkIsoDataThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoDataThresholdCalculatorHFSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoDataThresholdCalculatorHFSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoDataThresholdCalculatorHFSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIsoDataThresholdCalculatorHFSS in _itkIsoDataThresholdCalculatorPython:
_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFSS_swigregister(itkIsoDataThresholdCalculatorHFSS)
itkIsoDataThresholdCalculatorHFSS___New_orig__ = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFSS___New_orig__
itkIsoDataThresholdCalculatorHFSS_cast = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFSS_cast

class itkIsoDataThresholdCalculatorHFUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    r"""Proxy of C++ itkIsoDataThresholdCalculatorHFUC class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUC___New_orig__)
    Clone = _swig_new_instance_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUC_Clone)
    __swig_destroy__ = _itkIsoDataThresholdCalculatorPython.delete_itkIsoDataThresholdCalculatorHFUC
    cast = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUC_cast)

    def New(*args, **kargs):
        """New() -> itkIsoDataThresholdCalculatorHFUC

        Create a new object of the class itkIsoDataThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoDataThresholdCalculatorHFUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoDataThresholdCalculatorHFUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoDataThresholdCalculatorHFUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIsoDataThresholdCalculatorHFUC in _itkIsoDataThresholdCalculatorPython:
_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUC_swigregister(itkIsoDataThresholdCalculatorHFUC)
itkIsoDataThresholdCalculatorHFUC___New_orig__ = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUC___New_orig__
itkIsoDataThresholdCalculatorHFUC_cast = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUC_cast

class itkIsoDataThresholdCalculatorHFUS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS):
    r"""Proxy of C++ itkIsoDataThresholdCalculatorHFUS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUS___New_orig__)
    Clone = _swig_new_instance_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUS_Clone)
    __swig_destroy__ = _itkIsoDataThresholdCalculatorPython.delete_itkIsoDataThresholdCalculatorHFUS
    cast = _swig_new_static_method(_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUS_cast)

    def New(*args, **kargs):
        """New() -> itkIsoDataThresholdCalculatorHFUS

        Create a new object of the class itkIsoDataThresholdCalculatorHFUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsoDataThresholdCalculatorHFUS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsoDataThresholdCalculatorHFUS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsoDataThresholdCalculatorHFUS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkIsoDataThresholdCalculatorHFUS in _itkIsoDataThresholdCalculatorPython:
_itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUS_swigregister(itkIsoDataThresholdCalculatorHFUS)
itkIsoDataThresholdCalculatorHFUS___New_orig__ = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUS___New_orig__
itkIsoDataThresholdCalculatorHFUS_cast = _itkIsoDataThresholdCalculatorPython.itkIsoDataThresholdCalculatorHFUS_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def iso_data_threshold_calculator(*args, **kwargs):
    """Procedural interface for IsoDataThresholdCalculator"""
    import itk
    instance = itk.IsoDataThresholdCalculator.New(*args, **kwargs)
    return instance.__internal_call__()

def iso_data_threshold_calculator_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.IsoDataThresholdCalculator, itkTemplate.itkTemplate):
        filter_object = itk.IsoDataThresholdCalculator.values()[0]
    else:
        filter_object = itk.IsoDataThresholdCalculator

    iso_data_threshold_calculator.__doc__ = filter_object.__doc__
    iso_data_threshold_calculator.__doc__ += "\n Args are Input(s) to the filter.\n"
    iso_data_threshold_calculator.__doc__ += "Available Keyword Arguments:\n"
    iso_data_threshold_calculator.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



