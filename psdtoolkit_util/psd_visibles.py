
from psd_tools import PSDImage 
from collections.abc import Mapping, Iterable
from .visibles import Visibles 
from .serializable import Serializable 
from .duplicatable_dict import DuplicatableDict

class PSDPath (tuple):

  def __new__ (cls, value=""):
    if isinstance(value, str):
      if value:
        return super().__new__(cls, value.split("/"))
      else:
        return super().__new__(cls)
    elif isinstance(value, Iterable):
      return super().__new__(cls, value)
    else:
      raise TypeError("Constructor argument {!r} must be {!r} or {!r}.".format(value, str, Iterable)) #error

  def __repr__ (self):
    return "{}({})".format(self.__class__.__name__, list(self))

  def __str__ (self):
    return "/".join(self)

  @property
  def parent (self):
    return PSDPath(self[:-1])

  @property
  def name (self):
    if self:
      return self[-1]
    else:
      return None 

class PSDVisibles (DuplicatableDict, Serializable):

  def __init__ (self, value={}):
    if isinstance(value, PSDImage):
      super().__init__([ (PSDVisibles.get_layer_path(layer), layer.visible) for layer in value.descendants() ])
    elif isinstance(value, Mapping):
      super().__init__({ PSDPath(key): val for key, val in value.items() })
    elif isinstance(value, Iterable):
      super().__init__([ (PSDPath(key), val) for key, val in value ])
    else:
      raise TypeError("Constructor argument {!r} must be {!r}, {!r} or {!r}.".format(value, PSDImage, Mapping, Iterable)) #error

  def __contains__ (self, key):
    return super().__contains__(PSDPath(key))

  def __getitem__ (self, key):
    return super().__getitem__(PSDPath(key))

  def __setitem__ (self, key, value):
    return super().__setitem__(PSDPath(key), value)

  def __delitem__ (self, key):
    return super().__delitem__(PSDPath(key))

  @staticmethod
  def get_layer_path (layer):
    laynames = list()
    lay = layer
    while lay.parent:
      laynames.insert(0, lay.name)
      lay = lay.parent
    return PSDPath(laynames)

  def iter_sibling (self, path):
    p = PSDPath(path)
    for key in self.keys():
      if key.parent == p.parent:
        yield key

  def change_visible (self, path, state):
    p = PSDPath(path)
    if p in self:
      if p.name.startswith("!"):
        if state != self[p]:
          raise ValueError("Could not change layer {!r} visibility, because layer's name startswith '!'.".format(p)) #error
      elif p.name.startswith("*"):
        if state:
          for siblingp in self.iter_sibling(p):
            if siblingp.name.startswith("*"):
              self[siblingp] = False 
          self[p] = True
        else:
          raise ValueError("Could not change layer {!r} to invisible, because layer's name startswith '*'.".format(p)) #error
      else:
        self[p] = state
      if p.parent:
        self.change_visible(p.parent, state)
    else:
      raise KeyError("Could not find layer {!r} in {!r}.".format(p, self)) #error

  def serialize (self):
    return Visibles(self.values()).serialize()

  @classmethod
  def deserialize (cls, text):
    raise TypeError("{!r} has not supported .deserialize method.".format(cls)) #error

  @classmethod
  def open (cls, file, *, encoding=None):
    psd = PSDImage.open(file, encoding=encoding)
    return cls(psd)
