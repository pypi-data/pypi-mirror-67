# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkVelocityFieldTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkVelocityFieldTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkVelocityFieldTransformPython
            return _itkVelocityFieldTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkVelocityFieldTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkVelocityFieldTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkVelocityFieldTransformPython
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


import itkDisplacementFieldTransformPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import vnl_vector_refPython
import itkFixedArrayPython
import ITKCommonBasePython
import itkPointPython
import itkOptimizerParametersPython
import itkArrayPython
import itkImagePython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkArray2DPython
import itkDiffusionTensor3DPython
import itkTransformBasePython

def itkVelocityFieldTransformD3_New():
  return itkVelocityFieldTransformD3.New()


def itkVelocityFieldTransformD2_New():
  return itkVelocityFieldTransformD2.New()

class itkVelocityFieldTransformD2(itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2):
    """


    Provides local/dense/high-dimensionality transformation via a a
    velocity field.

    Nick Tustison

    Brian Avants

    C++ includes: itkVelocityFieldTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVelocityFieldTransformD2_Pointer":
        """__New_orig__() -> itkVelocityFieldTransformD2_Pointer"""
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVelocityFieldTransformD2_Pointer":
        """Clone(itkVelocityFieldTransformD2 self) -> itkVelocityFieldTransformD2_Pointer"""
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_Clone(self)


    def SetVelocityField(self, arg0: 'itkImageVD23') -> "void":
        """
        SetVelocityField(itkVelocityFieldTransformD2 self, itkImageVD23 arg0)

        Get/Set the
        velocity field. Set the displacement field. Create special set
        accessor to update interpolator and assign displacement field to
        transform parameters container. 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_SetVelocityField(self, arg0)


    def GetModifiableVelocityField(self) -> "itkImageVD23 *":
        """GetModifiableVelocityField(itkVelocityFieldTransformD2 self) -> itkImageVD23"""
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetModifiableVelocityField(self)


    def GetVelocityField(self, *args) -> "itkImageVD23 *":
        """
        GetVelocityField(itkVelocityFieldTransformD2 self) -> itkImageVD23
        GetVelocityField(itkVelocityFieldTransformD2 self) -> itkImageVD23
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetVelocityField(self, *args)


    def SetVelocityFieldInterpolator(self, arg0: 'itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,2 >,3 >,double > *') -> "void":
        """
        SetVelocityFieldInterpolator(itkVelocityFieldTransformD2 self, itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,2 >,3 >,double > * arg0)

        Get/Set the interpolator. Create out own set accessor that assigns the
        velocity field 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_SetVelocityFieldInterpolator(self, arg0)


    def GetModifiableVelocityFieldInterpolator(self) -> "itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,2 >,3 >,double > *":
        """GetModifiableVelocityFieldInterpolator(itkVelocityFieldTransformD2 self) -> itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,2 >,3 >,double > *"""
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetModifiableVelocityFieldInterpolator(self)


    def GetVelocityFieldInterpolator(self, *args) -> "itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,2 >,3 >,double > *":
        """
        GetVelocityFieldInterpolator(itkVelocityFieldTransformD2 self) -> itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,2 >,3 >,double > const
        GetVelocityFieldInterpolator(itkVelocityFieldTransformD2 self) -> itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,2 >,3 >,double > *
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetVelocityFieldInterpolator(self, *args)


    def GetVelocityFieldSetTime(self) -> "unsigned long const &":
        """
        GetVelocityFieldSetTime(itkVelocityFieldTransformD2 self) -> unsigned long const &

        Get the
        modification time of velocity field 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetVelocityFieldSetTime(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkVelocityFieldTransformD2 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkVelocityFieldTransformD2 self, itkArrayD update)

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
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_UpdateTransformParameters(self, update, factor)


    def GetInverse(self, inverse: 'itkVelocityFieldTransformD2') -> "bool":
        """
        GetInverse(itkVelocityFieldTransformD2 self, itkVelocityFieldTransformD2 inverse) -> bool

        Return an inverse of
        this transform. 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetInverse(self, inverse)


    def IntegrateVelocityField(self) -> "void":
        """
        IntegrateVelocityField(itkVelocityFieldTransformD2 self)

        Trigger the
        computation of the displacement field by integrating the velocity
        field. 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_IntegrateVelocityField(self)


    def SetLowerTimeBound(self, _arg: 'double') -> "void":
        """
        SetLowerTimeBound(itkVelocityFieldTransformD2 self, double _arg)

        Set the lower
        time bound defining the integration domain of the transform. We assume
        that the total possible time domain is [0,1] 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_SetLowerTimeBound(self, _arg)


    def GetLowerTimeBound(self) -> "double":
        """
        GetLowerTimeBound(itkVelocityFieldTransformD2 self) -> double

        Get the lower
        time bound defining the integration domain of the transform. We assume
        that the total possible time domain is [0,1] 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetLowerTimeBound(self)


    def SetUpperTimeBound(self, _arg: 'double') -> "void":
        """
        SetUpperTimeBound(itkVelocityFieldTransformD2 self, double _arg)

        Set the upper
        time bound defining the integration domain of the transform. We assume
        that the total possible time domain is [0,1] 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_SetUpperTimeBound(self, _arg)


    def GetUpperTimeBound(self) -> "double":
        """
        GetUpperTimeBound(itkVelocityFieldTransformD2 self) -> double

        Get the upper
        time bound defining the integration domain of the transform. We assume
        that the total possible time domain is [0,1] 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetUpperTimeBound(self)


    def SetNumberOfIntegrationSteps(self, _arg: 'unsigned int const') -> "void":
        """
        SetNumberOfIntegrationSteps(itkVelocityFieldTransformD2 self, unsigned int const _arg)

        Set the
        number of integration steps. Default = 100; 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_SetNumberOfIntegrationSteps(self, _arg)


    def GetNumberOfIntegrationSteps(self) -> "unsigned int":
        """
        GetNumberOfIntegrationSteps(itkVelocityFieldTransformD2 self) -> unsigned int

        Get the
        number of integration steps. Default = 100; 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetNumberOfIntegrationSteps(self)

    __swig_destroy__ = _itkVelocityFieldTransformPython.delete_itkVelocityFieldTransformD2

    def cast(obj: 'itkLightObject') -> "itkVelocityFieldTransformD2 *":
        """cast(itkLightObject obj) -> itkVelocityFieldTransformD2"""
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkVelocityFieldTransformD2

        Create a new object of the class itkVelocityFieldTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVelocityFieldTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVelocityFieldTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVelocityFieldTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVelocityFieldTransformD2.Clone = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_Clone, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2.SetVelocityField = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_SetVelocityField, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2.GetModifiableVelocityField = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetModifiableVelocityField, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2.GetVelocityField = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetVelocityField, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2.SetVelocityFieldInterpolator = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_SetVelocityFieldInterpolator, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2.GetModifiableVelocityFieldInterpolator = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetModifiableVelocityFieldInterpolator, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2.GetVelocityFieldInterpolator = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetVelocityFieldInterpolator, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2.GetVelocityFieldSetTime = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetVelocityFieldSetTime, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2.UpdateTransformParameters = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_UpdateTransformParameters, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2.GetInverse = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetInverse, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2.IntegrateVelocityField = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_IntegrateVelocityField, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2.SetLowerTimeBound = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_SetLowerTimeBound, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2.GetLowerTimeBound = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetLowerTimeBound, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2.SetUpperTimeBound = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_SetUpperTimeBound, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2.GetUpperTimeBound = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetUpperTimeBound, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2.SetNumberOfIntegrationSteps = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_SetNumberOfIntegrationSteps, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2.GetNumberOfIntegrationSteps = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_GetNumberOfIntegrationSteps, None, itkVelocityFieldTransformD2)
itkVelocityFieldTransformD2_swigregister = _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_swigregister
itkVelocityFieldTransformD2_swigregister(itkVelocityFieldTransformD2)

def itkVelocityFieldTransformD2___New_orig__() -> "itkVelocityFieldTransformD2_Pointer":
    """itkVelocityFieldTransformD2___New_orig__() -> itkVelocityFieldTransformD2_Pointer"""
    return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2___New_orig__()

def itkVelocityFieldTransformD2_cast(obj: 'itkLightObject') -> "itkVelocityFieldTransformD2 *":
    """itkVelocityFieldTransformD2_cast(itkLightObject obj) -> itkVelocityFieldTransformD2"""
    return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD2_cast(obj)

class itkVelocityFieldTransformD3(itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3):
    """


    Provides local/dense/high-dimensionality transformation via a a
    velocity field.

    Nick Tustison

    Brian Avants

    C++ includes: itkVelocityFieldTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVelocityFieldTransformD3_Pointer":
        """__New_orig__() -> itkVelocityFieldTransformD3_Pointer"""
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVelocityFieldTransformD3_Pointer":
        """Clone(itkVelocityFieldTransformD3 self) -> itkVelocityFieldTransformD3_Pointer"""
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_Clone(self)


    def SetVelocityField(self, arg0: 'itkImageVD34') -> "void":
        """
        SetVelocityField(itkVelocityFieldTransformD3 self, itkImageVD34 arg0)

        Get/Set the
        velocity field. Set the displacement field. Create special set
        accessor to update interpolator and assign displacement field to
        transform parameters container. 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_SetVelocityField(self, arg0)


    def GetModifiableVelocityField(self) -> "itkImageVD34 *":
        """GetModifiableVelocityField(itkVelocityFieldTransformD3 self) -> itkImageVD34"""
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetModifiableVelocityField(self)


    def GetVelocityField(self, *args) -> "itkImageVD34 *":
        """
        GetVelocityField(itkVelocityFieldTransformD3 self) -> itkImageVD34
        GetVelocityField(itkVelocityFieldTransformD3 self) -> itkImageVD34
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetVelocityField(self, *args)


    def SetVelocityFieldInterpolator(self, arg0: 'itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,3 >,4 >,double > *') -> "void":
        """
        SetVelocityFieldInterpolator(itkVelocityFieldTransformD3 self, itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,3 >,4 >,double > * arg0)

        Get/Set the interpolator. Create out own set accessor that assigns the
        velocity field 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_SetVelocityFieldInterpolator(self, arg0)


    def GetModifiableVelocityFieldInterpolator(self) -> "itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,3 >,4 >,double > *":
        """GetModifiableVelocityFieldInterpolator(itkVelocityFieldTransformD3 self) -> itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,3 >,4 >,double > *"""
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetModifiableVelocityFieldInterpolator(self)


    def GetVelocityFieldInterpolator(self, *args) -> "itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,3 >,4 >,double > *":
        """
        GetVelocityFieldInterpolator(itkVelocityFieldTransformD3 self) -> itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,3 >,4 >,double > const
        GetVelocityFieldInterpolator(itkVelocityFieldTransformD3 self) -> itk::VectorInterpolateImageFunction< itk::Image< itk::Vector< double,3 >,4 >,double > *
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetVelocityFieldInterpolator(self, *args)


    def GetVelocityFieldSetTime(self) -> "unsigned long const &":
        """
        GetVelocityFieldSetTime(itkVelocityFieldTransformD3 self) -> unsigned long const &

        Get the
        modification time of velocity field 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetVelocityFieldSetTime(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkVelocityFieldTransformD3 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkVelocityFieldTransformD3 self, itkArrayD update)

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
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_UpdateTransformParameters(self, update, factor)


    def GetInverse(self, inverse: 'itkVelocityFieldTransformD3') -> "bool":
        """
        GetInverse(itkVelocityFieldTransformD3 self, itkVelocityFieldTransformD3 inverse) -> bool

        Return an inverse of
        this transform. 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetInverse(self, inverse)


    def IntegrateVelocityField(self) -> "void":
        """
        IntegrateVelocityField(itkVelocityFieldTransformD3 self)

        Trigger the
        computation of the displacement field by integrating the velocity
        field. 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_IntegrateVelocityField(self)


    def SetLowerTimeBound(self, _arg: 'double') -> "void":
        """
        SetLowerTimeBound(itkVelocityFieldTransformD3 self, double _arg)

        Set the lower
        time bound defining the integration domain of the transform. We assume
        that the total possible time domain is [0,1] 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_SetLowerTimeBound(self, _arg)


    def GetLowerTimeBound(self) -> "double":
        """
        GetLowerTimeBound(itkVelocityFieldTransformD3 self) -> double

        Get the lower
        time bound defining the integration domain of the transform. We assume
        that the total possible time domain is [0,1] 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetLowerTimeBound(self)


    def SetUpperTimeBound(self, _arg: 'double') -> "void":
        """
        SetUpperTimeBound(itkVelocityFieldTransformD3 self, double _arg)

        Set the upper
        time bound defining the integration domain of the transform. We assume
        that the total possible time domain is [0,1] 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_SetUpperTimeBound(self, _arg)


    def GetUpperTimeBound(self) -> "double":
        """
        GetUpperTimeBound(itkVelocityFieldTransformD3 self) -> double

        Get the upper
        time bound defining the integration domain of the transform. We assume
        that the total possible time domain is [0,1] 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetUpperTimeBound(self)


    def SetNumberOfIntegrationSteps(self, _arg: 'unsigned int const') -> "void":
        """
        SetNumberOfIntegrationSteps(itkVelocityFieldTransformD3 self, unsigned int const _arg)

        Set the
        number of integration steps. Default = 100; 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_SetNumberOfIntegrationSteps(self, _arg)


    def GetNumberOfIntegrationSteps(self) -> "unsigned int":
        """
        GetNumberOfIntegrationSteps(itkVelocityFieldTransformD3 self) -> unsigned int

        Get the
        number of integration steps. Default = 100; 
        """
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetNumberOfIntegrationSteps(self)

    __swig_destroy__ = _itkVelocityFieldTransformPython.delete_itkVelocityFieldTransformD3

    def cast(obj: 'itkLightObject') -> "itkVelocityFieldTransformD3 *":
        """cast(itkLightObject obj) -> itkVelocityFieldTransformD3"""
        return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkVelocityFieldTransformD3

        Create a new object of the class itkVelocityFieldTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVelocityFieldTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVelocityFieldTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVelocityFieldTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVelocityFieldTransformD3.Clone = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_Clone, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3.SetVelocityField = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_SetVelocityField, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3.GetModifiableVelocityField = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetModifiableVelocityField, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3.GetVelocityField = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetVelocityField, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3.SetVelocityFieldInterpolator = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_SetVelocityFieldInterpolator, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3.GetModifiableVelocityFieldInterpolator = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetModifiableVelocityFieldInterpolator, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3.GetVelocityFieldInterpolator = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetVelocityFieldInterpolator, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3.GetVelocityFieldSetTime = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetVelocityFieldSetTime, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3.UpdateTransformParameters = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_UpdateTransformParameters, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3.GetInverse = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetInverse, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3.IntegrateVelocityField = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_IntegrateVelocityField, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3.SetLowerTimeBound = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_SetLowerTimeBound, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3.GetLowerTimeBound = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetLowerTimeBound, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3.SetUpperTimeBound = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_SetUpperTimeBound, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3.GetUpperTimeBound = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetUpperTimeBound, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3.SetNumberOfIntegrationSteps = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_SetNumberOfIntegrationSteps, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3.GetNumberOfIntegrationSteps = new_instancemethod(_itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_GetNumberOfIntegrationSteps, None, itkVelocityFieldTransformD3)
itkVelocityFieldTransformD3_swigregister = _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_swigregister
itkVelocityFieldTransformD3_swigregister(itkVelocityFieldTransformD3)

def itkVelocityFieldTransformD3___New_orig__() -> "itkVelocityFieldTransformD3_Pointer":
    """itkVelocityFieldTransformD3___New_orig__() -> itkVelocityFieldTransformD3_Pointer"""
    return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3___New_orig__()

def itkVelocityFieldTransformD3_cast(obj: 'itkLightObject') -> "itkVelocityFieldTransformD3 *":
    """itkVelocityFieldTransformD3_cast(itkLightObject obj) -> itkVelocityFieldTransformD3"""
    return _itkVelocityFieldTransformPython.itkVelocityFieldTransformD3_cast(obj)



