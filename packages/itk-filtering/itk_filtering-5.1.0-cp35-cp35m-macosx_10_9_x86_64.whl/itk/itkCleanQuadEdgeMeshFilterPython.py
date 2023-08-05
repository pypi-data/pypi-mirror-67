# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkCleanQuadEdgeMeshFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkCleanQuadEdgeMeshFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkCleanQuadEdgeMeshFilterPython
            return _itkCleanQuadEdgeMeshFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkCleanQuadEdgeMeshFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkCleanQuadEdgeMeshFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkCleanQuadEdgeMeshFilterPython
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
import itkQuadEdgeMeshBasePython
import itkPointPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import vnl_vector_refPython
import itkFixedArrayPython
import itkVectorPython
import ITKCommonBasePython
import itkQuadEdgeMeshPointPython
import itkGeometricalQuadEdgePython
import itkQuadEdgePython
import itkMapContainerPython
import itkQuadEdgeCellTraitsInfoPython
import itkQuadEdgeMeshLineCellPython
import itkArrayPython
import itkImagePython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkSymmetricSecondRankTensorPython

def itkCleanQuadEdgeMeshFilterQEMD3_New():
  return itkCleanQuadEdgeMeshFilterQEMD3.New()


def itkCleanQuadEdgeMeshFilterQEMD2_New():
  return itkCleanQuadEdgeMeshFilterQEMD2.New()

class itkCleanQuadEdgeMeshFilterQEMD2(itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2):
    """


    TODO.

    C++ includes: itkCleanQuadEdgeMeshFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCleanQuadEdgeMeshFilterQEMD2_Pointer":
        """__New_orig__() -> itkCleanQuadEdgeMeshFilterQEMD2_Pointer"""
        return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCleanQuadEdgeMeshFilterQEMD2_Pointer":
        """Clone(itkCleanQuadEdgeMeshFilterQEMD2 self) -> itkCleanQuadEdgeMeshFilterQEMD2_Pointer"""
        return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD2_Clone(self)


    def SetAbsoluteTolerance(self, _arg: 'float const') -> "void":
        """
        SetAbsoluteTolerance(itkCleanQuadEdgeMeshFilterQEMD2 self, float const _arg)

        TODO 
        """
        return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD2_SetAbsoluteTolerance(self, _arg)


    def GetAbsoluteTolerance(self) -> "float":
        """GetAbsoluteTolerance(itkCleanQuadEdgeMeshFilterQEMD2 self) -> float"""
        return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD2_GetAbsoluteTolerance(self)


    def SetRelativeTolerance(self, _arg: 'float') -> "void":
        """
        SetRelativeTolerance(itkCleanQuadEdgeMeshFilterQEMD2 self, float _arg)

        TODO 
        """
        return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD2_SetRelativeTolerance(self, _arg)


    def GetRelativeTolerance(self) -> "float":
        """GetRelativeTolerance(itkCleanQuadEdgeMeshFilterQEMD2 self) -> float"""
        return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD2_GetRelativeTolerance(self)

    __swig_destroy__ = _itkCleanQuadEdgeMeshFilterPython.delete_itkCleanQuadEdgeMeshFilterQEMD2

    def cast(obj: 'itkLightObject') -> "itkCleanQuadEdgeMeshFilterQEMD2 *":
        """cast(itkLightObject obj) -> itkCleanQuadEdgeMeshFilterQEMD2"""
        return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkCleanQuadEdgeMeshFilterQEMD2

        Create a new object of the class itkCleanQuadEdgeMeshFilterQEMD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCleanQuadEdgeMeshFilterQEMD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCleanQuadEdgeMeshFilterQEMD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCleanQuadEdgeMeshFilterQEMD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCleanQuadEdgeMeshFilterQEMD2.Clone = new_instancemethod(_itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD2_Clone, None, itkCleanQuadEdgeMeshFilterQEMD2)
itkCleanQuadEdgeMeshFilterQEMD2.SetAbsoluteTolerance = new_instancemethod(_itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD2_SetAbsoluteTolerance, None, itkCleanQuadEdgeMeshFilterQEMD2)
itkCleanQuadEdgeMeshFilterQEMD2.GetAbsoluteTolerance = new_instancemethod(_itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD2_GetAbsoluteTolerance, None, itkCleanQuadEdgeMeshFilterQEMD2)
itkCleanQuadEdgeMeshFilterQEMD2.SetRelativeTolerance = new_instancemethod(_itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD2_SetRelativeTolerance, None, itkCleanQuadEdgeMeshFilterQEMD2)
itkCleanQuadEdgeMeshFilterQEMD2.GetRelativeTolerance = new_instancemethod(_itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD2_GetRelativeTolerance, None, itkCleanQuadEdgeMeshFilterQEMD2)
itkCleanQuadEdgeMeshFilterQEMD2_swigregister = _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD2_swigregister
itkCleanQuadEdgeMeshFilterQEMD2_swigregister(itkCleanQuadEdgeMeshFilterQEMD2)

def itkCleanQuadEdgeMeshFilterQEMD2___New_orig__() -> "itkCleanQuadEdgeMeshFilterQEMD2_Pointer":
    """itkCleanQuadEdgeMeshFilterQEMD2___New_orig__() -> itkCleanQuadEdgeMeshFilterQEMD2_Pointer"""
    return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD2___New_orig__()

def itkCleanQuadEdgeMeshFilterQEMD2_cast(obj: 'itkLightObject') -> "itkCleanQuadEdgeMeshFilterQEMD2 *":
    """itkCleanQuadEdgeMeshFilterQEMD2_cast(itkLightObject obj) -> itkCleanQuadEdgeMeshFilterQEMD2"""
    return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD2_cast(obj)

class itkCleanQuadEdgeMeshFilterQEMD3(itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3):
    """


    TODO.

    C++ includes: itkCleanQuadEdgeMeshFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCleanQuadEdgeMeshFilterQEMD3_Pointer":
        """__New_orig__() -> itkCleanQuadEdgeMeshFilterQEMD3_Pointer"""
        return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCleanQuadEdgeMeshFilterQEMD3_Pointer":
        """Clone(itkCleanQuadEdgeMeshFilterQEMD3 self) -> itkCleanQuadEdgeMeshFilterQEMD3_Pointer"""
        return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD3_Clone(self)


    def SetAbsoluteTolerance(self, _arg: 'float const') -> "void":
        """
        SetAbsoluteTolerance(itkCleanQuadEdgeMeshFilterQEMD3 self, float const _arg)

        TODO 
        """
        return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD3_SetAbsoluteTolerance(self, _arg)


    def GetAbsoluteTolerance(self) -> "float":
        """GetAbsoluteTolerance(itkCleanQuadEdgeMeshFilterQEMD3 self) -> float"""
        return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD3_GetAbsoluteTolerance(self)


    def SetRelativeTolerance(self, _arg: 'float') -> "void":
        """
        SetRelativeTolerance(itkCleanQuadEdgeMeshFilterQEMD3 self, float _arg)

        TODO 
        """
        return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD3_SetRelativeTolerance(self, _arg)


    def GetRelativeTolerance(self) -> "float":
        """GetRelativeTolerance(itkCleanQuadEdgeMeshFilterQEMD3 self) -> float"""
        return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD3_GetRelativeTolerance(self)

    __swig_destroy__ = _itkCleanQuadEdgeMeshFilterPython.delete_itkCleanQuadEdgeMeshFilterQEMD3

    def cast(obj: 'itkLightObject') -> "itkCleanQuadEdgeMeshFilterQEMD3 *":
        """cast(itkLightObject obj) -> itkCleanQuadEdgeMeshFilterQEMD3"""
        return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkCleanQuadEdgeMeshFilterQEMD3

        Create a new object of the class itkCleanQuadEdgeMeshFilterQEMD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCleanQuadEdgeMeshFilterQEMD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCleanQuadEdgeMeshFilterQEMD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCleanQuadEdgeMeshFilterQEMD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCleanQuadEdgeMeshFilterQEMD3.Clone = new_instancemethod(_itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD3_Clone, None, itkCleanQuadEdgeMeshFilterQEMD3)
itkCleanQuadEdgeMeshFilterQEMD3.SetAbsoluteTolerance = new_instancemethod(_itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD3_SetAbsoluteTolerance, None, itkCleanQuadEdgeMeshFilterQEMD3)
itkCleanQuadEdgeMeshFilterQEMD3.GetAbsoluteTolerance = new_instancemethod(_itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD3_GetAbsoluteTolerance, None, itkCleanQuadEdgeMeshFilterQEMD3)
itkCleanQuadEdgeMeshFilterQEMD3.SetRelativeTolerance = new_instancemethod(_itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD3_SetRelativeTolerance, None, itkCleanQuadEdgeMeshFilterQEMD3)
itkCleanQuadEdgeMeshFilterQEMD3.GetRelativeTolerance = new_instancemethod(_itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD3_GetRelativeTolerance, None, itkCleanQuadEdgeMeshFilterQEMD3)
itkCleanQuadEdgeMeshFilterQEMD3_swigregister = _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD3_swigregister
itkCleanQuadEdgeMeshFilterQEMD3_swigregister(itkCleanQuadEdgeMeshFilterQEMD3)

def itkCleanQuadEdgeMeshFilterQEMD3___New_orig__() -> "itkCleanQuadEdgeMeshFilterQEMD3_Pointer":
    """itkCleanQuadEdgeMeshFilterQEMD3___New_orig__() -> itkCleanQuadEdgeMeshFilterQEMD3_Pointer"""
    return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD3___New_orig__()

def itkCleanQuadEdgeMeshFilterQEMD3_cast(obj: 'itkLightObject') -> "itkCleanQuadEdgeMeshFilterQEMD3 *":
    """itkCleanQuadEdgeMeshFilterQEMD3_cast(itkLightObject obj) -> itkCleanQuadEdgeMeshFilterQEMD3"""
    return _itkCleanQuadEdgeMeshFilterPython.itkCleanQuadEdgeMeshFilterQEMD3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def clean_quad_edge_mesh_filter(*args, **kwargs):
    """Procedural interface for CleanQuadEdgeMeshFilter"""
    import itk
    instance = itk.CleanQuadEdgeMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def clean_quad_edge_mesh_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.CleanQuadEdgeMeshFilter, itkTemplate.itkTemplate):
        filter_object = itk.CleanQuadEdgeMeshFilter.values()[0]
    else:
        filter_object = itk.CleanQuadEdgeMeshFilter

    clean_quad_edge_mesh_filter.__doc__ = filter_object.__doc__
    clean_quad_edge_mesh_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    clean_quad_edge_mesh_filter.__doc__ += "Available Keyword Arguments:\n"
    clean_quad_edge_mesh_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



