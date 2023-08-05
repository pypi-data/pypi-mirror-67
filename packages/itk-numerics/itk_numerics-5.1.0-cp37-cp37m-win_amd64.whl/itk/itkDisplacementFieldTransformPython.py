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
    from . import _itkDisplacementFieldTransformPython
else:
    import _itkDisplacementFieldTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkDisplacementFieldTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkDisplacementFieldTransformPython.SWIG_PyStaticMethod_New

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

def itkDisplacementFieldTransformD3_New():
  return itkDisplacementFieldTransformD3.New()


def itkDisplacementFieldTransformD2_New():
  return itkDisplacementFieldTransformD2.New()

class itkDisplacementFieldTransformD2(itkTransformBasePython.itkTransformD22):
    r"""Proxy of C++ itkDisplacementFieldTransformD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_Clone)
    SetDisplacementField = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_SetDisplacementField)
    GetModifiableDisplacementField = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_GetModifiableDisplacementField)
    GetDisplacementField = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_GetDisplacementField)
    SetInverseDisplacementField = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_SetInverseDisplacementField)
    GetModifiableInverseDisplacementField = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_GetModifiableInverseDisplacementField)
    GetInverseDisplacementField = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_GetInverseDisplacementField)
    SetInterpolator = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_SetInterpolator)
    GetModifiableInterpolator = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_GetModifiableInterpolator)
    GetInterpolator = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_GetInterpolator)
    SetInverseInterpolator = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_SetInverseInterpolator)
    GetModifiableInverseInterpolator = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_GetModifiableInverseInterpolator)
    GetInverseInterpolator = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_GetInverseInterpolator)
    GetDisplacementFieldSetTime = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_GetDisplacementFieldSetTime)
    TransformVector = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_TransformVector)
    TransformDiffusionTensor = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_TransformDiffusionTensor)
    TransformCovariantVector = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_TransformCovariantVector)
    ComputeJacobianWithRespectToParameters = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_ComputeJacobianWithRespectToParameters)
    ComputeJacobianWithRespectToPosition = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_ComputeJacobianWithRespectToPosition)
    GetInverseJacobianOfForwardFieldWithRespectToPosition = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_GetInverseJacobianOfForwardFieldWithRespectToPosition)
    UpdateTransformParameters = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_UpdateTransformParameters)
    GetInverse = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_GetInverse)
    SetIdentity = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_SetIdentity)
    SetCoordinateTolerance = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_SetCoordinateTolerance)
    GetCoordinateTolerance = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_GetCoordinateTolerance)
    SetDirectionTolerance = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_SetDirectionTolerance)
    GetDirectionTolerance = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_GetDirectionTolerance)
    __swig_destroy__ = _itkDisplacementFieldTransformPython.delete_itkDisplacementFieldTransformD2
    cast = _swig_new_static_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkDisplacementFieldTransformD2

        Create a new object of the class itkDisplacementFieldTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDisplacementFieldTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDisplacementFieldTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDisplacementFieldTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDisplacementFieldTransformD2 in _itkDisplacementFieldTransformPython:
_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_swigregister(itkDisplacementFieldTransformD2)
itkDisplacementFieldTransformD2___New_orig__ = _itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2___New_orig__
itkDisplacementFieldTransformD2_cast = _itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2_cast

class itkDisplacementFieldTransformD3(itkTransformBasePython.itkTransformD33):
    r"""Proxy of C++ itkDisplacementFieldTransformD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_Clone)
    SetDisplacementField = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_SetDisplacementField)
    GetModifiableDisplacementField = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_GetModifiableDisplacementField)
    GetDisplacementField = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_GetDisplacementField)
    SetInverseDisplacementField = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_SetInverseDisplacementField)
    GetModifiableInverseDisplacementField = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_GetModifiableInverseDisplacementField)
    GetInverseDisplacementField = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_GetInverseDisplacementField)
    SetInterpolator = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_SetInterpolator)
    GetModifiableInterpolator = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_GetModifiableInterpolator)
    GetInterpolator = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_GetInterpolator)
    SetInverseInterpolator = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_SetInverseInterpolator)
    GetModifiableInverseInterpolator = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_GetModifiableInverseInterpolator)
    GetInverseInterpolator = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_GetInverseInterpolator)
    GetDisplacementFieldSetTime = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_GetDisplacementFieldSetTime)
    TransformVector = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_TransformVector)
    TransformDiffusionTensor = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_TransformDiffusionTensor)
    TransformCovariantVector = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_TransformCovariantVector)
    ComputeJacobianWithRespectToParameters = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_ComputeJacobianWithRespectToParameters)
    ComputeJacobianWithRespectToPosition = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_ComputeJacobianWithRespectToPosition)
    GetInverseJacobianOfForwardFieldWithRespectToPosition = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_GetInverseJacobianOfForwardFieldWithRespectToPosition)
    UpdateTransformParameters = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_UpdateTransformParameters)
    GetInverse = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_GetInverse)
    SetIdentity = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_SetIdentity)
    SetCoordinateTolerance = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_SetCoordinateTolerance)
    GetCoordinateTolerance = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_GetCoordinateTolerance)
    SetDirectionTolerance = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_SetDirectionTolerance)
    GetDirectionTolerance = _swig_new_instance_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_GetDirectionTolerance)
    __swig_destroy__ = _itkDisplacementFieldTransformPython.delete_itkDisplacementFieldTransformD3
    cast = _swig_new_static_method(_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkDisplacementFieldTransformD3

        Create a new object of the class itkDisplacementFieldTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDisplacementFieldTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDisplacementFieldTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDisplacementFieldTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDisplacementFieldTransformD3 in _itkDisplacementFieldTransformPython:
_itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_swigregister(itkDisplacementFieldTransformD3)
itkDisplacementFieldTransformD3___New_orig__ = _itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3___New_orig__
itkDisplacementFieldTransformD3_cast = _itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3_cast



