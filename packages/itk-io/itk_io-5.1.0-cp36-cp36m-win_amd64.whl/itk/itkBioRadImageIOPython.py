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
    from . import _itkBioRadImageIOPython
else:
    import _itkBioRadImageIOPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBioRadImageIOPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBioRadImageIOPython.SWIG_PyStaticMethod_New

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


import ITKIOImageBaseBasePython
import ITKCommonBasePython
import pyBasePython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython

def itkBioRadImageIOFactory_New():
  return itkBioRadImageIOFactory.New()


def itkBioRadImageIO_New():
  return itkBioRadImageIO.New()

class itkBioRadImageIO(ITKIOImageBaseBasePython.itkImageIOBase):
    r"""Proxy of C++ itkBioRadImageIO class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBioRadImageIOPython.itkBioRadImageIO___New_orig__)
    Clone = _swig_new_instance_method(_itkBioRadImageIOPython.itkBioRadImageIO_Clone)
    __swig_destroy__ = _itkBioRadImageIOPython.delete_itkBioRadImageIO
    cast = _swig_new_static_method(_itkBioRadImageIOPython.itkBioRadImageIO_cast)

    def New(*args, **kargs):
        """New() -> itkBioRadImageIO

        Create a new object of the class itkBioRadImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBioRadImageIO.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBioRadImageIO.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBioRadImageIO.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBioRadImageIO in _itkBioRadImageIOPython:
_itkBioRadImageIOPython.itkBioRadImageIO_swigregister(itkBioRadImageIO)
itkBioRadImageIO___New_orig__ = _itkBioRadImageIOPython.itkBioRadImageIO___New_orig__
itkBioRadImageIO_cast = _itkBioRadImageIOPython.itkBioRadImageIO_cast

class itkBioRadImageIOFactory(ITKCommonBasePython.itkObjectFactoryBase):
    r"""Proxy of C++ itkBioRadImageIOFactory class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBioRadImageIOPython.itkBioRadImageIOFactory___New_orig__)
    RegisterOneFactory = _swig_new_static_method(_itkBioRadImageIOPython.itkBioRadImageIOFactory_RegisterOneFactory)
    __swig_destroy__ = _itkBioRadImageIOPython.delete_itkBioRadImageIOFactory
    cast = _swig_new_static_method(_itkBioRadImageIOPython.itkBioRadImageIOFactory_cast)

    def New(*args, **kargs):
        """New() -> itkBioRadImageIOFactory

        Create a new object of the class itkBioRadImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBioRadImageIOFactory.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBioRadImageIOFactory.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBioRadImageIOFactory.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBioRadImageIOFactory in _itkBioRadImageIOPython:
_itkBioRadImageIOPython.itkBioRadImageIOFactory_swigregister(itkBioRadImageIOFactory)
itkBioRadImageIOFactory___New_orig__ = _itkBioRadImageIOPython.itkBioRadImageIOFactory___New_orig__
itkBioRadImageIOFactory_RegisterOneFactory = _itkBioRadImageIOPython.itkBioRadImageIOFactory_RegisterOneFactory
itkBioRadImageIOFactory_cast = _itkBioRadImageIOPython.itkBioRadImageIOFactory_cast



