# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkExhaustiveOptimizerv4Python.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkExhaustiveOptimizerv4Python', [dirname(__file__)])
        except ImportError:
            import _itkExhaustiveOptimizerv4Python
            return _itkExhaustiveOptimizerv4Python
        if fp is not None:
            try:
                _mod = imp.load_module('_itkExhaustiveOptimizerv4Python', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkExhaustiveOptimizerv4Python = swig_import_helper()
    del swig_import_helper
else:
    import _itkExhaustiveOptimizerv4Python
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


import itkOptimizerParametersPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import itkArrayPython
import ITKCommonBasePython
import itkObjectToObjectOptimizerBasePython
import itkOptimizerParameterScalesEstimatorPython
import itkObjectToObjectMetricBasePython
import itkSingleValuedCostFunctionv4Python
import itkCostFunctionPython

def itkExhaustiveOptimizerv4D_New():
  return itkExhaustiveOptimizerv4D.New()


def itkExhaustiveOptimizerv4F_New():
  return itkExhaustiveOptimizerv4F.New()

class itkExhaustiveOptimizerv4D(itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD):
    """


    Optimizer that fully samples a grid on the parametric space.

    This optimizer is equivalent to an exhaustive search in a discrete
    grid defined over the parametric space. The grid is centered on the
    initial position. The subdivisions of the grid along each one of the
    dimensions of the parametric space is defined by an array of number of
    steps.

    A typical use is to plot the metric space to get an idea of how noisy
    it space with respect to translations along x, y and z in a 3D
    registration application: Here it is assumed that the transform is
    Euler3DTransform.

    The optimizer throws IterationEvents after every iteration. We use
    this to plot the metric space in an image as follows:

    The image size is expected to be 11 x 11 x 11.

    If you wish to use different step lengths along each parametric axis,
    you can use the SetScales() method. This accepts an array, each
    element represents the number of subdivisions per step length. For
    instance scales of [0.5 1 4] along with a step length of 2 will cause
    the optimizer to search the metric space on a grid with x,y,z spacing
    of [1 2 8].

    Physical dimensions of the grid are influenced by both the scales and
    the number of steps along each dimension, a side of the region is
    stepLength*(2*numberOfSteps[d]+1)*scaling[d].

    C++ includes: itkExhaustiveOptimizerv4.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkExhaustiveOptimizerv4D_Pointer":
        """__New_orig__() -> itkExhaustiveOptimizerv4D_Pointer"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkExhaustiveOptimizerv4D_Pointer":
        """Clone(itkExhaustiveOptimizerv4D self) -> itkExhaustiveOptimizerv4D_Pointer"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_Clone(self)


    def StartOptimization(self, doOnlyInitialization: 'bool'=False) -> "void":
        """
        StartOptimization(itkExhaustiveOptimizerv4D self, bool doOnlyInitialization=False)
        StartOptimization(itkExhaustiveOptimizerv4D self)
        """
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_StartOptimization(self, doOnlyInitialization)


    def StartWalking(self) -> "void":
        """
        StartWalking(itkExhaustiveOptimizerv4D self)

        Start optimization 
        """
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_StartWalking(self)


    def ResumeWalking(self) -> "void":
        """
        ResumeWalking(itkExhaustiveOptimizerv4D self)

        Resume the
        optimization 
        """
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_ResumeWalking(self)


    def StopWalking(self) -> "void":
        """
        StopWalking(itkExhaustiveOptimizerv4D self)

        Stop optimization 
        """
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_StopWalking(self)


    def SetStepLength(self, _arg: 'double const') -> "void":
        """SetStepLength(itkExhaustiveOptimizerv4D self, double const _arg)"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_SetStepLength(self, _arg)


    def SetNumberOfSteps(self, _arg: 'itkArrayUL') -> "void":
        """SetNumberOfSteps(itkExhaustiveOptimizerv4D self, itkArrayUL _arg)"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_SetNumberOfSteps(self, _arg)


    def GetStepLength(self) -> "double const &":
        """GetStepLength(itkExhaustiveOptimizerv4D self) -> double const &"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetStepLength(self)


    def GetNumberOfSteps(self) -> "itkArrayUL const &":
        """GetNumberOfSteps(itkExhaustiveOptimizerv4D self) -> itkArrayUL"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetNumberOfSteps(self)


    def GetCurrentValue(self) -> "double const &":
        """GetCurrentValue(itkExhaustiveOptimizerv4D self) -> double const &"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetCurrentValue(self)


    def GetMaximumMetricValue(self) -> "double const &":
        """GetMaximumMetricValue(itkExhaustiveOptimizerv4D self) -> double const &"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetMaximumMetricValue(self)


    def GetMinimumMetricValue(self) -> "double const &":
        """GetMinimumMetricValue(itkExhaustiveOptimizerv4D self) -> double const &"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetMinimumMetricValue(self)


    def GetMinimumMetricValuePosition(self) -> "itkOptimizerParametersD const &":
        """GetMinimumMetricValuePosition(itkExhaustiveOptimizerv4D self) -> itkOptimizerParametersD"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetMinimumMetricValuePosition(self)


    def GetMaximumMetricValuePosition(self) -> "itkOptimizerParametersD const &":
        """GetMaximumMetricValuePosition(itkExhaustiveOptimizerv4D self) -> itkOptimizerParametersD"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetMaximumMetricValuePosition(self)


    def GetCurrentIndex(self) -> "itkOptimizerParametersD const &":
        """GetCurrentIndex(itkExhaustiveOptimizerv4D self) -> itkOptimizerParametersD"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetCurrentIndex(self)


    def SetInitialPosition(self, param: 'itkOptimizerParametersD') -> "void":
        """
        SetInitialPosition(itkExhaustiveOptimizerv4D self, itkOptimizerParametersD param)

        Set the position
        to initialize the optimization. 
        """
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_SetInitialPosition(self, param)


    def GetInitialPosition(self) -> "itkOptimizerParametersD &":
        """
        GetInitialPosition(itkExhaustiveOptimizerv4D self) -> itkOptimizerParametersD

        Get the position
        to initialize the optimization. 
        """
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetInitialPosition(self)

    __swig_destroy__ = _itkExhaustiveOptimizerv4Python.delete_itkExhaustiveOptimizerv4D

    def cast(obj: 'itkLightObject') -> "itkExhaustiveOptimizerv4D *":
        """cast(itkLightObject obj) -> itkExhaustiveOptimizerv4D"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExhaustiveOptimizerv4D

        Create a new object of the class itkExhaustiveOptimizerv4D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExhaustiveOptimizerv4D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExhaustiveOptimizerv4D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExhaustiveOptimizerv4D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExhaustiveOptimizerv4D.Clone = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_Clone, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D.StartOptimization = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_StartOptimization, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D.StartWalking = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_StartWalking, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D.ResumeWalking = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_ResumeWalking, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D.StopWalking = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_StopWalking, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D.SetStepLength = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_SetStepLength, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D.SetNumberOfSteps = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_SetNumberOfSteps, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D.GetStepLength = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetStepLength, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D.GetNumberOfSteps = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetNumberOfSteps, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D.GetCurrentValue = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetCurrentValue, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D.GetMaximumMetricValue = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetMaximumMetricValue, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D.GetMinimumMetricValue = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetMinimumMetricValue, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D.GetMinimumMetricValuePosition = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetMinimumMetricValuePosition, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D.GetMaximumMetricValuePosition = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetMaximumMetricValuePosition, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D.GetCurrentIndex = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetCurrentIndex, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D.SetInitialPosition = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_SetInitialPosition, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D.GetInitialPosition = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetInitialPosition, None, itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D_swigregister = _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_swigregister
itkExhaustiveOptimizerv4D_swigregister(itkExhaustiveOptimizerv4D)

def itkExhaustiveOptimizerv4D___New_orig__() -> "itkExhaustiveOptimizerv4D_Pointer":
    """itkExhaustiveOptimizerv4D___New_orig__() -> itkExhaustiveOptimizerv4D_Pointer"""
    return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D___New_orig__()

def itkExhaustiveOptimizerv4D_cast(obj: 'itkLightObject') -> "itkExhaustiveOptimizerv4D *":
    """itkExhaustiveOptimizerv4D_cast(itkLightObject obj) -> itkExhaustiveOptimizerv4D"""
    return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_cast(obj)

class itkExhaustiveOptimizerv4F(itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF):
    """


    Optimizer that fully samples a grid on the parametric space.

    This optimizer is equivalent to an exhaustive search in a discrete
    grid defined over the parametric space. The grid is centered on the
    initial position. The subdivisions of the grid along each one of the
    dimensions of the parametric space is defined by an array of number of
    steps.

    A typical use is to plot the metric space to get an idea of how noisy
    it space with respect to translations along x, y and z in a 3D
    registration application: Here it is assumed that the transform is
    Euler3DTransform.

    The optimizer throws IterationEvents after every iteration. We use
    this to plot the metric space in an image as follows:

    The image size is expected to be 11 x 11 x 11.

    If you wish to use different step lengths along each parametric axis,
    you can use the SetScales() method. This accepts an array, each
    element represents the number of subdivisions per step length. For
    instance scales of [0.5 1 4] along with a step length of 2 will cause
    the optimizer to search the metric space on a grid with x,y,z spacing
    of [1 2 8].

    Physical dimensions of the grid are influenced by both the scales and
    the number of steps along each dimension, a side of the region is
    stepLength*(2*numberOfSteps[d]+1)*scaling[d].

    C++ includes: itkExhaustiveOptimizerv4.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkExhaustiveOptimizerv4F_Pointer":
        """__New_orig__() -> itkExhaustiveOptimizerv4F_Pointer"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkExhaustiveOptimizerv4F_Pointer":
        """Clone(itkExhaustiveOptimizerv4F self) -> itkExhaustiveOptimizerv4F_Pointer"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_Clone(self)


    def StartOptimization(self, doOnlyInitialization: 'bool'=False) -> "void":
        """
        StartOptimization(itkExhaustiveOptimizerv4F self, bool doOnlyInitialization=False)
        StartOptimization(itkExhaustiveOptimizerv4F self)
        """
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_StartOptimization(self, doOnlyInitialization)


    def StartWalking(self) -> "void":
        """
        StartWalking(itkExhaustiveOptimizerv4F self)

        Start optimization 
        """
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_StartWalking(self)


    def ResumeWalking(self) -> "void":
        """
        ResumeWalking(itkExhaustiveOptimizerv4F self)

        Resume the
        optimization 
        """
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_ResumeWalking(self)


    def StopWalking(self) -> "void":
        """
        StopWalking(itkExhaustiveOptimizerv4F self)

        Stop optimization 
        """
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_StopWalking(self)


    def SetStepLength(self, _arg: 'double const') -> "void":
        """SetStepLength(itkExhaustiveOptimizerv4F self, double const _arg)"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_SetStepLength(self, _arg)


    def SetNumberOfSteps(self, _arg: 'itkArrayUL') -> "void":
        """SetNumberOfSteps(itkExhaustiveOptimizerv4F self, itkArrayUL _arg)"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_SetNumberOfSteps(self, _arg)


    def GetStepLength(self) -> "double const &":
        """GetStepLength(itkExhaustiveOptimizerv4F self) -> double const &"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetStepLength(self)


    def GetNumberOfSteps(self) -> "itkArrayUL const &":
        """GetNumberOfSteps(itkExhaustiveOptimizerv4F self) -> itkArrayUL"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetNumberOfSteps(self)


    def GetCurrentValue(self) -> "float const &":
        """GetCurrentValue(itkExhaustiveOptimizerv4F self) -> float const &"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetCurrentValue(self)


    def GetMaximumMetricValue(self) -> "float const &":
        """GetMaximumMetricValue(itkExhaustiveOptimizerv4F self) -> float const &"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetMaximumMetricValue(self)


    def GetMinimumMetricValue(self) -> "float const &":
        """GetMinimumMetricValue(itkExhaustiveOptimizerv4F self) -> float const &"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetMinimumMetricValue(self)


    def GetMinimumMetricValuePosition(self) -> "itkOptimizerParametersF const &":
        """GetMinimumMetricValuePosition(itkExhaustiveOptimizerv4F self) -> itkOptimizerParametersF"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetMinimumMetricValuePosition(self)


    def GetMaximumMetricValuePosition(self) -> "itkOptimizerParametersF const &":
        """GetMaximumMetricValuePosition(itkExhaustiveOptimizerv4F self) -> itkOptimizerParametersF"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetMaximumMetricValuePosition(self)


    def GetCurrentIndex(self) -> "itkOptimizerParametersF const &":
        """GetCurrentIndex(itkExhaustiveOptimizerv4F self) -> itkOptimizerParametersF"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetCurrentIndex(self)


    def SetInitialPosition(self, param: 'itkOptimizerParametersF') -> "void":
        """
        SetInitialPosition(itkExhaustiveOptimizerv4F self, itkOptimizerParametersF param)

        Set the position
        to initialize the optimization. 
        """
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_SetInitialPosition(self, param)


    def GetInitialPosition(self) -> "itkOptimizerParametersF &":
        """
        GetInitialPosition(itkExhaustiveOptimizerv4F self) -> itkOptimizerParametersF

        Get the position
        to initialize the optimization. 
        """
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetInitialPosition(self)

    __swig_destroy__ = _itkExhaustiveOptimizerv4Python.delete_itkExhaustiveOptimizerv4F

    def cast(obj: 'itkLightObject') -> "itkExhaustiveOptimizerv4F *":
        """cast(itkLightObject obj) -> itkExhaustiveOptimizerv4F"""
        return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExhaustiveOptimizerv4F

        Create a new object of the class itkExhaustiveOptimizerv4F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExhaustiveOptimizerv4F.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExhaustiveOptimizerv4F.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExhaustiveOptimizerv4F.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExhaustiveOptimizerv4F.Clone = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_Clone, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F.StartOptimization = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_StartOptimization, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F.StartWalking = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_StartWalking, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F.ResumeWalking = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_ResumeWalking, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F.StopWalking = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_StopWalking, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F.SetStepLength = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_SetStepLength, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F.SetNumberOfSteps = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_SetNumberOfSteps, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F.GetStepLength = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetStepLength, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F.GetNumberOfSteps = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetNumberOfSteps, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F.GetCurrentValue = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetCurrentValue, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F.GetMaximumMetricValue = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetMaximumMetricValue, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F.GetMinimumMetricValue = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetMinimumMetricValue, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F.GetMinimumMetricValuePosition = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetMinimumMetricValuePosition, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F.GetMaximumMetricValuePosition = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetMaximumMetricValuePosition, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F.GetCurrentIndex = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetCurrentIndex, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F.SetInitialPosition = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_SetInitialPosition, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F.GetInitialPosition = new_instancemethod(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetInitialPosition, None, itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F_swigregister = _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_swigregister
itkExhaustiveOptimizerv4F_swigregister(itkExhaustiveOptimizerv4F)

def itkExhaustiveOptimizerv4F___New_orig__() -> "itkExhaustiveOptimizerv4F_Pointer":
    """itkExhaustiveOptimizerv4F___New_orig__() -> itkExhaustiveOptimizerv4F_Pointer"""
    return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F___New_orig__()

def itkExhaustiveOptimizerv4F_cast(obj: 'itkLightObject') -> "itkExhaustiveOptimizerv4F *":
    """itkExhaustiveOptimizerv4F_cast(itkLightObject obj) -> itkExhaustiveOptimizerv4F"""
    return _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_cast(obj)



