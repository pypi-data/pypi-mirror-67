# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _ITKLabelMapPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ITKLabelMapPython', [dirname(__file__)])
        except ImportError:
            import _ITKLabelMapPython
            return _ITKLabelMapPython
        if fp is not None:
            try:
                _mod = imp.load_module('_ITKLabelMapPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ITKLabelMapPython = swig_import_helper()
    del swig_import_helper
else:
    import _ITKLabelMapPython
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



import ITKPyBasePython
import ITKTransformPython
import ITKStatisticsPython
import ITKImageLabelPython
from itkLabelObjectLinePython import *
from itkLabelObjectPython import *
from itkShapeLabelObjectPython import *
from itkStatisticsLabelObjectPython import *
from ITKLabelMapBasePython import *
from itkLabelMapFilterPython import *
from itkInPlaceLabelMapFilterPython import *
from itkChangeRegionLabelMapFilterPython import *
from itkAggregateLabelMapFilterPython import *
from itkAutoCropLabelMapFilterPython import *
from itkBinaryFillholeImageFilterPython import *
from itkBinaryGrindPeakImageFilterPython import *
from itkBinaryImageToLabelMapFilterPython import *
from itkBinaryImageToShapeLabelMapFilterPython import *
from itkBinaryImageToStatisticsLabelMapFilterPython import *
from itkBinaryNotImageFilterPython import *
from itkBinaryReconstructionByDilationImageFilterPython import *
from itkBinaryReconstructionByErosionImageFilterPython import *
from itkBinaryShapeKeepNObjectsImageFilterPython import *
from itkBinaryShapeOpeningImageFilterPython import *
from itkBinaryStatisticsKeepNObjectsImageFilterPython import *
from itkBinaryStatisticsOpeningImageFilterPython import *
from itkChangeLabelLabelMapFilterPython import *
from itkCropLabelMapFilterPython import *
from itkLabelImageToLabelMapFilterPython import *
from itkLabelImageToShapeLabelMapFilterPython import *
from itkLabelImageToStatisticsLabelMapFilterPython import *
from itkLabelMapMaskImageFilterPython import *
from itkLabelMapToBinaryImageFilterPython import *
from itkLabelMapToLabelImageFilterPython import *
from itkLabelSelectionLabelMapFilterPython import *
from itkLabelShapeKeepNObjectsImageFilterPython import *
from itkLabelShapeOpeningImageFilterPython import *
from itkLabelStatisticsKeepNObjectsImageFilterPython import *
from itkLabelStatisticsOpeningImageFilterPython import *
from itkLabelUniqueLabelMapFilterPython import *
from itkMergeLabelMapFilterPython import *
from itkObjectByObjectLabelMapFilterPython import *
from itkPadLabelMapFilterPython import *
from itkRegionFromReferenceLabelMapFilterPython import *
from itkRelabelLabelMapFilterPython import *
from itkShapeKeepNObjectsLabelMapFilterPython import *
from itkShapeLabelMapFilterPython import *
from itkShapeOpeningLabelMapFilterPython import *
from itkShapePositionLabelMapFilterPython import *
from itkShapeRelabelImageFilterPython import *
from itkShapeRelabelLabelMapFilterPython import *
from itkShapeUniqueLabelMapFilterPython import *
from itkShiftScaleLabelMapFilterPython import *
from itkStatisticsKeepNObjectsLabelMapFilterPython import *
from itkStatisticsLabelMapFilterPython import *
from itkStatisticsOpeningLabelMapFilterPython import *
from itkStatisticsPositionLabelMapFilterPython import *
from itkStatisticsRelabelImageFilterPython import *
from itkStatisticsRelabelLabelMapFilterPython import *
from itkStatisticsUniqueLabelMapFilterPython import *




