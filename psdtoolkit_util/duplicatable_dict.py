
from collections import OrderedDict
from collections.abc import MutableMapping, Mapping, Iterable

class DuplicatableDict (MutableMapping): #低速ではあるものの重複要素と順序を維持する辞書型

  def __init__ (self, value={}):
    if isinstance(value, Mapping):
      self._keyandvalues = [ (key, val) for key, val in value.items() ]
    elif isinstance(value, Iterable):
      self._keyandvalues = [ (key, val) for key, val in value ]
    else:
      raise TypeError("Constructor argument must be {!r} or {!r}.".format(Mapping, Iterable)) #error

  def _find_by_key (self, key):
    for index, (k, value) in enumerate(self._keyandvalues):
      if k == key:
        return True, index
    else:
      return False, -1

  def __contains__ (self, key):
    found, index = self._find_by_key(key)
    return found

  def __getitem__ (self, key):
    found, index = self._find_by_key(key)
    if found:
      key, value = self._keyandvalues[index]
      return value
    else:
      raise KeyError("Could not find {!r} in {!r}.".format(key, self)) #error 

  def __setitem__ (self, key, value):
    found, index = self._find_by_key(key)
    if found:
      self._keyandvalues[index] = (key, value)
    else:
      self._keyandvalues.append((key, value))

  def __delitem__ (self, key):
    found, index = self._find_by_key(key)
    if found:
      self._keyandvalues.pop(index)
    else:
      raise KeyError("Could not find {!r} in {!r}.".format(key, self)) #error 

  def __iter__ (self):
    return iter(self.keys())

  def __len__ (self):
    return len(self.items())

  def items (self):
    return [ (key, value) for key, value in self._keyandvalues ]

  def keys (self):
    return [ key for key, value in self._keyandvalues ]

  def values (self):
    return [ value for key, value in self._keyandvalues ]
