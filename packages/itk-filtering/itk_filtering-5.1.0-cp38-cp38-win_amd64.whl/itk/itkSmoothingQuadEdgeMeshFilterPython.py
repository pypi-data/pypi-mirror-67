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
    from . import _itkSmoothingQuadEdgeMeshFilterPython
else:
    import _itkSmoothingQuadEdgeMeshFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSmoothingQuadEdgeMeshFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSmoothingQuadEdgeMeshFilterPython.SWIG_PyStaticMethod_New

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
import itkMatrixCoefficientsPython
import itkGeometricalQuadEdgePython
import itkQuadEdgePython
import itkQuadEdgeMeshBasePython
import itkFixedArrayPython
import itkMapContainerPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkPointPython
import itkQuadEdgeCellTraitsInfoPython
import itkQuadEdgeMeshPointPython
import itkImagePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkSymmetricSecondRankTensorPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkQuadEdgeMeshLineCellPython
import itkArrayPython
import itkQuadEdgeMeshToQuadEdgeMeshFilterPython

def itkSmoothingQuadEdgeMeshFilterQEMD3_New():
  return itkSmoothingQuadEdgeMeshFilterQEMD3.New()


def itkSmoothingQuadEdgeMeshFilterQEMD2_New():
  return itkSmoothingQuadEdgeMeshFilterQEMD2.New()

class itkSmoothingQuadEdgeMeshFilterQEMD2(itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2):
    r"""Proxy of C++ itkSmoothingQuadEdgeMeshFilterQEMD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2___New_orig__)
    Clone = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_Clone)
    SetCoefficientsMethod = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_SetCoefficientsMethod)
    SetNumberOfIterations = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_SetNumberOfIterations)
    GetNumberOfIterations = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_GetNumberOfIterations)
    SetDelaunayConforming = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_SetDelaunayConforming)
    GetDelaunayConforming = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_GetDelaunayConforming)
    SetRelaxationFactor = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_SetRelaxationFactor)
    GetRelaxationFactor = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_GetRelaxationFactor)
    __swig_destroy__ = _itkSmoothingQuadEdgeMeshFilterPython.delete_itkSmoothingQuadEdgeMeshFilterQEMD2
    cast = _swig_new_static_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_cast)

    def New(*args, **kargs):
        """New() -> itkSmoothingQuadEdgeMeshFilterQEMD2

        Create a new object of the class itkSmoothingQuadEdgeMeshFilterQEMD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSmoothingQuadEdgeMeshFilterQEMD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSmoothingQuadEdgeMeshFilterQEMD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSmoothingQuadEdgeMeshFilterQEMD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSmoothingQuadEdgeMeshFilterQEMD2 in _itkSmoothingQuadEdgeMeshFilterPython:
_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_swigregister(itkSmoothingQuadEdgeMeshFilterQEMD2)
itkSmoothingQuadEdgeMeshFilterQEMD2___New_orig__ = _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2___New_orig__
itkSmoothingQuadEdgeMeshFilterQEMD2_cast = _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_cast

class itkSmoothingQuadEdgeMeshFilterQEMD3(itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3):
    r"""Proxy of C++ itkSmoothingQuadEdgeMeshFilterQEMD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3___New_orig__)
    Clone = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_Clone)
    SetCoefficientsMethod = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_SetCoefficientsMethod)
    SetNumberOfIterations = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_SetNumberOfIterations)
    GetNumberOfIterations = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_GetNumberOfIterations)
    SetDelaunayConforming = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_SetDelaunayConforming)
    GetDelaunayConforming = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_GetDelaunayConforming)
    SetRelaxationFactor = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_SetRelaxationFactor)
    GetRelaxationFactor = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_GetRelaxationFactor)
    __swig_destroy__ = _itkSmoothingQuadEdgeMeshFilterPython.delete_itkSmoothingQuadEdgeMeshFilterQEMD3
    cast = _swig_new_static_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_cast)

    def New(*args, **kargs):
        """New() -> itkSmoothingQuadEdgeMeshFilterQEMD3

        Create a new object of the class itkSmoothingQuadEdgeMeshFilterQEMD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSmoothingQuadEdgeMeshFilterQEMD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSmoothingQuadEdgeMeshFilterQEMD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSmoothingQuadEdgeMeshFilterQEMD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSmoothingQuadEdgeMeshFilterQEMD3 in _itkSmoothingQuadEdgeMeshFilterPython:
_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_swigregister(itkSmoothingQuadEdgeMeshFilterQEMD3)
itkSmoothingQuadEdgeMeshFilterQEMD3___New_orig__ = _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3___New_orig__
itkSmoothingQuadEdgeMeshFilterQEMD3_cast = _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def smoothing_quad_edge_mesh_filter(*args, **kwargs):
    """Procedural interface for SmoothingQuadEdgeMeshFilter"""
    import itk
    instance = itk.SmoothingQuadEdgeMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def smoothing_quad_edge_mesh_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.SmoothingQuadEdgeMeshFilter, itkTemplate.itkTemplate):
        filter_object = itk.SmoothingQuadEdgeMeshFilter.values()[0]
    else:
        filter_object = itk.SmoothingQuadEdgeMeshFilter

    smoothing_quad_edge_mesh_filter.__doc__ = filter_object.__doc__
    smoothing_quad_edge_mesh_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    smoothing_quad_edge_mesh_filter.__doc__ += "Available Keyword Arguments:\n"
    smoothing_quad_edge_mesh_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



