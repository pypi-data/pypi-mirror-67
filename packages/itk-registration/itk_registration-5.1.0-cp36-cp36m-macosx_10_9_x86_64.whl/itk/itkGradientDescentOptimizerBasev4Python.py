# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkGradientDescentOptimizerBasev4Python.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkGradientDescentOptimizerBasev4Python', [dirname(__file__)])
        except ImportError:
            import _itkGradientDescentOptimizerBasev4Python
            return _itkGradientDescentOptimizerBasev4Python
        if fp is not None:
            try:
                _mod = imp.load_module('_itkGradientDescentOptimizerBasev4Python', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkGradientDescentOptimizerBasev4Python = swig_import_helper()
    del swig_import_helper
else:
    import _itkGradientDescentOptimizerBasev4Python
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


import itkArrayPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import itkObjectToObjectOptimizerBasePython
import itkOptimizerParametersPython
import ITKCommonBasePython
import itkObjectToObjectMetricBasePython
import itkSingleValuedCostFunctionv4Python
import itkCostFunctionPython
import itkOptimizerParameterScalesEstimatorPython
import itkIndexPython
import itkOffsetPython
import itkSizePython

def itkGradientDescentOptimizerBasev4TemplateF_New():
  return itkGradientDescentOptimizerBasev4TemplateF.New()


def itkGradientDescentOptimizerBasev4TemplateD_New():
  return itkGradientDescentOptimizerBasev4TemplateD.New()

class itkGradientDescentOptimizerBasev4TemplateD(itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD):
    """Proxy of C++ itkGradientDescentOptimizerBasev4TemplateD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetGradient(self) -> "itkArrayD const &":
        """GetGradient(itkGradientDescentOptimizerBasev4TemplateD self) -> itkArrayD"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_GetGradient(self)


    def GetStopCondition(self) -> "itkObjectToObjectOptimizerBaseTemplateEnums::StopConditionObjectToObjectOptimizer const &":
        """GetStopCondition(itkGradientDescentOptimizerBasev4TemplateD self) -> itkObjectToObjectOptimizerBaseTemplateEnums::StopConditionObjectToObjectOptimizer const &"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_GetStopCondition(self)


    def StartOptimization(self, doOnlyInitialization: 'bool'=False) -> "void":
        """
        StartOptimization(itkGradientDescentOptimizerBasev4TemplateD self, bool doOnlyInitialization=False)
        StartOptimization(itkGradientDescentOptimizerBasev4TemplateD self)
        """
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_StartOptimization(self, doOnlyInitialization)


    def ResumeOptimization(self) -> "void":
        """ResumeOptimization(itkGradientDescentOptimizerBasev4TemplateD self)"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_ResumeOptimization(self)


    def StopOptimization(self) -> "void":
        """StopOptimization(itkGradientDescentOptimizerBasev4TemplateD self)"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_StopOptimization(self)


    def ModifyGradientByScales(self) -> "void":
        """ModifyGradientByScales(itkGradientDescentOptimizerBasev4TemplateD self)"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_ModifyGradientByScales(self)


    def ModifyGradientByLearningRate(self) -> "void":
        """ModifyGradientByLearningRate(itkGradientDescentOptimizerBasev4TemplateD self)"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_ModifyGradientByLearningRate(self)


    def ModifyGradientByScalesOverSubRange(self, subrange: 'itkIndex2') -> "void":
        """ModifyGradientByScalesOverSubRange(itkGradientDescentOptimizerBasev4TemplateD self, itkIndex2 subrange)"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_ModifyGradientByScalesOverSubRange(self, subrange)


    def ModifyGradientByLearningRateOverSubRange(self, subrange: 'itkIndex2') -> "void":
        """ModifyGradientByLearningRateOverSubRange(itkGradientDescentOptimizerBasev4TemplateD self, itkIndex2 subrange)"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_ModifyGradientByLearningRateOverSubRange(self, subrange)

    __swig_destroy__ = _itkGradientDescentOptimizerBasev4Python.delete_itkGradientDescentOptimizerBasev4TemplateD

    def cast(obj: 'itkLightObject') -> "itkGradientDescentOptimizerBasev4TemplateD *":
        """cast(itkLightObject obj) -> itkGradientDescentOptimizerBasev4TemplateD"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkGradientDescentOptimizerBasev4TemplateD

        Create a new object of the class itkGradientDescentOptimizerBasev4TemplateD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientDescentOptimizerBasev4TemplateD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientDescentOptimizerBasev4TemplateD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientDescentOptimizerBasev4TemplateD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGradientDescentOptimizerBasev4TemplateD.GetGradient = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_GetGradient, None, itkGradientDescentOptimizerBasev4TemplateD)
itkGradientDescentOptimizerBasev4TemplateD.GetStopCondition = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_GetStopCondition, None, itkGradientDescentOptimizerBasev4TemplateD)
itkGradientDescentOptimizerBasev4TemplateD.StartOptimization = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_StartOptimization, None, itkGradientDescentOptimizerBasev4TemplateD)
itkGradientDescentOptimizerBasev4TemplateD.ResumeOptimization = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_ResumeOptimization, None, itkGradientDescentOptimizerBasev4TemplateD)
itkGradientDescentOptimizerBasev4TemplateD.StopOptimization = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_StopOptimization, None, itkGradientDescentOptimizerBasev4TemplateD)
itkGradientDescentOptimizerBasev4TemplateD.ModifyGradientByScales = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_ModifyGradientByScales, None, itkGradientDescentOptimizerBasev4TemplateD)
itkGradientDescentOptimizerBasev4TemplateD.ModifyGradientByLearningRate = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_ModifyGradientByLearningRate, None, itkGradientDescentOptimizerBasev4TemplateD)
itkGradientDescentOptimizerBasev4TemplateD.ModifyGradientByScalesOverSubRange = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_ModifyGradientByScalesOverSubRange, None, itkGradientDescentOptimizerBasev4TemplateD)
itkGradientDescentOptimizerBasev4TemplateD.ModifyGradientByLearningRateOverSubRange = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_ModifyGradientByLearningRateOverSubRange, None, itkGradientDescentOptimizerBasev4TemplateD)
itkGradientDescentOptimizerBasev4TemplateD_swigregister = _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_swigregister
itkGradientDescentOptimizerBasev4TemplateD_swigregister(itkGradientDescentOptimizerBasev4TemplateD)

def itkGradientDescentOptimizerBasev4TemplateD_cast(obj: 'itkLightObject') -> "itkGradientDescentOptimizerBasev4TemplateD *":
    """itkGradientDescentOptimizerBasev4TemplateD_cast(itkLightObject obj) -> itkGradientDescentOptimizerBasev4TemplateD"""
    return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateD_cast(obj)

class itkGradientDescentOptimizerBasev4TemplateF(itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF):
    """Proxy of C++ itkGradientDescentOptimizerBasev4TemplateF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetGradient(self) -> "itkArrayF const &":
        """GetGradient(itkGradientDescentOptimizerBasev4TemplateF self) -> itkArrayF"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_GetGradient(self)


    def GetStopCondition(self) -> "itkObjectToObjectOptimizerBaseTemplateEnums::StopConditionObjectToObjectOptimizer const &":
        """GetStopCondition(itkGradientDescentOptimizerBasev4TemplateF self) -> itkObjectToObjectOptimizerBaseTemplateEnums::StopConditionObjectToObjectOptimizer const &"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_GetStopCondition(self)


    def StartOptimization(self, doOnlyInitialization: 'bool'=False) -> "void":
        """
        StartOptimization(itkGradientDescentOptimizerBasev4TemplateF self, bool doOnlyInitialization=False)
        StartOptimization(itkGradientDescentOptimizerBasev4TemplateF self)
        """
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_StartOptimization(self, doOnlyInitialization)


    def ResumeOptimization(self) -> "void":
        """ResumeOptimization(itkGradientDescentOptimizerBasev4TemplateF self)"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_ResumeOptimization(self)


    def StopOptimization(self) -> "void":
        """StopOptimization(itkGradientDescentOptimizerBasev4TemplateF self)"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_StopOptimization(self)


    def ModifyGradientByScales(self) -> "void":
        """ModifyGradientByScales(itkGradientDescentOptimizerBasev4TemplateF self)"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_ModifyGradientByScales(self)


    def ModifyGradientByLearningRate(self) -> "void":
        """ModifyGradientByLearningRate(itkGradientDescentOptimizerBasev4TemplateF self)"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_ModifyGradientByLearningRate(self)


    def ModifyGradientByScalesOverSubRange(self, subrange: 'itkIndex2') -> "void":
        """ModifyGradientByScalesOverSubRange(itkGradientDescentOptimizerBasev4TemplateF self, itkIndex2 subrange)"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_ModifyGradientByScalesOverSubRange(self, subrange)


    def ModifyGradientByLearningRateOverSubRange(self, subrange: 'itkIndex2') -> "void":
        """ModifyGradientByLearningRateOverSubRange(itkGradientDescentOptimizerBasev4TemplateF self, itkIndex2 subrange)"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_ModifyGradientByLearningRateOverSubRange(self, subrange)

    __swig_destroy__ = _itkGradientDescentOptimizerBasev4Python.delete_itkGradientDescentOptimizerBasev4TemplateF

    def cast(obj: 'itkLightObject') -> "itkGradientDescentOptimizerBasev4TemplateF *":
        """cast(itkLightObject obj) -> itkGradientDescentOptimizerBasev4TemplateF"""
        return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkGradientDescentOptimizerBasev4TemplateF

        Create a new object of the class itkGradientDescentOptimizerBasev4TemplateF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientDescentOptimizerBasev4TemplateF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGradientDescentOptimizerBasev4TemplateF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGradientDescentOptimizerBasev4TemplateF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGradientDescentOptimizerBasev4TemplateF.GetGradient = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_GetGradient, None, itkGradientDescentOptimizerBasev4TemplateF)
itkGradientDescentOptimizerBasev4TemplateF.GetStopCondition = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_GetStopCondition, None, itkGradientDescentOptimizerBasev4TemplateF)
itkGradientDescentOptimizerBasev4TemplateF.StartOptimization = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_StartOptimization, None, itkGradientDescentOptimizerBasev4TemplateF)
itkGradientDescentOptimizerBasev4TemplateF.ResumeOptimization = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_ResumeOptimization, None, itkGradientDescentOptimizerBasev4TemplateF)
itkGradientDescentOptimizerBasev4TemplateF.StopOptimization = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_StopOptimization, None, itkGradientDescentOptimizerBasev4TemplateF)
itkGradientDescentOptimizerBasev4TemplateF.ModifyGradientByScales = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_ModifyGradientByScales, None, itkGradientDescentOptimizerBasev4TemplateF)
itkGradientDescentOptimizerBasev4TemplateF.ModifyGradientByLearningRate = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_ModifyGradientByLearningRate, None, itkGradientDescentOptimizerBasev4TemplateF)
itkGradientDescentOptimizerBasev4TemplateF.ModifyGradientByScalesOverSubRange = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_ModifyGradientByScalesOverSubRange, None, itkGradientDescentOptimizerBasev4TemplateF)
itkGradientDescentOptimizerBasev4TemplateF.ModifyGradientByLearningRateOverSubRange = new_instancemethod(_itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_ModifyGradientByLearningRateOverSubRange, None, itkGradientDescentOptimizerBasev4TemplateF)
itkGradientDescentOptimizerBasev4TemplateF_swigregister = _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_swigregister
itkGradientDescentOptimizerBasev4TemplateF_swigregister(itkGradientDescentOptimizerBasev4TemplateF)

def itkGradientDescentOptimizerBasev4TemplateF_cast(obj: 'itkLightObject') -> "itkGradientDescentOptimizerBasev4TemplateF *":
    """itkGradientDescentOptimizerBasev4TemplateF_cast(itkLightObject obj) -> itkGradientDescentOptimizerBasev4TemplateF"""
    return _itkGradientDescentOptimizerBasev4Python.itkGradientDescentOptimizerBasev4TemplateF_cast(obj)



