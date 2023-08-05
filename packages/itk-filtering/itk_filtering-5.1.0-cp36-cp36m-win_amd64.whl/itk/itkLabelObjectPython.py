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
    from . import _itkLabelObjectPython
else:
    import _itkLabelObjectPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLabelObjectPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLabelObjectPython.SWIG_PyStaticMethod_New

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


import itkLabelObjectLinePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import ITKCommonBasePython

def itkLabelObjectUL3_New():
  return itkLabelObjectUL3.New()


def itkLabelObjectUL2_New():
  return itkLabelObjectUL2.New()

class itkLabelObjectUL2(ITKCommonBasePython.itkLightObject):
    r"""Proxy of C++ itkLabelObjectUL2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_Clone)
    GetAttributeFromName = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL2_GetAttributeFromName)
    GetNameFromAttribute = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL2_GetNameFromAttribute)
    GetLabel = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_GetLabel)
    SetLabel = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_SetLabel)
    HasIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_HasIndex)
    AddIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_AddIndex)
    RemoveIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_RemoveIndex)
    AddLine = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_AddLine)
    GetNumberOfLines = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_GetNumberOfLines)
    GetLine = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_GetLine)
    Size = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_Size)
    Empty = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_Empty)
    Clear = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_Clear)
    GetIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_GetIndex)
    Optimize = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_Optimize)
    Shift = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_Shift)
    __swig_destroy__ = _itkLabelObjectPython.delete_itkLabelObjectUL2
    cast = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelObjectUL2

        Create a new object of the class itkLabelObjectUL2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelObjectUL2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelObjectUL2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelObjectUL2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelObjectUL2 in _itkLabelObjectPython:
_itkLabelObjectPython.itkLabelObjectUL2_swigregister(itkLabelObjectUL2)
itkLabelObjectUL2___New_orig__ = _itkLabelObjectPython.itkLabelObjectUL2___New_orig__
itkLabelObjectUL2_GetAttributeFromName = _itkLabelObjectPython.itkLabelObjectUL2_GetAttributeFromName
itkLabelObjectUL2_GetNameFromAttribute = _itkLabelObjectPython.itkLabelObjectUL2_GetNameFromAttribute
itkLabelObjectUL2_cast = _itkLabelObjectPython.itkLabelObjectUL2_cast

class itkLabelObjectUL3(ITKCommonBasePython.itkLightObject):
    r"""Proxy of C++ itkLabelObjectUL3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_Clone)
    GetAttributeFromName = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL3_GetAttributeFromName)
    GetNameFromAttribute = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL3_GetNameFromAttribute)
    GetLabel = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_GetLabel)
    SetLabel = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_SetLabel)
    HasIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_HasIndex)
    AddIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_AddIndex)
    RemoveIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_RemoveIndex)
    AddLine = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_AddLine)
    GetNumberOfLines = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_GetNumberOfLines)
    GetLine = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_GetLine)
    Size = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_Size)
    Empty = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_Empty)
    Clear = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_Clear)
    GetIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_GetIndex)
    Optimize = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_Optimize)
    Shift = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_Shift)
    __swig_destroy__ = _itkLabelObjectPython.delete_itkLabelObjectUL3
    cast = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelObjectUL3

        Create a new object of the class itkLabelObjectUL3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelObjectUL3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelObjectUL3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelObjectUL3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelObjectUL3 in _itkLabelObjectPython:
_itkLabelObjectPython.itkLabelObjectUL3_swigregister(itkLabelObjectUL3)
itkLabelObjectUL3___New_orig__ = _itkLabelObjectPython.itkLabelObjectUL3___New_orig__
itkLabelObjectUL3_GetAttributeFromName = _itkLabelObjectPython.itkLabelObjectUL3_GetAttributeFromName
itkLabelObjectUL3_GetNameFromAttribute = _itkLabelObjectPython.itkLabelObjectUL3_GetNameFromAttribute
itkLabelObjectUL3_cast = _itkLabelObjectPython.itkLabelObjectUL3_cast



