# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkChangeLabelLabelMapFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkChangeLabelLabelMapFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkChangeLabelLabelMapFilterPython
            return _itkChangeLabelLabelMapFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkChangeLabelLabelMapFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkChangeLabelLabelMapFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkChangeLabelLabelMapFilterPython
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
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImageToImageFilterCommonPython
import itkImageSourceCommonPython
import itkImagePython
import itkImageRegionPython
import itkRGBPixelPython
import itkFixedArrayPython
import stdcomplexPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_vectorPython
import vnl_matrixPython
import itkPointPython
import vnl_vector_refPython
import itkVectorPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBAPixelPython
import itkStatisticsLabelObjectPython
import itkAffineTransformPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkVariableLengthVectorPython
import itkArrayPython
import itkArray2DPython
import itkOptimizerParametersPython
import itkMatrixOffsetTransformBasePython
import itkShapeLabelObjectPython
import itkLabelObjectPython
import itkLabelObjectLinePython
import itkHistogramPython
import itkSamplePython
import itkImageSourcePython
import itkVectorImagePython
import itkLabelMapFilterPython

def itkChangeLabelLabelMapFilterLM3_New():
  return itkChangeLabelLabelMapFilterLM3.New()


def itkChangeLabelLabelMapFilterLM2_New():
  return itkChangeLabelLabelMapFilterLM2.New()

class itkChangeLabelLabelMapFilterLM2(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    """


    Replace the label Ids of selected LabelObjects with new label Ids.

    This filter takes as input a label map and a list of pairs of Label
    Ids, to produce as output a new label map where the label Ids have
    been replaced according to the pairs in the list.

    Labels that are relabeled to the same label Id are automatically
    merged and optimized into a single LabelObject. The background label
    can also be changed. Any object relabeled to the output background
    will automatically be removed.

    This implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/584 orhttp://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, RelabelComponentImageFilter,
    ChangeLabelImageFilter

    C++ includes: itkChangeLabelLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkChangeLabelLabelMapFilterLM2_Pointer":
        """__New_orig__() -> itkChangeLabelLabelMapFilterLM2_Pointer"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkChangeLabelLabelMapFilterLM2_Pointer":
        """Clone(itkChangeLabelLabelMapFilterLM2 self) -> itkChangeLabelLabelMapFilterLM2_Pointer"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_Clone(self)


    def SetChangeMap(self, changeMap: 'mapULUL') -> "void":
        """SetChangeMap(itkChangeLabelLabelMapFilterLM2 self, mapULUL changeMap)"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_SetChangeMap(self, changeMap)


    def GetChangeMap(self) -> "std::map< unsigned long,unsigned long,std::less< unsigned long >,std::allocator< std::pair< unsigned long const,unsigned long > > > const &":
        """GetChangeMap(itkChangeLabelLabelMapFilterLM2 self) -> mapULUL"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_GetChangeMap(self)


    def SetChange(self, oldLabel: 'unsigned long const &', newLabel: 'unsigned long const &') -> "void":
        """SetChange(itkChangeLabelLabelMapFilterLM2 self, unsigned long const & oldLabel, unsigned long const & newLabel)"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_SetChange(self, oldLabel, newLabel)


    def ClearChangeMap(self) -> "void":
        """ClearChangeMap(itkChangeLabelLabelMapFilterLM2 self)"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_ClearChangeMap(self)

    __swig_destroy__ = _itkChangeLabelLabelMapFilterPython.delete_itkChangeLabelLabelMapFilterLM2

    def cast(obj: 'itkLightObject') -> "itkChangeLabelLabelMapFilterLM2 *":
        """cast(itkLightObject obj) -> itkChangeLabelLabelMapFilterLM2"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkChangeLabelLabelMapFilterLM2

        Create a new object of the class itkChangeLabelLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkChangeLabelLabelMapFilterLM2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkChangeLabelLabelMapFilterLM2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkChangeLabelLabelMapFilterLM2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkChangeLabelLabelMapFilterLM2.Clone = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_Clone, None, itkChangeLabelLabelMapFilterLM2)
itkChangeLabelLabelMapFilterLM2.SetChangeMap = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_SetChangeMap, None, itkChangeLabelLabelMapFilterLM2)
itkChangeLabelLabelMapFilterLM2.GetChangeMap = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_GetChangeMap, None, itkChangeLabelLabelMapFilterLM2)
itkChangeLabelLabelMapFilterLM2.SetChange = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_SetChange, None, itkChangeLabelLabelMapFilterLM2)
itkChangeLabelLabelMapFilterLM2.ClearChangeMap = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_ClearChangeMap, None, itkChangeLabelLabelMapFilterLM2)
itkChangeLabelLabelMapFilterLM2_swigregister = _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_swigregister
itkChangeLabelLabelMapFilterLM2_swigregister(itkChangeLabelLabelMapFilterLM2)

def itkChangeLabelLabelMapFilterLM2___New_orig__() -> "itkChangeLabelLabelMapFilterLM2_Pointer":
    """itkChangeLabelLabelMapFilterLM2___New_orig__() -> itkChangeLabelLabelMapFilterLM2_Pointer"""
    return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2___New_orig__()

def itkChangeLabelLabelMapFilterLM2_cast(obj: 'itkLightObject') -> "itkChangeLabelLabelMapFilterLM2 *":
    """itkChangeLabelLabelMapFilterLM2_cast(itkLightObject obj) -> itkChangeLabelLabelMapFilterLM2"""
    return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_cast(obj)

class itkChangeLabelLabelMapFilterLM3(itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    """


    Replace the label Ids of selected LabelObjects with new label Ids.

    This filter takes as input a label map and a list of pairs of Label
    Ids, to produce as output a new label map where the label Ids have
    been replaced according to the pairs in the list.

    Labels that are relabeled to the same label Id are automatically
    merged and optimized into a single LabelObject. The background label
    can also be changed. Any object relabeled to the output background
    will automatically be removed.

    This implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/584 orhttp://www.insight-
    journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, RelabelComponentImageFilter,
    ChangeLabelImageFilter

    C++ includes: itkChangeLabelLabelMapFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkChangeLabelLabelMapFilterLM3_Pointer":
        """__New_orig__() -> itkChangeLabelLabelMapFilterLM3_Pointer"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkChangeLabelLabelMapFilterLM3_Pointer":
        """Clone(itkChangeLabelLabelMapFilterLM3 self) -> itkChangeLabelLabelMapFilterLM3_Pointer"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_Clone(self)


    def SetChangeMap(self, changeMap: 'mapULUL') -> "void":
        """SetChangeMap(itkChangeLabelLabelMapFilterLM3 self, mapULUL changeMap)"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_SetChangeMap(self, changeMap)


    def GetChangeMap(self) -> "std::map< unsigned long,unsigned long,std::less< unsigned long >,std::allocator< std::pair< unsigned long const,unsigned long > > > const &":
        """GetChangeMap(itkChangeLabelLabelMapFilterLM3 self) -> mapULUL"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_GetChangeMap(self)


    def SetChange(self, oldLabel: 'unsigned long const &', newLabel: 'unsigned long const &') -> "void":
        """SetChange(itkChangeLabelLabelMapFilterLM3 self, unsigned long const & oldLabel, unsigned long const & newLabel)"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_SetChange(self, oldLabel, newLabel)


    def ClearChangeMap(self) -> "void":
        """ClearChangeMap(itkChangeLabelLabelMapFilterLM3 self)"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_ClearChangeMap(self)

    __swig_destroy__ = _itkChangeLabelLabelMapFilterPython.delete_itkChangeLabelLabelMapFilterLM3

    def cast(obj: 'itkLightObject') -> "itkChangeLabelLabelMapFilterLM3 *":
        """cast(itkLightObject obj) -> itkChangeLabelLabelMapFilterLM3"""
        return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkChangeLabelLabelMapFilterLM3

        Create a new object of the class itkChangeLabelLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkChangeLabelLabelMapFilterLM3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkChangeLabelLabelMapFilterLM3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkChangeLabelLabelMapFilterLM3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkChangeLabelLabelMapFilterLM3.Clone = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_Clone, None, itkChangeLabelLabelMapFilterLM3)
itkChangeLabelLabelMapFilterLM3.SetChangeMap = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_SetChangeMap, None, itkChangeLabelLabelMapFilterLM3)
itkChangeLabelLabelMapFilterLM3.GetChangeMap = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_GetChangeMap, None, itkChangeLabelLabelMapFilterLM3)
itkChangeLabelLabelMapFilterLM3.SetChange = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_SetChange, None, itkChangeLabelLabelMapFilterLM3)
itkChangeLabelLabelMapFilterLM3.ClearChangeMap = new_instancemethod(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_ClearChangeMap, None, itkChangeLabelLabelMapFilterLM3)
itkChangeLabelLabelMapFilterLM3_swigregister = _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_swigregister
itkChangeLabelLabelMapFilterLM3_swigregister(itkChangeLabelLabelMapFilterLM3)

def itkChangeLabelLabelMapFilterLM3___New_orig__() -> "itkChangeLabelLabelMapFilterLM3_Pointer":
    """itkChangeLabelLabelMapFilterLM3___New_orig__() -> itkChangeLabelLabelMapFilterLM3_Pointer"""
    return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3___New_orig__()

def itkChangeLabelLabelMapFilterLM3_cast(obj: 'itkLightObject') -> "itkChangeLabelLabelMapFilterLM3 *":
    """itkChangeLabelLabelMapFilterLM3_cast(itkLightObject obj) -> itkChangeLabelLabelMapFilterLM3"""
    return _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def change_label_label_map_filter(*args, **kwargs):
    """Procedural interface for ChangeLabelLabelMapFilter"""
    import itk
    instance = itk.ChangeLabelLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def change_label_label_map_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ChangeLabelLabelMapFilter, itkTemplate.itkTemplate):
        filter_object = itk.ChangeLabelLabelMapFilter.values()[0]
    else:
        filter_object = itk.ChangeLabelLabelMapFilter

    change_label_label_map_filter.__doc__ = filter_object.__doc__
    change_label_label_map_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    change_label_label_map_filter.__doc__ += "Available Keyword Arguments:\n"
    change_label_label_map_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



