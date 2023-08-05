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
    from . import _itkStatisticsLabelObjectPython
else:
    import _itkStatisticsLabelObjectPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkStatisticsLabelObjectPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkStatisticsLabelObjectPython.SWIG_PyStaticMethod_New

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


import itkAffineTransformPython
import ITKCommonBasePython
import pyBasePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkMatrixPython
import itkPointPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkArray2DPython
import itkArrayPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkOptimizerParametersPython
import itkMatrixOffsetTransformBasePython
import itkHistogramPython
import itkSamplePython
import itkShapeLabelObjectPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkLabelObjectPython
import itkLabelObjectLinePython

def itkStatisticsLabelObjectUL3_New():
  return itkStatisticsLabelObjectUL3.New()


def itkStatisticsLabelObjectUL2_New():
  return itkStatisticsLabelObjectUL2.New()

class mapitkStatisticsLabelObjectUL2(object):
    r"""Proxy of C++ std::map< unsigned long,itkStatisticsLabelObjectUL2_Pointer,std::less< unsigned long > > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2___nonzero__)
    __bool__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2___bool__)
    __len__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2___len__)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()
    __getitem__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2___getitem__)
    __delitem__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2___delitem__)
    has_key = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_has_key)
    keys = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_keys)
    values = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_values)
    items = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_items)
    __contains__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2___contains__)
    key_iterator = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_key_iterator)
    value_iterator = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_value_iterator)
    __setitem__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2___setitem__)
    asdict = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_asdict)

    def __init__(self, *args):
        r"""
        __init__(mapitkStatisticsLabelObjectUL2 self, std::less< unsigned long > const & other) -> mapitkStatisticsLabelObjectUL2
        __init__(mapitkStatisticsLabelObjectUL2 self) -> mapitkStatisticsLabelObjectUL2
        __init__(mapitkStatisticsLabelObjectUL2 self, mapitkStatisticsLabelObjectUL2 other) -> mapitkStatisticsLabelObjectUL2
        """
        _itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_swiginit(self, _itkStatisticsLabelObjectPython.new_mapitkStatisticsLabelObjectUL2(*args))
    empty = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_empty)
    size = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_size)
    swap = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_swap)
    begin = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_begin)
    end = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_end)
    rbegin = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_rbegin)
    rend = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_rend)
    clear = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_clear)
    get_allocator = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_get_allocator)
    count = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_count)
    erase = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_erase)
    find = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_find)
    lower_bound = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_lower_bound)
    upper_bound = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_upper_bound)
    __swig_destroy__ = _itkStatisticsLabelObjectPython.delete_mapitkStatisticsLabelObjectUL2

# Register mapitkStatisticsLabelObjectUL2 in _itkStatisticsLabelObjectPython:
_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL2_swigregister(mapitkStatisticsLabelObjectUL2)

class vectoritkStatisticsLabelObjectUL2(object):
    r"""Proxy of C++ std::vector< itkStatisticsLabelObjectUL2_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2___nonzero__)
    __bool__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2___bool__)
    __len__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2___len__)
    __getslice__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2___getslice__)
    __setslice__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2___setslice__)
    __delslice__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2___delslice__)
    __delitem__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2___delitem__)
    __getitem__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2___getitem__)
    __setitem__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2___setitem__)
    pop = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_pop)
    append = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_append)
    empty = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_empty)
    size = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_size)
    swap = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_swap)
    begin = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_begin)
    end = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_end)
    rbegin = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_rbegin)
    rend = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_rend)
    clear = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_clear)
    get_allocator = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_get_allocator)
    pop_back = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_pop_back)
    erase = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_erase)

    def __init__(self, *args):
        r"""
        __init__(vectoritkStatisticsLabelObjectUL2 self) -> vectoritkStatisticsLabelObjectUL2
        __init__(vectoritkStatisticsLabelObjectUL2 self, vectoritkStatisticsLabelObjectUL2 other) -> vectoritkStatisticsLabelObjectUL2
        __init__(vectoritkStatisticsLabelObjectUL2 self, std::vector< itkStatisticsLabelObjectUL2_Pointer >::size_type size) -> vectoritkStatisticsLabelObjectUL2
        __init__(vectoritkStatisticsLabelObjectUL2 self, std::vector< itkStatisticsLabelObjectUL2_Pointer >::size_type size, std::vector< itkStatisticsLabelObjectUL2_Pointer >::value_type const & value) -> vectoritkStatisticsLabelObjectUL2
        """
        _itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_swiginit(self, _itkStatisticsLabelObjectPython.new_vectoritkStatisticsLabelObjectUL2(*args))
    push_back = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_push_back)
    front = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_front)
    back = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_back)
    assign = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_assign)
    resize = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_resize)
    insert = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_insert)
    reserve = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_reserve)
    capacity = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_capacity)
    __swig_destroy__ = _itkStatisticsLabelObjectPython.delete_vectoritkStatisticsLabelObjectUL2

# Register vectoritkStatisticsLabelObjectUL2 in _itkStatisticsLabelObjectPython:
_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL2_swigregister(vectoritkStatisticsLabelObjectUL2)

class mapitkStatisticsLabelObjectUL3(object):
    r"""Proxy of C++ std::map< unsigned long,itkStatisticsLabelObjectUL3_Pointer,std::less< unsigned long > > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3___nonzero__)
    __bool__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3___bool__)
    __len__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3___len__)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()
    __getitem__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3___getitem__)
    __delitem__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3___delitem__)
    has_key = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_has_key)
    keys = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_keys)
    values = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_values)
    items = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_items)
    __contains__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3___contains__)
    key_iterator = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_key_iterator)
    value_iterator = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_value_iterator)
    __setitem__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3___setitem__)
    asdict = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_asdict)

    def __init__(self, *args):
        r"""
        __init__(mapitkStatisticsLabelObjectUL3 self, std::less< unsigned long > const & other) -> mapitkStatisticsLabelObjectUL3
        __init__(mapitkStatisticsLabelObjectUL3 self) -> mapitkStatisticsLabelObjectUL3
        __init__(mapitkStatisticsLabelObjectUL3 self, mapitkStatisticsLabelObjectUL3 other) -> mapitkStatisticsLabelObjectUL3
        """
        _itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_swiginit(self, _itkStatisticsLabelObjectPython.new_mapitkStatisticsLabelObjectUL3(*args))
    empty = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_empty)
    size = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_size)
    swap = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_swap)
    begin = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_begin)
    end = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_end)
    rbegin = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_rbegin)
    rend = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_rend)
    clear = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_clear)
    get_allocator = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_get_allocator)
    count = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_count)
    erase = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_erase)
    find = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_find)
    lower_bound = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_lower_bound)
    upper_bound = _swig_new_instance_method(_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_upper_bound)
    __swig_destroy__ = _itkStatisticsLabelObjectPython.delete_mapitkStatisticsLabelObjectUL3

# Register mapitkStatisticsLabelObjectUL3 in _itkStatisticsLabelObjectPython:
_itkStatisticsLabelObjectPython.mapitkStatisticsLabelObjectUL3_swigregister(mapitkStatisticsLabelObjectUL3)

class vectoritkStatisticsLabelObjectUL3(object):
    r"""Proxy of C++ std::vector< itkStatisticsLabelObjectUL3_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3___nonzero__)
    __bool__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3___bool__)
    __len__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3___len__)
    __getslice__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3___getslice__)
    __setslice__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3___setslice__)
    __delslice__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3___delslice__)
    __delitem__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3___delitem__)
    __getitem__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3___getitem__)
    __setitem__ = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3___setitem__)
    pop = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_pop)
    append = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_append)
    empty = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_empty)
    size = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_size)
    swap = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_swap)
    begin = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_begin)
    end = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_end)
    rbegin = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_rbegin)
    rend = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_rend)
    clear = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_clear)
    get_allocator = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_get_allocator)
    pop_back = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_pop_back)
    erase = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_erase)

    def __init__(self, *args):
        r"""
        __init__(vectoritkStatisticsLabelObjectUL3 self) -> vectoritkStatisticsLabelObjectUL3
        __init__(vectoritkStatisticsLabelObjectUL3 self, vectoritkStatisticsLabelObjectUL3 other) -> vectoritkStatisticsLabelObjectUL3
        __init__(vectoritkStatisticsLabelObjectUL3 self, std::vector< itkStatisticsLabelObjectUL3_Pointer >::size_type size) -> vectoritkStatisticsLabelObjectUL3
        __init__(vectoritkStatisticsLabelObjectUL3 self, std::vector< itkStatisticsLabelObjectUL3_Pointer >::size_type size, std::vector< itkStatisticsLabelObjectUL3_Pointer >::value_type const & value) -> vectoritkStatisticsLabelObjectUL3
        """
        _itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_swiginit(self, _itkStatisticsLabelObjectPython.new_vectoritkStatisticsLabelObjectUL3(*args))
    push_back = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_push_back)
    front = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_front)
    back = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_back)
    assign = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_assign)
    resize = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_resize)
    insert = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_insert)
    reserve = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_reserve)
    capacity = _swig_new_instance_method(_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_capacity)
    __swig_destroy__ = _itkStatisticsLabelObjectPython.delete_vectoritkStatisticsLabelObjectUL3

# Register vectoritkStatisticsLabelObjectUL3 in _itkStatisticsLabelObjectPython:
_itkStatisticsLabelObjectPython.vectoritkStatisticsLabelObjectUL3_swigregister(vectoritkStatisticsLabelObjectUL3)

class itkStatisticsLabelObjectUL2(itkShapeLabelObjectPython.itkShapeLabelObjectUL2):
    r"""Proxy of C++ itkStatisticsLabelObjectUL2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2___New_orig__)
    Clone = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_Clone)
    GetAttributeFromName = _swig_new_static_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetAttributeFromName)
    GetNameFromAttribute = _swig_new_static_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetNameFromAttribute)
    GetMinimum = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetMinimum)
    SetMinimum = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetMinimum)
    GetMaximum = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetMaximum)
    SetMaximum = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetMaximum)
    GetMean = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetMean)
    SetMean = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetMean)
    GetSum = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetSum)
    SetSum = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetSum)
    GetStandardDeviation = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetStandardDeviation)
    GetVariance = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetVariance)
    SetVariance = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetVariance)
    GetMedian = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetMedian)
    SetMedian = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetMedian)
    GetMaximumIndex = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetMaximumIndex)
    SetMaximumIndex = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetMaximumIndex)
    GetMinimumIndex = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetMinimumIndex)
    SetMinimumIndex = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetMinimumIndex)
    GetCenterOfGravity = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetCenterOfGravity)
    SetCenterOfGravity = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetCenterOfGravity)
    GetWeightedPrincipalMoments = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetWeightedPrincipalMoments)
    SetWeightedPrincipalMoments = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetWeightedPrincipalMoments)
    GetWeightedPrincipalAxes = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetWeightedPrincipalAxes)
    SetWeightedPrincipalAxes = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetWeightedPrincipalAxes)
    GetSkewness = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetSkewness)
    SetSkewness = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetSkewness)
    GetKurtosis = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetKurtosis)
    SetKurtosis = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetKurtosis)
    GetWeightedElongation = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetWeightedElongation)
    SetWeightedElongation = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetWeightedElongation)
    GetHistogram = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetHistogram)
    SetHistogram = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetHistogram)
    GetWeightedFlatness = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetWeightedFlatness)
    SetWeightedFlatness = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_SetWeightedFlatness)
    GetWeightedPrincipalAxesToPhysicalAxesTransform = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetWeightedPrincipalAxesToPhysicalAxesTransform)
    GetPhysicalAxesToWeightedPrincipalAxesTransform = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetPhysicalAxesToWeightedPrincipalAxesTransform)
    __swig_destroy__ = _itkStatisticsLabelObjectPython.delete_itkStatisticsLabelObjectUL2
    cast = _swig_new_static_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsLabelObjectUL2

        Create a new object of the class itkStatisticsLabelObjectUL2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsLabelObjectUL2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkStatisticsLabelObjectUL2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkStatisticsLabelObjectUL2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStatisticsLabelObjectUL2 in _itkStatisticsLabelObjectPython:
_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_swigregister(itkStatisticsLabelObjectUL2)
itkStatisticsLabelObjectUL2___New_orig__ = _itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2___New_orig__
itkStatisticsLabelObjectUL2_GetAttributeFromName = _itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetAttributeFromName
itkStatisticsLabelObjectUL2_GetNameFromAttribute = _itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_GetNameFromAttribute
itkStatisticsLabelObjectUL2_cast = _itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL2_cast

class itkStatisticsLabelObjectUL3(itkShapeLabelObjectPython.itkShapeLabelObjectUL3):
    r"""Proxy of C++ itkStatisticsLabelObjectUL3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3___New_orig__)
    Clone = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_Clone)
    GetAttributeFromName = _swig_new_static_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetAttributeFromName)
    GetNameFromAttribute = _swig_new_static_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetNameFromAttribute)
    GetMinimum = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetMinimum)
    SetMinimum = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetMinimum)
    GetMaximum = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetMaximum)
    SetMaximum = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetMaximum)
    GetMean = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetMean)
    SetMean = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetMean)
    GetSum = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetSum)
    SetSum = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetSum)
    GetStandardDeviation = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetStandardDeviation)
    SetStandardDeviation = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetStandardDeviation)
    GetVariance = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetVariance)
    SetVariance = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetVariance)
    GetMedian = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetMedian)
    SetMedian = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetMedian)
    GetMaximumIndex = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetMaximumIndex)
    SetMaximumIndex = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetMaximumIndex)
    GetMinimumIndex = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetMinimumIndex)
    SetMinimumIndex = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetMinimumIndex)
    GetCenterOfGravity = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetCenterOfGravity)
    SetCenterOfGravity = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetCenterOfGravity)
    GetWeightedPrincipalMoments = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetWeightedPrincipalMoments)
    SetWeightedPrincipalMoments = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetWeightedPrincipalMoments)
    GetWeightedPrincipalAxes = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetWeightedPrincipalAxes)
    SetWeightedPrincipalAxes = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetWeightedPrincipalAxes)
    GetSkewness = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetSkewness)
    SetSkewness = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetSkewness)
    GetKurtosis = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetKurtosis)
    SetKurtosis = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetKurtosis)
    GetWeightedElongation = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetWeightedElongation)
    SetWeightedElongation = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetWeightedElongation)
    GetHistogram = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetHistogram)
    SetHistogram = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetHistogram)
    GetWeightedFlatness = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetWeightedFlatness)
    SetWeightedFlatness = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_SetWeightedFlatness)
    GetWeightedPrincipalAxesToPhysicalAxesTransform = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetWeightedPrincipalAxesToPhysicalAxesTransform)
    GetPhysicalAxesToWeightedPrincipalAxesTransform = _swig_new_instance_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetPhysicalAxesToWeightedPrincipalAxesTransform)
    __swig_destroy__ = _itkStatisticsLabelObjectPython.delete_itkStatisticsLabelObjectUL3
    cast = _swig_new_static_method(_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsLabelObjectUL3

        Create a new object of the class itkStatisticsLabelObjectUL3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsLabelObjectUL3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkStatisticsLabelObjectUL3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkStatisticsLabelObjectUL3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStatisticsLabelObjectUL3 in _itkStatisticsLabelObjectPython:
_itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_swigregister(itkStatisticsLabelObjectUL3)
itkStatisticsLabelObjectUL3___New_orig__ = _itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3___New_orig__
itkStatisticsLabelObjectUL3_GetAttributeFromName = _itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetAttributeFromName
itkStatisticsLabelObjectUL3_GetNameFromAttribute = _itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_GetNameFromAttribute
itkStatisticsLabelObjectUL3_cast = _itkStatisticsLabelObjectPython.itkStatisticsLabelObjectUL3_cast



