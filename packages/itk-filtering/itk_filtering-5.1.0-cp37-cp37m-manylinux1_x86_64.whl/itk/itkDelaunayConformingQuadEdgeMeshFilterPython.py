# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkDelaunayConformingQuadEdgeMeshFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkDelaunayConformingQuadEdgeMeshFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkDelaunayConformingQuadEdgeMeshFilterPython
            return _itkDelaunayConformingQuadEdgeMeshFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkDelaunayConformingQuadEdgeMeshFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkDelaunayConformingQuadEdgeMeshFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkDelaunayConformingQuadEdgeMeshFilterPython
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
import itkQuadEdgeMeshBasePython
import itkQuadEdgeMeshPointPython
import itkPointPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkVectorPython
import itkGeometricalQuadEdgePython
import itkQuadEdgePython
import itkQuadEdgeMeshLineCellPython
import itkArrayPython
import itkQuadEdgeCellTraitsInfoPython
import itkImagePython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkRGBAPixelPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkImageRegionPython
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkMapContainerPython
import itkQuadEdgeMeshToQuadEdgeMeshFilterPython

def itkDelaunayConformingQuadEdgeMeshFilterQEMD3_New():
  return itkDelaunayConformingQuadEdgeMeshFilterQEMD3.New()


def itkDelaunayConformingQuadEdgeMeshFilterQEMD2_New():
  return itkDelaunayConformingQuadEdgeMeshFilterQEMD2.New()

class itkDelaunayConformingQuadEdgeMeshFilterQEMD2(itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2):
    """


    FIXME Add documentation.

    C++ includes: itkDelaunayConformingQuadEdgeMeshFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDelaunayConformingQuadEdgeMeshFilterQEMD2_Pointer":
        """__New_orig__() -> itkDelaunayConformingQuadEdgeMeshFilterQEMD2_Pointer"""
        return _itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDelaunayConformingQuadEdgeMeshFilterQEMD2_Pointer":
        """Clone(itkDelaunayConformingQuadEdgeMeshFilterQEMD2 self) -> itkDelaunayConformingQuadEdgeMeshFilterQEMD2_Pointer"""
        return _itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD2_Clone(self)


    def GetNumberOfEdgeFlips(self) -> "unsigned long":
        """GetNumberOfEdgeFlips(itkDelaunayConformingQuadEdgeMeshFilterQEMD2 self) -> unsigned long"""
        return _itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD2_GetNumberOfEdgeFlips(self)


    def SetListOfConstrainedEdges(self, iList: 'std::list< itkQuadEdgeMeshLineCellCIDQEMCTI2 *,std::allocator< itkQuadEdgeMeshLineCellCIDQEMCTI2 * > > const &') -> "void":
        """SetListOfConstrainedEdges(itkDelaunayConformingQuadEdgeMeshFilterQEMD2 self, std::list< itkQuadEdgeMeshLineCellCIDQEMCTI2 *,std::allocator< itkQuadEdgeMeshLineCellCIDQEMCTI2 * > > const & iList)"""
        return _itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD2_SetListOfConstrainedEdges(self, iList)

    __swig_destroy__ = _itkDelaunayConformingQuadEdgeMeshFilterPython.delete_itkDelaunayConformingQuadEdgeMeshFilterQEMD2

    def cast(obj: 'itkLightObject') -> "itkDelaunayConformingQuadEdgeMeshFilterQEMD2 *":
        """cast(itkLightObject obj) -> itkDelaunayConformingQuadEdgeMeshFilterQEMD2"""
        return _itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkDelaunayConformingQuadEdgeMeshFilterQEMD2

        Create a new object of the class itkDelaunayConformingQuadEdgeMeshFilterQEMD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDelaunayConformingQuadEdgeMeshFilterQEMD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDelaunayConformingQuadEdgeMeshFilterQEMD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDelaunayConformingQuadEdgeMeshFilterQEMD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDelaunayConformingQuadEdgeMeshFilterQEMD2.Clone = new_instancemethod(_itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD2_Clone, None, itkDelaunayConformingQuadEdgeMeshFilterQEMD2)
itkDelaunayConformingQuadEdgeMeshFilterQEMD2.GetNumberOfEdgeFlips = new_instancemethod(_itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD2_GetNumberOfEdgeFlips, None, itkDelaunayConformingQuadEdgeMeshFilterQEMD2)
itkDelaunayConformingQuadEdgeMeshFilterQEMD2.SetListOfConstrainedEdges = new_instancemethod(_itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD2_SetListOfConstrainedEdges, None, itkDelaunayConformingQuadEdgeMeshFilterQEMD2)
itkDelaunayConformingQuadEdgeMeshFilterQEMD2_swigregister = _itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD2_swigregister
itkDelaunayConformingQuadEdgeMeshFilterQEMD2_swigregister(itkDelaunayConformingQuadEdgeMeshFilterQEMD2)

def itkDelaunayConformingQuadEdgeMeshFilterQEMD2___New_orig__() -> "itkDelaunayConformingQuadEdgeMeshFilterQEMD2_Pointer":
    """itkDelaunayConformingQuadEdgeMeshFilterQEMD2___New_orig__() -> itkDelaunayConformingQuadEdgeMeshFilterQEMD2_Pointer"""
    return _itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD2___New_orig__()

def itkDelaunayConformingQuadEdgeMeshFilterQEMD2_cast(obj: 'itkLightObject') -> "itkDelaunayConformingQuadEdgeMeshFilterQEMD2 *":
    """itkDelaunayConformingQuadEdgeMeshFilterQEMD2_cast(itkLightObject obj) -> itkDelaunayConformingQuadEdgeMeshFilterQEMD2"""
    return _itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD2_cast(obj)

class itkDelaunayConformingQuadEdgeMeshFilterQEMD3(itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3):
    """


    FIXME Add documentation.

    C++ includes: itkDelaunayConformingQuadEdgeMeshFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkDelaunayConformingQuadEdgeMeshFilterQEMD3_Pointer":
        """__New_orig__() -> itkDelaunayConformingQuadEdgeMeshFilterQEMD3_Pointer"""
        return _itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkDelaunayConformingQuadEdgeMeshFilterQEMD3_Pointer":
        """Clone(itkDelaunayConformingQuadEdgeMeshFilterQEMD3 self) -> itkDelaunayConformingQuadEdgeMeshFilterQEMD3_Pointer"""
        return _itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD3_Clone(self)


    def GetNumberOfEdgeFlips(self) -> "unsigned long":
        """GetNumberOfEdgeFlips(itkDelaunayConformingQuadEdgeMeshFilterQEMD3 self) -> unsigned long"""
        return _itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD3_GetNumberOfEdgeFlips(self)


    def SetListOfConstrainedEdges(self, iList: 'std::list< itkQuadEdgeMeshLineCellCIDQEMCTI3 *,std::allocator< itkQuadEdgeMeshLineCellCIDQEMCTI3 * > > const &') -> "void":
        """SetListOfConstrainedEdges(itkDelaunayConformingQuadEdgeMeshFilterQEMD3 self, std::list< itkQuadEdgeMeshLineCellCIDQEMCTI3 *,std::allocator< itkQuadEdgeMeshLineCellCIDQEMCTI3 * > > const & iList)"""
        return _itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD3_SetListOfConstrainedEdges(self, iList)

    __swig_destroy__ = _itkDelaunayConformingQuadEdgeMeshFilterPython.delete_itkDelaunayConformingQuadEdgeMeshFilterQEMD3

    def cast(obj: 'itkLightObject') -> "itkDelaunayConformingQuadEdgeMeshFilterQEMD3 *":
        """cast(itkLightObject obj) -> itkDelaunayConformingQuadEdgeMeshFilterQEMD3"""
        return _itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkDelaunayConformingQuadEdgeMeshFilterQEMD3

        Create a new object of the class itkDelaunayConformingQuadEdgeMeshFilterQEMD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDelaunayConformingQuadEdgeMeshFilterQEMD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDelaunayConformingQuadEdgeMeshFilterQEMD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDelaunayConformingQuadEdgeMeshFilterQEMD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDelaunayConformingQuadEdgeMeshFilterQEMD3.Clone = new_instancemethod(_itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD3_Clone, None, itkDelaunayConformingQuadEdgeMeshFilterQEMD3)
itkDelaunayConformingQuadEdgeMeshFilterQEMD3.GetNumberOfEdgeFlips = new_instancemethod(_itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD3_GetNumberOfEdgeFlips, None, itkDelaunayConformingQuadEdgeMeshFilterQEMD3)
itkDelaunayConformingQuadEdgeMeshFilterQEMD3.SetListOfConstrainedEdges = new_instancemethod(_itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD3_SetListOfConstrainedEdges, None, itkDelaunayConformingQuadEdgeMeshFilterQEMD3)
itkDelaunayConformingQuadEdgeMeshFilterQEMD3_swigregister = _itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD3_swigregister
itkDelaunayConformingQuadEdgeMeshFilterQEMD3_swigregister(itkDelaunayConformingQuadEdgeMeshFilterQEMD3)

def itkDelaunayConformingQuadEdgeMeshFilterQEMD3___New_orig__() -> "itkDelaunayConformingQuadEdgeMeshFilterQEMD3_Pointer":
    """itkDelaunayConformingQuadEdgeMeshFilterQEMD3___New_orig__() -> itkDelaunayConformingQuadEdgeMeshFilterQEMD3_Pointer"""
    return _itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD3___New_orig__()

def itkDelaunayConformingQuadEdgeMeshFilterQEMD3_cast(obj: 'itkLightObject') -> "itkDelaunayConformingQuadEdgeMeshFilterQEMD3 *":
    """itkDelaunayConformingQuadEdgeMeshFilterQEMD3_cast(itkLightObject obj) -> itkDelaunayConformingQuadEdgeMeshFilterQEMD3"""
    return _itkDelaunayConformingQuadEdgeMeshFilterPython.itkDelaunayConformingQuadEdgeMeshFilterQEMD3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def delaunay_conforming_quad_edge_mesh_filter(*args, **kwargs):
    """Procedural interface for DelaunayConformingQuadEdgeMeshFilter"""
    import itk
    instance = itk.DelaunayConformingQuadEdgeMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def delaunay_conforming_quad_edge_mesh_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.DelaunayConformingQuadEdgeMeshFilter, itkTemplate.itkTemplate):
        filter_object = itk.DelaunayConformingQuadEdgeMeshFilter.values()[0]
    else:
        filter_object = itk.DelaunayConformingQuadEdgeMeshFilter

    delaunay_conforming_quad_edge_mesh_filter.__doc__ = filter_object.__doc__
    delaunay_conforming_quad_edge_mesh_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    delaunay_conforming_quad_edge_mesh_filter.__doc__ += "Available Keyword Arguments:\n"
    delaunay_conforming_quad_edge_mesh_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



