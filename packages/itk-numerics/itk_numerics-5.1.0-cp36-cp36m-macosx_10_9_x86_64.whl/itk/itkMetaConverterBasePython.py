# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkMetaConverterBasePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkMetaConverterBasePython', [dirname(__file__)])
        except ImportError:
            import _itkMetaConverterBasePython
            return _itkMetaConverterBasePython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkMetaConverterBasePython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkMetaConverterBasePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkMetaConverterBasePython
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


import itkSpatialObjectBasePython
import itkSpatialObjectPropertyPython
import ITKCommonBasePython
import pyBasePython
import itkRGBAPixelPython
import itkFixedArrayPython
import itkCovariantVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkVectorPython
import itkBoundingBoxPython
import itkPointPython
import itkVectorContainerPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkContinuousIndexPython
import itkIndexPython
import itkMapContainerPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkOptimizerParametersPython
import itkArrayPython
import itkSymmetricSecondRankTensorPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkTransformBasePython
import itkImageRegionPython
class itkMetaConverterBase2(ITKCommonBasePython.itkObject):
    """


    Base class for MetaObject<-> SpatialObject converters.

    SpatialObject scenes are written and read using the MetaIO Library.
    This is managed by the MetaSceneConverter class, which converts
    MetaObject scenes to SpatialObject scenes and vice versa.

    MetaScene walks the scene and uses the converter on each object in the
    scene.

    C++ includes: itkMetaConverterBase.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def ReadMeta(self, name: 'char const *') -> "itkSpatialObject2_Pointer":
        """
        ReadMeta(itkMetaConverterBase2 self, char const * name) -> itkSpatialObject2_Pointer

        Read a MetaIO file, return
        a SpatialObject 
        """
        return _itkMetaConverterBasePython.itkMetaConverterBase2_ReadMeta(self, name)


    def WriteMeta(self, spatialObject: 'itkSpatialObject2', name: 'char const *') -> "bool":
        """
        WriteMeta(itkMetaConverterBase2 self, itkSpatialObject2 spatialObject, char const * name) -> bool

        Write a MetaIO file based
        on this SpatialObject 
        """
        return _itkMetaConverterBasePython.itkMetaConverterBase2_WriteMeta(self, spatialObject, name)


    def MetaObjectToSpatialObject(self, mo: 'MetaObject const *') -> "itkSpatialObject2_Pointer":
        """
        MetaObjectToSpatialObject(itkMetaConverterBase2 self, MetaObject const * mo) -> itkSpatialObject2_Pointer

        Convert
        the MetaObject to Spatial Object 
        """
        return _itkMetaConverterBasePython.itkMetaConverterBase2_MetaObjectToSpatialObject(self, mo)


    def SpatialObjectToMetaObject(self, spatialObject: 'itkSpatialObject2') -> "MetaObject *":
        """
        SpatialObjectToMetaObject(itkMetaConverterBase2 self, itkSpatialObject2 spatialObject) -> MetaObject *

        Convert
        the SpatialObject to MetaObject 
        """
        return _itkMetaConverterBasePython.itkMetaConverterBase2_SpatialObjectToMetaObject(self, spatialObject)


    def SetWriteImagesInSeparateFile(self, _arg: 'bool const') -> "void":
        """
        SetWriteImagesInSeparateFile(itkMetaConverterBase2 self, bool const _arg)

        Set/Get flag for writing images to separate files in metaImage
        instances 
        """
        return _itkMetaConverterBasePython.itkMetaConverterBase2_SetWriteImagesInSeparateFile(self, _arg)


    def GetWriteImagesInSeparateFile(self) -> "bool":
        """GetWriteImagesInSeparateFile(itkMetaConverterBase2 self) -> bool"""
        return _itkMetaConverterBasePython.itkMetaConverterBase2_GetWriteImagesInSeparateFile(self)

itkMetaConverterBase2.ReadMeta = new_instancemethod(_itkMetaConverterBasePython.itkMetaConverterBase2_ReadMeta, None, itkMetaConverterBase2)
itkMetaConverterBase2.WriteMeta = new_instancemethod(_itkMetaConverterBasePython.itkMetaConverterBase2_WriteMeta, None, itkMetaConverterBase2)
itkMetaConverterBase2.MetaObjectToSpatialObject = new_instancemethod(_itkMetaConverterBasePython.itkMetaConverterBase2_MetaObjectToSpatialObject, None, itkMetaConverterBase2)
itkMetaConverterBase2.SpatialObjectToMetaObject = new_instancemethod(_itkMetaConverterBasePython.itkMetaConverterBase2_SpatialObjectToMetaObject, None, itkMetaConverterBase2)
itkMetaConverterBase2.SetWriteImagesInSeparateFile = new_instancemethod(_itkMetaConverterBasePython.itkMetaConverterBase2_SetWriteImagesInSeparateFile, None, itkMetaConverterBase2)
itkMetaConverterBase2.GetWriteImagesInSeparateFile = new_instancemethod(_itkMetaConverterBasePython.itkMetaConverterBase2_GetWriteImagesInSeparateFile, None, itkMetaConverterBase2)
itkMetaConverterBase2_swigregister = _itkMetaConverterBasePython.itkMetaConverterBase2_swigregister
itkMetaConverterBase2_swigregister(itkMetaConverterBase2)

class itkMetaConverterBase3(ITKCommonBasePython.itkObject):
    """


    Base class for MetaObject<-> SpatialObject converters.

    SpatialObject scenes are written and read using the MetaIO Library.
    This is managed by the MetaSceneConverter class, which converts
    MetaObject scenes to SpatialObject scenes and vice versa.

    MetaScene walks the scene and uses the converter on each object in the
    scene.

    C++ includes: itkMetaConverterBase.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def ReadMeta(self, name: 'char const *') -> "itkSpatialObject3_Pointer":
        """
        ReadMeta(itkMetaConverterBase3 self, char const * name) -> itkSpatialObject3_Pointer

        Read a MetaIO file, return
        a SpatialObject 
        """
        return _itkMetaConverterBasePython.itkMetaConverterBase3_ReadMeta(self, name)


    def WriteMeta(self, spatialObject: 'itkSpatialObject3', name: 'char const *') -> "bool":
        """
        WriteMeta(itkMetaConverterBase3 self, itkSpatialObject3 spatialObject, char const * name) -> bool

        Write a MetaIO file based
        on this SpatialObject 
        """
        return _itkMetaConverterBasePython.itkMetaConverterBase3_WriteMeta(self, spatialObject, name)


    def MetaObjectToSpatialObject(self, mo: 'MetaObject const *') -> "itkSpatialObject3_Pointer":
        """
        MetaObjectToSpatialObject(itkMetaConverterBase3 self, MetaObject const * mo) -> itkSpatialObject3_Pointer

        Convert
        the MetaObject to Spatial Object 
        """
        return _itkMetaConverterBasePython.itkMetaConverterBase3_MetaObjectToSpatialObject(self, mo)


    def SpatialObjectToMetaObject(self, spatialObject: 'itkSpatialObject3') -> "MetaObject *":
        """
        SpatialObjectToMetaObject(itkMetaConverterBase3 self, itkSpatialObject3 spatialObject) -> MetaObject *

        Convert
        the SpatialObject to MetaObject 
        """
        return _itkMetaConverterBasePython.itkMetaConverterBase3_SpatialObjectToMetaObject(self, spatialObject)


    def SetWriteImagesInSeparateFile(self, _arg: 'bool const') -> "void":
        """
        SetWriteImagesInSeparateFile(itkMetaConverterBase3 self, bool const _arg)

        Set/Get flag for writing images to separate files in metaImage
        instances 
        """
        return _itkMetaConverterBasePython.itkMetaConverterBase3_SetWriteImagesInSeparateFile(self, _arg)


    def GetWriteImagesInSeparateFile(self) -> "bool":
        """GetWriteImagesInSeparateFile(itkMetaConverterBase3 self) -> bool"""
        return _itkMetaConverterBasePython.itkMetaConverterBase3_GetWriteImagesInSeparateFile(self)

itkMetaConverterBase3.ReadMeta = new_instancemethod(_itkMetaConverterBasePython.itkMetaConverterBase3_ReadMeta, None, itkMetaConverterBase3)
itkMetaConverterBase3.WriteMeta = new_instancemethod(_itkMetaConverterBasePython.itkMetaConverterBase3_WriteMeta, None, itkMetaConverterBase3)
itkMetaConverterBase3.MetaObjectToSpatialObject = new_instancemethod(_itkMetaConverterBasePython.itkMetaConverterBase3_MetaObjectToSpatialObject, None, itkMetaConverterBase3)
itkMetaConverterBase3.SpatialObjectToMetaObject = new_instancemethod(_itkMetaConverterBasePython.itkMetaConverterBase3_SpatialObjectToMetaObject, None, itkMetaConverterBase3)
itkMetaConverterBase3.SetWriteImagesInSeparateFile = new_instancemethod(_itkMetaConverterBasePython.itkMetaConverterBase3_SetWriteImagesInSeparateFile, None, itkMetaConverterBase3)
itkMetaConverterBase3.GetWriteImagesInSeparateFile = new_instancemethod(_itkMetaConverterBasePython.itkMetaConverterBase3_GetWriteImagesInSeparateFile, None, itkMetaConverterBase3)
itkMetaConverterBase3_swigregister = _itkMetaConverterBasePython.itkMetaConverterBase3_swigregister
itkMetaConverterBase3_swigregister(itkMetaConverterBase3)



