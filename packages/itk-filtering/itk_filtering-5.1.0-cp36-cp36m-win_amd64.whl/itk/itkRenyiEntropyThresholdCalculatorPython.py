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
    from . import _itkRenyiEntropyThresholdCalculatorPython
else:
    import _itkRenyiEntropyThresholdCalculatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkRenyiEntropyThresholdCalculatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkRenyiEntropyThresholdCalculatorPython.SWIG_PyStaticMethod_New

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


import itkHistogramThresholdCalculatorPython
import ITKCommonBasePython
import pyBasePython
import itkHistogramPython
import itkArrayPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkSamplePython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import itkSimpleDataObjectDecoratorPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkCovariantVectorPython

def itkRenyiEntropyThresholdCalculatorHFD_New():
  return itkRenyiEntropyThresholdCalculatorHFD.New()


def itkRenyiEntropyThresholdCalculatorHDD_New():
  return itkRenyiEntropyThresholdCalculatorHDD.New()


def itkRenyiEntropyThresholdCalculatorHFF_New():
  return itkRenyiEntropyThresholdCalculatorHFF.New()


def itkRenyiEntropyThresholdCalculatorHDF_New():
  return itkRenyiEntropyThresholdCalculatorHDF.New()


def itkRenyiEntropyThresholdCalculatorHFUS_New():
  return itkRenyiEntropyThresholdCalculatorHFUS.New()


def itkRenyiEntropyThresholdCalculatorHDUS_New():
  return itkRenyiEntropyThresholdCalculatorHDUS.New()


def itkRenyiEntropyThresholdCalculatorHFUC_New():
  return itkRenyiEntropyThresholdCalculatorHFUC.New()


def itkRenyiEntropyThresholdCalculatorHDUC_New():
  return itkRenyiEntropyThresholdCalculatorHDUC.New()


def itkRenyiEntropyThresholdCalculatorHFSS_New():
  return itkRenyiEntropyThresholdCalculatorHFSS.New()


def itkRenyiEntropyThresholdCalculatorHDSS_New():
  return itkRenyiEntropyThresholdCalculatorHDSS.New()

class itkRenyiEntropyThresholdCalculatorHDD(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD):
    r"""Proxy of C++ itkRenyiEntropyThresholdCalculatorHDD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDD___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDD_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHDD
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDD_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHDD

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHDD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHDD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHDD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRenyiEntropyThresholdCalculatorHDD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHDD in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDD_swigregister(itkRenyiEntropyThresholdCalculatorHDD)
itkRenyiEntropyThresholdCalculatorHDD___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDD___New_orig__
itkRenyiEntropyThresholdCalculatorHDD_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDD_cast

class itkRenyiEntropyThresholdCalculatorHDF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    r"""Proxy of C++ itkRenyiEntropyThresholdCalculatorHDF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDF___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDF_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHDF
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDF_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHDF

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHDF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHDF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRenyiEntropyThresholdCalculatorHDF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHDF in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDF_swigregister(itkRenyiEntropyThresholdCalculatorHDF)
itkRenyiEntropyThresholdCalculatorHDF___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDF___New_orig__
itkRenyiEntropyThresholdCalculatorHDF_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDF_cast

class itkRenyiEntropyThresholdCalculatorHDSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    r"""Proxy of C++ itkRenyiEntropyThresholdCalculatorHDSS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDSS___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDSS_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHDSS
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDSS_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHDSS

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHDSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHDSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRenyiEntropyThresholdCalculatorHDSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHDSS in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDSS_swigregister(itkRenyiEntropyThresholdCalculatorHDSS)
itkRenyiEntropyThresholdCalculatorHDSS___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDSS___New_orig__
itkRenyiEntropyThresholdCalculatorHDSS_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDSS_cast

class itkRenyiEntropyThresholdCalculatorHDUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    r"""Proxy of C++ itkRenyiEntropyThresholdCalculatorHDUC class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUC___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUC_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHDUC
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUC_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHDUC

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHDUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHDUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRenyiEntropyThresholdCalculatorHDUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHDUC in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUC_swigregister(itkRenyiEntropyThresholdCalculatorHDUC)
itkRenyiEntropyThresholdCalculatorHDUC___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUC___New_orig__
itkRenyiEntropyThresholdCalculatorHDUC_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUC_cast

class itkRenyiEntropyThresholdCalculatorHDUS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS):
    r"""Proxy of C++ itkRenyiEntropyThresholdCalculatorHDUS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUS___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUS_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHDUS
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUS_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHDUS

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHDUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHDUS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHDUS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRenyiEntropyThresholdCalculatorHDUS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHDUS in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUS_swigregister(itkRenyiEntropyThresholdCalculatorHDUS)
itkRenyiEntropyThresholdCalculatorHDUS___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUS___New_orig__
itkRenyiEntropyThresholdCalculatorHDUS_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUS_cast

class itkRenyiEntropyThresholdCalculatorHFD(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD):
    r"""Proxy of C++ itkRenyiEntropyThresholdCalculatorHFD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFD___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFD_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHFD
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFD_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHFD

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHFD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHFD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHFD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRenyiEntropyThresholdCalculatorHFD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHFD in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFD_swigregister(itkRenyiEntropyThresholdCalculatorHFD)
itkRenyiEntropyThresholdCalculatorHFD___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFD___New_orig__
itkRenyiEntropyThresholdCalculatorHFD_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFD_cast

class itkRenyiEntropyThresholdCalculatorHFF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    r"""Proxy of C++ itkRenyiEntropyThresholdCalculatorHFF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFF___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFF_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHFF
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFF_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHFF

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHFF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHFF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRenyiEntropyThresholdCalculatorHFF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHFF in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFF_swigregister(itkRenyiEntropyThresholdCalculatorHFF)
itkRenyiEntropyThresholdCalculatorHFF___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFF___New_orig__
itkRenyiEntropyThresholdCalculatorHFF_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFF_cast

class itkRenyiEntropyThresholdCalculatorHFSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    r"""Proxy of C++ itkRenyiEntropyThresholdCalculatorHFSS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFSS___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFSS_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHFSS
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFSS_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHFSS

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHFSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHFSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRenyiEntropyThresholdCalculatorHFSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHFSS in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFSS_swigregister(itkRenyiEntropyThresholdCalculatorHFSS)
itkRenyiEntropyThresholdCalculatorHFSS___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFSS___New_orig__
itkRenyiEntropyThresholdCalculatorHFSS_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFSS_cast

class itkRenyiEntropyThresholdCalculatorHFUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    r"""Proxy of C++ itkRenyiEntropyThresholdCalculatorHFUC class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUC___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUC_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHFUC
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUC_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHFUC

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHFUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHFUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRenyiEntropyThresholdCalculatorHFUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHFUC in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUC_swigregister(itkRenyiEntropyThresholdCalculatorHFUC)
itkRenyiEntropyThresholdCalculatorHFUC___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUC___New_orig__
itkRenyiEntropyThresholdCalculatorHFUC_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUC_cast

class itkRenyiEntropyThresholdCalculatorHFUS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS):
    r"""Proxy of C++ itkRenyiEntropyThresholdCalculatorHFUS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUS___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUS_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHFUS
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUS_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHFUS

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHFUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHFUS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHFUS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRenyiEntropyThresholdCalculatorHFUS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHFUS in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUS_swigregister(itkRenyiEntropyThresholdCalculatorHFUS)
itkRenyiEntropyThresholdCalculatorHFUS___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUS___New_orig__
itkRenyiEntropyThresholdCalculatorHFUS_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUS_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def renyi_entropy_threshold_calculator(*args, **kwargs):
    """Procedural interface for RenyiEntropyThresholdCalculator"""
    import itk
    instance = itk.RenyiEntropyThresholdCalculator.New(*args, **kwargs)
    return instance.__internal_call__()

def renyi_entropy_threshold_calculator_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.RenyiEntropyThresholdCalculator, itkTemplate.itkTemplate):
        filter_object = itk.RenyiEntropyThresholdCalculator.values()[0]
    else:
        filter_object = itk.RenyiEntropyThresholdCalculator

    renyi_entropy_threshold_calculator.__doc__ = filter_object.__doc__
    renyi_entropy_threshold_calculator.__doc__ += "\n Args are Input(s) to the filter.\n"
    renyi_entropy_threshold_calculator.__doc__ += "Available Keyword Arguments:\n"
    renyi_entropy_threshold_calculator.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



