"""Extendable JSON is an extendable drop in replacement of Python's JSON library.
By using @json_serialize and @json_deserialize decorators to enable custom objects
not normally serializable by default.

This library includes the ability to serialize Exceptions, Objects, and Datetime objects by default.

=============================

Usage:

.. code-block:: python

  import extendable_json as json
  json.dumps({"Key": "Value"})

outputs: "{"Key": "Value"}" as string

.. code-block:: python

  import extendable_json as json
  json.loads('"{"Key": "Value"}"')

outputs: {"Key": "Value"} as dict

=============================

To extend serialization to objects not normally serializable or customize serialization of an object,
decorate a function accepting a single value with @json_serialize.register giving the object to serialize
with this function.
Return a dict containing keys and values  of the object.

.. code-block:: python

   @json_serialize.register(MyObject)
   def serialize_my_object(val):
       return {"Attrib": str(val.attrib)}


Reverse this by decorating a function accepting a single value with @json_deserialize.register.
Using val as a dictionary, extract the serialized data into a new object loading with data from val.
Return the newly created object.

.. code-block:: python

    @json_deserialize.register(MyObject)
    def deserialize_my_object(val):
        myObject = MyObject()
        myObject.attrib = val['Attrib']
        return myObject

=============================
Exceptions
=============================

Exceptions may be serialized or deserialized.

Exceptions may be serialized within try/except block

.. code-block:: python

  try:
      # Exception thrown
  except Exception as e:
      import extendable_json as json
      json.dumps(e)

Once deserialized exceptions may be raised and/or the Traceback
is available with the traceback attr.

.. code-block:: python

    e = json.loads(exeption_json)
    raise e #To raise exception
    print(e.traceback) #To print traceback

"""
from .extensions import json_serialize, json_deserialize
from .exception_serialization import json_exception, json_serialize_exception, json_deserialize_exception
from .extendable_json import dump, dumps, load, loads
from .version import version, version_string
