# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkFastMarchingThresholdStoppingCriterionPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkFastMarchingThresholdStoppingCriterionPython', [dirname(__file__)])
        except ImportError:
            import _itkFastMarchingThresholdStoppingCriterionPython
            return _itkFastMarchingThresholdStoppingCriterionPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkFastMarchingThresholdStoppingCriterionPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkFastMarchingThresholdStoppingCriterionPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkFastMarchingThresholdStoppingCriterionPython
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
import itkFastMarchingStoppingCriterionBasePython
import itkNodePairPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkImagePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkCovariantVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython

def itkFastMarchingThresholdStoppingCriterionID3ID3_New():
  return itkFastMarchingThresholdStoppingCriterionID3ID3.New()


def itkFastMarchingThresholdStoppingCriterionID2ID2_New():
  return itkFastMarchingThresholdStoppingCriterionID2ID2.New()


def itkFastMarchingThresholdStoppingCriterionIF3IF3_New():
  return itkFastMarchingThresholdStoppingCriterionIF3IF3.New()


def itkFastMarchingThresholdStoppingCriterionIF2IF2_New():
  return itkFastMarchingThresholdStoppingCriterionIF2IF2.New()

class itkFastMarchingThresholdStoppingCriterionID2ID2(itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2):
    """


    Stopping Criterion is verified when Current Value is equal to or
    greater than the provided threshold.

    C++ includes: itkFastMarchingThresholdStoppingCriterion.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingThresholdStoppingCriterionID2ID2_Pointer":
        """__New_orig__() -> itkFastMarchingThresholdStoppingCriterionID2ID2_Pointer"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingThresholdStoppingCriterionID2ID2_Pointer":
        """Clone(itkFastMarchingThresholdStoppingCriterionID2ID2 self) -> itkFastMarchingThresholdStoppingCriterionID2ID2_Pointer"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2_Clone(self)


    def SetThreshold(self, _arg: 'double const') -> "void":
        """
        SetThreshold(itkFastMarchingThresholdStoppingCriterionID2ID2 self, double const _arg)

        Get/set the threshold
        used by the stopping criteria. 
        """
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2_SetThreshold(self, _arg)


    def GetThreshold(self) -> "double":
        """GetThreshold(itkFastMarchingThresholdStoppingCriterionID2ID2 self) -> double"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2_GetThreshold(self)

    __swig_destroy__ = _itkFastMarchingThresholdStoppingCriterionPython.delete_itkFastMarchingThresholdStoppingCriterionID2ID2

    def cast(obj: 'itkLightObject') -> "itkFastMarchingThresholdStoppingCriterionID2ID2 *":
        """cast(itkLightObject obj) -> itkFastMarchingThresholdStoppingCriterionID2ID2"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingThresholdStoppingCriterionID2ID2

        Create a new object of the class itkFastMarchingThresholdStoppingCriterionID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingThresholdStoppingCriterionID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingThresholdStoppingCriterionID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingThresholdStoppingCriterionID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingThresholdStoppingCriterionID2ID2.Clone = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2_Clone, None, itkFastMarchingThresholdStoppingCriterionID2ID2)
itkFastMarchingThresholdStoppingCriterionID2ID2.SetThreshold = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2_SetThreshold, None, itkFastMarchingThresholdStoppingCriterionID2ID2)
itkFastMarchingThresholdStoppingCriterionID2ID2.GetThreshold = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2_GetThreshold, None, itkFastMarchingThresholdStoppingCriterionID2ID2)
itkFastMarchingThresholdStoppingCriterionID2ID2_swigregister = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2_swigregister
itkFastMarchingThresholdStoppingCriterionID2ID2_swigregister(itkFastMarchingThresholdStoppingCriterionID2ID2)

def itkFastMarchingThresholdStoppingCriterionID2ID2___New_orig__() -> "itkFastMarchingThresholdStoppingCriterionID2ID2_Pointer":
    """itkFastMarchingThresholdStoppingCriterionID2ID2___New_orig__() -> itkFastMarchingThresholdStoppingCriterionID2ID2_Pointer"""
    return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2___New_orig__()

def itkFastMarchingThresholdStoppingCriterionID2ID2_cast(obj: 'itkLightObject') -> "itkFastMarchingThresholdStoppingCriterionID2ID2 *":
    """itkFastMarchingThresholdStoppingCriterionID2ID2_cast(itkLightObject obj) -> itkFastMarchingThresholdStoppingCriterionID2ID2"""
    return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2_cast(obj)

class itkFastMarchingThresholdStoppingCriterionID3ID3(itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3):
    """


    Stopping Criterion is verified when Current Value is equal to or
    greater than the provided threshold.

    C++ includes: itkFastMarchingThresholdStoppingCriterion.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingThresholdStoppingCriterionID3ID3_Pointer":
        """__New_orig__() -> itkFastMarchingThresholdStoppingCriterionID3ID3_Pointer"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingThresholdStoppingCriterionID3ID3_Pointer":
        """Clone(itkFastMarchingThresholdStoppingCriterionID3ID3 self) -> itkFastMarchingThresholdStoppingCriterionID3ID3_Pointer"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3_Clone(self)


    def SetThreshold(self, _arg: 'double const') -> "void":
        """
        SetThreshold(itkFastMarchingThresholdStoppingCriterionID3ID3 self, double const _arg)

        Get/set the threshold
        used by the stopping criteria. 
        """
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3_SetThreshold(self, _arg)


    def GetThreshold(self) -> "double":
        """GetThreshold(itkFastMarchingThresholdStoppingCriterionID3ID3 self) -> double"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3_GetThreshold(self)

    __swig_destroy__ = _itkFastMarchingThresholdStoppingCriterionPython.delete_itkFastMarchingThresholdStoppingCriterionID3ID3

    def cast(obj: 'itkLightObject') -> "itkFastMarchingThresholdStoppingCriterionID3ID3 *":
        """cast(itkLightObject obj) -> itkFastMarchingThresholdStoppingCriterionID3ID3"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingThresholdStoppingCriterionID3ID3

        Create a new object of the class itkFastMarchingThresholdStoppingCriterionID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingThresholdStoppingCriterionID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingThresholdStoppingCriterionID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingThresholdStoppingCriterionID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingThresholdStoppingCriterionID3ID3.Clone = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3_Clone, None, itkFastMarchingThresholdStoppingCriterionID3ID3)
itkFastMarchingThresholdStoppingCriterionID3ID3.SetThreshold = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3_SetThreshold, None, itkFastMarchingThresholdStoppingCriterionID3ID3)
itkFastMarchingThresholdStoppingCriterionID3ID3.GetThreshold = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3_GetThreshold, None, itkFastMarchingThresholdStoppingCriterionID3ID3)
itkFastMarchingThresholdStoppingCriterionID3ID3_swigregister = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3_swigregister
itkFastMarchingThresholdStoppingCriterionID3ID3_swigregister(itkFastMarchingThresholdStoppingCriterionID3ID3)

def itkFastMarchingThresholdStoppingCriterionID3ID3___New_orig__() -> "itkFastMarchingThresholdStoppingCriterionID3ID3_Pointer":
    """itkFastMarchingThresholdStoppingCriterionID3ID3___New_orig__() -> itkFastMarchingThresholdStoppingCriterionID3ID3_Pointer"""
    return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3___New_orig__()

def itkFastMarchingThresholdStoppingCriterionID3ID3_cast(obj: 'itkLightObject') -> "itkFastMarchingThresholdStoppingCriterionID3ID3 *":
    """itkFastMarchingThresholdStoppingCriterionID3ID3_cast(itkLightObject obj) -> itkFastMarchingThresholdStoppingCriterionID3ID3"""
    return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3_cast(obj)

class itkFastMarchingThresholdStoppingCriterionIF2IF2(itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2):
    """


    Stopping Criterion is verified when Current Value is equal to or
    greater than the provided threshold.

    C++ includes: itkFastMarchingThresholdStoppingCriterion.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingThresholdStoppingCriterionIF2IF2_Pointer":
        """__New_orig__() -> itkFastMarchingThresholdStoppingCriterionIF2IF2_Pointer"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingThresholdStoppingCriterionIF2IF2_Pointer":
        """Clone(itkFastMarchingThresholdStoppingCriterionIF2IF2 self) -> itkFastMarchingThresholdStoppingCriterionIF2IF2_Pointer"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_Clone(self)


    def SetThreshold(self, _arg: 'float const') -> "void":
        """
        SetThreshold(itkFastMarchingThresholdStoppingCriterionIF2IF2 self, float const _arg)

        Get/set the threshold
        used by the stopping criteria. 
        """
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_SetThreshold(self, _arg)


    def GetThreshold(self) -> "float":
        """GetThreshold(itkFastMarchingThresholdStoppingCriterionIF2IF2 self) -> float"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_GetThreshold(self)

    __swig_destroy__ = _itkFastMarchingThresholdStoppingCriterionPython.delete_itkFastMarchingThresholdStoppingCriterionIF2IF2

    def cast(obj: 'itkLightObject') -> "itkFastMarchingThresholdStoppingCriterionIF2IF2 *":
        """cast(itkLightObject obj) -> itkFastMarchingThresholdStoppingCriterionIF2IF2"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingThresholdStoppingCriterionIF2IF2

        Create a new object of the class itkFastMarchingThresholdStoppingCriterionIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingThresholdStoppingCriterionIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingThresholdStoppingCriterionIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingThresholdStoppingCriterionIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingThresholdStoppingCriterionIF2IF2.Clone = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_Clone, None, itkFastMarchingThresholdStoppingCriterionIF2IF2)
itkFastMarchingThresholdStoppingCriterionIF2IF2.SetThreshold = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_SetThreshold, None, itkFastMarchingThresholdStoppingCriterionIF2IF2)
itkFastMarchingThresholdStoppingCriterionIF2IF2.GetThreshold = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_GetThreshold, None, itkFastMarchingThresholdStoppingCriterionIF2IF2)
itkFastMarchingThresholdStoppingCriterionIF2IF2_swigregister = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_swigregister
itkFastMarchingThresholdStoppingCriterionIF2IF2_swigregister(itkFastMarchingThresholdStoppingCriterionIF2IF2)

def itkFastMarchingThresholdStoppingCriterionIF2IF2___New_orig__() -> "itkFastMarchingThresholdStoppingCriterionIF2IF2_Pointer":
    """itkFastMarchingThresholdStoppingCriterionIF2IF2___New_orig__() -> itkFastMarchingThresholdStoppingCriterionIF2IF2_Pointer"""
    return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2___New_orig__()

def itkFastMarchingThresholdStoppingCriterionIF2IF2_cast(obj: 'itkLightObject') -> "itkFastMarchingThresholdStoppingCriterionIF2IF2 *":
    """itkFastMarchingThresholdStoppingCriterionIF2IF2_cast(itkLightObject obj) -> itkFastMarchingThresholdStoppingCriterionIF2IF2"""
    return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_cast(obj)

class itkFastMarchingThresholdStoppingCriterionIF3IF3(itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3):
    """


    Stopping Criterion is verified when Current Value is equal to or
    greater than the provided threshold.

    C++ includes: itkFastMarchingThresholdStoppingCriterion.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFastMarchingThresholdStoppingCriterionIF3IF3_Pointer":
        """__New_orig__() -> itkFastMarchingThresholdStoppingCriterionIF3IF3_Pointer"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFastMarchingThresholdStoppingCriterionIF3IF3_Pointer":
        """Clone(itkFastMarchingThresholdStoppingCriterionIF3IF3 self) -> itkFastMarchingThresholdStoppingCriterionIF3IF3_Pointer"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_Clone(self)


    def SetThreshold(self, _arg: 'float const') -> "void":
        """
        SetThreshold(itkFastMarchingThresholdStoppingCriterionIF3IF3 self, float const _arg)

        Get/set the threshold
        used by the stopping criteria. 
        """
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_SetThreshold(self, _arg)


    def GetThreshold(self) -> "float":
        """GetThreshold(itkFastMarchingThresholdStoppingCriterionIF3IF3 self) -> float"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_GetThreshold(self)

    __swig_destroy__ = _itkFastMarchingThresholdStoppingCriterionPython.delete_itkFastMarchingThresholdStoppingCriterionIF3IF3

    def cast(obj: 'itkLightObject') -> "itkFastMarchingThresholdStoppingCriterionIF3IF3 *":
        """cast(itkLightObject obj) -> itkFastMarchingThresholdStoppingCriterionIF3IF3"""
        return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingThresholdStoppingCriterionIF3IF3

        Create a new object of the class itkFastMarchingThresholdStoppingCriterionIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingThresholdStoppingCriterionIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFastMarchingThresholdStoppingCriterionIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFastMarchingThresholdStoppingCriterionIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFastMarchingThresholdStoppingCriterionIF3IF3.Clone = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_Clone, None, itkFastMarchingThresholdStoppingCriterionIF3IF3)
itkFastMarchingThresholdStoppingCriterionIF3IF3.SetThreshold = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_SetThreshold, None, itkFastMarchingThresholdStoppingCriterionIF3IF3)
itkFastMarchingThresholdStoppingCriterionIF3IF3.GetThreshold = new_instancemethod(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_GetThreshold, None, itkFastMarchingThresholdStoppingCriterionIF3IF3)
itkFastMarchingThresholdStoppingCriterionIF3IF3_swigregister = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_swigregister
itkFastMarchingThresholdStoppingCriterionIF3IF3_swigregister(itkFastMarchingThresholdStoppingCriterionIF3IF3)

def itkFastMarchingThresholdStoppingCriterionIF3IF3___New_orig__() -> "itkFastMarchingThresholdStoppingCriterionIF3IF3_Pointer":
    """itkFastMarchingThresholdStoppingCriterionIF3IF3___New_orig__() -> itkFastMarchingThresholdStoppingCriterionIF3IF3_Pointer"""
    return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3___New_orig__()

def itkFastMarchingThresholdStoppingCriterionIF3IF3_cast(obj: 'itkLightObject') -> "itkFastMarchingThresholdStoppingCriterionIF3IF3 *":
    """itkFastMarchingThresholdStoppingCriterionIF3IF3_cast(itkLightObject obj) -> itkFastMarchingThresholdStoppingCriterionIF3IF3"""
    return _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_cast(obj)



