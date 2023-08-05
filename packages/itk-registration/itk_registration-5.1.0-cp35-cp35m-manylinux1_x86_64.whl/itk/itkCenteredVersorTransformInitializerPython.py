# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkCenteredVersorTransformInitializerPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkCenteredVersorTransformInitializerPython', [dirname(__file__)])
        except ImportError:
            import _itkCenteredVersorTransformInitializerPython
            return _itkCenteredVersorTransformInitializerPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkCenteredVersorTransformInitializerPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkCenteredVersorTransformInitializerPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkCenteredVersorTransformInitializerPython
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
import itkCenteredTransformInitializerPython
import itkVersorRigid3DTransformPython
import itkMatrixPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkArray2DPython
import itkVersorTransformPython
import itkRigid3DTransformPython
import itkMatrixOffsetTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkDiffusionTensor3DPython
import itkVariableLengthVectorPython
import itkTransformBasePython
import itkArrayPython
import itkOptimizerParametersPython
import itkVersorPython
import itkCenteredRigid2DTransformPython
import itkRigid2DTransformPython
import itkImageMomentsCalculatorPython
import itkSpatialObjectBasePython
import itkAffineTransformPython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkSpatialObjectPropertyPython
import itkRGBAPixelPython
import itkBoundingBoxPython
import itkVectorContainerPython
import itkContinuousIndexPython
import itkMapContainerPython
import itkImagePython
import itkRGBPixelPython

def itkCenteredVersorTransformInitializerID3ID3_New():
  return itkCenteredVersorTransformInitializerID3ID3.New()


def itkCenteredVersorTransformInitializerIF3IF3_New():
  return itkCenteredVersorTransformInitializerIF3IF3.New()


def itkCenteredVersorTransformInitializerIUS3IUS3_New():
  return itkCenteredVersorTransformInitializerIUS3IUS3.New()


def itkCenteredVersorTransformInitializerIUC3IUC3_New():
  return itkCenteredVersorTransformInitializerIUC3IUC3.New()


def itkCenteredVersorTransformInitializerISS3ISS3_New():
  return itkCenteredVersorTransformInitializerISS3ISS3.New()

class itkCenteredVersorTransformInitializerID3ID3(itkCenteredTransformInitializerPython.itkCenteredTransformInitializerVR3DTDID3ID3):
    """


    CenteredVersorTransformInitializer is a helper class intended to
    initialize the center of rotation, versor, and translation of the
    VersorRigid3DTransform.

    This class derived from the CenteredTransformInitializer and uses it
    in a more constrained context. It always uses the Moments mode, and
    also takes advantage of the second order moments in order to
    initialize the Versor representing rotation.

    C++ includes: itkCenteredVersorTransformInitializer.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCenteredVersorTransformInitializerID3ID3_Pointer":
        """__New_orig__() -> itkCenteredVersorTransformInitializerID3ID3_Pointer"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCenteredVersorTransformInitializerID3ID3_Pointer":
        """Clone(itkCenteredVersorTransformInitializerID3ID3 self) -> itkCenteredVersorTransformInitializerID3ID3_Pointer"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerID3ID3_Clone(self)


    def SetComputeRotation(self, _arg: 'bool const') -> "void":
        """
        SetComputeRotation(itkCenteredVersorTransformInitializerID3ID3 self, bool const _arg)

        Enable the use
        of the principal axes of each image to compute an initial rotation
        that will align them. 
        """
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerID3ID3_SetComputeRotation(self, _arg)


    def GetComputeRotation(self) -> "bool":
        """GetComputeRotation(itkCenteredVersorTransformInitializerID3ID3 self) -> bool"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerID3ID3_GetComputeRotation(self)


    def ComputeRotationOn(self) -> "void":
        """ComputeRotationOn(itkCenteredVersorTransformInitializerID3ID3 self)"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerID3ID3_ComputeRotationOn(self)


    def ComputeRotationOff(self) -> "void":
        """ComputeRotationOff(itkCenteredVersorTransformInitializerID3ID3 self)"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerID3ID3_ComputeRotationOff(self)

    __swig_destroy__ = _itkCenteredVersorTransformInitializerPython.delete_itkCenteredVersorTransformInitializerID3ID3

    def cast(obj: 'itkLightObject') -> "itkCenteredVersorTransformInitializerID3ID3 *":
        """cast(itkLightObject obj) -> itkCenteredVersorTransformInitializerID3ID3"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkCenteredVersorTransformInitializerID3ID3

        Create a new object of the class itkCenteredVersorTransformInitializerID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCenteredVersorTransformInitializerID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCenteredVersorTransformInitializerID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCenteredVersorTransformInitializerID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCenteredVersorTransformInitializerID3ID3.Clone = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerID3ID3_Clone, None, itkCenteredVersorTransformInitializerID3ID3)
itkCenteredVersorTransformInitializerID3ID3.SetComputeRotation = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerID3ID3_SetComputeRotation, None, itkCenteredVersorTransformInitializerID3ID3)
itkCenteredVersorTransformInitializerID3ID3.GetComputeRotation = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerID3ID3_GetComputeRotation, None, itkCenteredVersorTransformInitializerID3ID3)
itkCenteredVersorTransformInitializerID3ID3.ComputeRotationOn = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerID3ID3_ComputeRotationOn, None, itkCenteredVersorTransformInitializerID3ID3)
itkCenteredVersorTransformInitializerID3ID3.ComputeRotationOff = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerID3ID3_ComputeRotationOff, None, itkCenteredVersorTransformInitializerID3ID3)
itkCenteredVersorTransformInitializerID3ID3_swigregister = _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerID3ID3_swigregister
itkCenteredVersorTransformInitializerID3ID3_swigregister(itkCenteredVersorTransformInitializerID3ID3)

def itkCenteredVersorTransformInitializerID3ID3___New_orig__() -> "itkCenteredVersorTransformInitializerID3ID3_Pointer":
    """itkCenteredVersorTransformInitializerID3ID3___New_orig__() -> itkCenteredVersorTransformInitializerID3ID3_Pointer"""
    return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerID3ID3___New_orig__()

def itkCenteredVersorTransformInitializerID3ID3_cast(obj: 'itkLightObject') -> "itkCenteredVersorTransformInitializerID3ID3 *":
    """itkCenteredVersorTransformInitializerID3ID3_cast(itkLightObject obj) -> itkCenteredVersorTransformInitializerID3ID3"""
    return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerID3ID3_cast(obj)

class itkCenteredVersorTransformInitializerIF3IF3(itkCenteredTransformInitializerPython.itkCenteredTransformInitializerVR3DTDIF3IF3):
    """


    CenteredVersorTransformInitializer is a helper class intended to
    initialize the center of rotation, versor, and translation of the
    VersorRigid3DTransform.

    This class derived from the CenteredTransformInitializer and uses it
    in a more constrained context. It always uses the Moments mode, and
    also takes advantage of the second order moments in order to
    initialize the Versor representing rotation.

    C++ includes: itkCenteredVersorTransformInitializer.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCenteredVersorTransformInitializerIF3IF3_Pointer":
        """__New_orig__() -> itkCenteredVersorTransformInitializerIF3IF3_Pointer"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCenteredVersorTransformInitializerIF3IF3_Pointer":
        """Clone(itkCenteredVersorTransformInitializerIF3IF3 self) -> itkCenteredVersorTransformInitializerIF3IF3_Pointer"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIF3IF3_Clone(self)


    def SetComputeRotation(self, _arg: 'bool const') -> "void":
        """
        SetComputeRotation(itkCenteredVersorTransformInitializerIF3IF3 self, bool const _arg)

        Enable the use
        of the principal axes of each image to compute an initial rotation
        that will align them. 
        """
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIF3IF3_SetComputeRotation(self, _arg)


    def GetComputeRotation(self) -> "bool":
        """GetComputeRotation(itkCenteredVersorTransformInitializerIF3IF3 self) -> bool"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIF3IF3_GetComputeRotation(self)


    def ComputeRotationOn(self) -> "void":
        """ComputeRotationOn(itkCenteredVersorTransformInitializerIF3IF3 self)"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIF3IF3_ComputeRotationOn(self)


    def ComputeRotationOff(self) -> "void":
        """ComputeRotationOff(itkCenteredVersorTransformInitializerIF3IF3 self)"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIF3IF3_ComputeRotationOff(self)

    __swig_destroy__ = _itkCenteredVersorTransformInitializerPython.delete_itkCenteredVersorTransformInitializerIF3IF3

    def cast(obj: 'itkLightObject') -> "itkCenteredVersorTransformInitializerIF3IF3 *":
        """cast(itkLightObject obj) -> itkCenteredVersorTransformInitializerIF3IF3"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkCenteredVersorTransformInitializerIF3IF3

        Create a new object of the class itkCenteredVersorTransformInitializerIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCenteredVersorTransformInitializerIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCenteredVersorTransformInitializerIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCenteredVersorTransformInitializerIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCenteredVersorTransformInitializerIF3IF3.Clone = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIF3IF3_Clone, None, itkCenteredVersorTransformInitializerIF3IF3)
itkCenteredVersorTransformInitializerIF3IF3.SetComputeRotation = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIF3IF3_SetComputeRotation, None, itkCenteredVersorTransformInitializerIF3IF3)
itkCenteredVersorTransformInitializerIF3IF3.GetComputeRotation = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIF3IF3_GetComputeRotation, None, itkCenteredVersorTransformInitializerIF3IF3)
itkCenteredVersorTransformInitializerIF3IF3.ComputeRotationOn = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIF3IF3_ComputeRotationOn, None, itkCenteredVersorTransformInitializerIF3IF3)
itkCenteredVersorTransformInitializerIF3IF3.ComputeRotationOff = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIF3IF3_ComputeRotationOff, None, itkCenteredVersorTransformInitializerIF3IF3)
itkCenteredVersorTransformInitializerIF3IF3_swigregister = _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIF3IF3_swigregister
itkCenteredVersorTransformInitializerIF3IF3_swigregister(itkCenteredVersorTransformInitializerIF3IF3)

def itkCenteredVersorTransformInitializerIF3IF3___New_orig__() -> "itkCenteredVersorTransformInitializerIF3IF3_Pointer":
    """itkCenteredVersorTransformInitializerIF3IF3___New_orig__() -> itkCenteredVersorTransformInitializerIF3IF3_Pointer"""
    return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIF3IF3___New_orig__()

def itkCenteredVersorTransformInitializerIF3IF3_cast(obj: 'itkLightObject') -> "itkCenteredVersorTransformInitializerIF3IF3 *":
    """itkCenteredVersorTransformInitializerIF3IF3_cast(itkLightObject obj) -> itkCenteredVersorTransformInitializerIF3IF3"""
    return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIF3IF3_cast(obj)

class itkCenteredVersorTransformInitializerISS3ISS3(itkCenteredTransformInitializerPython.itkCenteredTransformInitializerVR3DTDISS3ISS3):
    """


    CenteredVersorTransformInitializer is a helper class intended to
    initialize the center of rotation, versor, and translation of the
    VersorRigid3DTransform.

    This class derived from the CenteredTransformInitializer and uses it
    in a more constrained context. It always uses the Moments mode, and
    also takes advantage of the second order moments in order to
    initialize the Versor representing rotation.

    C++ includes: itkCenteredVersorTransformInitializer.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCenteredVersorTransformInitializerISS3ISS3_Pointer":
        """__New_orig__() -> itkCenteredVersorTransformInitializerISS3ISS3_Pointer"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCenteredVersorTransformInitializerISS3ISS3_Pointer":
        """Clone(itkCenteredVersorTransformInitializerISS3ISS3 self) -> itkCenteredVersorTransformInitializerISS3ISS3_Pointer"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerISS3ISS3_Clone(self)


    def SetComputeRotation(self, _arg: 'bool const') -> "void":
        """
        SetComputeRotation(itkCenteredVersorTransformInitializerISS3ISS3 self, bool const _arg)

        Enable the use
        of the principal axes of each image to compute an initial rotation
        that will align them. 
        """
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerISS3ISS3_SetComputeRotation(self, _arg)


    def GetComputeRotation(self) -> "bool":
        """GetComputeRotation(itkCenteredVersorTransformInitializerISS3ISS3 self) -> bool"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerISS3ISS3_GetComputeRotation(self)


    def ComputeRotationOn(self) -> "void":
        """ComputeRotationOn(itkCenteredVersorTransformInitializerISS3ISS3 self)"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerISS3ISS3_ComputeRotationOn(self)


    def ComputeRotationOff(self) -> "void":
        """ComputeRotationOff(itkCenteredVersorTransformInitializerISS3ISS3 self)"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerISS3ISS3_ComputeRotationOff(self)

    __swig_destroy__ = _itkCenteredVersorTransformInitializerPython.delete_itkCenteredVersorTransformInitializerISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkCenteredVersorTransformInitializerISS3ISS3 *":
        """cast(itkLightObject obj) -> itkCenteredVersorTransformInitializerISS3ISS3"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkCenteredVersorTransformInitializerISS3ISS3

        Create a new object of the class itkCenteredVersorTransformInitializerISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCenteredVersorTransformInitializerISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCenteredVersorTransformInitializerISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCenteredVersorTransformInitializerISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCenteredVersorTransformInitializerISS3ISS3.Clone = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerISS3ISS3_Clone, None, itkCenteredVersorTransformInitializerISS3ISS3)
itkCenteredVersorTransformInitializerISS3ISS3.SetComputeRotation = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerISS3ISS3_SetComputeRotation, None, itkCenteredVersorTransformInitializerISS3ISS3)
itkCenteredVersorTransformInitializerISS3ISS3.GetComputeRotation = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerISS3ISS3_GetComputeRotation, None, itkCenteredVersorTransformInitializerISS3ISS3)
itkCenteredVersorTransformInitializerISS3ISS3.ComputeRotationOn = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerISS3ISS3_ComputeRotationOn, None, itkCenteredVersorTransformInitializerISS3ISS3)
itkCenteredVersorTransformInitializerISS3ISS3.ComputeRotationOff = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerISS3ISS3_ComputeRotationOff, None, itkCenteredVersorTransformInitializerISS3ISS3)
itkCenteredVersorTransformInitializerISS3ISS3_swigregister = _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerISS3ISS3_swigregister
itkCenteredVersorTransformInitializerISS3ISS3_swigregister(itkCenteredVersorTransformInitializerISS3ISS3)

def itkCenteredVersorTransformInitializerISS3ISS3___New_orig__() -> "itkCenteredVersorTransformInitializerISS3ISS3_Pointer":
    """itkCenteredVersorTransformInitializerISS3ISS3___New_orig__() -> itkCenteredVersorTransformInitializerISS3ISS3_Pointer"""
    return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerISS3ISS3___New_orig__()

def itkCenteredVersorTransformInitializerISS3ISS3_cast(obj: 'itkLightObject') -> "itkCenteredVersorTransformInitializerISS3ISS3 *":
    """itkCenteredVersorTransformInitializerISS3ISS3_cast(itkLightObject obj) -> itkCenteredVersorTransformInitializerISS3ISS3"""
    return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerISS3ISS3_cast(obj)

class itkCenteredVersorTransformInitializerIUC3IUC3(itkCenteredTransformInitializerPython.itkCenteredTransformInitializerVR3DTDIUC3IUC3):
    """


    CenteredVersorTransformInitializer is a helper class intended to
    initialize the center of rotation, versor, and translation of the
    VersorRigid3DTransform.

    This class derived from the CenteredTransformInitializer and uses it
    in a more constrained context. It always uses the Moments mode, and
    also takes advantage of the second order moments in order to
    initialize the Versor representing rotation.

    C++ includes: itkCenteredVersorTransformInitializer.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCenteredVersorTransformInitializerIUC3IUC3_Pointer":
        """__New_orig__() -> itkCenteredVersorTransformInitializerIUC3IUC3_Pointer"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCenteredVersorTransformInitializerIUC3IUC3_Pointer":
        """Clone(itkCenteredVersorTransformInitializerIUC3IUC3 self) -> itkCenteredVersorTransformInitializerIUC3IUC3_Pointer"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUC3IUC3_Clone(self)


    def SetComputeRotation(self, _arg: 'bool const') -> "void":
        """
        SetComputeRotation(itkCenteredVersorTransformInitializerIUC3IUC3 self, bool const _arg)

        Enable the use
        of the principal axes of each image to compute an initial rotation
        that will align them. 
        """
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUC3IUC3_SetComputeRotation(self, _arg)


    def GetComputeRotation(self) -> "bool":
        """GetComputeRotation(itkCenteredVersorTransformInitializerIUC3IUC3 self) -> bool"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUC3IUC3_GetComputeRotation(self)


    def ComputeRotationOn(self) -> "void":
        """ComputeRotationOn(itkCenteredVersorTransformInitializerIUC3IUC3 self)"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUC3IUC3_ComputeRotationOn(self)


    def ComputeRotationOff(self) -> "void":
        """ComputeRotationOff(itkCenteredVersorTransformInitializerIUC3IUC3 self)"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUC3IUC3_ComputeRotationOff(self)

    __swig_destroy__ = _itkCenteredVersorTransformInitializerPython.delete_itkCenteredVersorTransformInitializerIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkCenteredVersorTransformInitializerIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkCenteredVersorTransformInitializerIUC3IUC3"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkCenteredVersorTransformInitializerIUC3IUC3

        Create a new object of the class itkCenteredVersorTransformInitializerIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCenteredVersorTransformInitializerIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCenteredVersorTransformInitializerIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCenteredVersorTransformInitializerIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCenteredVersorTransformInitializerIUC3IUC3.Clone = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUC3IUC3_Clone, None, itkCenteredVersorTransformInitializerIUC3IUC3)
itkCenteredVersorTransformInitializerIUC3IUC3.SetComputeRotation = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUC3IUC3_SetComputeRotation, None, itkCenteredVersorTransformInitializerIUC3IUC3)
itkCenteredVersorTransformInitializerIUC3IUC3.GetComputeRotation = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUC3IUC3_GetComputeRotation, None, itkCenteredVersorTransformInitializerIUC3IUC3)
itkCenteredVersorTransformInitializerIUC3IUC3.ComputeRotationOn = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUC3IUC3_ComputeRotationOn, None, itkCenteredVersorTransformInitializerIUC3IUC3)
itkCenteredVersorTransformInitializerIUC3IUC3.ComputeRotationOff = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUC3IUC3_ComputeRotationOff, None, itkCenteredVersorTransformInitializerIUC3IUC3)
itkCenteredVersorTransformInitializerIUC3IUC3_swigregister = _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUC3IUC3_swigregister
itkCenteredVersorTransformInitializerIUC3IUC3_swigregister(itkCenteredVersorTransformInitializerIUC3IUC3)

def itkCenteredVersorTransformInitializerIUC3IUC3___New_orig__() -> "itkCenteredVersorTransformInitializerIUC3IUC3_Pointer":
    """itkCenteredVersorTransformInitializerIUC3IUC3___New_orig__() -> itkCenteredVersorTransformInitializerIUC3IUC3_Pointer"""
    return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUC3IUC3___New_orig__()

def itkCenteredVersorTransformInitializerIUC3IUC3_cast(obj: 'itkLightObject') -> "itkCenteredVersorTransformInitializerIUC3IUC3 *":
    """itkCenteredVersorTransformInitializerIUC3IUC3_cast(itkLightObject obj) -> itkCenteredVersorTransformInitializerIUC3IUC3"""
    return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUC3IUC3_cast(obj)

class itkCenteredVersorTransformInitializerIUS3IUS3(itkCenteredTransformInitializerPython.itkCenteredTransformInitializerVR3DTDIUS3IUS3):
    """


    CenteredVersorTransformInitializer is a helper class intended to
    initialize the center of rotation, versor, and translation of the
    VersorRigid3DTransform.

    This class derived from the CenteredTransformInitializer and uses it
    in a more constrained context. It always uses the Moments mode, and
    also takes advantage of the second order moments in order to
    initialize the Versor representing rotation.

    C++ includes: itkCenteredVersorTransformInitializer.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCenteredVersorTransformInitializerIUS3IUS3_Pointer":
        """__New_orig__() -> itkCenteredVersorTransformInitializerIUS3IUS3_Pointer"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUS3IUS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCenteredVersorTransformInitializerIUS3IUS3_Pointer":
        """Clone(itkCenteredVersorTransformInitializerIUS3IUS3 self) -> itkCenteredVersorTransformInitializerIUS3IUS3_Pointer"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUS3IUS3_Clone(self)


    def SetComputeRotation(self, _arg: 'bool const') -> "void":
        """
        SetComputeRotation(itkCenteredVersorTransformInitializerIUS3IUS3 self, bool const _arg)

        Enable the use
        of the principal axes of each image to compute an initial rotation
        that will align them. 
        """
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUS3IUS3_SetComputeRotation(self, _arg)


    def GetComputeRotation(self) -> "bool":
        """GetComputeRotation(itkCenteredVersorTransformInitializerIUS3IUS3 self) -> bool"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUS3IUS3_GetComputeRotation(self)


    def ComputeRotationOn(self) -> "void":
        """ComputeRotationOn(itkCenteredVersorTransformInitializerIUS3IUS3 self)"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUS3IUS3_ComputeRotationOn(self)


    def ComputeRotationOff(self) -> "void":
        """ComputeRotationOff(itkCenteredVersorTransformInitializerIUS3IUS3 self)"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUS3IUS3_ComputeRotationOff(self)

    __swig_destroy__ = _itkCenteredVersorTransformInitializerPython.delete_itkCenteredVersorTransformInitializerIUS3IUS3

    def cast(obj: 'itkLightObject') -> "itkCenteredVersorTransformInitializerIUS3IUS3 *":
        """cast(itkLightObject obj) -> itkCenteredVersorTransformInitializerIUS3IUS3"""
        return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUS3IUS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkCenteredVersorTransformInitializerIUS3IUS3

        Create a new object of the class itkCenteredVersorTransformInitializerIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCenteredVersorTransformInitializerIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCenteredVersorTransformInitializerIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCenteredVersorTransformInitializerIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCenteredVersorTransformInitializerIUS3IUS3.Clone = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUS3IUS3_Clone, None, itkCenteredVersorTransformInitializerIUS3IUS3)
itkCenteredVersorTransformInitializerIUS3IUS3.SetComputeRotation = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUS3IUS3_SetComputeRotation, None, itkCenteredVersorTransformInitializerIUS3IUS3)
itkCenteredVersorTransformInitializerIUS3IUS3.GetComputeRotation = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUS3IUS3_GetComputeRotation, None, itkCenteredVersorTransformInitializerIUS3IUS3)
itkCenteredVersorTransformInitializerIUS3IUS3.ComputeRotationOn = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUS3IUS3_ComputeRotationOn, None, itkCenteredVersorTransformInitializerIUS3IUS3)
itkCenteredVersorTransformInitializerIUS3IUS3.ComputeRotationOff = new_instancemethod(_itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUS3IUS3_ComputeRotationOff, None, itkCenteredVersorTransformInitializerIUS3IUS3)
itkCenteredVersorTransformInitializerIUS3IUS3_swigregister = _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUS3IUS3_swigregister
itkCenteredVersorTransformInitializerIUS3IUS3_swigregister(itkCenteredVersorTransformInitializerIUS3IUS3)

def itkCenteredVersorTransformInitializerIUS3IUS3___New_orig__() -> "itkCenteredVersorTransformInitializerIUS3IUS3_Pointer":
    """itkCenteredVersorTransformInitializerIUS3IUS3___New_orig__() -> itkCenteredVersorTransformInitializerIUS3IUS3_Pointer"""
    return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUS3IUS3___New_orig__()

def itkCenteredVersorTransformInitializerIUS3IUS3_cast(obj: 'itkLightObject') -> "itkCenteredVersorTransformInitializerIUS3IUS3 *":
    """itkCenteredVersorTransformInitializerIUS3IUS3_cast(itkLightObject obj) -> itkCenteredVersorTransformInitializerIUS3IUS3"""
    return _itkCenteredVersorTransformInitializerPython.itkCenteredVersorTransformInitializerIUS3IUS3_cast(obj)



