import traceback as tb
import sys

import extendable_json.extendable_json as json
from extendable_json import json_serialize, json_deserialize
from extendable_json import version

@json_serialize.register(Exception)
def json_exception(e):
    t, v, tb = sys.exc_info()
    return json_serialize_exception(type_=t, value=v, traceback=tb)

def json_serialize_exception(type_, value, traceback, **kwargs):
    """Dumps the given exceptions info, as returned by ``sys.exc_info()``
    :param typ: the exception's type (class)
    :param val: the exceptions' value (instance)
    :param tb: the exception's traceback (a ``traceback`` object)
    :param include_local_traceback: whether or not to include the local traceback
                                    in the dumped info. This may expose the other
                                    side to implementation details (code) and
                                    package structure, and may theoretically impose
                                    a security risk.
    :returns: A dict of {'type': [module name, exception name], 'args': arguments, 'attrs', attributes,
        'traceback': traceback text}. This dict can be safely passed to json.dumps.
    """
    tbtext = "".join(tb.format_exception(type_, value, traceback))
    attrs = []
    args=[]
    ignored_attrs = frozenset(["_remote_tb", "with_traceback"])
    for name in dir(value):
        if name == "args":
            for a in value.args:
                try:
                    args.append(json.dumps(a))
                except:
                    args.append(repr(a))
        elif name.startswith("_") or name in ignored_attrs:
            continue
        else:
            try:
                attrval = getattr(val, name)
            except AttributeError:
                continue
            try:
                attrval = json.dumps(attrval)
            except:
                attrval = repr(attrval)
            attrs.append((name, attrval))
    return {"type": [type_.__module__, type_.__name__], "args": args, "attrs": attrs, "traceback": tbtext, "kwargs":kwargs}

@json_deserialize.register(Exception)
def json_deserialize_exception(val):
    """
    Loads a dumped exception (the tuple returned by :func:`dump`) info a
    throwable exception object. If the exception cannot be instantiated for any
    reason (i.e., the security parameters do not allow it, or the exception
    class simply doesn't exist on the local machine), a :class:`GenericException`
    instance will be returned instead, containing all of the original exception's
    details.
    :param val: the dumped exception
    :returns: A throwable exception object
    """
    if not 'type' in val:
        return
    modname, clsname = tuple(val['type'])
    args = val['args']
    attrs = val['attrs']
    tbtext = val['traceback']

    if modname not in sys.modules:
        try:
            __import__(modname, None, None, "*")
        except Exception:
            pass

    if modname in sys.modules:
        cls = getattr(sys.modules[modname], clsname, None)
    else:
        cls = None

    if not isinstance(cls, type) or not issubclass(cls, BaseException):
        cls = None

    if cls is None:
        cls = GenericException

    exc = cls.__new__(cls)

    obj_args = []
    for a in args:
        try:
            obj_args.append(json.loads(a))
        except:
            obj_args.append(a)
    exc.args = obj_args

    for name, attrval in attrs:
        try:
            setattr(exc, name, attrval)
        except AttributeError:      # handle immutable attrs (@property)
            pass
    exc.traceback = tbtext
    return exc

class GenericException(Exception):
    """A 'generic exception' that is raised when the exception the gotten from
    the other party cannot be instantiated locally"""
    pass
