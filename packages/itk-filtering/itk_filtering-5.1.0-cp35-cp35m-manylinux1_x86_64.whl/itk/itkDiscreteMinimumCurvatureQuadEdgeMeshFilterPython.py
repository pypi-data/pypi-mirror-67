# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython
            return _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


import ITKCommonBasePython
import pyBasePython
import itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython
import itkDiscreteCurvatureQuadEdgeMeshFilterPython
import itkQuadEdgeMeshToQuadEdgeMeshFilterPython
import itkQuadEdgeMeshBasePython
import itkQuadEdgeCellTraitsInfoPython
import itkQuadEdgeMeshPointPython
import itkGeometricalQuadEdgePython
import itkQuadEdgePython
import itkPointPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import itkImagePython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBAPixelPython
import itkMapContainerPython
import itkQuadEdgeMeshLineCellPython
import itkArrayPython

def itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_New():
  return itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3.New()


def itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_New():
  return itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2.New()

class itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2(itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2):
    """


    FIXME add documentation here.

    C++ includes: itkDiscreteMinimumCurvatureQuadEdgeMeshFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_Pointer":
        """__New_orig__() -> itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_Pointer"""
        return _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_Pointer":
        """Clone(itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2 self) -> itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_Pointer"""
        return _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_Clone(self)

    OutputIsFloatingPointCheck = _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_OutputIsFloatingPointCheck
    __swig_destroy__ = _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.delete_itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2

    def cast(obj: 'itkLightObject') -> "itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2 *":
        """cast(itkLightObject obj) -> itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2"""
        return _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2

        Create a new object of the class itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2.Clone = new_instancemethod(_itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_Clone, None, itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2)
itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_swigregister = _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_swigregister
itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_swigregister(itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2)

def itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2___New_orig__() -> "itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_Pointer":
    """itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2___New_orig__() -> itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_Pointer"""
    return _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2___New_orig__()

def itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_cast(obj: 'itkLightObject') -> "itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2 *":
    """itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_cast(itkLightObject obj) -> itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2"""
    return _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2_cast(obj)

class itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3(itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterPython.itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3):
    """


    FIXME add documentation here.

    C++ includes: itkDiscreteMinimumCurvatureQuadEdgeMeshFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_Pointer":
        """__New_orig__() -> itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_Pointer"""
        return _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_Pointer":
        """Clone(itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3 self) -> itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_Pointer"""
        return _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_Clone(self)

    OutputIsFloatingPointCheck = _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_OutputIsFloatingPointCheck
    __swig_destroy__ = _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.delete_itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3

    def cast(obj: 'itkLightObject') -> "itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3 *":
        """cast(itkLightObject obj) -> itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3"""
        return _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3

        Create a new object of the class itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3.Clone = new_instancemethod(_itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_Clone, None, itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3)
itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_swigregister = _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_swigregister
itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_swigregister(itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3)

def itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3___New_orig__() -> "itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_Pointer":
    """itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3___New_orig__() -> itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_Pointer"""
    return _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3___New_orig__()

def itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_cast(obj: 'itkLightObject') -> "itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3 *":
    """itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_cast(itkLightObject obj) -> itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3"""
    return _itkDiscreteMinimumCurvatureQuadEdgeMeshFilterPython.itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def discrete_minimum_curvature_quad_edge_mesh_filter(*args, **kwargs):
    """Procedural interface for DiscreteMinimumCurvatureQuadEdgeMeshFilter"""
    import itk
    instance = itk.DiscreteMinimumCurvatureQuadEdgeMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def discrete_minimum_curvature_quad_edge_mesh_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.DiscreteMinimumCurvatureQuadEdgeMeshFilter, itkTemplate.itkTemplate):
        filter_object = itk.DiscreteMinimumCurvatureQuadEdgeMeshFilter.values()[0]
    else:
        filter_object = itk.DiscreteMinimumCurvatureQuadEdgeMeshFilter

    discrete_minimum_curvature_quad_edge_mesh_filter.__doc__ = filter_object.__doc__
    discrete_minimum_curvature_quad_edge_mesh_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    discrete_minimum_curvature_quad_edge_mesh_filter.__doc__ += "Available Keyword Arguments:\n"
    discrete_minimum_curvature_quad_edge_mesh_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



