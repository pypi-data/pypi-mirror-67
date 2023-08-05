# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkFastMarchingStoppingCriterionBasePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkFastMarchingStoppingCriterionBasePython', [dirname(__file__)])
        except ImportError:
            import _itkFastMarchingStoppingCriterionBasePython
            return _itkFastMarchingStoppingCriterionBasePython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkFastMarchingStoppingCriterionBasePython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkFastMarchingStoppingCriterionBasePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkFastMarchingStoppingCriterionBasePython
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


import itkNodePairPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import itkImagePython
import ITKCommonBasePython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkRGBPixelPython
import itkPointPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython

def itkFastMarchingStoppingCriterionBaseID3ID3_New():
  return itkFastMarchingStoppingCriterionBaseID3ID3.New()


def itkFastMarchingStoppingCriterionBaseID2ID2_New():
  return itkFastMarchingStoppingCriterionBaseID2ID2.New()


def itkFastMarchingStoppingCriterionBaseIF3IF3_New():
  return itkFastMarchingStoppingCriterionBaseIF3IF3.New()


def itkFastMarchingStoppingCriterionBaseIF2IF2_New():
  return itkFastMarchingStoppingCriterionBaseIF2IF2.New()

class itkFastMarchingStoppingCriterionBaseID2ID2(ITKCommonBasePython.itkStoppingCriterionBase):
    """


    Abstract Stopping Criterion dedicated for Fast Marching Methods.

    C++ includes: itkFastMarchingStoppingCriterionBase.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Reinitialize(self) -> "void":
        """
        Reinitialize(itkFastMarchingStoppingCriterionBaseID2ID2 self)

        Reinitialize internal
        values. 
        """
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_Reinitialize(self)


    def SetCurrentNodePair(self, iNodePair: 'itkNodePairI2D') -> "void":
        """SetCurrentNodePair(itkFastMarchingStoppingCriterionBaseID2ID2 self, itkNodePairI2D iNodePair)"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_SetCurrentNodePair(self, iNodePair)


    def SetDomain(self, _arg: 'itkImageD2') -> "void":
        """SetDomain(itkFastMarchingStoppingCriterionBaseID2ID2 self, itkImageD2 _arg)"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_SetDomain(self, _arg)


    def GetModifiableDomain(self) -> "itkImageD2 *":
        """GetModifiableDomain(itkFastMarchingStoppingCriterionBaseID2ID2 self) -> itkImageD2"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_GetModifiableDomain(self)


    def GetDomain(self, *args) -> "itkImageD2 *":
        """
        GetDomain(itkFastMarchingStoppingCriterionBaseID2ID2 self) -> itkImageD2
        GetDomain(itkFastMarchingStoppingCriterionBaseID2ID2 self) -> itkImageD2
        """
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_GetDomain(self, *args)

    __swig_destroy__ = _itkFastMarchingStoppingCriterionBasePython.delete_itkFastMarchingStoppingCriterionBaseID2ID2

    def cast(obj: 'itkLightObject') -> "itkFastMarchingStoppingCriterionBaseID2ID2 *":
        """cast(itkLightObject obj) -> itkFastMarchingStoppingCriterionBaseID2ID2"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingStoppingCriterionBaseID2ID2

        Create a new object of the class itkFastMarchingStoppingCriterionBaseID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingStoppingCriterionBaseID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingStoppingCriterionBaseID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingStoppingCriterionBaseID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingStoppingCriterionBaseID2ID2.Reinitialize = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_Reinitialize, None, itkFastMarchingStoppingCriterionBaseID2ID2)
itkFastMarchingStoppingCriterionBaseID2ID2.SetCurrentNodePair = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_SetCurrentNodePair, None, itkFastMarchingStoppingCriterionBaseID2ID2)
itkFastMarchingStoppingCriterionBaseID2ID2.SetDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_SetDomain, None, itkFastMarchingStoppingCriterionBaseID2ID2)
itkFastMarchingStoppingCriterionBaseID2ID2.GetModifiableDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_GetModifiableDomain, None, itkFastMarchingStoppingCriterionBaseID2ID2)
itkFastMarchingStoppingCriterionBaseID2ID2.GetDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_GetDomain, None, itkFastMarchingStoppingCriterionBaseID2ID2)
itkFastMarchingStoppingCriterionBaseID2ID2_swigregister = _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_swigregister
itkFastMarchingStoppingCriterionBaseID2ID2_swigregister(itkFastMarchingStoppingCriterionBaseID2ID2)

def itkFastMarchingStoppingCriterionBaseID2ID2_cast(obj: 'itkLightObject') -> "itkFastMarchingStoppingCriterionBaseID2ID2 *":
    """itkFastMarchingStoppingCriterionBaseID2ID2_cast(itkLightObject obj) -> itkFastMarchingStoppingCriterionBaseID2ID2"""
    return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_cast(obj)

class itkFastMarchingStoppingCriterionBaseID3ID3(ITKCommonBasePython.itkStoppingCriterionBase):
    """


    Abstract Stopping Criterion dedicated for Fast Marching Methods.

    C++ includes: itkFastMarchingStoppingCriterionBase.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Reinitialize(self) -> "void":
        """
        Reinitialize(itkFastMarchingStoppingCriterionBaseID3ID3 self)

        Reinitialize internal
        values. 
        """
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_Reinitialize(self)


    def SetCurrentNodePair(self, iNodePair: 'itkNodePairI3D') -> "void":
        """SetCurrentNodePair(itkFastMarchingStoppingCriterionBaseID3ID3 self, itkNodePairI3D iNodePair)"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_SetCurrentNodePair(self, iNodePair)


    def SetDomain(self, _arg: 'itkImageD3') -> "void":
        """SetDomain(itkFastMarchingStoppingCriterionBaseID3ID3 self, itkImageD3 _arg)"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_SetDomain(self, _arg)


    def GetModifiableDomain(self) -> "itkImageD3 *":
        """GetModifiableDomain(itkFastMarchingStoppingCriterionBaseID3ID3 self) -> itkImageD3"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_GetModifiableDomain(self)


    def GetDomain(self, *args) -> "itkImageD3 *":
        """
        GetDomain(itkFastMarchingStoppingCriterionBaseID3ID3 self) -> itkImageD3
        GetDomain(itkFastMarchingStoppingCriterionBaseID3ID3 self) -> itkImageD3
        """
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_GetDomain(self, *args)

    __swig_destroy__ = _itkFastMarchingStoppingCriterionBasePython.delete_itkFastMarchingStoppingCriterionBaseID3ID3

    def cast(obj: 'itkLightObject') -> "itkFastMarchingStoppingCriterionBaseID3ID3 *":
        """cast(itkLightObject obj) -> itkFastMarchingStoppingCriterionBaseID3ID3"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingStoppingCriterionBaseID3ID3

        Create a new object of the class itkFastMarchingStoppingCriterionBaseID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingStoppingCriterionBaseID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingStoppingCriterionBaseID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingStoppingCriterionBaseID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingStoppingCriterionBaseID3ID3.Reinitialize = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_Reinitialize, None, itkFastMarchingStoppingCriterionBaseID3ID3)
itkFastMarchingStoppingCriterionBaseID3ID3.SetCurrentNodePair = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_SetCurrentNodePair, None, itkFastMarchingStoppingCriterionBaseID3ID3)
itkFastMarchingStoppingCriterionBaseID3ID3.SetDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_SetDomain, None, itkFastMarchingStoppingCriterionBaseID3ID3)
itkFastMarchingStoppingCriterionBaseID3ID3.GetModifiableDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_GetModifiableDomain, None, itkFastMarchingStoppingCriterionBaseID3ID3)
itkFastMarchingStoppingCriterionBaseID3ID3.GetDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_GetDomain, None, itkFastMarchingStoppingCriterionBaseID3ID3)
itkFastMarchingStoppingCriterionBaseID3ID3_swigregister = _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_swigregister
itkFastMarchingStoppingCriterionBaseID3ID3_swigregister(itkFastMarchingStoppingCriterionBaseID3ID3)

def itkFastMarchingStoppingCriterionBaseID3ID3_cast(obj: 'itkLightObject') -> "itkFastMarchingStoppingCriterionBaseID3ID3 *":
    """itkFastMarchingStoppingCriterionBaseID3ID3_cast(itkLightObject obj) -> itkFastMarchingStoppingCriterionBaseID3ID3"""
    return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_cast(obj)

class itkFastMarchingStoppingCriterionBaseIF2IF2(ITKCommonBasePython.itkStoppingCriterionBase):
    """


    Abstract Stopping Criterion dedicated for Fast Marching Methods.

    C++ includes: itkFastMarchingStoppingCriterionBase.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Reinitialize(self) -> "void":
        """
        Reinitialize(itkFastMarchingStoppingCriterionBaseIF2IF2 self)

        Reinitialize internal
        values. 
        """
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_Reinitialize(self)


    def SetCurrentNodePair(self, iNodePair: 'itkNodePairI2F') -> "void":
        """SetCurrentNodePair(itkFastMarchingStoppingCriterionBaseIF2IF2 self, itkNodePairI2F iNodePair)"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_SetCurrentNodePair(self, iNodePair)


    def SetDomain(self, _arg: 'itkImageF2') -> "void":
        """SetDomain(itkFastMarchingStoppingCriterionBaseIF2IF2 self, itkImageF2 _arg)"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_SetDomain(self, _arg)


    def GetModifiableDomain(self) -> "itkImageF2 *":
        """GetModifiableDomain(itkFastMarchingStoppingCriterionBaseIF2IF2 self) -> itkImageF2"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_GetModifiableDomain(self)


    def GetDomain(self, *args) -> "itkImageF2 *":
        """
        GetDomain(itkFastMarchingStoppingCriterionBaseIF2IF2 self) -> itkImageF2
        GetDomain(itkFastMarchingStoppingCriterionBaseIF2IF2 self) -> itkImageF2
        """
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_GetDomain(self, *args)

    __swig_destroy__ = _itkFastMarchingStoppingCriterionBasePython.delete_itkFastMarchingStoppingCriterionBaseIF2IF2

    def cast(obj: 'itkLightObject') -> "itkFastMarchingStoppingCriterionBaseIF2IF2 *":
        """cast(itkLightObject obj) -> itkFastMarchingStoppingCriterionBaseIF2IF2"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingStoppingCriterionBaseIF2IF2

        Create a new object of the class itkFastMarchingStoppingCriterionBaseIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingStoppingCriterionBaseIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingStoppingCriterionBaseIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingStoppingCriterionBaseIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingStoppingCriterionBaseIF2IF2.Reinitialize = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_Reinitialize, None, itkFastMarchingStoppingCriterionBaseIF2IF2)
itkFastMarchingStoppingCriterionBaseIF2IF2.SetCurrentNodePair = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_SetCurrentNodePair, None, itkFastMarchingStoppingCriterionBaseIF2IF2)
itkFastMarchingStoppingCriterionBaseIF2IF2.SetDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_SetDomain, None, itkFastMarchingStoppingCriterionBaseIF2IF2)
itkFastMarchingStoppingCriterionBaseIF2IF2.GetModifiableDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_GetModifiableDomain, None, itkFastMarchingStoppingCriterionBaseIF2IF2)
itkFastMarchingStoppingCriterionBaseIF2IF2.GetDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_GetDomain, None, itkFastMarchingStoppingCriterionBaseIF2IF2)
itkFastMarchingStoppingCriterionBaseIF2IF2_swigregister = _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_swigregister
itkFastMarchingStoppingCriterionBaseIF2IF2_swigregister(itkFastMarchingStoppingCriterionBaseIF2IF2)

def itkFastMarchingStoppingCriterionBaseIF2IF2_cast(obj: 'itkLightObject') -> "itkFastMarchingStoppingCriterionBaseIF2IF2 *":
    """itkFastMarchingStoppingCriterionBaseIF2IF2_cast(itkLightObject obj) -> itkFastMarchingStoppingCriterionBaseIF2IF2"""
    return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_cast(obj)

class itkFastMarchingStoppingCriterionBaseIF3IF3(ITKCommonBasePython.itkStoppingCriterionBase):
    """


    Abstract Stopping Criterion dedicated for Fast Marching Methods.

    C++ includes: itkFastMarchingStoppingCriterionBase.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Reinitialize(self) -> "void":
        """
        Reinitialize(itkFastMarchingStoppingCriterionBaseIF3IF3 self)

        Reinitialize internal
        values. 
        """
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_Reinitialize(self)


    def SetCurrentNodePair(self, iNodePair: 'itkNodePairI3F') -> "void":
        """SetCurrentNodePair(itkFastMarchingStoppingCriterionBaseIF3IF3 self, itkNodePairI3F iNodePair)"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_SetCurrentNodePair(self, iNodePair)


    def SetDomain(self, _arg: 'itkImageF3') -> "void":
        """SetDomain(itkFastMarchingStoppingCriterionBaseIF3IF3 self, itkImageF3 _arg)"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_SetDomain(self, _arg)


    def GetModifiableDomain(self) -> "itkImageF3 *":
        """GetModifiableDomain(itkFastMarchingStoppingCriterionBaseIF3IF3 self) -> itkImageF3"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_GetModifiableDomain(self)


    def GetDomain(self, *args) -> "itkImageF3 *":
        """
        GetDomain(itkFastMarchingStoppingCriterionBaseIF3IF3 self) -> itkImageF3
        GetDomain(itkFastMarchingStoppingCriterionBaseIF3IF3 self) -> itkImageF3
        """
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_GetDomain(self, *args)

    __swig_destroy__ = _itkFastMarchingStoppingCriterionBasePython.delete_itkFastMarchingStoppingCriterionBaseIF3IF3

    def cast(obj: 'itkLightObject') -> "itkFastMarchingStoppingCriterionBaseIF3IF3 *":
        """cast(itkLightObject obj) -> itkFastMarchingStoppingCriterionBaseIF3IF3"""
        return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingStoppingCriterionBaseIF3IF3

        Create a new object of the class itkFastMarchingStoppingCriterionBaseIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingStoppingCriterionBaseIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingStoppingCriterionBaseIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingStoppingCriterionBaseIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingStoppingCriterionBaseIF3IF3.Reinitialize = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_Reinitialize, None, itkFastMarchingStoppingCriterionBaseIF3IF3)
itkFastMarchingStoppingCriterionBaseIF3IF3.SetCurrentNodePair = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_SetCurrentNodePair, None, itkFastMarchingStoppingCriterionBaseIF3IF3)
itkFastMarchingStoppingCriterionBaseIF3IF3.SetDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_SetDomain, None, itkFastMarchingStoppingCriterionBaseIF3IF3)
itkFastMarchingStoppingCriterionBaseIF3IF3.GetModifiableDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_GetModifiableDomain, None, itkFastMarchingStoppingCriterionBaseIF3IF3)
itkFastMarchingStoppingCriterionBaseIF3IF3.GetDomain = new_instancemethod(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_GetDomain, None, itkFastMarchingStoppingCriterionBaseIF3IF3)
itkFastMarchingStoppingCriterionBaseIF3IF3_swigregister = _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_swigregister
itkFastMarchingStoppingCriterionBaseIF3IF3_swigregister(itkFastMarchingStoppingCriterionBaseIF3IF3)

def itkFastMarchingStoppingCriterionBaseIF3IF3_cast(obj: 'itkLightObject') -> "itkFastMarchingStoppingCriterionBaseIF3IF3 *":
    """itkFastMarchingStoppingCriterionBaseIF3IF3_cast(itkLightObject obj) -> itkFastMarchingStoppingCriterionBaseIF3IF3"""
    return _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_cast(obj)



