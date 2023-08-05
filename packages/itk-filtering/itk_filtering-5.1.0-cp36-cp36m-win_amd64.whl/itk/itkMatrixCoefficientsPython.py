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
    from . import _itkMatrixCoefficientsPython
else:
    import _itkMatrixCoefficientsPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMatrixCoefficientsPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMatrixCoefficientsPython.SWIG_PyStaticMethod_New

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


import itkQuadEdgeMeshBasePython
import itkQuadEdgeCellTraitsInfoPython
import ITKCommonBasePython
import pyBasePython
import itkQuadEdgeMeshPointPython
import itkGeometricalQuadEdgePython
import itkQuadEdgePython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkVectorPython
import itkMapContainerPython
import itkImagePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkSizePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkIndexPython
import itkOffsetPython
import itkImageRegionPython
import itkQuadEdgeMeshLineCellPython
import itkArrayPython
class itkMatrixCoefficientsQEMD2(object):
    r"""Proxy of C++ itkMatrixCoefficientsQEMD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkMatrixCoefficientsQEMD2
    __call__ = _swig_new_instance_method(_itkMatrixCoefficientsPython.itkMatrixCoefficientsQEMD2___call__)

# Register itkMatrixCoefficientsQEMD2 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkMatrixCoefficientsQEMD2_swigregister(itkMatrixCoefficientsQEMD2)

class itkMatrixCoefficientsQEMD3(object):
    r"""Proxy of C++ itkMatrixCoefficientsQEMD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkMatrixCoefficientsQEMD3
    __call__ = _swig_new_instance_method(_itkMatrixCoefficientsPython.itkMatrixCoefficientsQEMD3___call__)

# Register itkMatrixCoefficientsQEMD3 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkMatrixCoefficientsQEMD3_swigregister(itkMatrixCoefficientsQEMD3)

class itkOnesMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    r"""Proxy of C++ itkOnesMatrixCoefficientsQEMD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(itkOnesMatrixCoefficientsQEMD2 self) -> itkOnesMatrixCoefficientsQEMD2
        __init__(itkOnesMatrixCoefficientsQEMD2 self, itkOnesMatrixCoefficientsQEMD2 arg0) -> itkOnesMatrixCoefficientsQEMD2
        """
        _itkMatrixCoefficientsPython.itkOnesMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkOnesMatrixCoefficientsQEMD2(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkOnesMatrixCoefficientsQEMD2

# Register itkOnesMatrixCoefficientsQEMD2 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkOnesMatrixCoefficientsQEMD2_swigregister(itkOnesMatrixCoefficientsQEMD2)

class itkOnesMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    r"""Proxy of C++ itkOnesMatrixCoefficientsQEMD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(itkOnesMatrixCoefficientsQEMD3 self) -> itkOnesMatrixCoefficientsQEMD3
        __init__(itkOnesMatrixCoefficientsQEMD3 self, itkOnesMatrixCoefficientsQEMD3 arg0) -> itkOnesMatrixCoefficientsQEMD3
        """
        _itkMatrixCoefficientsPython.itkOnesMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkOnesMatrixCoefficientsQEMD3(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkOnesMatrixCoefficientsQEMD3

# Register itkOnesMatrixCoefficientsQEMD3 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkOnesMatrixCoefficientsQEMD3_swigregister(itkOnesMatrixCoefficientsQEMD3)

class itkAuthalicMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    r"""Proxy of C++ itkAuthalicMatrixCoefficientsQEMD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(itkAuthalicMatrixCoefficientsQEMD2 self) -> itkAuthalicMatrixCoefficientsQEMD2
        __init__(itkAuthalicMatrixCoefficientsQEMD2 self, itkAuthalicMatrixCoefficientsQEMD2 arg0) -> itkAuthalicMatrixCoefficientsQEMD2
        """
        _itkMatrixCoefficientsPython.itkAuthalicMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkAuthalicMatrixCoefficientsQEMD2(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkAuthalicMatrixCoefficientsQEMD2

# Register itkAuthalicMatrixCoefficientsQEMD2 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkAuthalicMatrixCoefficientsQEMD2_swigregister(itkAuthalicMatrixCoefficientsQEMD2)

class itkAuthalicMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    r"""Proxy of C++ itkAuthalicMatrixCoefficientsQEMD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(itkAuthalicMatrixCoefficientsQEMD3 self) -> itkAuthalicMatrixCoefficientsQEMD3
        __init__(itkAuthalicMatrixCoefficientsQEMD3 self, itkAuthalicMatrixCoefficientsQEMD3 arg0) -> itkAuthalicMatrixCoefficientsQEMD3
        """
        _itkMatrixCoefficientsPython.itkAuthalicMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkAuthalicMatrixCoefficientsQEMD3(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkAuthalicMatrixCoefficientsQEMD3

# Register itkAuthalicMatrixCoefficientsQEMD3 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkAuthalicMatrixCoefficientsQEMD3_swigregister(itkAuthalicMatrixCoefficientsQEMD3)

class itkConformalMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    r"""Proxy of C++ itkConformalMatrixCoefficientsQEMD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(itkConformalMatrixCoefficientsQEMD2 self) -> itkConformalMatrixCoefficientsQEMD2
        __init__(itkConformalMatrixCoefficientsQEMD2 self, itkConformalMatrixCoefficientsQEMD2 arg0) -> itkConformalMatrixCoefficientsQEMD2
        """
        _itkMatrixCoefficientsPython.itkConformalMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkConformalMatrixCoefficientsQEMD2(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkConformalMatrixCoefficientsQEMD2

# Register itkConformalMatrixCoefficientsQEMD2 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkConformalMatrixCoefficientsQEMD2_swigregister(itkConformalMatrixCoefficientsQEMD2)

class itkConformalMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    r"""Proxy of C++ itkConformalMatrixCoefficientsQEMD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(itkConformalMatrixCoefficientsQEMD3 self) -> itkConformalMatrixCoefficientsQEMD3
        __init__(itkConformalMatrixCoefficientsQEMD3 self, itkConformalMatrixCoefficientsQEMD3 arg0) -> itkConformalMatrixCoefficientsQEMD3
        """
        _itkMatrixCoefficientsPython.itkConformalMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkConformalMatrixCoefficientsQEMD3(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkConformalMatrixCoefficientsQEMD3

# Register itkConformalMatrixCoefficientsQEMD3 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkConformalMatrixCoefficientsQEMD3_swigregister(itkConformalMatrixCoefficientsQEMD3)

class itkHarmonicMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    r"""Proxy of C++ itkHarmonicMatrixCoefficientsQEMD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(itkHarmonicMatrixCoefficientsQEMD2 self) -> itkHarmonicMatrixCoefficientsQEMD2
        __init__(itkHarmonicMatrixCoefficientsQEMD2 self, itkHarmonicMatrixCoefficientsQEMD2 arg0) -> itkHarmonicMatrixCoefficientsQEMD2
        """
        _itkMatrixCoefficientsPython.itkHarmonicMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkHarmonicMatrixCoefficientsQEMD2(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkHarmonicMatrixCoefficientsQEMD2

# Register itkHarmonicMatrixCoefficientsQEMD2 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkHarmonicMatrixCoefficientsQEMD2_swigregister(itkHarmonicMatrixCoefficientsQEMD2)

class itkHarmonicMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    r"""Proxy of C++ itkHarmonicMatrixCoefficientsQEMD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(itkHarmonicMatrixCoefficientsQEMD3 self) -> itkHarmonicMatrixCoefficientsQEMD3
        __init__(itkHarmonicMatrixCoefficientsQEMD3 self, itkHarmonicMatrixCoefficientsQEMD3 arg0) -> itkHarmonicMatrixCoefficientsQEMD3
        """
        _itkMatrixCoefficientsPython.itkHarmonicMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkHarmonicMatrixCoefficientsQEMD3(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkHarmonicMatrixCoefficientsQEMD3

# Register itkHarmonicMatrixCoefficientsQEMD3 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkHarmonicMatrixCoefficientsQEMD3_swigregister(itkHarmonicMatrixCoefficientsQEMD3)

class itkIntrinsicMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    r"""Proxy of C++ itkIntrinsicMatrixCoefficientsQEMD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(itkIntrinsicMatrixCoefficientsQEMD2 self, float const & iLambda) -> itkIntrinsicMatrixCoefficientsQEMD2
        __init__(itkIntrinsicMatrixCoefficientsQEMD2 self, itkIntrinsicMatrixCoefficientsQEMD2 arg0) -> itkIntrinsicMatrixCoefficientsQEMD2
        """
        _itkMatrixCoefficientsPython.itkIntrinsicMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkIntrinsicMatrixCoefficientsQEMD2(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkIntrinsicMatrixCoefficientsQEMD2

# Register itkIntrinsicMatrixCoefficientsQEMD2 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkIntrinsicMatrixCoefficientsQEMD2_swigregister(itkIntrinsicMatrixCoefficientsQEMD2)

class itkIntrinsicMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    r"""Proxy of C++ itkIntrinsicMatrixCoefficientsQEMD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(itkIntrinsicMatrixCoefficientsQEMD3 self, float const & iLambda) -> itkIntrinsicMatrixCoefficientsQEMD3
        __init__(itkIntrinsicMatrixCoefficientsQEMD3 self, itkIntrinsicMatrixCoefficientsQEMD3 arg0) -> itkIntrinsicMatrixCoefficientsQEMD3
        """
        _itkMatrixCoefficientsPython.itkIntrinsicMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkIntrinsicMatrixCoefficientsQEMD3(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkIntrinsicMatrixCoefficientsQEMD3

# Register itkIntrinsicMatrixCoefficientsQEMD3 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkIntrinsicMatrixCoefficientsQEMD3_swigregister(itkIntrinsicMatrixCoefficientsQEMD3)

class itkInverseEuclideanDistanceMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    r"""Proxy of C++ itkInverseEuclideanDistanceMatrixCoefficientsQEMD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(itkInverseEuclideanDistanceMatrixCoefficientsQEMD2 self) -> itkInverseEuclideanDistanceMatrixCoefficientsQEMD2
        __init__(itkInverseEuclideanDistanceMatrixCoefficientsQEMD2 self, itkInverseEuclideanDistanceMatrixCoefficientsQEMD2 arg0) -> itkInverseEuclideanDistanceMatrixCoefficientsQEMD2
        """
        _itkMatrixCoefficientsPython.itkInverseEuclideanDistanceMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkInverseEuclideanDistanceMatrixCoefficientsQEMD2(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkInverseEuclideanDistanceMatrixCoefficientsQEMD2

# Register itkInverseEuclideanDistanceMatrixCoefficientsQEMD2 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkInverseEuclideanDistanceMatrixCoefficientsQEMD2_swigregister(itkInverseEuclideanDistanceMatrixCoefficientsQEMD2)

class itkInverseEuclideanDistanceMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    r"""Proxy of C++ itkInverseEuclideanDistanceMatrixCoefficientsQEMD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(itkInverseEuclideanDistanceMatrixCoefficientsQEMD3 self) -> itkInverseEuclideanDistanceMatrixCoefficientsQEMD3
        __init__(itkInverseEuclideanDistanceMatrixCoefficientsQEMD3 self, itkInverseEuclideanDistanceMatrixCoefficientsQEMD3 arg0) -> itkInverseEuclideanDistanceMatrixCoefficientsQEMD3
        """
        _itkMatrixCoefficientsPython.itkInverseEuclideanDistanceMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkInverseEuclideanDistanceMatrixCoefficientsQEMD3(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkInverseEuclideanDistanceMatrixCoefficientsQEMD3

# Register itkInverseEuclideanDistanceMatrixCoefficientsQEMD3 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkInverseEuclideanDistanceMatrixCoefficientsQEMD3_swigregister(itkInverseEuclideanDistanceMatrixCoefficientsQEMD3)



