# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkRelabelLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkRelabelLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkRelabelLabelMapFilterPython
            return _itkRelabelLabelMapFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkRelabelLabelMapFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkRelabelLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkRelabelLabelMapFilterPython
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
import itkInPlaceLabelMapFilterPython
import ITKLabelMapBasePython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImagePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkSizePython
import itkOffsetPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkCovariantVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkIndexPython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkStatisticsLabelObjectPython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkAffineTransformPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkArray2DPython
import itkMatrixOffsetTransformBasePython
import itkHistogramPython
import itkSamplePython
import itkLabelMapFilterPython

def itkRelabelLabelMapFilterLM3_New():
  return itkRelabelLabelMapFilterLM3.New()


def itkRelabelLabelMapFilterLM3_Superclass_New():
  return itkRelabelLabelMapFilterLM3_Superclass.New()


def itkRelabelLabelMapFilterLM2_New():
  return itkRelabelLabelMapFilterLM2.New()


def itkRelabelLabelMapFilterLM2_Superclass_New():
  return itkRelabelLabelMapFilterLM2_Superclass.New()

class itkRelabelLabelMapFilterLM2_Superclass(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    """Proxy of C++ itkRelabelLabelMapFilterLM2_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRelabelLabelMapFilterLM2_Superclass_Pointer":
        """__New_orig__() -> itkRelabelLabelMapFilterLM2_Superclass_Pointer"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRelabelLabelMapFilterLM2_Superclass_Pointer":
        """Clone(itkRelabelLabelMapFilterLM2_Superclass self) -> itkRelabelLabelMapFilterLM2_Superclass_Pointer"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_Clone(self)


    def SetReverseOrdering(self, _arg: 'bool const') -> "void":
        """SetReverseOrdering(itkRelabelLabelMapFilterLM2_Superclass self, bool const _arg)"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_SetReverseOrdering(self, _arg)


    def GetReverseOrdering(self) -> "bool const &":
        """GetReverseOrdering(itkRelabelLabelMapFilterLM2_Superclass self) -> bool const &"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_GetReverseOrdering(self)


    def ReverseOrderingOn(self) -> "void":
        """ReverseOrderingOn(itkRelabelLabelMapFilterLM2_Superclass self)"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_ReverseOrderingOn(self)


    def ReverseOrderingOff(self) -> "void":
        """ReverseOrderingOff(itkRelabelLabelMapFilterLM2_Superclass self)"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_ReverseOrderingOff(self)

    __swig_destroy__ = _itkRelabelLabelMapFilterPython.delete_itkRelabelLabelMapFilterLM2_Superclass

    def cast(obj: 'itkLightObject') -> "itkRelabelLabelMapFilterLM2_Superclass *":
        """cast(itkLightObject obj) -> itkRelabelLabelMapFilterLM2_Superclass"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkRelabelLabelMapFilterLM2_Superclass

        Create a new object of the class itkRelabelLabelMapFilterLM2_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRelabelLabelMapFilterLM2_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRelabelLabelMapFilterLM2_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRelabelLabelMapFilterLM2_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRelabelLabelMapFilterLM2_Superclass.Clone = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_Clone, None, itkRelabelLabelMapFilterLM2_Superclass)
itkRelabelLabelMapFilterLM2_Superclass.SetReverseOrdering = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_SetReverseOrdering, None, itkRelabelLabelMapFilterLM2_Superclass)
itkRelabelLabelMapFilterLM2_Superclass.GetReverseOrdering = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_GetReverseOrdering, None, itkRelabelLabelMapFilterLM2_Superclass)
itkRelabelLabelMapFilterLM2_Superclass.ReverseOrderingOn = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_ReverseOrderingOn, None, itkRelabelLabelMapFilterLM2_Superclass)
itkRelabelLabelMapFilterLM2_Superclass.ReverseOrderingOff = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_ReverseOrderingOff, None, itkRelabelLabelMapFilterLM2_Superclass)
itkRelabelLabelMapFilterLM2_Superclass_swigregister = _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_swigregister
itkRelabelLabelMapFilterLM2_Superclass_swigregister(itkRelabelLabelMapFilterLM2_Superclass)

def itkRelabelLabelMapFilterLM2_Superclass___New_orig__() -> "itkRelabelLabelMapFilterLM2_Superclass_Pointer":
    """itkRelabelLabelMapFilterLM2_Superclass___New_orig__() -> itkRelabelLabelMapFilterLM2_Superclass_Pointer"""
    return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass___New_orig__()

def itkRelabelLabelMapFilterLM2_Superclass_cast(obj: 'itkLightObject') -> "itkRelabelLabelMapFilterLM2_Superclass *":
    """itkRelabelLabelMapFilterLM2_Superclass_cast(itkLightObject obj) -> itkRelabelLabelMapFilterLM2_Superclass"""
    return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Superclass_cast(obj)

class itkRelabelLabelMapFilterLM3_Superclass(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    """Proxy of C++ itkRelabelLabelMapFilterLM3_Superclass class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRelabelLabelMapFilterLM3_Superclass_Pointer":
        """__New_orig__() -> itkRelabelLabelMapFilterLM3_Superclass_Pointer"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRelabelLabelMapFilterLM3_Superclass_Pointer":
        """Clone(itkRelabelLabelMapFilterLM3_Superclass self) -> itkRelabelLabelMapFilterLM3_Superclass_Pointer"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_Clone(self)


    def SetReverseOrdering(self, _arg: 'bool const') -> "void":
        """SetReverseOrdering(itkRelabelLabelMapFilterLM3_Superclass self, bool const _arg)"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_SetReverseOrdering(self, _arg)


    def GetReverseOrdering(self) -> "bool const &":
        """GetReverseOrdering(itkRelabelLabelMapFilterLM3_Superclass self) -> bool const &"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_GetReverseOrdering(self)


    def ReverseOrderingOn(self) -> "void":
        """ReverseOrderingOn(itkRelabelLabelMapFilterLM3_Superclass self)"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_ReverseOrderingOn(self)


    def ReverseOrderingOff(self) -> "void":
        """ReverseOrderingOff(itkRelabelLabelMapFilterLM3_Superclass self)"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_ReverseOrderingOff(self)

    __swig_destroy__ = _itkRelabelLabelMapFilterPython.delete_itkRelabelLabelMapFilterLM3_Superclass

    def cast(obj: 'itkLightObject') -> "itkRelabelLabelMapFilterLM3_Superclass *":
        """cast(itkLightObject obj) -> itkRelabelLabelMapFilterLM3_Superclass"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkRelabelLabelMapFilterLM3_Superclass

        Create a new object of the class itkRelabelLabelMapFilterLM3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRelabelLabelMapFilterLM3_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRelabelLabelMapFilterLM3_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRelabelLabelMapFilterLM3_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRelabelLabelMapFilterLM3_Superclass.Clone = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_Clone, None, itkRelabelLabelMapFilterLM3_Superclass)
itkRelabelLabelMapFilterLM3_Superclass.SetReverseOrdering = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_SetReverseOrdering, None, itkRelabelLabelMapFilterLM3_Superclass)
itkRelabelLabelMapFilterLM3_Superclass.GetReverseOrdering = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_GetReverseOrdering, None, itkRelabelLabelMapFilterLM3_Superclass)
itkRelabelLabelMapFilterLM3_Superclass.ReverseOrderingOn = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_ReverseOrderingOn, None, itkRelabelLabelMapFilterLM3_Superclass)
itkRelabelLabelMapFilterLM3_Superclass.ReverseOrderingOff = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_ReverseOrderingOff, None, itkRelabelLabelMapFilterLM3_Superclass)
itkRelabelLabelMapFilterLM3_Superclass_swigregister = _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_swigregister
itkRelabelLabelMapFilterLM3_Superclass_swigregister(itkRelabelLabelMapFilterLM3_Superclass)

def itkRelabelLabelMapFilterLM3_Superclass___New_orig__() -> "itkRelabelLabelMapFilterLM3_Superclass_Pointer":
    """itkRelabelLabelMapFilterLM3_Superclass___New_orig__() -> itkRelabelLabelMapFilterLM3_Superclass_Pointer"""
    return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass___New_orig__()

def itkRelabelLabelMapFilterLM3_Superclass_cast(obj: 'itkLightObject') -> "itkRelabelLabelMapFilterLM3_Superclass *":
    """itkRelabelLabelMapFilterLM3_Superclass_cast(itkLightObject obj) -> itkRelabelLabelMapFilterLM3_Superclass"""
    return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Superclass_cast(obj)

class itkRelabelLabelMapFilterLM2(itkRelabelLabelMapFilterLM2_Superclass):
    """


    This filter relabels the LabelObjects; the new labels are arranged
    consecutively with consideration for the background value.

    This filter takes the LabelObjects from the input and reassigns them
    to the output by calling the PushLabelObject method, which by default,
    attempts to reorganize the labels consecutively. The user can assign
    an arbitrary value to the background; the filter will assign the
    labels consecutively by skipping the background value.

    This implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/584 orhttp://www.insight-
    journal.org/browse/publication/176 Gaetan Lehmann. Biologie du
    Developpement et de la Reproduction, INRA de Jouy-en-Josas, France.

    See:   ShapeLabelObject, RelabelComponentImageFilter

    C++ includes: itkRelabelLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRelabelLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkRelabelLabelMapFilterLM2_Pointer"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRelabelLabelMapFilterLM2_Pointer":
        """Clone(itkRelabelLabelMapFilterLM2 self) -> itkRelabelLabelMapFilterLM2_Pointer"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Clone(self)

    __swig_destroy__ = _itkRelabelLabelMapFilterPython.delete_itkRelabelLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkRelabelLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkRelabelLabelMapFilterLM2"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkRelabelLabelMapFilterLM2

        Create a new object of the class itkRelabelLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRelabelLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRelabelLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRelabelLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRelabelLabelMapFilterLM2.Clone = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_Clone, None, itkRelabelLabelMapFilterLM2)
itkRelabelLabelMapFilterLM2_swigregister = _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_swigregister
itkRelabelLabelMapFilterLM2_swigregister(itkRelabelLabelMapFilterLM2)

def itkRelabelLabelMapFilterLM2___New_orig__() -> "itkRelabelLabelMapFilterLM2_Pointer":
    """itkRelabelLabelMapFilterLM2___New_orig__() -> itkRelabelLabelMapFilterLM2_Pointer"""
    return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2___New_orig__()

def itkRelabelLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkRelabelLabelMapFilterLM2 *":
    """itkRelabelLabelMapFilterLM2_cast(itkLightObject obj) -> itkRelabelLabelMapFilterLM2"""
    return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM2_cast(obj)

class itkRelabelLabelMapFilterLM3(itkRelabelLabelMapFilterLM3_Superclass):
    """


    This filter relabels the LabelObjects; the new labels are arranged
    consecutively with consideration for the background value.

    This filter takes the LabelObjects from the input and reassigns them
    to the output by calling the PushLabelObject method, which by default,
    attempts to reorganize the labels consecutively. The user can assign
    an arbitrary value to the background; the filter will assign the
    labels consecutively by skipping the background value.

    This implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/584 orhttp://www.insight-
    journal.org/browse/publication/176 Gaetan Lehmann. Biologie du
    Developpement et de la Reproduction, INRA de Jouy-en-Josas, France.

    See:   ShapeLabelObject, RelabelComponentImageFilter

    C++ includes: itkRelabelLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRelabelLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkRelabelLabelMapFilterLM3_Pointer"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRelabelLabelMapFilterLM3_Pointer":
        """Clone(itkRelabelLabelMapFilterLM3 self) -> itkRelabelLabelMapFilterLM3_Pointer"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Clone(self)

    __swig_destroy__ = _itkRelabelLabelMapFilterPython.delete_itkRelabelLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkRelabelLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkRelabelLabelMapFilterLM3"""
        return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkRelabelLabelMapFilterLM3

        Create a new object of the class itkRelabelLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRelabelLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRelabelLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRelabelLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRelabelLabelMapFilterLM3.Clone = new_instancemethod(_itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_Clone, None, itkRelabelLabelMapFilterLM3)
itkRelabelLabelMapFilterLM3_swigregister = _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_swigregister
itkRelabelLabelMapFilterLM3_swigregister(itkRelabelLabelMapFilterLM3)

def itkRelabelLabelMapFilterLM3___New_orig__() -> "itkRelabelLabelMapFilterLM3_Pointer":
    """itkRelabelLabelMapFilterLM3___New_orig__() -> itkRelabelLabelMapFilterLM3_Pointer"""
    return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3___New_orig__()

def itkRelabelLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkRelabelLabelMapFilterLM3 *":
    """itkRelabelLabelMapFilterLM3_cast(itkLightObject obj) -> itkRelabelLabelMapFilterLM3"""
    return _itkRelabelLabelMapFilterPython.itkRelabelLabelMapFilterLM3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def relabel_label_map_filter(*args, **kwargs):
    """Procedural interface for RelabelLabelMapFilter"""
    import itk
    instance = itk.RelabelLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def relabel_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.RelabelLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.RelabelLabelMapFilter.values()[0]
    else:
        filter_object = itk.RelabelLabelMapFilter

    relabel_label_map_filter.__doc__ = filter_object.__doc__
    relabel_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    relabel_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    relabel_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])
import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def attribute_relabel_label_map_filter(*args, **kwargs):
    """Procedural interface for AttributeRelabelLabelMapFilter"""
    import itk
    instance = itk.AttributeRelabelLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def attribute_relabel_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.AttributeRelabelLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.AttributeRelabelLabelMapFilter.values()[0]
    else:
        filter_object = itk.AttributeRelabelLabelMapFilter

    attribute_relabel_label_map_filter.__doc__ = filter_object.__doc__
    attribute_relabel_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    attribute_relabel_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    attribute_relabel_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



