# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSpatialObjectReaderPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSpatialObjectReaderPython', [dirname(__file__)])
        except ImportError:
            import _itkSpatialObjectReaderPython
            return _itkSpatialObjectReaderPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkSpatialObjectReaderPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkSpatialObjectReaderPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSpatialObjectReaderPython
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


import itkMetaConverterBasePython
import ITKCommonBasePython
import pyBasePython
import itkSpatialObjectBasePython
import itkCovariantVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkVectorPython
import itkAffineTransformPython
import itkMatrixPython
import itkPointPython
import vnl_matrix_fixedPython
import itkMatrixOffsetTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkOptimizerParametersPython
import itkArrayPython
import itkTransformBasePython
import itkArray2DPython
import itkBoundingBoxPython
import itkMapContainerPython
import itkVectorContainerPython
import itkOffsetPython
import itkSizePython
import itkContinuousIndexPython
import itkIndexPython
import itkImageRegionPython
import itkSpatialObjectPropertyPython
import itkRGBAPixelPython
import itkGroupSpatialObjectPython

def itkSpatialObjectReader3_New():
  return itkSpatialObjectReader3.New()


def itkSpatialObjectReader2_New():
  return itkSpatialObjectReader2.New()

class itkSpatialObjectReader2(ITKCommonBasePython.itkObject):
    """Proxy of C++ itkSpatialObjectReader2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSpatialObjectReader2_Pointer":
        """__New_orig__() -> itkSpatialObjectReader2_Pointer"""
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSpatialObjectReader2_Pointer":
        """Clone(itkSpatialObjectReader2 self) -> itkSpatialObjectReader2_Pointer"""
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader2_Clone(self)


    def Update(self) -> "void":
        """
        Update(itkSpatialObjectReader2 self)

        Load a scene file. 
        """
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader2_Update(self)


    def SetFileName(self, *args) -> "void":
        """
        SetFileName(itkSpatialObjectReader2 self, char const * _arg)
        SetFileName(itkSpatialObjectReader2 self, std::string const & _arg)

        Set the filename 
        """
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader2_SetFileName(self, *args)


    def GetFileName(self) -> "char const *":
        """
        GetFileName(itkSpatialObjectReader2 self) -> char const *

        Get the filename 
        """
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader2_GetFileName(self)


    def GetOutput(self) -> "itkSpatialObject2_Pointer":
        """
        GetOutput(itkSpatialObjectReader2 self) -> itkSpatialObject2_Pointer

        Get the output 
        """
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader2_GetOutput(self)


    def GetGroup(self) -> "itkGroupSpatialObject2_Pointer":
        """
        GetGroup(itkSpatialObjectReader2 self) -> itkGroupSpatialObject2_Pointer

        Get the output, with a
        group spatial object added to the top. This addition makes it easy to
        use GetChildren() to get the list of objects read. 
        """
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader2_GetGroup(self)


    def GetEvent(self) -> "itkMetaEvent const *":
        """
        GetEvent(itkSpatialObjectReader2 self) -> itkMetaEvent

        Set/GetEvent 
        """
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader2_GetEvent(self)


    def SetEvent(self, event: 'itkMetaEvent') -> "void":
        """SetEvent(itkSpatialObjectReader2 self, itkMetaEvent event)"""
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader2_SetEvent(self, event)


    def RegisterMetaConverter(self, metaTypeName: 'char const *', spatialObjectTypeName: 'char const *', converter: 'itkMetaConverterBase2') -> "void":
        """
        RegisterMetaConverter(itkSpatialObjectReader2 self, char const * metaTypeName, char const * spatialObjectTypeName, itkMetaConverterBase2 converter)

        Add a
        converter for a new MetaObject/SpatialObject type 
        """
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader2_RegisterMetaConverter(self, metaTypeName, spatialObjectTypeName, converter)

    __swig_destroy__ = _itkSpatialObjectReaderPython.delete_itkSpatialObjectReader2

    def cast(obj: 'itkLightObject') -> "itkSpatialObjectReader2 *":
        """cast(itkLightObject obj) -> itkSpatialObjectReader2"""
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSpatialObjectReader2

        Create a new object of the class itkSpatialObjectReader2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpatialObjectReader2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpatialObjectReader2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpatialObjectReader2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSpatialObjectReader2.Clone = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader2_Clone, None, itkSpatialObjectReader2)
itkSpatialObjectReader2.Update = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader2_Update, None, itkSpatialObjectReader2)
itkSpatialObjectReader2.SetFileName = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader2_SetFileName, None, itkSpatialObjectReader2)
itkSpatialObjectReader2.GetFileName = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader2_GetFileName, None, itkSpatialObjectReader2)
itkSpatialObjectReader2.GetOutput = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader2_GetOutput, None, itkSpatialObjectReader2)
itkSpatialObjectReader2.GetGroup = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader2_GetGroup, None, itkSpatialObjectReader2)
itkSpatialObjectReader2.GetEvent = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader2_GetEvent, None, itkSpatialObjectReader2)
itkSpatialObjectReader2.SetEvent = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader2_SetEvent, None, itkSpatialObjectReader2)
itkSpatialObjectReader2.RegisterMetaConverter = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader2_RegisterMetaConverter, None, itkSpatialObjectReader2)
itkSpatialObjectReader2_swigregister = _itkSpatialObjectReaderPython.itkSpatialObjectReader2_swigregister
itkSpatialObjectReader2_swigregister(itkSpatialObjectReader2)

def itkSpatialObjectReader2___New_orig__() -> "itkSpatialObjectReader2_Pointer":
    """itkSpatialObjectReader2___New_orig__() -> itkSpatialObjectReader2_Pointer"""
    return _itkSpatialObjectReaderPython.itkSpatialObjectReader2___New_orig__()

def itkSpatialObjectReader2_cast(obj: 'itkLightObject') -> "itkSpatialObjectReader2 *":
    """itkSpatialObjectReader2_cast(itkLightObject obj) -> itkSpatialObjectReader2"""
    return _itkSpatialObjectReaderPython.itkSpatialObjectReader2_cast(obj)

class itkSpatialObjectReader3(ITKCommonBasePython.itkObject):
    """Proxy of C++ itkSpatialObjectReader3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSpatialObjectReader3_Pointer":
        """__New_orig__() -> itkSpatialObjectReader3_Pointer"""
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSpatialObjectReader3_Pointer":
        """Clone(itkSpatialObjectReader3 self) -> itkSpatialObjectReader3_Pointer"""
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader3_Clone(self)


    def Update(self) -> "void":
        """
        Update(itkSpatialObjectReader3 self)

        Load a scene file. 
        """
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader3_Update(self)


    def SetFileName(self, *args) -> "void":
        """
        SetFileName(itkSpatialObjectReader3 self, char const * _arg)
        SetFileName(itkSpatialObjectReader3 self, std::string const & _arg)

        Set the filename 
        """
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader3_SetFileName(self, *args)


    def GetFileName(self) -> "char const *":
        """
        GetFileName(itkSpatialObjectReader3 self) -> char const *

        Get the filename 
        """
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader3_GetFileName(self)


    def GetOutput(self) -> "itkSpatialObject3_Pointer":
        """
        GetOutput(itkSpatialObjectReader3 self) -> itkSpatialObject3_Pointer

        Get the output 
        """
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader3_GetOutput(self)


    def GetGroup(self) -> "itkGroupSpatialObject3_Pointer":
        """
        GetGroup(itkSpatialObjectReader3 self) -> itkGroupSpatialObject3_Pointer

        Get the output, with a
        group spatial object added to the top. This addition makes it easy to
        use GetChildren() to get the list of objects read. 
        """
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader3_GetGroup(self)


    def GetEvent(self) -> "itkMetaEvent const *":
        """
        GetEvent(itkSpatialObjectReader3 self) -> itkMetaEvent

        Set/GetEvent 
        """
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader3_GetEvent(self)


    def SetEvent(self, event: 'itkMetaEvent') -> "void":
        """SetEvent(itkSpatialObjectReader3 self, itkMetaEvent event)"""
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader3_SetEvent(self, event)


    def RegisterMetaConverter(self, metaTypeName: 'char const *', spatialObjectTypeName: 'char const *', converter: 'itkMetaConverterBase3') -> "void":
        """
        RegisterMetaConverter(itkSpatialObjectReader3 self, char const * metaTypeName, char const * spatialObjectTypeName, itkMetaConverterBase3 converter)

        Add a
        converter for a new MetaObject/SpatialObject type 
        """
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader3_RegisterMetaConverter(self, metaTypeName, spatialObjectTypeName, converter)

    __swig_destroy__ = _itkSpatialObjectReaderPython.delete_itkSpatialObjectReader3

    def cast(obj: 'itkLightObject') -> "itkSpatialObjectReader3 *":
        """cast(itkLightObject obj) -> itkSpatialObjectReader3"""
        return _itkSpatialObjectReaderPython.itkSpatialObjectReader3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSpatialObjectReader3

        Create a new object of the class itkSpatialObjectReader3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSpatialObjectReader3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSpatialObjectReader3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSpatialObjectReader3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSpatialObjectReader3.Clone = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader3_Clone, None, itkSpatialObjectReader3)
itkSpatialObjectReader3.Update = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader3_Update, None, itkSpatialObjectReader3)
itkSpatialObjectReader3.SetFileName = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader3_SetFileName, None, itkSpatialObjectReader3)
itkSpatialObjectReader3.GetFileName = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader3_GetFileName, None, itkSpatialObjectReader3)
itkSpatialObjectReader3.GetOutput = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader3_GetOutput, None, itkSpatialObjectReader3)
itkSpatialObjectReader3.GetGroup = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader3_GetGroup, None, itkSpatialObjectReader3)
itkSpatialObjectReader3.GetEvent = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader3_GetEvent, None, itkSpatialObjectReader3)
itkSpatialObjectReader3.SetEvent = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader3_SetEvent, None, itkSpatialObjectReader3)
itkSpatialObjectReader3.RegisterMetaConverter = new_instancemethod(_itkSpatialObjectReaderPython.itkSpatialObjectReader3_RegisterMetaConverter, None, itkSpatialObjectReader3)
itkSpatialObjectReader3_swigregister = _itkSpatialObjectReaderPython.itkSpatialObjectReader3_swigregister
itkSpatialObjectReader3_swigregister(itkSpatialObjectReader3)

def itkSpatialObjectReader3___New_orig__() -> "itkSpatialObjectReader3_Pointer":
    """itkSpatialObjectReader3___New_orig__() -> itkSpatialObjectReader3_Pointer"""
    return _itkSpatialObjectReaderPython.itkSpatialObjectReader3___New_orig__()

def itkSpatialObjectReader3_cast(obj: 'itkLightObject') -> "itkSpatialObjectReader3 *":
    """itkSpatialObjectReader3_cast(itkLightObject obj) -> itkSpatialObjectReader3"""
    return _itkSpatialObjectReaderPython.itkSpatialObjectReader3_cast(obj)



