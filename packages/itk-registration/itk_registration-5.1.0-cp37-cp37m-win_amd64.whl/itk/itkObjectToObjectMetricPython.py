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
    from . import _itkObjectToObjectMetricPython
else:
    import _itkObjectToObjectMetricPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkObjectToObjectMetricPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkObjectToObjectMetricPython.SWIG_PyStaticMethod_New

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


import itkDisplacementFieldTransformPython
import ITKCommonBasePython
import pyBasePython
import itkArray2DPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vectorPython
import itkArrayPython
import itkImagePython
import itkVectorPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkOffsetPython
import itkSizePython
import itkCovariantVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkIndexPython
import itkRGBPixelPython
import itkVariableLengthVectorPython
import itkTransformBasePython
import itkOptimizerParametersPython
import itkDiffusionTensor3DPython
import itkObjectToObjectMetricBasePython
import itkSingleValuedCostFunctionv4Python
import itkCostFunctionPython

def itkObjectToObjectMetric33_New():
  return itkObjectToObjectMetric33.New()


def itkObjectToObjectMetric22_New():
  return itkObjectToObjectMetric22.New()

class itkObjectToObjectMetric22(itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD):
    r"""Proxy of C++ itkObjectToObjectMetric22 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetFixedTransform = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SetFixedTransform)
    GetModifiableFixedTransform = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetModifiableFixedTransform)
    GetFixedTransform = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetFixedTransform)
    SetMovingTransform = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SetMovingTransform)
    GetModifiableMovingTransform = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetModifiableMovingTransform)
    GetMovingTransform = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetMovingTransform)
    SetTransform = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SetTransform)
    GetTransform = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetTransform)
    GetNumberOfValidPoints = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetNumberOfValidPoints)
    SetVirtualDomain = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SetVirtualDomain)
    SetVirtualDomainFromImage = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SetVirtualDomainFromImage)
    SupportsArbitraryVirtualDomainSamples = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_SupportsArbitraryVirtualDomainSamples)
    GetVirtualDomainTimeStamp = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualDomainTimeStamp)
    GetVirtualSpacing = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualSpacing)
    GetVirtualOrigin = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualOrigin)
    GetVirtualDirection = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualDirection)
    GetVirtualRegion = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualRegion)
    GetModifiableVirtualImage = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetModifiableVirtualImage)
    GetVirtualImage = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_GetVirtualImage)
    ComputeParameterOffsetFromVirtualIndex = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_ComputeParameterOffsetFromVirtualIndex)
    ComputeParameterOffsetFromVirtualPoint = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_ComputeParameterOffsetFromVirtualPoint)
    IsInsideVirtualDomain = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_IsInsideVirtualDomain)
    __swig_destroy__ = _itkObjectToObjectMetricPython.delete_itkObjectToObjectMetric22
    cast = _swig_new_static_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_cast)

    def New(*args, **kargs):
        """New() -> itkObjectToObjectMetric22

        Create a new object of the class itkObjectToObjectMetric22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkObjectToObjectMetric22.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkObjectToObjectMetric22.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkObjectToObjectMetric22.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkObjectToObjectMetric22 in _itkObjectToObjectMetricPython:
_itkObjectToObjectMetricPython.itkObjectToObjectMetric22_swigregister(itkObjectToObjectMetric22)
itkObjectToObjectMetric22_cast = _itkObjectToObjectMetricPython.itkObjectToObjectMetric22_cast

class itkObjectToObjectMetric33(itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD):
    r"""Proxy of C++ itkObjectToObjectMetric33 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetFixedTransform = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SetFixedTransform)
    GetModifiableFixedTransform = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetModifiableFixedTransform)
    GetFixedTransform = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetFixedTransform)
    SetMovingTransform = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SetMovingTransform)
    GetModifiableMovingTransform = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetModifiableMovingTransform)
    GetMovingTransform = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetMovingTransform)
    SetTransform = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SetTransform)
    GetTransform = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetTransform)
    GetNumberOfValidPoints = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetNumberOfValidPoints)
    SetVirtualDomain = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SetVirtualDomain)
    SetVirtualDomainFromImage = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SetVirtualDomainFromImage)
    SupportsArbitraryVirtualDomainSamples = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_SupportsArbitraryVirtualDomainSamples)
    GetVirtualDomainTimeStamp = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualDomainTimeStamp)
    GetVirtualSpacing = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualSpacing)
    GetVirtualOrigin = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualOrigin)
    GetVirtualDirection = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualDirection)
    GetVirtualRegion = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualRegion)
    GetModifiableVirtualImage = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetModifiableVirtualImage)
    GetVirtualImage = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_GetVirtualImage)
    ComputeParameterOffsetFromVirtualIndex = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_ComputeParameterOffsetFromVirtualIndex)
    ComputeParameterOffsetFromVirtualPoint = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_ComputeParameterOffsetFromVirtualPoint)
    IsInsideVirtualDomain = _swig_new_instance_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_IsInsideVirtualDomain)
    __swig_destroy__ = _itkObjectToObjectMetricPython.delete_itkObjectToObjectMetric33
    cast = _swig_new_static_method(_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_cast)

    def New(*args, **kargs):
        """New() -> itkObjectToObjectMetric33

        Create a new object of the class itkObjectToObjectMetric33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkObjectToObjectMetric33.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkObjectToObjectMetric33.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkObjectToObjectMetric33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkObjectToObjectMetric33 in _itkObjectToObjectMetricPython:
_itkObjectToObjectMetricPython.itkObjectToObjectMetric33_swigregister(itkObjectToObjectMetric33)
itkObjectToObjectMetric33_cast = _itkObjectToObjectMetricPython.itkObjectToObjectMetric33_cast



