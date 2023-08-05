# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkConstantVelocityFieldTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkConstantVelocityFieldTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkConstantVelocityFieldTransformPython
            return _itkConstantVelocityFieldTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkConstantVelocityFieldTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkConstantVelocityFieldTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkConstantVelocityFieldTransformPython
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
import itkArrayPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkDisplacementFieldTransformPython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkArray2DPython
import itkCovariantVectorPython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkDiffusionTensor3DPython
import itkVariableLengthVectorPython
import itkOptimizerParametersPython
import itkImagePython
import itkImageRegionPython
import itkRGBPixelPython
import itkRGBAPixelPython

def itkConstantVelocityFieldTransformD3_New():
  return itkConstantVelocityFieldTransformD3.New()


def itkConstantVelocityFieldTransformD2_New():
  return itkConstantVelocityFieldTransformD2.New()

class itkConstantVelocityFieldTransformD2(itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2):
    """


    Provides local/dense/high-dimensionality transformation via a a
    constant velocity field.

    Nick Tustison

    Brian Avants

    C++ includes: itkConstantVelocityFieldTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkConstantVelocityFieldTransformD2_Pointer":
        """__New_orig__() -> itkConstantVelocityFieldTransformD2_Pointer"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkConstantVelocityFieldTransformD2_Pointer":
        """Clone(itkConstantVelocityFieldTransformD2 self) -> itkConstantVelocityFieldTransformD2_Pointer"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_Clone(self)


    def SetConstantVelocityField(self, arg0: 'itkImageVD22') -> "void":
        """
        SetConstantVelocityField(itkConstantVelocityFieldTransformD2 self, itkImageVD22 arg0)

        Get/Set
        the velocity field. Set the displacement field. Create special set
        accessor to update interpolator and assign displacement field to
        transform parameters container. 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetConstantVelocityField(self, arg0)


    def GetModifiableConstantVelocityField(self) -> "itkImageVD22 *":
        """GetModifiableConstantVelocityField(itkConstantVelocityFieldTransformD2 self) -> itkImageVD22"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetModifiableConstantVelocityField(self)


    def GetConstantVelocityField(self, *args) -> "itkImageVD22 *":
        """
        GetConstantVelocityField(itkConstantVelocityFieldTransformD2 self) -> itkImageVD22
        GetConstantVelocityField(itkConstantVelocityFieldTransformD2 self) -> itkImageVD22
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetConstantVelocityField(self, *args)


    def SetConstantVelocityFieldInterpolator(self, arg0: 'itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,2 >,2 >,double > *') -> "void":
        """
        SetConstantVelocityFieldInterpolator(itkConstantVelocityFieldTransformD2 self, itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,2 >,2 >,double > * arg0)

        Get/Set the interpolator. Create out own set accessor that assigns
        the velocity field 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetConstantVelocityFieldInterpolator(self, arg0)


    def GetModifiableConstantVelocityFieldInterpolator(self) -> "itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,2 >,2 >,double > *":
        """GetModifiableConstantVelocityFieldInterpolator(itkConstantVelocityFieldTransformD2 self) -> itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,2 >,2 >,double > *"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetModifiableConstantVelocityFieldInterpolator(self)


    def GetConstantVelocityFieldInterpolator(self, *args) -> "itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,2 >,2 >,double > *":
        """
        GetConstantVelocityFieldInterpolator(itkConstantVelocityFieldTransformD2 self) -> itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,2 >,2 >,double > const
        GetConstantVelocityFieldInterpolator(itkConstantVelocityFieldTransformD2 self) -> itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,2 >,2 >,double > *
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetConstantVelocityFieldInterpolator(self, *args)


    def GetConstantVelocityFieldSetTime(self) -> "unsigned long const &":
        """
        GetConstantVelocityFieldSetTime(itkConstantVelocityFieldTransformD2 self) -> unsigned long const &

        Get
        the modification time of velocity field 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetConstantVelocityFieldSetTime(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkConstantVelocityFieldTransformD2 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkConstantVelocityFieldTransformD2 self, itkArrayD update)

        Update
        the transform's parameters by the values in update.

        Parameters:
        -----------

        update:  must be of the same length as returned by
        GetNumberOfParameters(). Throw an exception otherwise.

        factor:  is a scalar multiplier for each value in update.
        SetParameters is called at the end of this method, to allow the
        transform to perform any required operations on the updated parameters
        - typically a conversion to member variables for use in
        TransformPoint. 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_UpdateTransformParameters(self, update, factor)


    def GetInverse(self, inverse: 'itkConstantVelocityFieldTransformD2') -> "bool":
        """
        GetInverse(itkConstantVelocityFieldTransformD2 self, itkConstantVelocityFieldTransformD2 inverse) -> bool

        Return an inverse of
        this transform. 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetInverse(self, inverse)


    def IntegrateVelocityField(self) -> "void":
        """
        IntegrateVelocityField(itkConstantVelocityFieldTransformD2 self)

        Trigger the
        computation of the displacement field by integrating the constant
        velocity field. 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_IntegrateVelocityField(self)


    def SetCalculateNumberOfIntegrationStepsAutomatically(self, _arg: 'bool const') -> "void":
        """SetCalculateNumberOfIntegrationStepsAutomatically(itkConstantVelocityFieldTransformD2 self, bool const _arg)"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetCalculateNumberOfIntegrationStepsAutomatically(self, _arg)


    def GetCalculateNumberOfIntegrationStepsAutomatically(self) -> "bool":
        """GetCalculateNumberOfIntegrationStepsAutomatically(itkConstantVelocityFieldTransformD2 self) -> bool"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetCalculateNumberOfIntegrationStepsAutomatically(self)


    def CalculateNumberOfIntegrationStepsAutomaticallyOn(self) -> "void":
        """CalculateNumberOfIntegrationStepsAutomaticallyOn(itkConstantVelocityFieldTransformD2 self)"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_CalculateNumberOfIntegrationStepsAutomaticallyOn(self)


    def CalculateNumberOfIntegrationStepsAutomaticallyOff(self) -> "void":
        """CalculateNumberOfIntegrationStepsAutomaticallyOff(itkConstantVelocityFieldTransformD2 self)"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_CalculateNumberOfIntegrationStepsAutomaticallyOff(self)


    def SetLowerTimeBound(self, _arg: 'double') -> "void":
        """
        SetLowerTimeBound(itkConstantVelocityFieldTransformD2 self, double _arg)

        Set the lower
        time bound defining the integration domain of the transform. We assume
        that the total possible time domain is [0,1] 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetLowerTimeBound(self, _arg)


    def GetLowerTimeBound(self) -> "double":
        """
        GetLowerTimeBound(itkConstantVelocityFieldTransformD2 self) -> double

        Get the lower
        time bound defining the integration domain of the transform. We assume
        that the total possible time domain is [0,1] 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetLowerTimeBound(self)


    def SetUpperTimeBound(self, _arg: 'double') -> "void":
        """
        SetUpperTimeBound(itkConstantVelocityFieldTransformD2 self, double _arg)

        Set the upper
        time bound defining the integration domain of the transform. We assume
        that the total possible time domain is [0,1] 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetUpperTimeBound(self, _arg)


    def GetUpperTimeBound(self) -> "double":
        """
        GetUpperTimeBound(itkConstantVelocityFieldTransformD2 self) -> double

        Get the upper
        time bound defining the integration domain of the transform. We assume
        that the total possible time domain is [0,1] 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetUpperTimeBound(self)


    def SetNumberOfIntegrationSteps(self, _arg: 'unsigned int const') -> "void":
        """
        SetNumberOfIntegrationSteps(itkConstantVelocityFieldTransformD2 self, unsigned int const _arg)

        Set the
        number of integration steps. Default = 100; 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetNumberOfIntegrationSteps(self, _arg)


    def GetNumberOfIntegrationSteps(self) -> "unsigned int":
        """
        GetNumberOfIntegrationSteps(itkConstantVelocityFieldTransformD2 self) -> unsigned int

        Get the
        number of integration steps. Default = 100; 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetNumberOfIntegrationSteps(self)

    __swig_destroy__ = _itkConstantVelocityFieldTransformPython.delete_itkConstantVelocityFieldTransformD2

    def cast(obj: 'itkLightObject') -> "itkConstantVelocityFieldTransformD2 *":
        """cast(itkLightObject obj) -> itkConstantVelocityFieldTransformD2"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_cast(obj)

    cast = staticmethod(cast)

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

itkConstantVelocityFieldTransformD2.Clone = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_Clone, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.SetConstantVelocityField = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetConstantVelocityField, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.GetModifiableConstantVelocityField = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetModifiableConstantVelocityField, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.GetConstantVelocityField = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetConstantVelocityField, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.SetConstantVelocityFieldInterpolator = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetConstantVelocityFieldInterpolator, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.GetModifiableConstantVelocityFieldInterpolator = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetModifiableConstantVelocityFieldInterpolator, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.GetConstantVelocityFieldInterpolator = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetConstantVelocityFieldInterpolator, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.GetConstantVelocityFieldSetTime = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetConstantVelocityFieldSetTime, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.UpdateTransformParameters = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_UpdateTransformParameters, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.GetInverse = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetInverse, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.IntegrateVelocityField = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_IntegrateVelocityField, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.SetCalculateNumberOfIntegrationStepsAutomatically = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetCalculateNumberOfIntegrationStepsAutomatically, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.GetCalculateNumberOfIntegrationStepsAutomatically = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetCalculateNumberOfIntegrationStepsAutomatically, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.CalculateNumberOfIntegrationStepsAutomaticallyOn = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_CalculateNumberOfIntegrationStepsAutomaticallyOn, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.CalculateNumberOfIntegrationStepsAutomaticallyOff = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_CalculateNumberOfIntegrationStepsAutomaticallyOff, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.SetLowerTimeBound = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetLowerTimeBound, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.GetLowerTimeBound = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetLowerTimeBound, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.SetUpperTimeBound = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetUpperTimeBound, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.GetUpperTimeBound = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetUpperTimeBound, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.SetNumberOfIntegrationSteps = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_SetNumberOfIntegrationSteps, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2.GetNumberOfIntegrationSteps = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_GetNumberOfIntegrationSteps, None, itkConstantVelocityFieldTransformD2)
itkConstantVelocityFieldTransformD2_swigregister = _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_swigregister
itkConstantVelocityFieldTransformD2_swigregister(itkConstantVelocityFieldTransformD2)

def itkConstantVelocityFieldTransformD2___New_orig__() -> "itkConstantVelocityFieldTransformD2_Pointer":
    """itkConstantVelocityFieldTransformD2___New_orig__() -> itkConstantVelocityFieldTransformD2_Pointer"""
    return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2___New_orig__()

def itkConstantVelocityFieldTransformD2_cast(obj: 'itkLightObject') -> "itkConstantVelocityFieldTransformD2 *":
    """itkConstantVelocityFieldTransformD2_cast(itkLightObject obj) -> itkConstantVelocityFieldTransformD2"""
    return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2_cast(obj)

class itkConstantVelocityFieldTransformD3(itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3):
    """


    Provides local/dense/high-dimensionality transformation via a a
    constant velocity field.

    Nick Tustison

    Brian Avants

    C++ includes: itkConstantVelocityFieldTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkConstantVelocityFieldTransformD3_Pointer":
        """__New_orig__() -> itkConstantVelocityFieldTransformD3_Pointer"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkConstantVelocityFieldTransformD3_Pointer":
        """Clone(itkConstantVelocityFieldTransformD3 self) -> itkConstantVelocityFieldTransformD3_Pointer"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_Clone(self)


    def SetConstantVelocityField(self, arg0: 'itkImageVD33') -> "void":
        """
        SetConstantVelocityField(itkConstantVelocityFieldTransformD3 self, itkImageVD33 arg0)

        Get/Set
        the velocity field. Set the displacement field. Create special set
        accessor to update interpolator and assign displacement field to
        transform parameters container. 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetConstantVelocityField(self, arg0)


    def GetModifiableConstantVelocityField(self) -> "itkImageVD33 *":
        """GetModifiableConstantVelocityField(itkConstantVelocityFieldTransformD3 self) -> itkImageVD33"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetModifiableConstantVelocityField(self)


    def GetConstantVelocityField(self, *args) -> "itkImageVD33 *":
        """
        GetConstantVelocityField(itkConstantVelocityFieldTransformD3 self) -> itkImageVD33
        GetConstantVelocityField(itkConstantVelocityFieldTransformD3 self) -> itkImageVD33
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetConstantVelocityField(self, *args)


    def SetConstantVelocityFieldInterpolator(self, arg0: 'itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,3 >,3 >,double > *') -> "void":
        """
        SetConstantVelocityFieldInterpolator(itkConstantVelocityFieldTransformD3 self, itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,3 >,3 >,double > * arg0)

        Get/Set the interpolator. Create out own set accessor that assigns
        the velocity field 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetConstantVelocityFieldInterpolator(self, arg0)


    def GetModifiableConstantVelocityFieldInterpolator(self) -> "itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,3 >,3 >,double > *":
        """GetModifiableConstantVelocityFieldInterpolator(itkConstantVelocityFieldTransformD3 self) -> itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,3 >,3 >,double > *"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetModifiableConstantVelocityFieldInterpolator(self)


    def GetConstantVelocityFieldInterpolator(self, *args) -> "itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,3 >,3 >,double > *":
        """
        GetConstantVelocityFieldInterpolator(itkConstantVelocityFieldTransformD3 self) -> itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,3 >,3 >,double > const
        GetConstantVelocityFieldInterpolator(itkConstantVelocityFieldTransformD3 self) -> itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,3 >,3 >,double > *
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetConstantVelocityFieldInterpolator(self, *args)


    def GetConstantVelocityFieldSetTime(self) -> "unsigned long const &":
        """
        GetConstantVelocityFieldSetTime(itkConstantVelocityFieldTransformD3 self) -> unsigned long const &

        Get
        the modification time of velocity field 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetConstantVelocityFieldSetTime(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkConstantVelocityFieldTransformD3 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkConstantVelocityFieldTransformD3 self, itkArrayD update)

        Update
        the transform's parameters by the values in update.

        Parameters:
        -----------

        update:  must be of the same length as returned by
        GetNumberOfParameters(). Throw an exception otherwise.

        factor:  is a scalar multiplier for each value in update.
        SetParameters is called at the end of this method, to allow the
        transform to perform any required operations on the updated parameters
        - typically a conversion to member variables for use in
        TransformPoint. 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_UpdateTransformParameters(self, update, factor)


    def GetInverse(self, inverse: 'itkConstantVelocityFieldTransformD3') -> "bool":
        """
        GetInverse(itkConstantVelocityFieldTransformD3 self, itkConstantVelocityFieldTransformD3 inverse) -> bool

        Return an inverse of
        this transform. 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetInverse(self, inverse)


    def IntegrateVelocityField(self) -> "void":
        """
        IntegrateVelocityField(itkConstantVelocityFieldTransformD3 self)

        Trigger the
        computation of the displacement field by integrating the constant
        velocity field. 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_IntegrateVelocityField(self)


    def SetCalculateNumberOfIntegrationStepsAutomatically(self, _arg: 'bool const') -> "void":
        """SetCalculateNumberOfIntegrationStepsAutomatically(itkConstantVelocityFieldTransformD3 self, bool const _arg)"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetCalculateNumberOfIntegrationStepsAutomatically(self, _arg)


    def GetCalculateNumberOfIntegrationStepsAutomatically(self) -> "bool":
        """GetCalculateNumberOfIntegrationStepsAutomatically(itkConstantVelocityFieldTransformD3 self) -> bool"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetCalculateNumberOfIntegrationStepsAutomatically(self)


    def CalculateNumberOfIntegrationStepsAutomaticallyOn(self) -> "void":
        """CalculateNumberOfIntegrationStepsAutomaticallyOn(itkConstantVelocityFieldTransformD3 self)"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_CalculateNumberOfIntegrationStepsAutomaticallyOn(self)


    def CalculateNumberOfIntegrationStepsAutomaticallyOff(self) -> "void":
        """CalculateNumberOfIntegrationStepsAutomaticallyOff(itkConstantVelocityFieldTransformD3 self)"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_CalculateNumberOfIntegrationStepsAutomaticallyOff(self)


    def SetLowerTimeBound(self, _arg: 'double') -> "void":
        """
        SetLowerTimeBound(itkConstantVelocityFieldTransformD3 self, double _arg)

        Set the lower
        time bound defining the integration domain of the transform. We assume
        that the total possible time domain is [0,1] 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetLowerTimeBound(self, _arg)


    def GetLowerTimeBound(self) -> "double":
        """
        GetLowerTimeBound(itkConstantVelocityFieldTransformD3 self) -> double

        Get the lower
        time bound defining the integration domain of the transform. We assume
        that the total possible time domain is [0,1] 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetLowerTimeBound(self)


    def SetUpperTimeBound(self, _arg: 'double') -> "void":
        """
        SetUpperTimeBound(itkConstantVelocityFieldTransformD3 self, double _arg)

        Set the upper
        time bound defining the integration domain of the transform. We assume
        that the total possible time domain is [0,1] 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetUpperTimeBound(self, _arg)


    def GetUpperTimeBound(self) -> "double":
        """
        GetUpperTimeBound(itkConstantVelocityFieldTransformD3 self) -> double

        Get the upper
        time bound defining the integration domain of the transform. We assume
        that the total possible time domain is [0,1] 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetUpperTimeBound(self)


    def SetNumberOfIntegrationSteps(self, _arg: 'unsigned int const') -> "void":
        """
        SetNumberOfIntegrationSteps(itkConstantVelocityFieldTransformD3 self, unsigned int const _arg)

        Set the
        number of integration steps. Default = 100; 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetNumberOfIntegrationSteps(self, _arg)


    def GetNumberOfIntegrationSteps(self) -> "unsigned int":
        """
        GetNumberOfIntegrationSteps(itkConstantVelocityFieldTransformD3 self) -> unsigned int

        Get the
        number of integration steps. Default = 100; 
        """
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetNumberOfIntegrationSteps(self)

    __swig_destroy__ = _itkConstantVelocityFieldTransformPython.delete_itkConstantVelocityFieldTransformD3

    def cast(obj: 'itkLightObject') -> "itkConstantVelocityFieldTransformD3 *":
        """cast(itkLightObject obj) -> itkConstantVelocityFieldTransformD3"""
        return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_cast(obj)

    cast = staticmethod(cast)

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

itkConstantVelocityFieldTransformD3.Clone = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_Clone, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.SetConstantVelocityField = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetConstantVelocityField, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.GetModifiableConstantVelocityField = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetModifiableConstantVelocityField, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.GetConstantVelocityField = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetConstantVelocityField, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.SetConstantVelocityFieldInterpolator = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetConstantVelocityFieldInterpolator, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.GetModifiableConstantVelocityFieldInterpolator = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetModifiableConstantVelocityFieldInterpolator, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.GetConstantVelocityFieldInterpolator = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetConstantVelocityFieldInterpolator, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.GetConstantVelocityFieldSetTime = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetConstantVelocityFieldSetTime, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.UpdateTransformParameters = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_UpdateTransformParameters, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.GetInverse = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetInverse, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.IntegrateVelocityField = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_IntegrateVelocityField, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.SetCalculateNumberOfIntegrationStepsAutomatically = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetCalculateNumberOfIntegrationStepsAutomatically, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.GetCalculateNumberOfIntegrationStepsAutomatically = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetCalculateNumberOfIntegrationStepsAutomatically, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.CalculateNumberOfIntegrationStepsAutomaticallyOn = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_CalculateNumberOfIntegrationStepsAutomaticallyOn, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.CalculateNumberOfIntegrationStepsAutomaticallyOff = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_CalculateNumberOfIntegrationStepsAutomaticallyOff, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.SetLowerTimeBound = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetLowerTimeBound, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.GetLowerTimeBound = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetLowerTimeBound, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.SetUpperTimeBound = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetUpperTimeBound, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.GetUpperTimeBound = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetUpperTimeBound, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.SetNumberOfIntegrationSteps = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_SetNumberOfIntegrationSteps, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3.GetNumberOfIntegrationSteps = new_instancemethod(_itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_GetNumberOfIntegrationSteps, None, itkConstantVelocityFieldTransformD3)
itkConstantVelocityFieldTransformD3_swigregister = _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_swigregister
itkConstantVelocityFieldTransformD3_swigregister(itkConstantVelocityFieldTransformD3)

def itkConstantVelocityFieldTransformD3___New_orig__() -> "itkConstantVelocityFieldTransformD3_Pointer":
    """itkConstantVelocityFieldTransformD3___New_orig__() -> itkConstantVelocityFieldTransformD3_Pointer"""
    return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3___New_orig__()

def itkConstantVelocityFieldTransformD3_cast(obj: 'itkLightObject') -> "itkConstantVelocityFieldTransformD3 *":
    """itkConstantVelocityFieldTransformD3_cast(itkLightObject obj) -> itkConstantVelocityFieldTransformD3"""
    return _itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3_cast(obj)



