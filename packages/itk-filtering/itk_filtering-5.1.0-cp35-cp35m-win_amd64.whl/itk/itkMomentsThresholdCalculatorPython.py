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
    from . import _itkMomentsThresholdCalculatorPython
else:
    import _itkMomentsThresholdCalculatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMomentsThresholdCalculatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMomentsThresholdCalculatorPython.SWIG_PyStaticMethod_New

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

def itkMomentsThresholdCalculatorHFD_New():
  return itkMomentsThresholdCalculatorHFD.New()


def itkMomentsThresholdCalculatorHDD_New():
  return itkMomentsThresholdCalculatorHDD.New()


def itkMomentsThresholdCalculatorHFF_New():
  return itkMomentsThresholdCalculatorHFF.New()


def itkMomentsThresholdCalculatorHDF_New():
  return itkMomentsThresholdCalculatorHDF.New()


def itkMomentsThresholdCalculatorHFUS_New():
  return itkMomentsThresholdCalculatorHFUS.New()


def itkMomentsThresholdCalculatorHDUS_New():
  return itkMomentsThresholdCalculatorHDUS.New()


def itkMomentsThresholdCalculatorHFUC_New():
  return itkMomentsThresholdCalculatorHFUC.New()


def itkMomentsThresholdCalculatorHDUC_New():
  return itkMomentsThresholdCalculatorHDUC.New()


def itkMomentsThresholdCalculatorHFSS_New():
  return itkMomentsThresholdCalculatorHFSS.New()


def itkMomentsThresholdCalculatorHDSS_New():
  return itkMomentsThresholdCalculatorHDSS.New()

class itkMomentsThresholdCalculatorHDD(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD):
    r"""Proxy of C++ itkMomentsThresholdCalculatorHDD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDD___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDD_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHDD
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDD_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHDD

        Create a new object of the class itkMomentsThresholdCalculatorHDD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHDD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHDD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMomentsThresholdCalculatorHDD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHDD in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDD_swigregister(itkMomentsThresholdCalculatorHDD)
itkMomentsThresholdCalculatorHDD___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDD___New_orig__
itkMomentsThresholdCalculatorHDD_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDD_cast

class itkMomentsThresholdCalculatorHDF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    r"""Proxy of C++ itkMomentsThresholdCalculatorHDF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHDF
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHDF

        Create a new object of the class itkMomentsThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHDF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHDF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMomentsThresholdCalculatorHDF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHDF in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF_swigregister(itkMomentsThresholdCalculatorHDF)
itkMomentsThresholdCalculatorHDF___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF___New_orig__
itkMomentsThresholdCalculatorHDF_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF_cast

class itkMomentsThresholdCalculatorHDSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    r"""Proxy of C++ itkMomentsThresholdCalculatorHDSS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHDSS
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHDSS

        Create a new object of the class itkMomentsThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHDSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHDSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMomentsThresholdCalculatorHDSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHDSS in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS_swigregister(itkMomentsThresholdCalculatorHDSS)
itkMomentsThresholdCalculatorHDSS___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS___New_orig__
itkMomentsThresholdCalculatorHDSS_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS_cast

class itkMomentsThresholdCalculatorHDUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    r"""Proxy of C++ itkMomentsThresholdCalculatorHDUC class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHDUC
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHDUC

        Create a new object of the class itkMomentsThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHDUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHDUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMomentsThresholdCalculatorHDUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHDUC in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC_swigregister(itkMomentsThresholdCalculatorHDUC)
itkMomentsThresholdCalculatorHDUC___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC___New_orig__
itkMomentsThresholdCalculatorHDUC_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC_cast

class itkMomentsThresholdCalculatorHDUS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS):
    r"""Proxy of C++ itkMomentsThresholdCalculatorHDUS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUS___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUS_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHDUS
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUS_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHDUS

        Create a new object of the class itkMomentsThresholdCalculatorHDUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHDUS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHDUS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMomentsThresholdCalculatorHDUS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHDUS in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUS_swigregister(itkMomentsThresholdCalculatorHDUS)
itkMomentsThresholdCalculatorHDUS___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUS___New_orig__
itkMomentsThresholdCalculatorHDUS_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUS_cast

class itkMomentsThresholdCalculatorHFD(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD):
    r"""Proxy of C++ itkMomentsThresholdCalculatorHFD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFD___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFD_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHFD
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFD_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHFD

        Create a new object of the class itkMomentsThresholdCalculatorHFD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHFD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHFD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMomentsThresholdCalculatorHFD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHFD in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFD_swigregister(itkMomentsThresholdCalculatorHFD)
itkMomentsThresholdCalculatorHFD___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFD___New_orig__
itkMomentsThresholdCalculatorHFD_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFD_cast

class itkMomentsThresholdCalculatorHFF(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    r"""Proxy of C++ itkMomentsThresholdCalculatorHFF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHFF
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHFF

        Create a new object of the class itkMomentsThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHFF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHFF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMomentsThresholdCalculatorHFF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHFF in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF_swigregister(itkMomentsThresholdCalculatorHFF)
itkMomentsThresholdCalculatorHFF___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF___New_orig__
itkMomentsThresholdCalculatorHFF_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF_cast

class itkMomentsThresholdCalculatorHFSS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    r"""Proxy of C++ itkMomentsThresholdCalculatorHFSS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHFSS
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHFSS

        Create a new object of the class itkMomentsThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHFSS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHFSS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMomentsThresholdCalculatorHFSS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHFSS in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS_swigregister(itkMomentsThresholdCalculatorHFSS)
itkMomentsThresholdCalculatorHFSS___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS___New_orig__
itkMomentsThresholdCalculatorHFSS_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS_cast

class itkMomentsThresholdCalculatorHFUC(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    r"""Proxy of C++ itkMomentsThresholdCalculatorHFUC class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHFUC
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHFUC

        Create a new object of the class itkMomentsThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHFUC.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHFUC.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMomentsThresholdCalculatorHFUC.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHFUC in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC_swigregister(itkMomentsThresholdCalculatorHFUC)
itkMomentsThresholdCalculatorHFUC___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC___New_orig__
itkMomentsThresholdCalculatorHFUC_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC_cast

class itkMomentsThresholdCalculatorHFUS(itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS):
    r"""Proxy of C++ itkMomentsThresholdCalculatorHFUS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUS___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUS_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHFUS
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUS_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHFUS

        Create a new object of the class itkMomentsThresholdCalculatorHFUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHFUS.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHFUS.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMomentsThresholdCalculatorHFUS.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHFUS in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUS_swigregister(itkMomentsThresholdCalculatorHFUS)
itkMomentsThresholdCalculatorHFUS___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUS___New_orig__
itkMomentsThresholdCalculatorHFUS_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUS_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def moments_threshold_calculator(*args, **kwargs):
    """Procedural interface for MomentsThresholdCalculator"""
    import itk
    instance = itk.MomentsThresholdCalculator.New(*args, **kwargs)
    return instance.__internal_call__()

def moments_threshold_calculator_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.MomentsThresholdCalculator, itkTemplate.itkTemplate):
        filter_object = itk.MomentsThresholdCalculator.values()[0]
    else:
        filter_object = itk.MomentsThresholdCalculator

    moments_threshold_calculator.__doc__ = filter_object.__doc__
    moments_threshold_calculator.__doc__ += "\n Args are Input(s) to the filter.\n"
    moments_threshold_calculator.__doc__ += "Available Keyword Arguments:\n"
    moments_threshold_calculator.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



