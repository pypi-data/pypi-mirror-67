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
    from . import _itkConstantVelocityFieldTransformPython
else:
    import _itkConstantVelocityFieldTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkConstantVelocityFieldTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkConstantVelocityFieldTransformPython.SWIG_PyStaticMethod_New

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
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkPointPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import vnl_matrix_fixedPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import itkOptimizerParametersPython
import itkArrayPython
import itkTransformBasePython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkImagePython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageRegionPython

def itkConstantVelocityFieldTransformD3_New():
  return itkConstantVelocityFieldTransformD3.New()


def itkConstantVelocityFieldTransformD2_New():
  return itkConstantVelocityFieldTransformD2.New()

class itkConstantVelocityFieldTransformD2(itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2):
    r"""Proxy of C++ itkConstantVelocityFieldTransformD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_Clone)
    SetConstantVelocityField = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetConstantVelocityField)
    GetModifiableConstantVelocityField = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetModifiableConstantVelocityField)
    GetConstantVelocityField = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetConstantVelocityField)
    SetConstantVelocityFieldInterpolator = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetConstantVelocityFieldInterpolator)
    GetModifiableConstantVelocityFieldInterpolator = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetModifiableConstantVelocityFieldInterpolator)
    GetConstantVelocityFieldInterpolator = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetConstantVelocityFieldInterpolator)
    GetConstantVelocityFieldSetTime = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetConstantVelocityFieldSetTime)
    UpdateTransformParameters = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_UpdateTransformParameters)
    GetInverse = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetInverse)
    IntegrateVelocityField = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_IntegrateVelocityField)
    SetCalculateNumberOfIntegrationStepsAutomatically = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetCalculateNumberOfIntegrationStepsAutomatically)
    GetCalculateNumberOfIntegrationStepsAutomatically = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetCalculateNumberOfIntegrationStepsAutomatically)
    CalculateNumberOfIntegrationStepsAutomaticallyOn = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_CalculateNumberOfIntegrationStepsAutomaticallyOn)
    CalculateNumberOfIntegrationStepsAutomaticallyOff = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_CalculateNumberOfIntegrationStepsAutomaticallyOff)
    SetLowerTimeBound = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetLowerTimeBound)
    GetLowerTimeBound = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetLowerTimeBound)
    SetUpperTimeBound = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetUpperTimeBound)
    GetUpperTimeBound = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetUpperTimeBound)
    SetNumberOfIntegrationSteps = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetNumberOfIntegrationSteps)
    GetNumberOfIntegrationSteps = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetNumberOfIntegrationSteps)
    __swig_destroy__ = _itkConstantVelocityFieldTransformPython.delete_itkConstantVelocityFieldTransformD2
    cast = _swig_new_static_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkConstantVelocityFieldTransformD2

        Create a new object of the class itkConstantVelocityFieldTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkConstantVelocityFieldTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkConstantVelocityFieldTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkConstantVelocityFieldTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkConstantVelocityFieldTransformD2 in _itkConstantVelocityFieldTransformPython:
_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_swigregister(itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2___New_orig__ = _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2___New_orig__
itkConstantVelocityFieldTransformD2_cast = _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_cast

class itkConstantVelocityFieldTransformD3(itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3):
    r"""Proxy of C++ itkConstantVelocityFieldTransformD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_Clone)
    SetConstantVelocityField = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetConstantVelocityField)
    GetModifiableConstantVelocityField = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetModifiableConstantVelocityField)
    GetConstantVelocityField = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetConstantVelocityField)
    SetConstantVelocityFieldInterpolator = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetConstantVelocityFieldInterpolator)
    GetModifiableConstantVelocityFieldInterpolator = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetModifiableConstantVelocityFieldInterpolator)
    GetConstantVelocityFieldInterpolator = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetConstantVelocityFieldInterpolator)
    GetConstantVelocityFieldSetTime = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetConstantVelocityFieldSetTime)
    UpdateTransformParameters = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_UpdateTransformParameters)
    GetInverse = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetInverse)
    IntegrateVelocityField = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_IntegrateVelocityField)
    SetCalculateNumberOfIntegrationStepsAutomatically = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetCalculateNumberOfIntegrationStepsAutomatically)
    GetCalculateNumberOfIntegrationStepsAutomatically = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetCalculateNumberOfIntegrationStepsAutomatically)
    CalculateNumberOfIntegrationStepsAutomaticallyOn = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_CalculateNumberOfIntegrationStepsAutomaticallyOn)
    CalculateNumberOfIntegrationStepsAutomaticallyOff = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_CalculateNumberOfIntegrationStepsAutomaticallyOff)
    SetLowerTimeBound = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetLowerTimeBound)
    GetLowerTimeBound = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetLowerTimeBound)
    SetUpperTimeBound = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetUpperTimeBound)
    GetUpperTimeBound = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetUpperTimeBound)
    SetNumberOfIntegrationSteps = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetNumberOfIntegrationSteps)
    GetNumberOfIntegrationSteps = _swig_new_instance_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetNumberOfIntegrationSteps)
    __swig_destroy__ = _itkConstantVelocityFieldTransformPython.delete_itkConstantVelocityFieldTransformD3
    cast = _swig_new_static_method(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkConstantVelocityFieldTransformD3

        Create a new object of the class itkConstantVelocityFieldTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkConstantVelocityFieldTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkConstantVelocityFieldTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkConstantVelocityFieldTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkConstantVelocityFieldTransformD3 in _itkConstantVelocityFieldTransformPython:
_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_swigregister(itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3___New_orig__ = _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3___New_orig__
itkConstantVelocityFieldTransformD3_cast = _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_cast



