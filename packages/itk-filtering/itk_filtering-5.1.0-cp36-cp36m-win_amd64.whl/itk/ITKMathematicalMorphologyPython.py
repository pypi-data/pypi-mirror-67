# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ITKMathematicalMorphologyPython
else:
    import _ITKMathematicalMorphologyPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _ITKMathematicalMorphologyPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _ITKMathematicalMorphologyPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



import ITKPyBasePython
import ITKThresholdingPython
import ITKImageIntensityPython
import ITKImageGridPython
import ITKImageFilterBasePython
import ITKConnectedComponentsPython
from itkFlatStructuringElementPython import *
from itkBlackTopHatImageFilterPython import *
from itkClosingByReconstructionImageFilterPython import *
from itkDoubleThresholdImageFilterPython import *
from itkGrayscaleConnectedClosingImageFilterPython import *
from itkGrayscaleConnectedOpeningImageFilterPython import *
from itkGrayscaleDilateImageFilterPython import *
from itkGrayscaleErodeImageFilterPython import *
from itkGrayscaleFillholeImageFilterPython import *
from itkGrayscaleFunctionDilateImageFilterPython import *
from itkGrayscaleFunctionErodeImageFilterPython import *
from itkGrayscaleGeodesicDilateImageFilterPython import *
from itkGrayscaleGeodesicErodeImageFilterPython import *
from itkGrayscaleGrindPeakImageFilterPython import *
from itkGrayscaleMorphologicalClosingImageFilterPython import *
from itkGrayscaleMorphologicalOpeningImageFilterPython import *
from itkHConcaveImageFilterPython import *
from itkHConvexImageFilterPython import *
from itkHMaximaImageFilterPython import *
from itkHMinimaImageFilterPython import *
from itkMorphologicalGradientImageFilterPython import *
from itkOpeningByReconstructionImageFilterPython import *
from itkReconstructionByDilationImageFilterPython import *
from itkReconstructionByErosionImageFilterPython import *
from itkRegionalMaximaImageFilterPython import *
from itkRegionalMinimaImageFilterPython import *
from itkValuedRegionalMaximaImageFilterPython import *
from itkValuedRegionalMinimaImageFilterPython import *
from itkWhiteTopHatImageFilterPython import *




