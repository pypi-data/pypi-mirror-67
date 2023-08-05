# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSmoothingQuadEdgeMeshFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSmoothingQuadEdgeMeshFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkSmoothingQuadEdgeMeshFilterPython
            return _itkSmoothingQuadEdgeMeshFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkSmoothingQuadEdgeMeshFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkSmoothingQuadEdgeMeshFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSmoothingQuadEdgeMeshFilterPython
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


import itkMatrixCoefficientsPython
import itkQuadEdgeMeshBasePython
import itkFixedArrayPython
import pyBasePython
import itkGeometricalQuadEdgePython
import itkQuadEdgePython
import itkQuadEdgeMeshLineCellPython
import itkQuadEdgeCellTraitsInfoPython
import ITKCommonBasePython
import itkQuadEdgeMeshPointPython
import itkPointPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkArrayPython
import itkMapContainerPython
import itkImagePython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkIndexPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkQuadEdgeMeshToQuadEdgeMeshFilterPython

def itkSmoothingQuadEdgeMeshFilterQEMD3_New():
  return itkSmoothingQuadEdgeMeshFilterQEMD3.New()


def itkSmoothingQuadEdgeMeshFilterQEMD2_New():
  return itkSmoothingQuadEdgeMeshFilterQEMD2.New()

class itkSmoothingQuadEdgeMeshFilterQEMD2(itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2):
    """


    QuadEdgeMesh Smoothing Filter.

    This filter adjusts point coordinates using Laplacian smoothing. The
    effect is to "relax" the mesh, making the cells better shaped and
    the vertices more evenly distributed.

    For one iteration the location of one vertex is computed as follows:
    \\[ \\boldsymbol{ v' }_i = v_i + m_RelaxationFactor \\cdot
    \\frac{ \\sum_j w_{ij} ( \\boldsymbol{ v_j } - \\boldsymbol{
    v_i } ) }{ \\sum_j w_{ij} } \\]

    where $ w_{ij} $ is computed by the means of the set functor
    CoefficientsComputation

    This process is then repeated for m_NumberOfIterations (the more
    iterations, the smoother the output mesh will be).

    At each iteration, one can run DelaunayConformingQuadEdgeMeshFilter
    resulting a more regular (in terms of connectivity) and smoother mesh.
    Depending on the mesh size and configuration it could be an expensive
    process to run it at each iterations, especially if the number of
    iterations is large. Note that one can still run N iterations without
    DelaunayConformingQuadEdgeMeshFilter, then run this filter and apply
    this process M times.

    C++ includes: itkSmoothingQuadEdgeMeshFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSmoothingQuadEdgeMeshFilterQEMD2_Pointer":
        """__New_orig__() -> itkSmoothingQuadEdgeMeshFilterQEMD2_Pointer"""
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSmoothingQuadEdgeMeshFilterQEMD2_Pointer":
        """Clone(itkSmoothingQuadEdgeMeshFilterQEMD2 self) -> itkSmoothingQuadEdgeMeshFilterQEMD2_Pointer"""
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_Clone(self)


    def SetCoefficientsMethod(self, iMethod: 'itkMatrixCoefficientsQEMD2') -> "void":
        """SetCoefficientsMethod(itkSmoothingQuadEdgeMeshFilterQEMD2 self, itkMatrixCoefficientsQEMD2 iMethod)"""
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_SetCoefficientsMethod(self, iMethod)


    def SetNumberOfIterations(self, _arg: 'unsigned int const') -> "void":
        """
        SetNumberOfIterations(itkSmoothingQuadEdgeMeshFilterQEMD2 self, unsigned int const _arg)

        Set/Get the
        number of iterations 
        """
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_SetNumberOfIterations(self, _arg)


    def GetNumberOfIterations(self) -> "unsigned int":
        """GetNumberOfIterations(itkSmoothingQuadEdgeMeshFilterQEMD2 self) -> unsigned int"""
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_GetNumberOfIterations(self)


    def SetDelaunayConforming(self, _arg: 'bool const') -> "void":
        """
        SetDelaunayConforming(itkSmoothingQuadEdgeMeshFilterQEMD2 self, bool const _arg)

        Set/Get if
        DelaunayConformingQuadEdgeMeshFilter is used at the end of each
        iterations 
        """
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_SetDelaunayConforming(self, _arg)


    def GetDelaunayConforming(self) -> "bool":
        """GetDelaunayConforming(itkSmoothingQuadEdgeMeshFilterQEMD2 self) -> bool"""
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_GetDelaunayConforming(self)


    def SetRelaxationFactor(self, _arg: 'float const') -> "void":
        """
        SetRelaxationFactor(itkSmoothingQuadEdgeMeshFilterQEMD2 self, float const _arg)

        Set/Get
        relaxation factor applied for each iteration 
        """
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_SetRelaxationFactor(self, _arg)


    def GetRelaxationFactor(self) -> "float":
        """GetRelaxationFactor(itkSmoothingQuadEdgeMeshFilterQEMD2 self) -> float"""
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_GetRelaxationFactor(self)

    __swig_destroy__ = _itkSmoothingQuadEdgeMeshFilterPython.delete_itkSmoothingQuadEdgeMeshFilterQEMD2

    def cast(obj: 'itkLightObject') -> "itkSmoothingQuadEdgeMeshFilterQEMD2 *":
        """cast(itkLightObject obj) -> itkSmoothingQuadEdgeMeshFilterQEMD2"""
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_cast(obj)

    cast = staticmethod(cast)

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

itkSmoothingQuadEdgeMeshFilterQEMD2.Clone = new_instancemethod(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_Clone, None, itkSmoothingQuadEdgeMeshFilterQEMD2)
itkSmoothingQuadEdgeMeshFilterQEMD2.SetCoefficientsMethod = new_instancemethod(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_SetCoefficientsMethod, None, itkSmoothingQuadEdgeMeshFilterQEMD2)
itkSmoothingQuadEdgeMeshFilterQEMD2.SetNumberOfIterations = new_instancemethod(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_SetNumberOfIterations, None, itkSmoothingQuadEdgeMeshFilterQEMD2)
itkSmoothingQuadEdgeMeshFilterQEMD2.GetNumberOfIterations = new_instancemethod(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_GetNumberOfIterations, None, itkSmoothingQuadEdgeMeshFilterQEMD2)
itkSmoothingQuadEdgeMeshFilterQEMD2.SetDelaunayConforming = new_instancemethod(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_SetDelaunayConforming, None, itkSmoothingQuadEdgeMeshFilterQEMD2)
itkSmoothingQuadEdgeMeshFilterQEMD2.GetDelaunayConforming = new_instancemethod(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_GetDelaunayConforming, None, itkSmoothingQuadEdgeMeshFilterQEMD2)
itkSmoothingQuadEdgeMeshFilterQEMD2.SetRelaxationFactor = new_instancemethod(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_SetRelaxationFactor, None, itkSmoothingQuadEdgeMeshFilterQEMD2)
itkSmoothingQuadEdgeMeshFilterQEMD2.GetRelaxationFactor = new_instancemethod(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_GetRelaxationFactor, None, itkSmoothingQuadEdgeMeshFilterQEMD2)
itkSmoothingQuadEdgeMeshFilterQEMD2_swigregister = _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_swigregister
itkSmoothingQuadEdgeMeshFilterQEMD2_swigregister(itkSmoothingQuadEdgeMeshFilterQEMD2)

def itkSmoothingQuadEdgeMeshFilterQEMD2___New_orig__() -> "itkSmoothingQuadEdgeMeshFilterQEMD2_Pointer":
    """itkSmoothingQuadEdgeMeshFilterQEMD2___New_orig__() -> itkSmoothingQuadEdgeMeshFilterQEMD2_Pointer"""
    return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2___New_orig__()

def itkSmoothingQuadEdgeMeshFilterQEMD2_cast(obj: 'itkLightObject') -> "itkSmoothingQuadEdgeMeshFilterQEMD2 *":
    """itkSmoothingQuadEdgeMeshFilterQEMD2_cast(itkLightObject obj) -> itkSmoothingQuadEdgeMeshFilterQEMD2"""
    return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_cast(obj)

class itkSmoothingQuadEdgeMeshFilterQEMD3(itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3):
    """


    QuadEdgeMesh Smoothing Filter.

    This filter adjusts point coordinates using Laplacian smoothing. The
    effect is to "relax" the mesh, making the cells better shaped and
    the vertices more evenly distributed.

    For one iteration the location of one vertex is computed as follows:
    \\[ \\boldsymbol{ v' }_i = v_i + m_RelaxationFactor \\cdot
    \\frac{ \\sum_j w_{ij} ( \\boldsymbol{ v_j } - \\boldsymbol{
    v_i } ) }{ \\sum_j w_{ij} } \\]

    where $ w_{ij} $ is computed by the means of the set functor
    CoefficientsComputation

    This process is then repeated for m_NumberOfIterations (the more
    iterations, the smoother the output mesh will be).

    At each iteration, one can run DelaunayConformingQuadEdgeMeshFilter
    resulting a more regular (in terms of connectivity) and smoother mesh.
    Depending on the mesh size and configuration it could be an expensive
    process to run it at each iterations, especially if the number of
    iterations is large. Note that one can still run N iterations without
    DelaunayConformingQuadEdgeMeshFilter, then run this filter and apply
    this process M times.

    C++ includes: itkSmoothingQuadEdgeMeshFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSmoothingQuadEdgeMeshFilterQEMD3_Pointer":
        """__New_orig__() -> itkSmoothingQuadEdgeMeshFilterQEMD3_Pointer"""
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSmoothingQuadEdgeMeshFilterQEMD3_Pointer":
        """Clone(itkSmoothingQuadEdgeMeshFilterQEMD3 self) -> itkSmoothingQuadEdgeMeshFilterQEMD3_Pointer"""
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_Clone(self)


    def SetCoefficientsMethod(self, iMethod: 'itkMatrixCoefficientsQEMD3') -> "void":
        """SetCoefficientsMethod(itkSmoothingQuadEdgeMeshFilterQEMD3 self, itkMatrixCoefficientsQEMD3 iMethod)"""
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_SetCoefficientsMethod(self, iMethod)


    def SetNumberOfIterations(self, _arg: 'unsigned int const') -> "void":
        """
        SetNumberOfIterations(itkSmoothingQuadEdgeMeshFilterQEMD3 self, unsigned int const _arg)

        Set/Get the
        number of iterations 
        """
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_SetNumberOfIterations(self, _arg)


    def GetNumberOfIterations(self) -> "unsigned int":
        """GetNumberOfIterations(itkSmoothingQuadEdgeMeshFilterQEMD3 self) -> unsigned int"""
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_GetNumberOfIterations(self)


    def SetDelaunayConforming(self, _arg: 'bool const') -> "void":
        """
        SetDelaunayConforming(itkSmoothingQuadEdgeMeshFilterQEMD3 self, bool const _arg)

        Set/Get if
        DelaunayConformingQuadEdgeMeshFilter is used at the end of each
        iterations 
        """
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_SetDelaunayConforming(self, _arg)


    def GetDelaunayConforming(self) -> "bool":
        """GetDelaunayConforming(itkSmoothingQuadEdgeMeshFilterQEMD3 self) -> bool"""
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_GetDelaunayConforming(self)


    def SetRelaxationFactor(self, _arg: 'float const') -> "void":
        """
        SetRelaxationFactor(itkSmoothingQuadEdgeMeshFilterQEMD3 self, float const _arg)

        Set/Get
        relaxation factor applied for each iteration 
        """
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_SetRelaxationFactor(self, _arg)


    def GetRelaxationFactor(self) -> "float":
        """GetRelaxationFactor(itkSmoothingQuadEdgeMeshFilterQEMD3 self) -> float"""
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_GetRelaxationFactor(self)

    __swig_destroy__ = _itkSmoothingQuadEdgeMeshFilterPython.delete_itkSmoothingQuadEdgeMeshFilterQEMD3

    def cast(obj: 'itkLightObject') -> "itkSmoothingQuadEdgeMeshFilterQEMD3 *":
        """cast(itkLightObject obj) -> itkSmoothingQuadEdgeMeshFilterQEMD3"""
        return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_cast(obj)

    cast = staticmethod(cast)

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

itkSmoothingQuadEdgeMeshFilterQEMD3.Clone = new_instancemethod(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_Clone, None, itkSmoothingQuadEdgeMeshFilterQEMD3)
itkSmoothingQuadEdgeMeshFilterQEMD3.SetCoefficientsMethod = new_instancemethod(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_SetCoefficientsMethod, None, itkSmoothingQuadEdgeMeshFilterQEMD3)
itkSmoothingQuadEdgeMeshFilterQEMD3.SetNumberOfIterations = new_instancemethod(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_SetNumberOfIterations, None, itkSmoothingQuadEdgeMeshFilterQEMD3)
itkSmoothingQuadEdgeMeshFilterQEMD3.GetNumberOfIterations = new_instancemethod(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_GetNumberOfIterations, None, itkSmoothingQuadEdgeMeshFilterQEMD3)
itkSmoothingQuadEdgeMeshFilterQEMD3.SetDelaunayConforming = new_instancemethod(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_SetDelaunayConforming, None, itkSmoothingQuadEdgeMeshFilterQEMD3)
itkSmoothingQuadEdgeMeshFilterQEMD3.GetDelaunayConforming = new_instancemethod(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_GetDelaunayConforming, None, itkSmoothingQuadEdgeMeshFilterQEMD3)
itkSmoothingQuadEdgeMeshFilterQEMD3.SetRelaxationFactor = new_instancemethod(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_SetRelaxationFactor, None, itkSmoothingQuadEdgeMeshFilterQEMD3)
itkSmoothingQuadEdgeMeshFilterQEMD3.GetRelaxationFactor = new_instancemethod(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_GetRelaxationFactor, None, itkSmoothingQuadEdgeMeshFilterQEMD3)
itkSmoothingQuadEdgeMeshFilterQEMD3_swigregister = _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_swigregister
itkSmoothingQuadEdgeMeshFilterQEMD3_swigregister(itkSmoothingQuadEdgeMeshFilterQEMD3)

def itkSmoothingQuadEdgeMeshFilterQEMD3___New_orig__() -> "itkSmoothingQuadEdgeMeshFilterQEMD3_Pointer":
    """itkSmoothingQuadEdgeMeshFilterQEMD3___New_orig__() -> itkSmoothingQuadEdgeMeshFilterQEMD3_Pointer"""
    return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3___New_orig__()

def itkSmoothingQuadEdgeMeshFilterQEMD3_cast(obj: 'itkLightObject') -> "itkSmoothingQuadEdgeMeshFilterQEMD3 *":
    """itkSmoothingQuadEdgeMeshFilterQEMD3_cast(itkLightObject obj) -> itkSmoothingQuadEdgeMeshFilterQEMD3"""
    return _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_cast(obj)


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



