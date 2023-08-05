# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkComplexToModulusImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkComplexToModulusImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkComplexToModulusImageFilterPython
            return _itkComplexToModulusImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkComplexToModulusImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkComplexToModulusImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkComplexToModulusImageFilterPython
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


import itkUnaryGeneratorImageFilterPython
import itkInPlaceImageFilterBPython
import itkImageToImageFilterBPython
import itkImagePython
import ITKCommonBasePython
import pyBasePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkSizePython
import itkOffsetPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkCovariantVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkIndexPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython

def itkComplexToModulusImageFilterICF3IF3_New():
  return itkComplexToModulusImageFilterICF3IF3.New()


def itkComplexToModulusImageFilterICF2IF2_New():
  return itkComplexToModulusImageFilterICF2IF2.New()

class itkComplexToModulusImageFilterICF2IF2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterICF2IF2):
    """


    Computes pixel-wise the Modulus of a complex image.

    C++ includes: itkComplexToModulusImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkComplexToModulusImageFilterICF2IF2_Pointer":
        """__New_orig__() -> itkComplexToModulusImageFilterICF2IF2_Pointer"""
        return _itkComplexToModulusImageFilterPython.itkComplexToModulusImageFilterICF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkComplexToModulusImageFilterICF2IF2_Pointer":
        """Clone(itkComplexToModulusImageFilterICF2IF2 self) -> itkComplexToModulusImageFilterICF2IF2_Pointer"""
        return _itkComplexToModulusImageFilterPython.itkComplexToModulusImageFilterICF2IF2_Clone(self)

    InputMultiplyOperatorCheck = _itkComplexToModulusImageFilterPython.itkComplexToModulusImageFilterICF2IF2_InputMultiplyOperatorCheck
    __swig_destroy__ = _itkComplexToModulusImageFilterPython.delete_itkComplexToModulusImageFilterICF2IF2

    def cast(obj: 'itkLightObject') -> "itkComplexToModulusImageFilterICF2IF2 *":
        """cast(itkLightObject obj) -> itkComplexToModulusImageFilterICF2IF2"""
        return _itkComplexToModulusImageFilterPython.itkComplexToModulusImageFilterICF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkComplexToModulusImageFilterICF2IF2

        Create a new object of the class itkComplexToModulusImageFilterICF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToModulusImageFilterICF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkComplexToModulusImageFilterICF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkComplexToModulusImageFilterICF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkComplexToModulusImageFilterICF2IF2.Clone = new_instancemethod(_itkComplexToModulusImageFilterPython.itkComplexToModulusImageFilterICF2IF2_Clone, None, itkComplexToModulusImageFilterICF2IF2)
itkComplexToModulusImageFilterICF2IF2_swigregister = _itkComplexToModulusImageFilterPython.itkComplexToModulusImageFilterICF2IF2_swigregister
itkComplexToModulusImageFilterICF2IF2_swigregister(itkComplexToModulusImageFilterICF2IF2)

def itkComplexToModulusImageFilterICF2IF2___New_orig__() -> "itkComplexToModulusImageFilterICF2IF2_Pointer":
    """itkComplexToModulusImageFilterICF2IF2___New_orig__() -> itkComplexToModulusImageFilterICF2IF2_Pointer"""
    return _itkComplexToModulusImageFilterPython.itkComplexToModulusImageFilterICF2IF2___New_orig__()

def itkComplexToModulusImageFilterICF2IF2_cast(obj: 'itkLightObject') -> "itkComplexToModulusImageFilterICF2IF2 *":
    """itkComplexToModulusImageFilterICF2IF2_cast(itkLightObject obj) -> itkComplexToModulusImageFilterICF2IF2"""
    return _itkComplexToModulusImageFilterPython.itkComplexToModulusImageFilterICF2IF2_cast(obj)

class itkComplexToModulusImageFilterICF3IF3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterICF3IF3):
    """


    Computes pixel-wise the Modulus of a complex image.

    C++ includes: itkComplexToModulusImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkComplexToModulusImageFilterICF3IF3_Pointer":
        """__New_orig__() -> itkComplexToModulusImageFilterICF3IF3_Pointer"""
        return _itkComplexToModulusImageFilterPython.itkComplexToModulusImageFilterICF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkComplexToModulusImageFilterICF3IF3_Pointer":
        """Clone(itkComplexToModulusImageFilterICF3IF3 self) -> itkComplexToModulusImageFilterICF3IF3_Pointer"""
        return _itkComplexToModulusImageFilterPython.itkComplexToModulusImageFilterICF3IF3_Clone(self)

    InputMultiplyOperatorCheck = _itkComplexToModulusImageFilterPython.itkComplexToModulusImageFilterICF3IF3_InputMultiplyOperatorCheck
    __swig_destroy__ = _itkComplexToModulusImageFilterPython.delete_itkComplexToModulusImageFilterICF3IF3

    def cast(obj: 'itkLightObject') -> "itkComplexToModulusImageFilterICF3IF3 *":
        """cast(itkLightObject obj) -> itkComplexToModulusImageFilterICF3IF3"""
        return _itkComplexToModulusImageFilterPython.itkComplexToModulusImageFilterICF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkComplexToModulusImageFilterICF3IF3

        Create a new object of the class itkComplexToModulusImageFilterICF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToModulusImageFilterICF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkComplexToModulusImageFilterICF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkComplexToModulusImageFilterICF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkComplexToModulusImageFilterICF3IF3.Clone = new_instancemethod(_itkComplexToModulusImageFilterPython.itkComplexToModulusImageFilterICF3IF3_Clone, None, itkComplexToModulusImageFilterICF3IF3)
itkComplexToModulusImageFilterICF3IF3_swigregister = _itkComplexToModulusImageFilterPython.itkComplexToModulusImageFilterICF3IF3_swigregister
itkComplexToModulusImageFilterICF3IF3_swigregister(itkComplexToModulusImageFilterICF3IF3)

def itkComplexToModulusImageFilterICF3IF3___New_orig__() -> "itkComplexToModulusImageFilterICF3IF3_Pointer":
    """itkComplexToModulusImageFilterICF3IF3___New_orig__() -> itkComplexToModulusImageFilterICF3IF3_Pointer"""
    return _itkComplexToModulusImageFilterPython.itkComplexToModulusImageFilterICF3IF3___New_orig__()

def itkComplexToModulusImageFilterICF3IF3_cast(obj: 'itkLightObject') -> "itkComplexToModulusImageFilterICF3IF3 *":
    """itkComplexToModulusImageFilterICF3IF3_cast(itkLightObject obj) -> itkComplexToModulusImageFilterICF3IF3"""
    return _itkComplexToModulusImageFilterPython.itkComplexToModulusImageFilterICF3IF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def complex_to_modulus_image_filter(*args, **kwargs):
    """Procedural interface for ComplexToModulusImageFilter"""
    import itk
    instance = itk.ComplexToModulusImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def complex_to_modulus_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ComplexToModulusImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.ComplexToModulusImageFilter.values()[0]
    else:
        filter_object = itk.ComplexToModulusImageFilter

    complex_to_modulus_image_filter.__doc__ = filter_object.__doc__
    complex_to_modulus_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    complex_to_modulus_image_filter.__doc__ += "Available Keyword Arguments:\n"
    complex_to_modulus_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



