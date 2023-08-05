# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkGaussianExponentialDiffeomorphicTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkGaussianExponentialDiffeomorphicTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkGaussianExponentialDiffeomorphicTransformPython
            return _itkGaussianExponentialDiffeomorphicTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkGaussianExponentialDiffeomorphicTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkGaussianExponentialDiffeomorphicTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkGaussianExponentialDiffeomorphicTransformPython
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


import itkConstantVelocityFieldTransformPython
import itkOptimizerParametersPython
import itkArrayPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import ITKCommonBasePython
import itkDisplacementFieldTransformPython
import vnl_matrix_fixedPython
import itkArray2DPython
import itkCovariantVectorPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkVectorPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkImagePython
import itkPointPython
import itkMatrixPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkVariableLengthVectorPython

def itkGaussianExponentialDiffeomorphicTransformD3_New():
  return itkGaussianExponentialDiffeomorphicTransformD3.New()


def itkGaussianExponentialDiffeomorphicTransformD2_New():
  return itkGaussianExponentialDiffeomorphicTransformD2.New()

class itkGaussianExponentialDiffeomorphicTransformD2(itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2):
    """


    Exponential transform using a Gaussian smoothing kernel.

    Exponential transform inspired by the work of J. Ashburner (see
    reference below). Assuming a constant velocity field, the transform
    takes as input the update field at time point t = 1, $u$ and smooths
    it using Gaussian smoothing, $S_{update}$ defined by
    GaussianSmoothingVarianceForTheUpdateField We add that the current
    estimate of the velocity field and then perform a second smoothing
    step such that the new velocity field is

    \\begin{eqnarray*} v_{new} = S_{velocity}( v_{old} + S_{update}( u )
    ). \\end{eqnarray*}

    We then exponentiate $v_{new}$ using the class
    ExponentialDisplacementImageFilter to yield both the forward and
    inverse displacement fields.

    J. Ashburner. A Fast Diffeomorphic Image Registration Algorithm.
    NeuroImage, 38(1):95-113, 2007.

    Nick Tustison

    Brian Avants

    C++ includes: itkGaussianExponentialDiffeomorphicTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGaussianExponentialDiffeomorphicTransformD2_Pointer":
        """__New_orig__() -> itkGaussianExponentialDiffeomorphicTransformD2_Pointer"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGaussianExponentialDiffeomorphicTransformD2_Pointer":
        """Clone(itkGaussianExponentialDiffeomorphicTransformD2 self) -> itkGaussianExponentialDiffeomorphicTransformD2_Pointer"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_Clone(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkGaussianExponentialDiffeomorphicTransformD2 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkGaussianExponentialDiffeomorphicTransformD2 self, itkArrayD update)

        Update
        the transform's parameters by the values in update. We overwrite the
        base class implementation as we might want to smooth the update field
        before adding it to the velocity field 
        """
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_UpdateTransformParameters(self, update, factor)


    def GaussianSmoothConstantVelocityField(self, arg0: 'itkImageVD22', arg1: 'double') -> "itkImageVD22_Pointer":
        """
        GaussianSmoothConstantVelocityField(itkGaussianExponentialDiffeomorphicTransformD2 self, itkImageVD22 arg0, double arg1) -> itkImageVD22_Pointer

        Smooth the velocity field in-place. WARNING:  Not thread safe. Does
        its own threading. 
        """
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GaussianSmoothConstantVelocityField(self, arg0, arg1)


    def SetGaussianSmoothingVarianceForTheConstantVelocityField(self, _arg: 'double const') -> "void":
        """
        SetGaussianSmoothingVarianceForTheConstantVelocityField(itkGaussianExponentialDiffeomorphicTransformD2 self, double const _arg)

        Set/Get Gaussian smoothing parameter for the smoothed velocity field.

        """
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_SetGaussianSmoothingVarianceForTheConstantVelocityField(self, _arg)


    def GetGaussianSmoothingVarianceForTheConstantVelocityField(self) -> "double":
        """GetGaussianSmoothingVarianceForTheConstantVelocityField(itkGaussianExponentialDiffeomorphicTransformD2 self) -> double"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GetGaussianSmoothingVarianceForTheConstantVelocityField(self)


    def SetGaussianSmoothingVarianceForTheUpdateField(self, _arg: 'double const') -> "void":
        """
        SetGaussianSmoothingVarianceForTheUpdateField(itkGaussianExponentialDiffeomorphicTransformD2 self, double const _arg)

        Set/Get
        Gaussian smoothing parameter for the smoothed update field. 
        """
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_SetGaussianSmoothingVarianceForTheUpdateField(self, _arg)


    def GetGaussianSmoothingVarianceForTheUpdateField(self) -> "double":
        """GetGaussianSmoothingVarianceForTheUpdateField(itkGaussianExponentialDiffeomorphicTransformD2 self) -> double"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GetGaussianSmoothingVarianceForTheUpdateField(self)

    __swig_destroy__ = _itkGaussianExponentialDiffeomorphicTransformPython.delete_itkGaussianExponentialDiffeomorphicTransformD2

    def cast(obj: 'itkLightObject') -> "itkGaussianExponentialDiffeomorphicTransformD2 *":
        """cast(itkLightObject obj) -> itkGaussianExponentialDiffeomorphicTransformD2"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkGaussianExponentialDiffeomorphicTransformD2

        Create a new object of the class itkGaussianExponentialDiffeomorphicTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianExponentialDiffeomorphicTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGaussianExponentialDiffeomorphicTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGaussianExponentialDiffeomorphicTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGaussianExponentialDiffeomorphicTransformD2.Clone = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_Clone, None, itkGaussianExponentialDiffeomorphicTransformD2)
itkGaussianExponentialDiffeomorphicTransformD2.UpdateTransformParameters = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_UpdateTransformParameters, None, itkGaussianExponentialDiffeomorphicTransformD2)
itkGaussianExponentialDiffeomorphicTransformD2.GaussianSmoothConstantVelocityField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GaussianSmoothConstantVelocityField, None, itkGaussianExponentialDiffeomorphicTransformD2)
itkGaussianExponentialDiffeomorphicTransformD2.SetGaussianSmoothingVarianceForTheConstantVelocityField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_SetGaussianSmoothingVarianceForTheConstantVelocityField, None, itkGaussianExponentialDiffeomorphicTransformD2)
itkGaussianExponentialDiffeomorphicTransformD2.GetGaussianSmoothingVarianceForTheConstantVelocityField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GetGaussianSmoothingVarianceForTheConstantVelocityField, None, itkGaussianExponentialDiffeomorphicTransformD2)
itkGaussianExponentialDiffeomorphicTransformD2.SetGaussianSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_SetGaussianSmoothingVarianceForTheUpdateField, None, itkGaussianExponentialDiffeomorphicTransformD2)
itkGaussianExponentialDiffeomorphicTransformD2.GetGaussianSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GetGaussianSmoothingVarianceForTheUpdateField, None, itkGaussianExponentialDiffeomorphicTransformD2)
itkGaussianExponentialDiffeomorphicTransformD2_swigregister = _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_swigregister
itkGaussianExponentialDiffeomorphicTransformD2_swigregister(itkGaussianExponentialDiffeomorphicTransformD2)

def itkGaussianExponentialDiffeomorphicTransformD2___New_orig__() -> "itkGaussianExponentialDiffeomorphicTransformD2_Pointer":
    """itkGaussianExponentialDiffeomorphicTransformD2___New_orig__() -> itkGaussianExponentialDiffeomorphicTransformD2_Pointer"""
    return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2___New_orig__()

def itkGaussianExponentialDiffeomorphicTransformD2_cast(obj: 'itkLightObject') -> "itkGaussianExponentialDiffeomorphicTransformD2 *":
    """itkGaussianExponentialDiffeomorphicTransformD2_cast(itkLightObject obj) -> itkGaussianExponentialDiffeomorphicTransformD2"""
    return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_cast(obj)

class itkGaussianExponentialDiffeomorphicTransformD3(itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3):
    """


    Exponential transform using a Gaussian smoothing kernel.

    Exponential transform inspired by the work of J. Ashburner (see
    reference below). Assuming a constant velocity field, the transform
    takes as input the update field at time point t = 1, $u$ and smooths
    it using Gaussian smoothing, $S_{update}$ defined by
    GaussianSmoothingVarianceForTheUpdateField We add that the current
    estimate of the velocity field and then perform a second smoothing
    step such that the new velocity field is

    \\begin{eqnarray*} v_{new} = S_{velocity}( v_{old} + S_{update}( u )
    ). \\end{eqnarray*}

    We then exponentiate $v_{new}$ using the class
    ExponentialDisplacementImageFilter to yield both the forward and
    inverse displacement fields.

    J. Ashburner. A Fast Diffeomorphic Image Registration Algorithm.
    NeuroImage, 38(1):95-113, 2007.

    Nick Tustison

    Brian Avants

    C++ includes: itkGaussianExponentialDiffeomorphicTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGaussianExponentialDiffeomorphicTransformD3_Pointer":
        """__New_orig__() -> itkGaussianExponentialDiffeomorphicTransformD3_Pointer"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGaussianExponentialDiffeomorphicTransformD3_Pointer":
        """Clone(itkGaussianExponentialDiffeomorphicTransformD3 self) -> itkGaussianExponentialDiffeomorphicTransformD3_Pointer"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_Clone(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkGaussianExponentialDiffeomorphicTransformD3 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkGaussianExponentialDiffeomorphicTransformD3 self, itkArrayD update)

        Update
        the transform's parameters by the values in update. We overwrite the
        base class implementation as we might want to smooth the update field
        before adding it to the velocity field 
        """
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_UpdateTransformParameters(self, update, factor)


    def GaussianSmoothConstantVelocityField(self, arg0: 'itkImageVD33', arg1: 'double') -> "itkImageVD33_Pointer":
        """
        GaussianSmoothConstantVelocityField(itkGaussianExponentialDiffeomorphicTransformD3 self, itkImageVD33 arg0, double arg1) -> itkImageVD33_Pointer

        Smooth the velocity field in-place. WARNING:  Not thread safe. Does
        its own threading. 
        """
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GaussianSmoothConstantVelocityField(self, arg0, arg1)


    def SetGaussianSmoothingVarianceForTheConstantVelocityField(self, _arg: 'double const') -> "void":
        """
        SetGaussianSmoothingVarianceForTheConstantVelocityField(itkGaussianExponentialDiffeomorphicTransformD3 self, double const _arg)

        Set/Get Gaussian smoothing parameter for the smoothed velocity field.

        """
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_SetGaussianSmoothingVarianceForTheConstantVelocityField(self, _arg)


    def GetGaussianSmoothingVarianceForTheConstantVelocityField(self) -> "double":
        """GetGaussianSmoothingVarianceForTheConstantVelocityField(itkGaussianExponentialDiffeomorphicTransformD3 self) -> double"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GetGaussianSmoothingVarianceForTheConstantVelocityField(self)


    def SetGaussianSmoothingVarianceForTheUpdateField(self, _arg: 'double const') -> "void":
        """
        SetGaussianSmoothingVarianceForTheUpdateField(itkGaussianExponentialDiffeomorphicTransformD3 self, double const _arg)

        Set/Get
        Gaussian smoothing parameter for the smoothed update field. 
        """
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_SetGaussianSmoothingVarianceForTheUpdateField(self, _arg)


    def GetGaussianSmoothingVarianceForTheUpdateField(self) -> "double":
        """GetGaussianSmoothingVarianceForTheUpdateField(itkGaussianExponentialDiffeomorphicTransformD3 self) -> double"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GetGaussianSmoothingVarianceForTheUpdateField(self)

    __swig_destroy__ = _itkGaussianExponentialDiffeomorphicTransformPython.delete_itkGaussianExponentialDiffeomorphicTransformD3

    def cast(obj: 'itkLightObject') -> "itkGaussianExponentialDiffeomorphicTransformD3 *":
        """cast(itkLightObject obj) -> itkGaussianExponentialDiffeomorphicTransformD3"""
        return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkGaussianExponentialDiffeomorphicTransformD3

        Create a new object of the class itkGaussianExponentialDiffeomorphicTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianExponentialDiffeomorphicTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGaussianExponentialDiffeomorphicTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGaussianExponentialDiffeomorphicTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGaussianExponentialDiffeomorphicTransformD3.Clone = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_Clone, None, itkGaussianExponentialDiffeomorphicTransformD3)
itkGaussianExponentialDiffeomorphicTransformD3.UpdateTransformParameters = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_UpdateTransformParameters, None, itkGaussianExponentialDiffeomorphicTransformD3)
itkGaussianExponentialDiffeomorphicTransformD3.GaussianSmoothConstantVelocityField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GaussianSmoothConstantVelocityField, None, itkGaussianExponentialDiffeomorphicTransformD3)
itkGaussianExponentialDiffeomorphicTransformD3.SetGaussianSmoothingVarianceForTheConstantVelocityField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_SetGaussianSmoothingVarianceForTheConstantVelocityField, None, itkGaussianExponentialDiffeomorphicTransformD3)
itkGaussianExponentialDiffeomorphicTransformD3.GetGaussianSmoothingVarianceForTheConstantVelocityField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GetGaussianSmoothingVarianceForTheConstantVelocityField, None, itkGaussianExponentialDiffeomorphicTransformD3)
itkGaussianExponentialDiffeomorphicTransformD3.SetGaussianSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_SetGaussianSmoothingVarianceForTheUpdateField, None, itkGaussianExponentialDiffeomorphicTransformD3)
itkGaussianExponentialDiffeomorphicTransformD3.GetGaussianSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GetGaussianSmoothingVarianceForTheUpdateField, None, itkGaussianExponentialDiffeomorphicTransformD3)
itkGaussianExponentialDiffeomorphicTransformD3_swigregister = _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_swigregister
itkGaussianExponentialDiffeomorphicTransformD3_swigregister(itkGaussianExponentialDiffeomorphicTransformD3)

def itkGaussianExponentialDiffeomorphicTransformD3___New_orig__() -> "itkGaussianExponentialDiffeomorphicTransformD3_Pointer":
    """itkGaussianExponentialDiffeomorphicTransformD3___New_orig__() -> itkGaussianExponentialDiffeomorphicTransformD3_Pointer"""
    return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3___New_orig__()

def itkGaussianExponentialDiffeomorphicTransformD3_cast(obj: 'itkLightObject') -> "itkGaussianExponentialDiffeomorphicTransformD3 *":
    """itkGaussianExponentialDiffeomorphicTransformD3_cast(itkLightObject obj) -> itkGaussianExponentialDiffeomorphicTransformD3"""
    return _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_cast(obj)



