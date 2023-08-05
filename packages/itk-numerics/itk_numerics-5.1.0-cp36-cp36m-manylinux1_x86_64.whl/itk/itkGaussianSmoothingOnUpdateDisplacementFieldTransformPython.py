# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython
            return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython
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
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import itkDisplacementFieldTransformPython
import itkTransformBasePython
import ITKCommonBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkFixedArrayPython
import itkMatrixPython
import itkVectorPython
import vnl_vector_refPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkVariableLengthVectorPython
import itkOptimizerParametersPython
import itkArray2DPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkImagePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkImageRegionPython

def itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_New():
  return itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3.New()


def itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_New():
  return itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2.New()

class itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2(itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2):
    """


    Modifies the UpdateTransformParameters method to peform a Gaussian
    smoothing of the displacement field after adding the update array.

    This class is the same as  DisplacementFieldTransform, except for the
    changes to UpdateTransformParameters. The method smooths the result of
    the addition of the update array and the displacement field, using a
    GaussianOperator filter.

    To free the memory allocated and cached in
    GaussianSmoothDisplacementField on demand, see
    FreeGaussianSmoothingTempField.

    C++ includes: itkGaussianSmoothingOnUpdateDisplacementFieldTransform.h

    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_Pointer":
        """__New_orig__() -> itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_Pointer"""
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_Pointer":
        """Clone(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2 self) -> itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_Pointer"""
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_Clone(self)


    def SetGaussianSmoothingVarianceForTheUpdateField(self, _arg: 'double const') -> "void":
        """
        SetGaussianSmoothingVarianceForTheUpdateField(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2 self, double const _arg)

        Get/Set the
        Gaussian smoothing standard deviation for the update field. Default =
        1.75. 
        """
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_SetGaussianSmoothingVarianceForTheUpdateField(self, _arg)


    def GetGaussianSmoothingVarianceForTheUpdateField(self) -> "double const &":
        """GetGaussianSmoothingVarianceForTheUpdateField(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2 self) -> double const &"""
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_GetGaussianSmoothingVarianceForTheUpdateField(self)


    def SetGaussianSmoothingVarianceForTheTotalField(self, _arg: 'double const') -> "void":
        """
        SetGaussianSmoothingVarianceForTheTotalField(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2 self, double const _arg)

        Get/Set the
        Gaussian smoothing standard deviation for the total field. Default =
        0.5. 
        """
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_SetGaussianSmoothingVarianceForTheTotalField(self, _arg)


    def GetGaussianSmoothingVarianceForTheTotalField(self) -> "double const &":
        """GetGaussianSmoothingVarianceForTheTotalField(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2 self) -> double const &"""
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_GetGaussianSmoothingVarianceForTheTotalField(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2 self, itkArrayD update)

        Update
        the transform's parameters by the values in update. We assume update
        is of the same length as Parameters. Throw exception otherwise. factor
        is a scalar multiplier for each value in update.
        GaussianSmoothDisplacementField is called after the update is added to
        the field. See base class for more details. 
        """
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_UpdateTransformParameters(self, update, factor)


    def GaussianSmoothDisplacementField(self, arg0: 'itkImageVD22', arg1: 'double') -> "itkImageVD22_Pointer":
        """
        GaussianSmoothDisplacementField(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2 self, itkImageVD22 arg0, double arg1) -> itkImageVD22_Pointer

        Smooth the displacement field in-place. Uses m_GaussSmoothSigma to
        change the variance for the GaussianOperator. WARNING:  Not thread
        safe. Does its own threading. 
        """
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_GaussianSmoothDisplacementField(self, arg0, arg1)

    __swig_destroy__ = _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.delete_itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2

    def cast(obj: 'itkLightObject') -> "itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2 *":
        """cast(itkLightObject obj) -> itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2"""
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2

        Create a new object of the class itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2.Clone = new_instancemethod(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_Clone, None, itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2.SetGaussianSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_SetGaussianSmoothingVarianceForTheUpdateField, None, itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2.GetGaussianSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_GetGaussianSmoothingVarianceForTheUpdateField, None, itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2.SetGaussianSmoothingVarianceForTheTotalField = new_instancemethod(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_SetGaussianSmoothingVarianceForTheTotalField, None, itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2.GetGaussianSmoothingVarianceForTheTotalField = new_instancemethod(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_GetGaussianSmoothingVarianceForTheTotalField, None, itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2.UpdateTransformParameters = new_instancemethod(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_UpdateTransformParameters, None, itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2.GaussianSmoothDisplacementField = new_instancemethod(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_GaussianSmoothDisplacementField, None, itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_swigregister = _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_swigregister
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_swigregister(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2)

def itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2___New_orig__() -> "itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_Pointer":
    """itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2___New_orig__() -> itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_Pointer"""
    return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2___New_orig__()

def itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_cast(obj: 'itkLightObject') -> "itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2 *":
    """itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_cast(itkLightObject obj) -> itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2"""
    return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_cast(obj)

class itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3(itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3):
    """


    Modifies the UpdateTransformParameters method to peform a Gaussian
    smoothing of the displacement field after adding the update array.

    This class is the same as  DisplacementFieldTransform, except for the
    changes to UpdateTransformParameters. The method smooths the result of
    the addition of the update array and the displacement field, using a
    GaussianOperator filter.

    To free the memory allocated and cached in
    GaussianSmoothDisplacementField on demand, see
    FreeGaussianSmoothingTempField.

    C++ includes: itkGaussianSmoothingOnUpdateDisplacementFieldTransform.h

    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_Pointer":
        """__New_orig__() -> itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_Pointer"""
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_Pointer":
        """Clone(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3 self) -> itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_Pointer"""
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_Clone(self)


    def SetGaussianSmoothingVarianceForTheUpdateField(self, _arg: 'double const') -> "void":
        """
        SetGaussianSmoothingVarianceForTheUpdateField(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3 self, double const _arg)

        Get/Set the
        Gaussian smoothing standard deviation for the update field. Default =
        1.75. 
        """
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_SetGaussianSmoothingVarianceForTheUpdateField(self, _arg)


    def GetGaussianSmoothingVarianceForTheUpdateField(self) -> "double const &":
        """GetGaussianSmoothingVarianceForTheUpdateField(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3 self) -> double const &"""
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_GetGaussianSmoothingVarianceForTheUpdateField(self)


    def SetGaussianSmoothingVarianceForTheTotalField(self, _arg: 'double const') -> "void":
        """
        SetGaussianSmoothingVarianceForTheTotalField(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3 self, double const _arg)

        Get/Set the
        Gaussian smoothing standard deviation for the total field. Default =
        0.5. 
        """
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_SetGaussianSmoothingVarianceForTheTotalField(self, _arg)


    def GetGaussianSmoothingVarianceForTheTotalField(self) -> "double const &":
        """GetGaussianSmoothingVarianceForTheTotalField(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3 self) -> double const &"""
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_GetGaussianSmoothingVarianceForTheTotalField(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3 self, itkArrayD update)

        Update
        the transform's parameters by the values in update. We assume update
        is of the same length as Parameters. Throw exception otherwise. factor
        is a scalar multiplier for each value in update.
        GaussianSmoothDisplacementField is called after the update is added to
        the field. See base class for more details. 
        """
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_UpdateTransformParameters(self, update, factor)


    def GaussianSmoothDisplacementField(self, arg0: 'itkImageVD33', arg1: 'double') -> "itkImageVD33_Pointer":
        """
        GaussianSmoothDisplacementField(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3 self, itkImageVD33 arg0, double arg1) -> itkImageVD33_Pointer

        Smooth the displacement field in-place. Uses m_GaussSmoothSigma to
        change the variance for the GaussianOperator. WARNING:  Not thread
        safe. Does its own threading. 
        """
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_GaussianSmoothDisplacementField(self, arg0, arg1)

    __swig_destroy__ = _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.delete_itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3

    def cast(obj: 'itkLightObject') -> "itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3 *":
        """cast(itkLightObject obj) -> itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3"""
        return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3

        Create a new object of the class itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3.Clone = new_instancemethod(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_Clone, None, itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3.SetGaussianSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_SetGaussianSmoothingVarianceForTheUpdateField, None, itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3.GetGaussianSmoothingVarianceForTheUpdateField = new_instancemethod(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_GetGaussianSmoothingVarianceForTheUpdateField, None, itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3.SetGaussianSmoothingVarianceForTheTotalField = new_instancemethod(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_SetGaussianSmoothingVarianceForTheTotalField, None, itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3.GetGaussianSmoothingVarianceForTheTotalField = new_instancemethod(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_GetGaussianSmoothingVarianceForTheTotalField, None, itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3.UpdateTransformParameters = new_instancemethod(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_UpdateTransformParameters, None, itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3.GaussianSmoothDisplacementField = new_instancemethod(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_GaussianSmoothDisplacementField, None, itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_swigregister = _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_swigregister
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_swigregister(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3)

def itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3___New_orig__() -> "itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_Pointer":
    """itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3___New_orig__() -> itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_Pointer"""
    return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3___New_orig__()

def itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_cast(obj: 'itkLightObject') -> "itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3 *":
    """itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_cast(itkLightObject obj) -> itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3"""
    return _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_cast(obj)



