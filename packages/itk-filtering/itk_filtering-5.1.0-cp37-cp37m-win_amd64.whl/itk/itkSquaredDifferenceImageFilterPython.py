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
    from . import _itkSquaredDifferenceImageFilterPython
else:
    import _itkSquaredDifferenceImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSquaredDifferenceImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSquaredDifferenceImageFilterPython.SWIG_PyStaticMethod_New

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
import itkBinaryGeneratorImageFilterPython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkInPlaceImageFilterBPython
import itkImageToImageFilterBPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImagePython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkIndexPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkSimpleDataObjectDecoratorPython
import itkArrayPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython

def itkSquaredDifferenceImageFilterID3ID3ID3_New():
  return itkSquaredDifferenceImageFilterID3ID3ID3.New()


def itkSquaredDifferenceImageFilterID2ID2ID2_New():
  return itkSquaredDifferenceImageFilterID2ID2ID2.New()


def itkSquaredDifferenceImageFilterIF3IF3IF3_New():
  return itkSquaredDifferenceImageFilterIF3IF3IF3.New()


def itkSquaredDifferenceImageFilterIF2IF2IF2_New():
  return itkSquaredDifferenceImageFilterIF2IF2IF2.New()


def itkSquaredDifferenceImageFilterIUS3IUS3IUS3_New():
  return itkSquaredDifferenceImageFilterIUS3IUS3IUS3.New()


def itkSquaredDifferenceImageFilterIUS2IUS2IUS2_New():
  return itkSquaredDifferenceImageFilterIUS2IUS2IUS2.New()


def itkSquaredDifferenceImageFilterIUC3IUC3IUC3_New():
  return itkSquaredDifferenceImageFilterIUC3IUC3IUC3.New()


def itkSquaredDifferenceImageFilterIUC2IUC2IUC2_New():
  return itkSquaredDifferenceImageFilterIUC2IUC2IUC2.New()


def itkSquaredDifferenceImageFilterISS3ISS3ISS3_New():
  return itkSquaredDifferenceImageFilterISS3ISS3ISS3.New()


def itkSquaredDifferenceImageFilterISS2ISS2ISS2_New():
  return itkSquaredDifferenceImageFilterISS2ISS2ISS2.New()

class itkSquaredDifferenceImageFilterID2ID2ID2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID2ID2ID2):
    r"""Proxy of C++ itkSquaredDifferenceImageFilterID2ID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID2ID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID2ID2ID2_Clone)
    Input1ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID2ID2ID2_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID2ID2ID2_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID2ID2ID2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSquaredDifferenceImageFilterPython.delete_itkSquaredDifferenceImageFilterID2ID2ID2
    cast = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID2ID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkSquaredDifferenceImageFilterID2ID2ID2

        Create a new object of the class itkSquaredDifferenceImageFilterID2ID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquaredDifferenceImageFilterID2ID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquaredDifferenceImageFilterID2ID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquaredDifferenceImageFilterID2ID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSquaredDifferenceImageFilterID2ID2ID2 in _itkSquaredDifferenceImageFilterPython:
_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID2ID2ID2_swigregister(itkSquaredDifferenceImageFilterID2ID2ID2)
itkSquaredDifferenceImageFilterID2ID2ID2___New_orig__ = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID2ID2ID2___New_orig__
itkSquaredDifferenceImageFilterID2ID2ID2_cast = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID2ID2ID2_cast

class itkSquaredDifferenceImageFilterID3ID3ID3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID3ID3ID3):
    r"""Proxy of C++ itkSquaredDifferenceImageFilterID3ID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID3ID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID3ID3ID3_Clone)
    Input1ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID3ID3ID3_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID3ID3ID3_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID3ID3ID3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSquaredDifferenceImageFilterPython.delete_itkSquaredDifferenceImageFilterID3ID3ID3
    cast = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID3ID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkSquaredDifferenceImageFilterID3ID3ID3

        Create a new object of the class itkSquaredDifferenceImageFilterID3ID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquaredDifferenceImageFilterID3ID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquaredDifferenceImageFilterID3ID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquaredDifferenceImageFilterID3ID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSquaredDifferenceImageFilterID3ID3ID3 in _itkSquaredDifferenceImageFilterPython:
_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID3ID3ID3_swigregister(itkSquaredDifferenceImageFilterID3ID3ID3)
itkSquaredDifferenceImageFilterID3ID3ID3___New_orig__ = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID3ID3ID3___New_orig__
itkSquaredDifferenceImageFilterID3ID3ID3_cast = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterID3ID3ID3_cast

class itkSquaredDifferenceImageFilterIF2IF2IF2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF2IF2IF2):
    r"""Proxy of C++ itkSquaredDifferenceImageFilterIF2IF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF2IF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF2IF2IF2_Clone)
    Input1ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF2IF2IF2_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF2IF2IF2_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF2IF2IF2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSquaredDifferenceImageFilterPython.delete_itkSquaredDifferenceImageFilterIF2IF2IF2
    cast = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF2IF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkSquaredDifferenceImageFilterIF2IF2IF2

        Create a new object of the class itkSquaredDifferenceImageFilterIF2IF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquaredDifferenceImageFilterIF2IF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquaredDifferenceImageFilterIF2IF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquaredDifferenceImageFilterIF2IF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSquaredDifferenceImageFilterIF2IF2IF2 in _itkSquaredDifferenceImageFilterPython:
_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF2IF2IF2_swigregister(itkSquaredDifferenceImageFilterIF2IF2IF2)
itkSquaredDifferenceImageFilterIF2IF2IF2___New_orig__ = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF2IF2IF2___New_orig__
itkSquaredDifferenceImageFilterIF2IF2IF2_cast = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF2IF2IF2_cast

class itkSquaredDifferenceImageFilterIF3IF3IF3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF3IF3IF3):
    r"""Proxy of C++ itkSquaredDifferenceImageFilterIF3IF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF3IF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF3IF3IF3_Clone)
    Input1ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF3IF3IF3_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF3IF3IF3_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF3IF3IF3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSquaredDifferenceImageFilterPython.delete_itkSquaredDifferenceImageFilterIF3IF3IF3
    cast = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF3IF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkSquaredDifferenceImageFilterIF3IF3IF3

        Create a new object of the class itkSquaredDifferenceImageFilterIF3IF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquaredDifferenceImageFilterIF3IF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquaredDifferenceImageFilterIF3IF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquaredDifferenceImageFilterIF3IF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSquaredDifferenceImageFilterIF3IF3IF3 in _itkSquaredDifferenceImageFilterPython:
_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF3IF3IF3_swigregister(itkSquaredDifferenceImageFilterIF3IF3IF3)
itkSquaredDifferenceImageFilterIF3IF3IF3___New_orig__ = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF3IF3IF3___New_orig__
itkSquaredDifferenceImageFilterIF3IF3IF3_cast = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIF3IF3IF3_cast

class itkSquaredDifferenceImageFilterISS2ISS2ISS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS2ISS2ISS2):
    r"""Proxy of C++ itkSquaredDifferenceImageFilterISS2ISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS2ISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS2ISS2ISS2_Clone)
    Input1ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS2ISS2ISS2_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS2ISS2ISS2_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS2ISS2ISS2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSquaredDifferenceImageFilterPython.delete_itkSquaredDifferenceImageFilterISS2ISS2ISS2
    cast = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS2ISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkSquaredDifferenceImageFilterISS2ISS2ISS2

        Create a new object of the class itkSquaredDifferenceImageFilterISS2ISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquaredDifferenceImageFilterISS2ISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquaredDifferenceImageFilterISS2ISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquaredDifferenceImageFilterISS2ISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSquaredDifferenceImageFilterISS2ISS2ISS2 in _itkSquaredDifferenceImageFilterPython:
_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS2ISS2ISS2_swigregister(itkSquaredDifferenceImageFilterISS2ISS2ISS2)
itkSquaredDifferenceImageFilterISS2ISS2ISS2___New_orig__ = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS2ISS2ISS2___New_orig__
itkSquaredDifferenceImageFilterISS2ISS2ISS2_cast = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS2ISS2ISS2_cast

class itkSquaredDifferenceImageFilterISS3ISS3ISS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS3ISS3ISS3):
    r"""Proxy of C++ itkSquaredDifferenceImageFilterISS3ISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS3ISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS3ISS3ISS3_Clone)
    Input1ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS3ISS3ISS3_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS3ISS3ISS3_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS3ISS3ISS3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSquaredDifferenceImageFilterPython.delete_itkSquaredDifferenceImageFilterISS3ISS3ISS3
    cast = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS3ISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkSquaredDifferenceImageFilterISS3ISS3ISS3

        Create a new object of the class itkSquaredDifferenceImageFilterISS3ISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquaredDifferenceImageFilterISS3ISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquaredDifferenceImageFilterISS3ISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquaredDifferenceImageFilterISS3ISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSquaredDifferenceImageFilterISS3ISS3ISS3 in _itkSquaredDifferenceImageFilterPython:
_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS3ISS3ISS3_swigregister(itkSquaredDifferenceImageFilterISS3ISS3ISS3)
itkSquaredDifferenceImageFilterISS3ISS3ISS3___New_orig__ = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS3ISS3ISS3___New_orig__
itkSquaredDifferenceImageFilterISS3ISS3ISS3_cast = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterISS3ISS3ISS3_cast

class itkSquaredDifferenceImageFilterIUC2IUC2IUC2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC2IUC2IUC2):
    r"""Proxy of C++ itkSquaredDifferenceImageFilterIUC2IUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC2IUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC2IUC2IUC2_Clone)
    Input1ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC2IUC2IUC2_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC2IUC2IUC2_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC2IUC2IUC2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSquaredDifferenceImageFilterPython.delete_itkSquaredDifferenceImageFilterIUC2IUC2IUC2
    cast = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC2IUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkSquaredDifferenceImageFilterIUC2IUC2IUC2

        Create a new object of the class itkSquaredDifferenceImageFilterIUC2IUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquaredDifferenceImageFilterIUC2IUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquaredDifferenceImageFilterIUC2IUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquaredDifferenceImageFilterIUC2IUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSquaredDifferenceImageFilterIUC2IUC2IUC2 in _itkSquaredDifferenceImageFilterPython:
_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC2IUC2IUC2_swigregister(itkSquaredDifferenceImageFilterIUC2IUC2IUC2)
itkSquaredDifferenceImageFilterIUC2IUC2IUC2___New_orig__ = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC2IUC2IUC2___New_orig__
itkSquaredDifferenceImageFilterIUC2IUC2IUC2_cast = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC2IUC2IUC2_cast

class itkSquaredDifferenceImageFilterIUC3IUC3IUC3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC3IUC3IUC3):
    r"""Proxy of C++ itkSquaredDifferenceImageFilterIUC3IUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC3IUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC3IUC3IUC3_Clone)
    Input1ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC3IUC3IUC3_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC3IUC3IUC3_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC3IUC3IUC3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSquaredDifferenceImageFilterPython.delete_itkSquaredDifferenceImageFilterIUC3IUC3IUC3
    cast = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC3IUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkSquaredDifferenceImageFilterIUC3IUC3IUC3

        Create a new object of the class itkSquaredDifferenceImageFilterIUC3IUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquaredDifferenceImageFilterIUC3IUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquaredDifferenceImageFilterIUC3IUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquaredDifferenceImageFilterIUC3IUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSquaredDifferenceImageFilterIUC3IUC3IUC3 in _itkSquaredDifferenceImageFilterPython:
_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC3IUC3IUC3_swigregister(itkSquaredDifferenceImageFilterIUC3IUC3IUC3)
itkSquaredDifferenceImageFilterIUC3IUC3IUC3___New_orig__ = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC3IUC3IUC3___New_orig__
itkSquaredDifferenceImageFilterIUC3IUC3IUC3_cast = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUC3IUC3IUC3_cast

class itkSquaredDifferenceImageFilterIUS2IUS2IUS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS2IUS2IUS2):
    r"""Proxy of C++ itkSquaredDifferenceImageFilterIUS2IUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS2IUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS2IUS2IUS2_Clone)
    Input1ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS2IUS2IUS2_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS2IUS2IUS2_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS2IUS2IUS2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSquaredDifferenceImageFilterPython.delete_itkSquaredDifferenceImageFilterIUS2IUS2IUS2
    cast = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS2IUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkSquaredDifferenceImageFilterIUS2IUS2IUS2

        Create a new object of the class itkSquaredDifferenceImageFilterIUS2IUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquaredDifferenceImageFilterIUS2IUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquaredDifferenceImageFilterIUS2IUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquaredDifferenceImageFilterIUS2IUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSquaredDifferenceImageFilterIUS2IUS2IUS2 in _itkSquaredDifferenceImageFilterPython:
_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS2IUS2IUS2_swigregister(itkSquaredDifferenceImageFilterIUS2IUS2IUS2)
itkSquaredDifferenceImageFilterIUS2IUS2IUS2___New_orig__ = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS2IUS2IUS2___New_orig__
itkSquaredDifferenceImageFilterIUS2IUS2IUS2_cast = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS2IUS2IUS2_cast

class itkSquaredDifferenceImageFilterIUS3IUS3IUS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS3IUS3IUS3):
    r"""Proxy of C++ itkSquaredDifferenceImageFilterIUS3IUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS3IUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS3IUS3IUS3_Clone)
    Input1ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS3IUS3IUS3_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS3IUS3IUS3_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS3IUS3IUS3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSquaredDifferenceImageFilterPython.delete_itkSquaredDifferenceImageFilterIUS3IUS3IUS3
    cast = _swig_new_static_method(_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS3IUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkSquaredDifferenceImageFilterIUS3IUS3IUS3

        Create a new object of the class itkSquaredDifferenceImageFilterIUS3IUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquaredDifferenceImageFilterIUS3IUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquaredDifferenceImageFilterIUS3IUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquaredDifferenceImageFilterIUS3IUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSquaredDifferenceImageFilterIUS3IUS3IUS3 in _itkSquaredDifferenceImageFilterPython:
_itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS3IUS3IUS3_swigregister(itkSquaredDifferenceImageFilterIUS3IUS3IUS3)
itkSquaredDifferenceImageFilterIUS3IUS3IUS3___New_orig__ = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS3IUS3IUS3___New_orig__
itkSquaredDifferenceImageFilterIUS3IUS3IUS3_cast = _itkSquaredDifferenceImageFilterPython.itkSquaredDifferenceImageFilterIUS3IUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def squared_difference_image_filter(*args, **kwargs):
    """Procedural interface for SquaredDifferenceImageFilter"""
    import itk
    instance = itk.SquaredDifferenceImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def squared_difference_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.SquaredDifferenceImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.SquaredDifferenceImageFilter.values()[0]
    else:
        filter_object = itk.SquaredDifferenceImageFilter

    squared_difference_image_filter.__doc__ = filter_object.__doc__
    squared_difference_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    squared_difference_image_filter.__doc__ += "Available Keyword Arguments:\n"
    squared_difference_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



