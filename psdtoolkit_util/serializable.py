
from abc import ABC, abstractmethod, abstractclassmethod

class Serializable (ABC):

  @abstractmethod
  def serialize (self) -> str:
    pass

  @abstractclassmethod
  def deserialize (cls, text) -> "Serializable":
    pass

def serialize (value):
  if isinstance(value, Serializable):
    return value.serialize()
  else:
    return str(value)
