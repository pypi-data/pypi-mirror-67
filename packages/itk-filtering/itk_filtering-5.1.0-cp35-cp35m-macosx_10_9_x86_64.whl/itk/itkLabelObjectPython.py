# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLabelObjectPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLabelObjectPython', [dirname(__file__)])
        except ImportError:
            import _itkLabelObjectPython
            return _itkLabelObjectPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkLabelObjectPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkLabelObjectPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLabelObjectPython
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
import itkOffsetPython
import itkSizePython
import itkIndexPython
import itkLabelObjectLinePython

def itkLabelObjectUL3_New():
  return itkLabelObjectUL3.New()


def itkLabelObjectUL2_New():
  return itkLabelObjectUL2.New()

class itkLabelObjectUL2(ITKCommonBasePython.itkLightObject):
    """


    The base class for the representation of an labeled binary object in
    an image.

    LabelObject is the base class to represent a labeled object in an
    image. It should be used associated with the LabelMap.

    LabelObject store mainly 2 things: the label of the object, and a set
    of lines which are part of the object. No attribute is available in
    that class, so this class can be used as a base class to implement a
    label object with attribute, or when no attribute is needed (see the
    reconstruction filters for an example. If a simple attribute is
    needed, AttributeLabelObject can be used directly.

    All the subclasses of LabelObject have to reimplement the
    CopyAttributesFrom() and CopyAllFrom() method. No need to reimplement
    CopyLinesFrom() since all derived class share the same type line data
    members.

    The pixels locations belonging to the LabelObject can be obtained
    using:

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:http://www.insight-
    journal.org/browse/publication/176

    See:   LabelMapFilter, AttributeLabelObject

    C++ includes: itkLabelObject.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelObjectUL2_Pointer":
        """__New_orig__() -> itkLabelObjectUL2_Pointer"""
        return _itkLabelObjectPython.itkLabelObjectUL2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelObjectUL2_Pointer":
        """Clone(itkLabelObjectUL2 self) -> itkLabelObjectUL2_Pointer"""
        return _itkLabelObjectPython.itkLabelObjectUL2_Clone(self)


    def GetAttributeFromName(s: 'std::string const &') -> "unsigned int":
        """GetAttributeFromName(std::string const & s) -> unsigned int"""
        return _itkLabelObjectPython.itkLabelObjectUL2_GetAttributeFromName(s)

    GetAttributeFromName = staticmethod(GetAttributeFromName)

    def GetNameFromAttribute(a: 'unsigned int const &') -> "std::string":
        """GetNameFromAttribute(unsigned int const & a) -> std::string"""
        return _itkLabelObjectPython.itkLabelObjectUL2_GetNameFromAttribute(a)

    GetNameFromAttribute = staticmethod(GetNameFromAttribute)

    def GetLabel(self) -> "unsigned long const &":
        """
        GetLabel(itkLabelObjectUL2 self) -> unsigned long const &

        Set/Get the label
        associated with the object. 
        """
        return _itkLabelObjectPython.itkLabelObjectUL2_GetLabel(self)


    def SetLabel(self, label: 'unsigned long const &') -> "void":
        """SetLabel(itkLabelObjectUL2 self, unsigned long const & label)"""
        return _itkLabelObjectPython.itkLabelObjectUL2_SetLabel(self, label)


    def HasIndex(self, idx: 'itkIndex2') -> "bool":
        """
        HasIndex(itkLabelObjectUL2 self, itkIndex2 idx) -> bool

        Return true if the object
        contain the given index and false otherwise. Worst case complexity is
        O(L) where L is the number of lines in the object. 
        """
        return _itkLabelObjectPython.itkLabelObjectUL2_HasIndex(self, idx)


    def AddIndex(self, idx: 'itkIndex2') -> "void":
        """
        AddIndex(itkLabelObjectUL2 self, itkIndex2 idx)

        Add an index to the
        object. If the index is already in the object, the index can be found
        several time in the object. 
        """
        return _itkLabelObjectPython.itkLabelObjectUL2_AddIndex(self, idx)


    def RemoveIndex(self, idx: 'itkIndex2') -> "bool":
        """
        RemoveIndex(itkLabelObjectUL2 self, itkIndex2 idx) -> bool

        Remove an index to the
        object. Depending on the configuration, it can either reduce the size
        of the corresponding line, add one more line, remove the line from the
        line container. 
        """
        return _itkLabelObjectPython.itkLabelObjectUL2_RemoveIndex(self, idx)


    def AddLine(self, *args) -> "void":
        """
        AddLine(itkLabelObjectUL2 self, itkIndex2 idx, unsigned long const & length)
        AddLine(itkLabelObjectUL2 self, itkLabelObjectLine2 line)

        Add a new line to the
        object, without any check. 
        """
        return _itkLabelObjectPython.itkLabelObjectUL2_AddLine(self, *args)


    def GetNumberOfLines(self) -> "unsigned long":
        """GetNumberOfLines(itkLabelObjectUL2 self) -> unsigned long"""
        return _itkLabelObjectPython.itkLabelObjectUL2_GetNumberOfLines(self)


    def GetLine(self, *args) -> "itkLabelObjectLine2 &":
        """
        GetLine(itkLabelObjectUL2 self, unsigned long i) -> itkLabelObjectLine2
        GetLine(itkLabelObjectUL2 self, unsigned long i) -> itkLabelObjectLine2
        """
        return _itkLabelObjectPython.itkLabelObjectUL2_GetLine(self, *args)


    def Size(self) -> "unsigned long":
        """
        Size(itkLabelObjectUL2 self) -> unsigned long

        Returns the number of pixels
        contained in the object.

        WARNING:  To get an accurate result, you need to make sure there is no
        duplication in the line container. One way to ensure this (at a cost)
        is to call the Optimize method. 
        """
        return _itkLabelObjectPython.itkLabelObjectUL2_Size(self)


    def Empty(self) -> "bool":
        """
        Empty(itkLabelObjectUL2 self) -> bool

        Returns true if there no line
        in the container (and thus no pixel in the object. 
        """
        return _itkLabelObjectPython.itkLabelObjectUL2_Empty(self)


    def Clear(self) -> "void":
        """Clear(itkLabelObjectUL2 self)"""
        return _itkLabelObjectPython.itkLabelObjectUL2_Clear(self)


    def GetIndex(self, i: 'unsigned long') -> "itkIndex2":
        """
        GetIndex(itkLabelObjectUL2 self, unsigned long i) -> itkIndex2

        Get the index of the ith
        pixel associated with the object. Valid indices are from 0 to
        LabelObject->GetSize() - 1. 
        """
        return _itkLabelObjectPython.itkLabelObjectUL2_GetIndex(self, i)


    def Optimize(self) -> "void":
        """
        Optimize(itkLabelObjectUL2 self)

        Reorder the lines, merge
        the touching lines and ensure that no pixel is covered by two lines 
        """
        return _itkLabelObjectPython.itkLabelObjectUL2_Optimize(self)


    def Shift(self, offset: 'itkOffset2') -> "void":
        """
        Shift(itkLabelObjectUL2 self, itkOffset2 offset)

        Shift the object position 
        """
        return _itkLabelObjectPython.itkLabelObjectUL2_Shift(self, offset)

    __swig_destroy__ = _itkLabelObjectPython.delete_itkLabelObjectUL2

    def cast(obj: 'itkLightObject') -> "itkLabelObjectUL2 *":
        """cast(itkLightObject obj) -> itkLabelObjectUL2"""
        return _itkLabelObjectPython.itkLabelObjectUL2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelObjectUL2

        Create a new object of the class itkLabelObjectUL2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelObjectUL2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelObjectUL2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelObjectUL2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelObjectUL2.Clone = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL2_Clone, None, itkLabelObjectUL2)
itkLabelObjectUL2.GetLabel = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL2_GetLabel, None, itkLabelObjectUL2)
itkLabelObjectUL2.SetLabel = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL2_SetLabel, None, itkLabelObjectUL2)
itkLabelObjectUL2.HasIndex = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL2_HasIndex, None, itkLabelObjectUL2)
itkLabelObjectUL2.AddIndex = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL2_AddIndex, None, itkLabelObjectUL2)
itkLabelObjectUL2.RemoveIndex = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL2_RemoveIndex, None, itkLabelObjectUL2)
itkLabelObjectUL2.AddLine = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL2_AddLine, None, itkLabelObjectUL2)
itkLabelObjectUL2.GetNumberOfLines = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL2_GetNumberOfLines, None, itkLabelObjectUL2)
itkLabelObjectUL2.GetLine = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL2_GetLine, None, itkLabelObjectUL2)
itkLabelObjectUL2.Size = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL2_Size, None, itkLabelObjectUL2)
itkLabelObjectUL2.Empty = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL2_Empty, None, itkLabelObjectUL2)
itkLabelObjectUL2.Clear = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL2_Clear, None, itkLabelObjectUL2)
itkLabelObjectUL2.GetIndex = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL2_GetIndex, None, itkLabelObjectUL2)
itkLabelObjectUL2.Optimize = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL2_Optimize, None, itkLabelObjectUL2)
itkLabelObjectUL2.Shift = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL2_Shift, None, itkLabelObjectUL2)
itkLabelObjectUL2_swigregister = _itkLabelObjectPython.itkLabelObjectUL2_swigregister
itkLabelObjectUL2_swigregister(itkLabelObjectUL2)

def itkLabelObjectUL2___New_orig__() -> "itkLabelObjectUL2_Pointer":
    """itkLabelObjectUL2___New_orig__() -> itkLabelObjectUL2_Pointer"""
    return _itkLabelObjectPython.itkLabelObjectUL2___New_orig__()

def itkLabelObjectUL2_GetAttributeFromName(s: 'std::string const &') -> "unsigned int":
    """itkLabelObjectUL2_GetAttributeFromName(std::string const & s) -> unsigned int"""
    return _itkLabelObjectPython.itkLabelObjectUL2_GetAttributeFromName(s)

def itkLabelObjectUL2_GetNameFromAttribute(a: 'unsigned int const &') -> "std::string":
    """itkLabelObjectUL2_GetNameFromAttribute(unsigned int const & a) -> std::string"""
    return _itkLabelObjectPython.itkLabelObjectUL2_GetNameFromAttribute(a)

def itkLabelObjectUL2_cast(obj: 'itkLightObject') -> "itkLabelObjectUL2 *":
    """itkLabelObjectUL2_cast(itkLightObject obj) -> itkLabelObjectUL2"""
    return _itkLabelObjectPython.itkLabelObjectUL2_cast(obj)

class itkLabelObjectUL3(ITKCommonBasePython.itkLightObject):
    """


    The base class for the representation of an labeled binary object in
    an image.

    LabelObject is the base class to represent a labeled object in an
    image. It should be used associated with the LabelMap.

    LabelObject store mainly 2 things: the label of the object, and a set
    of lines which are part of the object. No attribute is available in
    that class, so this class can be used as a base class to implement a
    label object with attribute, or when no attribute is needed (see the
    reconstruction filters for an example. If a simple attribute is
    needed, AttributeLabelObject can be used directly.

    All the subclasses of LabelObject have to reimplement the
    CopyAttributesFrom() and CopyAllFrom() method. No need to reimplement
    CopyLinesFrom() since all derived class share the same type line data
    members.

    The pixels locations belonging to the LabelObject can be obtained
    using:

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:http://www.insight-
    journal.org/browse/publication/176

    See:   LabelMapFilter, AttributeLabelObject

    C++ includes: itkLabelObject.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelObjectUL3_Pointer":
        """__New_orig__() -> itkLabelObjectUL3_Pointer"""
        return _itkLabelObjectPython.itkLabelObjectUL3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelObjectUL3_Pointer":
        """Clone(itkLabelObjectUL3 self) -> itkLabelObjectUL3_Pointer"""
        return _itkLabelObjectPython.itkLabelObjectUL3_Clone(self)


    def GetAttributeFromName(s: 'std::string const &') -> "unsigned int":
        """GetAttributeFromName(std::string const & s) -> unsigned int"""
        return _itkLabelObjectPython.itkLabelObjectUL3_GetAttributeFromName(s)

    GetAttributeFromName = staticmethod(GetAttributeFromName)

    def GetNameFromAttribute(a: 'unsigned int const &') -> "std::string":
        """GetNameFromAttribute(unsigned int const & a) -> std::string"""
        return _itkLabelObjectPython.itkLabelObjectUL3_GetNameFromAttribute(a)

    GetNameFromAttribute = staticmethod(GetNameFromAttribute)

    def GetLabel(self) -> "unsigned long const &":
        """
        GetLabel(itkLabelObjectUL3 self) -> unsigned long const &

        Set/Get the label
        associated with the object. 
        """
        return _itkLabelObjectPython.itkLabelObjectUL3_GetLabel(self)


    def SetLabel(self, label: 'unsigned long const &') -> "void":
        """SetLabel(itkLabelObjectUL3 self, unsigned long const & label)"""
        return _itkLabelObjectPython.itkLabelObjectUL3_SetLabel(self, label)


    def HasIndex(self, idx: 'itkIndex3') -> "bool":
        """
        HasIndex(itkLabelObjectUL3 self, itkIndex3 idx) -> bool

        Return true if the object
        contain the given index and false otherwise. Worst case complexity is
        O(L) where L is the number of lines in the object. 
        """
        return _itkLabelObjectPython.itkLabelObjectUL3_HasIndex(self, idx)


    def AddIndex(self, idx: 'itkIndex3') -> "void":
        """
        AddIndex(itkLabelObjectUL3 self, itkIndex3 idx)

        Add an index to the
        object. If the index is already in the object, the index can be found
        several time in the object. 
        """
        return _itkLabelObjectPython.itkLabelObjectUL3_AddIndex(self, idx)


    def RemoveIndex(self, idx: 'itkIndex3') -> "bool":
        """
        RemoveIndex(itkLabelObjectUL3 self, itkIndex3 idx) -> bool

        Remove an index to the
        object. Depending on the configuration, it can either reduce the size
        of the corresponding line, add one more line, remove the line from the
        line container. 
        """
        return _itkLabelObjectPython.itkLabelObjectUL3_RemoveIndex(self, idx)


    def AddLine(self, *args) -> "void":
        """
        AddLine(itkLabelObjectUL3 self, itkIndex3 idx, unsigned long const & length)
        AddLine(itkLabelObjectUL3 self, itkLabelObjectLine3 line)

        Add a new line to the
        object, without any check. 
        """
        return _itkLabelObjectPython.itkLabelObjectUL3_AddLine(self, *args)


    def GetNumberOfLines(self) -> "unsigned long":
        """GetNumberOfLines(itkLabelObjectUL3 self) -> unsigned long"""
        return _itkLabelObjectPython.itkLabelObjectUL3_GetNumberOfLines(self)


    def GetLine(self, *args) -> "itkLabelObjectLine3 &":
        """
        GetLine(itkLabelObjectUL3 self, unsigned long i) -> itkLabelObjectLine3
        GetLine(itkLabelObjectUL3 self, unsigned long i) -> itkLabelObjectLine3
        """
        return _itkLabelObjectPython.itkLabelObjectUL3_GetLine(self, *args)


    def Size(self) -> "unsigned long":
        """
        Size(itkLabelObjectUL3 self) -> unsigned long

        Returns the number of pixels
        contained in the object.

        WARNING:  To get an accurate result, you need to make sure there is no
        duplication in the line container. One way to ensure this (at a cost)
        is to call the Optimize method. 
        """
        return _itkLabelObjectPython.itkLabelObjectUL3_Size(self)


    def Empty(self) -> "bool":
        """
        Empty(itkLabelObjectUL3 self) -> bool

        Returns true if there no line
        in the container (and thus no pixel in the object. 
        """
        return _itkLabelObjectPython.itkLabelObjectUL3_Empty(self)


    def Clear(self) -> "void":
        """Clear(itkLabelObjectUL3 self)"""
        return _itkLabelObjectPython.itkLabelObjectUL3_Clear(self)


    def GetIndex(self, i: 'unsigned long') -> "itkIndex3":
        """
        GetIndex(itkLabelObjectUL3 self, unsigned long i) -> itkIndex3

        Get the index of the ith
        pixel associated with the object. Valid indices are from 0 to
        LabelObject->GetSize() - 1. 
        """
        return _itkLabelObjectPython.itkLabelObjectUL3_GetIndex(self, i)


    def Optimize(self) -> "void":
        """
        Optimize(itkLabelObjectUL3 self)

        Reorder the lines, merge
        the touching lines and ensure that no pixel is covered by two lines 
        """
        return _itkLabelObjectPython.itkLabelObjectUL3_Optimize(self)


    def Shift(self, offset: 'itkOffset3') -> "void":
        """
        Shift(itkLabelObjectUL3 self, itkOffset3 offset)

        Shift the object position 
        """
        return _itkLabelObjectPython.itkLabelObjectUL3_Shift(self, offset)

    __swig_destroy__ = _itkLabelObjectPython.delete_itkLabelObjectUL3

    def cast(obj: 'itkLightObject') -> "itkLabelObjectUL3 *":
        """cast(itkLightObject obj) -> itkLabelObjectUL3"""
        return _itkLabelObjectPython.itkLabelObjectUL3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelObjectUL3

        Create a new object of the class itkLabelObjectUL3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelObjectUL3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelObjectUL3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelObjectUL3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelObjectUL3.Clone = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL3_Clone, None, itkLabelObjectUL3)
itkLabelObjectUL3.GetLabel = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL3_GetLabel, None, itkLabelObjectUL3)
itkLabelObjectUL3.SetLabel = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL3_SetLabel, None, itkLabelObjectUL3)
itkLabelObjectUL3.HasIndex = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL3_HasIndex, None, itkLabelObjectUL3)
itkLabelObjectUL3.AddIndex = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL3_AddIndex, None, itkLabelObjectUL3)
itkLabelObjectUL3.RemoveIndex = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL3_RemoveIndex, None, itkLabelObjectUL3)
itkLabelObjectUL3.AddLine = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL3_AddLine, None, itkLabelObjectUL3)
itkLabelObjectUL3.GetNumberOfLines = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL3_GetNumberOfLines, None, itkLabelObjectUL3)
itkLabelObjectUL3.GetLine = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL3_GetLine, None, itkLabelObjectUL3)
itkLabelObjectUL3.Size = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL3_Size, None, itkLabelObjectUL3)
itkLabelObjectUL3.Empty = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL3_Empty, None, itkLabelObjectUL3)
itkLabelObjectUL3.Clear = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL3_Clear, None, itkLabelObjectUL3)
itkLabelObjectUL3.GetIndex = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL3_GetIndex, None, itkLabelObjectUL3)
itkLabelObjectUL3.Optimize = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL3_Optimize, None, itkLabelObjectUL3)
itkLabelObjectUL3.Shift = new_instancemethod(_itkLabelObjectPython.itkLabelObjectUL3_Shift, None, itkLabelObjectUL3)
itkLabelObjectUL3_swigregister = _itkLabelObjectPython.itkLabelObjectUL3_swigregister
itkLabelObjectUL3_swigregister(itkLabelObjectUL3)

def itkLabelObjectUL3___New_orig__() -> "itkLabelObjectUL3_Pointer":
    """itkLabelObjectUL3___New_orig__() -> itkLabelObjectUL3_Pointer"""
    return _itkLabelObjectPython.itkLabelObjectUL3___New_orig__()

def itkLabelObjectUL3_GetAttributeFromName(s: 'std::string const &') -> "unsigned int":
    """itkLabelObjectUL3_GetAttributeFromName(std::string const & s) -> unsigned int"""
    return _itkLabelObjectPython.itkLabelObjectUL3_GetAttributeFromName(s)

def itkLabelObjectUL3_GetNameFromAttribute(a: 'unsigned int const &') -> "std::string":
    """itkLabelObjectUL3_GetNameFromAttribute(unsigned int const & a) -> std::string"""
    return _itkLabelObjectPython.itkLabelObjectUL3_GetNameFromAttribute(a)

def itkLabelObjectUL3_cast(obj: 'itkLightObject') -> "itkLabelObjectUL3 *":
    """itkLabelObjectUL3_cast(itkLightObject obj) -> itkLabelObjectUL3"""
    return _itkLabelObjectPython.itkLabelObjectUL3_cast(obj)



