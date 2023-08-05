# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkDiscreteCurvatureQuadEdgeMeshFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkDiscreteCurvatureQuadEdgeMeshFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkDiscreteCurvatureQuadEdgeMeshFilterPython
            return _itkDiscreteCurvatureQuadEdgeMeshFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkDiscreteCurvatureQuadEdgeMeshFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkDiscreteCurvatureQuadEdgeMeshFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkDiscreteCurvatureQuadEdgeMeshFilterPython
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


import itkQuadEdgeMeshToQuadEdgeMeshFilterPython
import ITKCommonBasePython
import pyBasePython
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

def itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3_New():
  return itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3.New()


def itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2_New():
  return itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2.New()

class itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2(itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2):
    """


    FIXME.

    C++ includes: itkDiscreteCurvatureQuadEdgeMeshFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    OutputIsFloatingPointCheck = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2_OutputIsFloatingPointCheck
    __swig_destroy__ = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.delete_itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2

    def cast(obj: 'itkLightObject') -> "itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2 *":
        """cast(itkLightObject obj) -> itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2"""
        return _itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2

        Create a new object of the class itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2_swigregister = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2_swigregister
itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2_swigregister(itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2)

def itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2_cast(obj: 'itkLightObject') -> "itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2 *":
    """itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2_cast(itkLightObject obj) -> itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2"""
    return _itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2_cast(obj)

class itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3(itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3):
    """


    FIXME.

    C++ includes: itkDiscreteCurvatureQuadEdgeMeshFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    OutputIsFloatingPointCheck = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3_OutputIsFloatingPointCheck
    __swig_destroy__ = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.delete_itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3

    def cast(obj: 'itkLightObject') -> "itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3 *":
        """cast(itkLightObject obj) -> itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3"""
        return _itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3

        Create a new object of the class itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3_swigregister = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3_swigregister
itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3_swigregister(itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3)

def itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3_cast(obj: 'itkLightObject') -> "itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3 *":
    """itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3_cast(itkLightObject obj) -> itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3"""
    return _itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def discrete_curvature_quad_edge_mesh_filter(*args, **kwargs):
    """Procedural interface for DiscreteCurvatureQuadEdgeMeshFilter"""
    import itk
    instance = itk.DiscreteCurvatureQuadEdgeMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def discrete_curvature_quad_edge_mesh_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.DiscreteCurvatureQuadEdgeMeshFilter, itkTemplate.itkTemplate):
        filter_object = itk.DiscreteCurvatureQuadEdgeMeshFilter.values()[0]
    else:
        filter_object = itk.DiscreteCurvatureQuadEdgeMeshFilter

    discrete_curvature_quad_edge_mesh_filter.__doc__ = filter_object.__doc__
    discrete_curvature_quad_edge_mesh_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    discrete_curvature_quad_edge_mesh_filter.__doc__ += "Available Keyword Arguments:\n"
    discrete_curvature_quad_edge_mesh_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



