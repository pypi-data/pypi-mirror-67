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
    from . import _itkMultiResolutionPDEDeformableRegistrationPython
else:
    import _itkMultiResolutionPDEDeformableRegistrationPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMultiResolutionPDEDeformableRegistrationPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMultiResolutionPDEDeformableRegistrationPython.SWIG_PyStaticMethod_New

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


import itkResampleImageFilterPython
import itkSizePython
import pyBasePython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkFixedArrayPython
import itkMatrixPython
import vnl_matrixPython
import vnl_vectorPython
import stdcomplexPython
import itkVectorPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkPointPython
import vnl_matrix_fixedPython
import itkArrayPython
import itkDiffusionTensor3DPython
import ITKCommonBasePython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkOptimizerParametersPython
import itkImageToImageFilterAPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkImagePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkVectorImagePython
import itkExtrapolateImageFunctionPython
import itkContinuousIndexPython
import itkImageFunctionBasePython
import itkFunctionBasePython
import itkInterpolateImageFunctionPython
import itkPDEDeformableRegistrationFilterPython
import itkDenseFiniteDifferenceImageFilterPython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkFiniteDifferenceFunctionPython
import itkMultiResolutionPyramidImageFilterPython

def itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_New():
  return itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D.New()


def itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_New():
  return itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D.New()


def itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_New():
  return itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F.New()


def itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_New():
  return itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F.New()

class itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D(itkImageToImageFilterAPython.itkImageToImageFilterIVF22IVF22):
    r"""Proxy of C++ itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D___New_orig__)
    Clone = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_Clone)
    SetFixedImage = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_SetFixedImage)
    GetFixedImage = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_GetFixedImage)
    SetMovingImage = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_SetMovingImage)
    GetMovingImage = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_GetMovingImage)
    SetInitialDisplacementField = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_SetInitialDisplacementField)
    SetArbitraryInitialDisplacementField = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_SetArbitraryInitialDisplacementField)
    GetDisplacementField = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_GetDisplacementField)
    SetRegistrationFilter = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_SetRegistrationFilter)
    GetModifiableRegistrationFilter = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_GetModifiableRegistrationFilter)
    GetRegistrationFilter = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_GetRegistrationFilter)
    SetFixedImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_SetFixedImagePyramid)
    GetModifiableFixedImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_GetModifiableFixedImagePyramid)
    GetFixedImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_GetFixedImagePyramid)
    SetMovingImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_SetMovingImagePyramid)
    GetModifiableMovingImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_GetModifiableMovingImagePyramid)
    GetMovingImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_GetMovingImagePyramid)
    SetNumberOfLevels = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_SetNumberOfLevels)
    GetNumberOfLevels = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_GetNumberOfLevels)
    GetCurrentLevel = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_GetCurrentLevel)
    SetFieldExpander = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_SetFieldExpander)
    GetModifiableFieldExpander = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_GetModifiableFieldExpander)
    GetFieldExpander = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_GetFieldExpander)
    SetNumberOfIterations = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_SetNumberOfIterations)
    GetNumberOfIterations = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_GetNumberOfIterations)
    StopRegistration = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_StopRegistration)
    __swig_destroy__ = _itkMultiResolutionPDEDeformableRegistrationPython.delete_itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D
    cast = _swig_new_static_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_cast)

    def New(*args, **kargs):
        """New() -> itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D

        Create a new object of the class itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D in _itkMultiResolutionPDEDeformableRegistrationPython:
_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_swigregister(itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D)
itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D___New_orig__ = _itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D___New_orig__
itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_cast = _itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID2ID2IVF22D_cast

class itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D(itkImageToImageFilterAPython.itkImageToImageFilterIVF33IVF33):
    r"""Proxy of C++ itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D___New_orig__)
    Clone = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_Clone)
    SetFixedImage = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_SetFixedImage)
    GetFixedImage = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_GetFixedImage)
    SetMovingImage = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_SetMovingImage)
    GetMovingImage = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_GetMovingImage)
    SetInitialDisplacementField = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_SetInitialDisplacementField)
    SetArbitraryInitialDisplacementField = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_SetArbitraryInitialDisplacementField)
    GetDisplacementField = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_GetDisplacementField)
    SetRegistrationFilter = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_SetRegistrationFilter)
    GetModifiableRegistrationFilter = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_GetModifiableRegistrationFilter)
    GetRegistrationFilter = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_GetRegistrationFilter)
    SetFixedImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_SetFixedImagePyramid)
    GetModifiableFixedImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_GetModifiableFixedImagePyramid)
    GetFixedImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_GetFixedImagePyramid)
    SetMovingImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_SetMovingImagePyramid)
    GetModifiableMovingImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_GetModifiableMovingImagePyramid)
    GetMovingImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_GetMovingImagePyramid)
    SetNumberOfLevels = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_SetNumberOfLevels)
    GetNumberOfLevels = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_GetNumberOfLevels)
    GetCurrentLevel = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_GetCurrentLevel)
    SetFieldExpander = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_SetFieldExpander)
    GetModifiableFieldExpander = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_GetModifiableFieldExpander)
    GetFieldExpander = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_GetFieldExpander)
    SetNumberOfIterations = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_SetNumberOfIterations)
    GetNumberOfIterations = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_GetNumberOfIterations)
    StopRegistration = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_StopRegistration)
    __swig_destroy__ = _itkMultiResolutionPDEDeformableRegistrationPython.delete_itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D
    cast = _swig_new_static_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_cast)

    def New(*args, **kargs):
        """New() -> itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D

        Create a new object of the class itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D in _itkMultiResolutionPDEDeformableRegistrationPython:
_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_swigregister(itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D)
itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D___New_orig__ = _itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D___New_orig__
itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_cast = _itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationID3ID3IVF33D_cast

class itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F(itkImageToImageFilterAPython.itkImageToImageFilterIVF22IVF22):
    r"""Proxy of C++ itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F___New_orig__)
    Clone = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_Clone)
    SetFixedImage = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_SetFixedImage)
    GetFixedImage = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_GetFixedImage)
    SetMovingImage = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_SetMovingImage)
    GetMovingImage = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_GetMovingImage)
    SetInitialDisplacementField = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_SetInitialDisplacementField)
    SetArbitraryInitialDisplacementField = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_SetArbitraryInitialDisplacementField)
    GetDisplacementField = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_GetDisplacementField)
    SetRegistrationFilter = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_SetRegistrationFilter)
    GetModifiableRegistrationFilter = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_GetModifiableRegistrationFilter)
    GetRegistrationFilter = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_GetRegistrationFilter)
    SetFixedImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_SetFixedImagePyramid)
    GetModifiableFixedImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_GetModifiableFixedImagePyramid)
    GetFixedImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_GetFixedImagePyramid)
    SetMovingImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_SetMovingImagePyramid)
    GetModifiableMovingImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_GetModifiableMovingImagePyramid)
    GetMovingImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_GetMovingImagePyramid)
    SetNumberOfLevels = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_SetNumberOfLevels)
    GetNumberOfLevels = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_GetNumberOfLevels)
    GetCurrentLevel = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_GetCurrentLevel)
    SetFieldExpander = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_SetFieldExpander)
    GetModifiableFieldExpander = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_GetModifiableFieldExpander)
    GetFieldExpander = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_GetFieldExpander)
    SetNumberOfIterations = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_SetNumberOfIterations)
    GetNumberOfIterations = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_GetNumberOfIterations)
    StopRegistration = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_StopRegistration)
    __swig_destroy__ = _itkMultiResolutionPDEDeformableRegistrationPython.delete_itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F
    cast = _swig_new_static_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_cast)

    def New(*args, **kargs):
        """New() -> itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F

        Create a new object of the class itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F in _itkMultiResolutionPDEDeformableRegistrationPython:
_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_swigregister(itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F)
itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F___New_orig__ = _itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F___New_orig__
itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_cast = _itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF2IF2IVF22F_cast

class itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F(itkImageToImageFilterAPython.itkImageToImageFilterIVF33IVF33):
    r"""Proxy of C++ itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F___New_orig__)
    Clone = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_Clone)
    SetFixedImage = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_SetFixedImage)
    GetFixedImage = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_GetFixedImage)
    SetMovingImage = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_SetMovingImage)
    GetMovingImage = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_GetMovingImage)
    SetInitialDisplacementField = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_SetInitialDisplacementField)
    SetArbitraryInitialDisplacementField = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_SetArbitraryInitialDisplacementField)
    GetDisplacementField = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_GetDisplacementField)
    SetRegistrationFilter = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_SetRegistrationFilter)
    GetModifiableRegistrationFilter = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_GetModifiableRegistrationFilter)
    GetRegistrationFilter = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_GetRegistrationFilter)
    SetFixedImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_SetFixedImagePyramid)
    GetModifiableFixedImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_GetModifiableFixedImagePyramid)
    GetFixedImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_GetFixedImagePyramid)
    SetMovingImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_SetMovingImagePyramid)
    GetModifiableMovingImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_GetModifiableMovingImagePyramid)
    GetMovingImagePyramid = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_GetMovingImagePyramid)
    SetNumberOfLevels = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_SetNumberOfLevels)
    GetNumberOfLevels = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_GetNumberOfLevels)
    GetCurrentLevel = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_GetCurrentLevel)
    SetFieldExpander = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_SetFieldExpander)
    GetModifiableFieldExpander = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_GetModifiableFieldExpander)
    GetFieldExpander = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_GetFieldExpander)
    SetNumberOfIterations = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_SetNumberOfIterations)
    GetNumberOfIterations = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_GetNumberOfIterations)
    StopRegistration = _swig_new_instance_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_StopRegistration)
    __swig_destroy__ = _itkMultiResolutionPDEDeformableRegistrationPython.delete_itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F
    cast = _swig_new_static_method(_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_cast)

    def New(*args, **kargs):
        """New() -> itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F

        Create a new object of the class itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F in _itkMultiResolutionPDEDeformableRegistrationPython:
_itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_swigregister(itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F)
itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F___New_orig__ = _itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F___New_orig__
itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_cast = _itkMultiResolutionPDEDeformableRegistrationPython.itkMultiResolutionPDEDeformableRegistrationIF3IF3IVF33F_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def multi_resolution_pde_deformable_registration(*args, **kwargs):
    """Procedural interface for MultiResolutionPDEDeformableRegistration"""
    import itk
    instance = itk.MultiResolutionPDEDeformableRegistration.New(*args, **kwargs)
    return instance.__internal_call__()

def multi_resolution_pde_deformable_registration_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.MultiResolutionPDEDeformableRegistration, itkTemplate.itkTemplate):
        filter_object = itk.MultiResolutionPDEDeformableRegistration.values()[0]
    else:
        filter_object = itk.MultiResolutionPDEDeformableRegistration

    multi_resolution_pde_deformable_registration.__doc__ = filter_object.__doc__
    multi_resolution_pde_deformable_registration.__doc__ += "\n Args are Input(s) to the filter.\n"
    multi_resolution_pde_deformable_registration.__doc__ += "Available Keyword Arguments:\n"
    multi_resolution_pde_deformable_registration.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



