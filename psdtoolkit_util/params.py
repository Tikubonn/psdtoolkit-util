
import re 
from io import StringIO
from collections import OrderedDict
from .serializable import Serializable, serialize

class Params (OrderedDict, Serializable):

  serialization_type_table = {}

  def _cast_serialize_params (self):
    params = self.copy()
    for key, ty in self.serialization_type_table.items():
      if key in params and not isinstance(params[key], Serializable): 
        params[key] = ty(params[key])
    return params

  def serialize (self):
    with StringIO() as buffer:
      params = self._cast_serialize_params()
      for index, (key, value) in enumerate(params.items()):
        if 0 < index:
          buffer.write(" ")
        buffer.write(key)
        buffer.write(serialize(value))
      return buffer.getvalue()

  @classmethod
  def deserialize (cls, text):
    params = cls()
    paramparts = re.split(r"\s+", text)
    for parampart in paramparts:
      key, value = parampart[:2], parampart[2:] 
      if key in cls.serialization_type_table:
        val = cls.serialization_type_table[key].deserialize(value)
      else:
        val = value
      params[key] = val
    return params
