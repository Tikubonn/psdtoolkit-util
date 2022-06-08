
from .serializable import Serializable

class Flip (int, Serializable): #enum.Enumは継承不可なのでそれっぽい型を定義

  def __repr__ (self):
    return "{:s}({!r})".format(self.__class__.__name__, int(self))

  def __and__ (self, flip):
    return Flip(super().__and__(flip))

  def __or__ (self, flip):
    return Flip(super().__or__(flip))

  def __xor__ (self, flip):
    return Flip(super().__xor__(flip))

  def __invert__ (self):
    return Flip(super().__invert__())

  def flip_x (self, state):
    if state:
      return Flip(self | self.X)
    else:
      return Flip(self & ~self.X)

  def flip_y (self, state):
    if state:
      return Flip(self | self.Y)
    else:
      return Flip(self & ~self.Y)

  def serialize (self):
    return "{:d}".format(self)

  @classmethod
  def deserialize (cls, text):
    return cls(int(text))

Flip.NONE = Flip(0)
Flip.X = Flip(1)
Flip.Y = Flip(2)
Flip.XY = Flip(Flip.X | Flip.Y)
