# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkUnsharpMaskLevelSetImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkUnsharpMaskLevelSetImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkUnsharpMaskLevelSetImageFilterPython
            return _itkUnsharpMaskLevelSetImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkUnsharpMaskLevelSetImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkUnsharpMaskLevelSetImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkUnsharpMaskLevelSetImageFilterPython
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
import itkSparseFieldFourthOrderLevelSetImageFilterPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkLevelSetFunctionPython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkFiniteDifferenceFunctionPython
import itkCovariantVectorPython
import itkSparseFieldLevelSetImageFilterPython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImagePython
import itkRGBAPixelPython
import itkPointPython
import itkRGBPixelPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterAPython

def itkUnsharpMaskLevelSetImageFilterID3ID3_New():
  return itkUnsharpMaskLevelSetImageFilterID3ID3.New()


def itkUnsharpMaskLevelSetImageFilterID2ID2_New():
  return itkUnsharpMaskLevelSetImageFilterID2ID2.New()


def itkUnsharpMaskLevelSetImageFilterIF3IF3_New():
  return itkUnsharpMaskLevelSetImageFilterIF3IF3.New()


def itkUnsharpMaskLevelSetImageFilterIF2IF2_New():
  return itkUnsharpMaskLevelSetImageFilterIF2IF2.New()

class itkUnsharpMaskLevelSetImageFilterID2ID2(itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterID2ID2):
    """


    This class implements a detail enhancing filter by making use of the
    4th-order level set isotropic diffusion (smoothing) PDE.

    INPUT and OUTPUT This is a volume to volume filter; however, it is
    meant to process (smooth) surfaces. The input surface is an isosurface
    of the input volume. The isosurface value to be processed can be set
    by calling SetIsoSurfaceValue (default is 0). The output surface is
    the 0-isosurface of the output volume, regardless of the input
    isosurface value. To visualize the input/output surfaces to this
    filter a mesh extraction method such as marching cubes can be used.

    be used for general purpose surface processing. It is motivated by
    unsharp masking from image processing which is a way of enhancing
    detail. This filter acts much like the
    IsotropicFourthOrderLevelSetImageFilter because it first smoothes the
    normal vectors via isotropic diffusion. However, as a post-processing
    step we extrapolate from the original normals in the direction
    opposite to the new processes normals. By refitting the surface to
    these extrapolated vectors we achieve detail enhancement. This process
    is not the same as running the isotropic diffusion process in reverse.
    IMPORTANT Because this filters enhances details on the surface, it
    will also amplify post-processing. Do not use it on noisy data.
    PARAMETERS As mentioned before, the IsoSurfaceValue parameter chooses
    which isosurface of the input to process. The MaxFilterIterations
    parameter determine the number of iterations for which this filter
    will run. Since, this filter enhances detail AND noise
    MaxFilterIterations above a couple of hundred are unreasonable.
    Finally NormalProcessUnsharpWeight controls the amount of
    extrapolation (or equivalently the amount of detail enhancement). This
    value should be in the range [0.1,1] for reasonable results.

    C++ includes: itkUnsharpMaskLevelSetImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkUnsharpMaskLevelSetImageFilterID2ID2_Pointer":
        """__New_orig__() -> itkUnsharpMaskLevelSetImageFilterID2ID2_Pointer"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkUnsharpMaskLevelSetImageFilterID2ID2_Pointer":
        """Clone(itkUnsharpMaskLevelSetImageFilterID2ID2 self) -> itkUnsharpMaskLevelSetImageFilterID2ID2_Pointer"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2_Clone(self)


    def GetMaxFilterIteration(self) -> "unsigned int":
        """GetMaxFilterIteration(itkUnsharpMaskLevelSetImageFilterID2ID2 self) -> unsigned int"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2_GetMaxFilterIteration(self)


    def SetMaxFilterIteration(self, _arg: 'unsigned int const') -> "void":
        """SetMaxFilterIteration(itkUnsharpMaskLevelSetImageFilterID2ID2 self, unsigned int const _arg)"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2_SetMaxFilterIteration(self, _arg)

    __swig_destroy__ = _itkUnsharpMaskLevelSetImageFilterPython.delete_itkUnsharpMaskLevelSetImageFilterID2ID2

    def cast(obj: 'itkLightObject') -> "itkUnsharpMaskLevelSetImageFilterID2ID2 *":
        """cast(itkLightObject obj) -> itkUnsharpMaskLevelSetImageFilterID2ID2"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkUnsharpMaskLevelSetImageFilterID2ID2

        Create a new object of the class itkUnsharpMaskLevelSetImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnsharpMaskLevelSetImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkUnsharpMaskLevelSetImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkUnsharpMaskLevelSetImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkUnsharpMaskLevelSetImageFilterID2ID2.Clone = new_instancemethod(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2_Clone, None, itkUnsharpMaskLevelSetImageFilterID2ID2)
itkUnsharpMaskLevelSetImageFilterID2ID2.GetMaxFilterIteration = new_instancemethod(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2_GetMaxFilterIteration, None, itkUnsharpMaskLevelSetImageFilterID2ID2)
itkUnsharpMaskLevelSetImageFilterID2ID2.SetMaxFilterIteration = new_instancemethod(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2_SetMaxFilterIteration, None, itkUnsharpMaskLevelSetImageFilterID2ID2)
itkUnsharpMaskLevelSetImageFilterID2ID2_swigregister = _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2_swigregister
itkUnsharpMaskLevelSetImageFilterID2ID2_swigregister(itkUnsharpMaskLevelSetImageFilterID2ID2)

def itkUnsharpMaskLevelSetImageFilterID2ID2___New_orig__() -> "itkUnsharpMaskLevelSetImageFilterID2ID2_Pointer":
    """itkUnsharpMaskLevelSetImageFilterID2ID2___New_orig__() -> itkUnsharpMaskLevelSetImageFilterID2ID2_Pointer"""
    return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2___New_orig__()

def itkUnsharpMaskLevelSetImageFilterID2ID2_cast(obj: 'itkLightObject') -> "itkUnsharpMaskLevelSetImageFilterID2ID2 *":
    """itkUnsharpMaskLevelSetImageFilterID2ID2_cast(itkLightObject obj) -> itkUnsharpMaskLevelSetImageFilterID2ID2"""
    return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2_cast(obj)

class itkUnsharpMaskLevelSetImageFilterID3ID3(itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterID3ID3):
    """


    This class implements a detail enhancing filter by making use of the
    4th-order level set isotropic diffusion (smoothing) PDE.

    INPUT and OUTPUT This is a volume to volume filter; however, it is
    meant to process (smooth) surfaces. The input surface is an isosurface
    of the input volume. The isosurface value to be processed can be set
    by calling SetIsoSurfaceValue (default is 0). The output surface is
    the 0-isosurface of the output volume, regardless of the input
    isosurface value. To visualize the input/output surfaces to this
    filter a mesh extraction method such as marching cubes can be used.

    be used for general purpose surface processing. It is motivated by
    unsharp masking from image processing which is a way of enhancing
    detail. This filter acts much like the
    IsotropicFourthOrderLevelSetImageFilter because it first smoothes the
    normal vectors via isotropic diffusion. However, as a post-processing
    step we extrapolate from the original normals in the direction
    opposite to the new processes normals. By refitting the surface to
    these extrapolated vectors we achieve detail enhancement. This process
    is not the same as running the isotropic diffusion process in reverse.
    IMPORTANT Because this filters enhances details on the surface, it
    will also amplify post-processing. Do not use it on noisy data.
    PARAMETERS As mentioned before, the IsoSurfaceValue parameter chooses
    which isosurface of the input to process. The MaxFilterIterations
    parameter determine the number of iterations for which this filter
    will run. Since, this filter enhances detail AND noise
    MaxFilterIterations above a couple of hundred are unreasonable.
    Finally NormalProcessUnsharpWeight controls the amount of
    extrapolation (or equivalently the amount of detail enhancement). This
    value should be in the range [0.1,1] for reasonable results.

    C++ includes: itkUnsharpMaskLevelSetImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkUnsharpMaskLevelSetImageFilterID3ID3_Pointer":
        """__New_orig__() -> itkUnsharpMaskLevelSetImageFilterID3ID3_Pointer"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkUnsharpMaskLevelSetImageFilterID3ID3_Pointer":
        """Clone(itkUnsharpMaskLevelSetImageFilterID3ID3 self) -> itkUnsharpMaskLevelSetImageFilterID3ID3_Pointer"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3_Clone(self)


    def GetMaxFilterIteration(self) -> "unsigned int":
        """GetMaxFilterIteration(itkUnsharpMaskLevelSetImageFilterID3ID3 self) -> unsigned int"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3_GetMaxFilterIteration(self)


    def SetMaxFilterIteration(self, _arg: 'unsigned int const') -> "void":
        """SetMaxFilterIteration(itkUnsharpMaskLevelSetImageFilterID3ID3 self, unsigned int const _arg)"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3_SetMaxFilterIteration(self, _arg)

    __swig_destroy__ = _itkUnsharpMaskLevelSetImageFilterPython.delete_itkUnsharpMaskLevelSetImageFilterID3ID3

    def cast(obj: 'itkLightObject') -> "itkUnsharpMaskLevelSetImageFilterID3ID3 *":
        """cast(itkLightObject obj) -> itkUnsharpMaskLevelSetImageFilterID3ID3"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkUnsharpMaskLevelSetImageFilterID3ID3

        Create a new object of the class itkUnsharpMaskLevelSetImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnsharpMaskLevelSetImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkUnsharpMaskLevelSetImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkUnsharpMaskLevelSetImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkUnsharpMaskLevelSetImageFilterID3ID3.Clone = new_instancemethod(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3_Clone, None, itkUnsharpMaskLevelSetImageFilterID3ID3)
itkUnsharpMaskLevelSetImageFilterID3ID3.GetMaxFilterIteration = new_instancemethod(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3_GetMaxFilterIteration, None, itkUnsharpMaskLevelSetImageFilterID3ID3)
itkUnsharpMaskLevelSetImageFilterID3ID3.SetMaxFilterIteration = new_instancemethod(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3_SetMaxFilterIteration, None, itkUnsharpMaskLevelSetImageFilterID3ID3)
itkUnsharpMaskLevelSetImageFilterID3ID3_swigregister = _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3_swigregister
itkUnsharpMaskLevelSetImageFilterID3ID3_swigregister(itkUnsharpMaskLevelSetImageFilterID3ID3)

def itkUnsharpMaskLevelSetImageFilterID3ID3___New_orig__() -> "itkUnsharpMaskLevelSetImageFilterID3ID3_Pointer":
    """itkUnsharpMaskLevelSetImageFilterID3ID3___New_orig__() -> itkUnsharpMaskLevelSetImageFilterID3ID3_Pointer"""
    return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3___New_orig__()

def itkUnsharpMaskLevelSetImageFilterID3ID3_cast(obj: 'itkLightObject') -> "itkUnsharpMaskLevelSetImageFilterID3ID3 *":
    """itkUnsharpMaskLevelSetImageFilterID3ID3_cast(itkLightObject obj) -> itkUnsharpMaskLevelSetImageFilterID3ID3"""
    return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3_cast(obj)

class itkUnsharpMaskLevelSetImageFilterIF2IF2(itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterIF2IF2):
    """


    This class implements a detail enhancing filter by making use of the
    4th-order level set isotropic diffusion (smoothing) PDE.

    INPUT and OUTPUT This is a volume to volume filter; however, it is
    meant to process (smooth) surfaces. The input surface is an isosurface
    of the input volume. The isosurface value to be processed can be set
    by calling SetIsoSurfaceValue (default is 0). The output surface is
    the 0-isosurface of the output volume, regardless of the input
    isosurface value. To visualize the input/output surfaces to this
    filter a mesh extraction method such as marching cubes can be used.

    be used for general purpose surface processing. It is motivated by
    unsharp masking from image processing which is a way of enhancing
    detail. This filter acts much like the
    IsotropicFourthOrderLevelSetImageFilter because it first smoothes the
    normal vectors via isotropic diffusion. However, as a post-processing
    step we extrapolate from the original normals in the direction
    opposite to the new processes normals. By refitting the surface to
    these extrapolated vectors we achieve detail enhancement. This process
    is not the same as running the isotropic diffusion process in reverse.
    IMPORTANT Because this filters enhances details on the surface, it
    will also amplify post-processing. Do not use it on noisy data.
    PARAMETERS As mentioned before, the IsoSurfaceValue parameter chooses
    which isosurface of the input to process. The MaxFilterIterations
    parameter determine the number of iterations for which this filter
    will run. Since, this filter enhances detail AND noise
    MaxFilterIterations above a couple of hundred are unreasonable.
    Finally NormalProcessUnsharpWeight controls the amount of
    extrapolation (or equivalently the amount of detail enhancement). This
    value should be in the range [0.1,1] for reasonable results.

    C++ includes: itkUnsharpMaskLevelSetImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkUnsharpMaskLevelSetImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkUnsharpMaskLevelSetImageFilterIF2IF2_Pointer"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkUnsharpMaskLevelSetImageFilterIF2IF2_Pointer":
        """Clone(itkUnsharpMaskLevelSetImageFilterIF2IF2 self) -> itkUnsharpMaskLevelSetImageFilterIF2IF2_Pointer"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2_Clone(self)


    def GetMaxFilterIteration(self) -> "unsigned int":
        """GetMaxFilterIteration(itkUnsharpMaskLevelSetImageFilterIF2IF2 self) -> unsigned int"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2_GetMaxFilterIteration(self)


    def SetMaxFilterIteration(self, _arg: 'unsigned int const') -> "void":
        """SetMaxFilterIteration(itkUnsharpMaskLevelSetImageFilterIF2IF2 self, unsigned int const _arg)"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2_SetMaxFilterIteration(self, _arg)

    __swig_destroy__ = _itkUnsharpMaskLevelSetImageFilterPython.delete_itkUnsharpMaskLevelSetImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkUnsharpMaskLevelSetImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkUnsharpMaskLevelSetImageFilterIF2IF2"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkUnsharpMaskLevelSetImageFilterIF2IF2

        Create a new object of the class itkUnsharpMaskLevelSetImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnsharpMaskLevelSetImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkUnsharpMaskLevelSetImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkUnsharpMaskLevelSetImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkUnsharpMaskLevelSetImageFilterIF2IF2.Clone = new_instancemethod(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2_Clone, None, itkUnsharpMaskLevelSetImageFilterIF2IF2)
itkUnsharpMaskLevelSetImageFilterIF2IF2.GetMaxFilterIteration = new_instancemethod(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2_GetMaxFilterIteration, None, itkUnsharpMaskLevelSetImageFilterIF2IF2)
itkUnsharpMaskLevelSetImageFilterIF2IF2.SetMaxFilterIteration = new_instancemethod(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2_SetMaxFilterIteration, None, itkUnsharpMaskLevelSetImageFilterIF2IF2)
itkUnsharpMaskLevelSetImageFilterIF2IF2_swigregister = _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2_swigregister
itkUnsharpMaskLevelSetImageFilterIF2IF2_swigregister(itkUnsharpMaskLevelSetImageFilterIF2IF2)

def itkUnsharpMaskLevelSetImageFilterIF2IF2___New_orig__() -> "itkUnsharpMaskLevelSetImageFilterIF2IF2_Pointer":
    """itkUnsharpMaskLevelSetImageFilterIF2IF2___New_orig__() -> itkUnsharpMaskLevelSetImageFilterIF2IF2_Pointer"""
    return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2___New_orig__()

def itkUnsharpMaskLevelSetImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkUnsharpMaskLevelSetImageFilterIF2IF2 *":
    """itkUnsharpMaskLevelSetImageFilterIF2IF2_cast(itkLightObject obj) -> itkUnsharpMaskLevelSetImageFilterIF2IF2"""
    return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2_cast(obj)

class itkUnsharpMaskLevelSetImageFilterIF3IF3(itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterIF3IF3):
    """


    This class implements a detail enhancing filter by making use of the
    4th-order level set isotropic diffusion (smoothing) PDE.

    INPUT and OUTPUT This is a volume to volume filter; however, it is
    meant to process (smooth) surfaces. The input surface is an isosurface
    of the input volume. The isosurface value to be processed can be set
    by calling SetIsoSurfaceValue (default is 0). The output surface is
    the 0-isosurface of the output volume, regardless of the input
    isosurface value. To visualize the input/output surfaces to this
    filter a mesh extraction method such as marching cubes can be used.

    be used for general purpose surface processing. It is motivated by
    unsharp masking from image processing which is a way of enhancing
    detail. This filter acts much like the
    IsotropicFourthOrderLevelSetImageFilter because it first smoothes the
    normal vectors via isotropic diffusion. However, as a post-processing
    step we extrapolate from the original normals in the direction
    opposite to the new processes normals. By refitting the surface to
    these extrapolated vectors we achieve detail enhancement. This process
    is not the same as running the isotropic diffusion process in reverse.
    IMPORTANT Because this filters enhances details on the surface, it
    will also amplify post-processing. Do not use it on noisy data.
    PARAMETERS As mentioned before, the IsoSurfaceValue parameter chooses
    which isosurface of the input to process. The MaxFilterIterations
    parameter determine the number of iterations for which this filter
    will run. Since, this filter enhances detail AND noise
    MaxFilterIterations above a couple of hundred are unreasonable.
    Finally NormalProcessUnsharpWeight controls the amount of
    extrapolation (or equivalently the amount of detail enhancement). This
    value should be in the range [0.1,1] for reasonable results.

    C++ includes: itkUnsharpMaskLevelSetImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkUnsharpMaskLevelSetImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkUnsharpMaskLevelSetImageFilterIF3IF3_Pointer"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkUnsharpMaskLevelSetImageFilterIF3IF3_Pointer":
        """Clone(itkUnsharpMaskLevelSetImageFilterIF3IF3 self) -> itkUnsharpMaskLevelSetImageFilterIF3IF3_Pointer"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3_Clone(self)


    def GetMaxFilterIteration(self) -> "unsigned int":
        """GetMaxFilterIteration(itkUnsharpMaskLevelSetImageFilterIF3IF3 self) -> unsigned int"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3_GetMaxFilterIteration(self)


    def SetMaxFilterIteration(self, _arg: 'unsigned int const') -> "void":
        """SetMaxFilterIteration(itkUnsharpMaskLevelSetImageFilterIF3IF3 self, unsigned int const _arg)"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3_SetMaxFilterIteration(self, _arg)

    __swig_destroy__ = _itkUnsharpMaskLevelSetImageFilterPython.delete_itkUnsharpMaskLevelSetImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkUnsharpMaskLevelSetImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkUnsharpMaskLevelSetImageFilterIF3IF3"""
        return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkUnsharpMaskLevelSetImageFilterIF3IF3

        Create a new object of the class itkUnsharpMaskLevelSetImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnsharpMaskLevelSetImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkUnsharpMaskLevelSetImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkUnsharpMaskLevelSetImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkUnsharpMaskLevelSetImageFilterIF3IF3.Clone = new_instancemethod(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3_Clone, None, itkUnsharpMaskLevelSetImageFilterIF3IF3)
itkUnsharpMaskLevelSetImageFilterIF3IF3.GetMaxFilterIteration = new_instancemethod(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3_GetMaxFilterIteration, None, itkUnsharpMaskLevelSetImageFilterIF3IF3)
itkUnsharpMaskLevelSetImageFilterIF3IF3.SetMaxFilterIteration = new_instancemethod(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3_SetMaxFilterIteration, None, itkUnsharpMaskLevelSetImageFilterIF3IF3)
itkUnsharpMaskLevelSetImageFilterIF3IF3_swigregister = _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3_swigregister
itkUnsharpMaskLevelSetImageFilterIF3IF3_swigregister(itkUnsharpMaskLevelSetImageFilterIF3IF3)

def itkUnsharpMaskLevelSetImageFilterIF3IF3___New_orig__() -> "itkUnsharpMaskLevelSetImageFilterIF3IF3_Pointer":
    """itkUnsharpMaskLevelSetImageFilterIF3IF3___New_orig__() -> itkUnsharpMaskLevelSetImageFilterIF3IF3_Pointer"""
    return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3___New_orig__()

def itkUnsharpMaskLevelSetImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkUnsharpMaskLevelSetImageFilterIF3IF3 *":
    """itkUnsharpMaskLevelSetImageFilterIF3IF3_cast(itkLightObject obj) -> itkUnsharpMaskLevelSetImageFilterIF3IF3"""
    return _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def unsharp_mask_level_set_image_filter(*args, **kwargs):
    """Procedural interface for UnsharpMaskLevelSetImageFilter"""
    import itk
    instance = itk.UnsharpMaskLevelSetImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def unsharp_mask_level_set_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.UnsharpMaskLevelSetImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.UnsharpMaskLevelSetImageFilter.values()[0]
    else:
        filter_object = itk.UnsharpMaskLevelSetImageFilter

    unsharp_mask_level_set_image_filter.__doc__ = filter_object.__doc__
    unsharp_mask_level_set_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    unsharp_mask_level_set_image_filter.__doc__ += "Available Keyword Arguments:\n"
    unsharp_mask_level_set_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



