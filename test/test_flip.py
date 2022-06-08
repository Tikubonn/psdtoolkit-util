
from unittest import TestCase 
from psdtoolkit_util import Flip 

class TestFlip (TestCase):

  def test_flip_x (self):
    self.assertEqual(Flip.NONE, Flip.NONE.flip_x(False))
    self.assertEqual(Flip.X, Flip.NONE.flip_x(True))
    self.assertEqual(Flip.NONE, Flip.NONE.flip_x(True).flip_x(False))
    self.assertEqual(Flip.X, Flip.NONE.flip_x(True).flip_y(False))
    self.assertEqual(Flip.XY, Flip.NONE.flip_x(True).flip_y(True))

  def test_flip_y (self):
    self.assertEqual(Flip.NONE, Flip.NONE.flip_y(False))
    self.assertEqual(Flip.Y, Flip.NONE.flip_y(True))
    self.assertEqual(Flip.NONE, Flip.NONE.flip_y(True).flip_y(False))
    self.assertEqual(Flip.Y, Flip.NONE.flip_y(True).flip_x(False))
    self.assertEqual(Flip.XY, Flip.NONE.flip_y(True).flip_x(True))

  def test_serialize (self):
    self.assertEqual(Flip.NONE.serialize(), "0")
    self.assertEqual(Flip.X.serialize(), "1")
    self.assertEqual(Flip.Y.serialize(), "2")
    self.assertEqual(Flip.XY.serialize(), "3")

  def test_deserialize (self):
    self.assertEqual(Flip.deserialize("0"), Flip.NONE)
    self.assertEqual(Flip.deserialize("1"), Flip.X)
    self.assertEqual(Flip.deserialize("2"), Flip.Y)
    self.assertEqual(Flip.deserialize("3"), Flip.XY)

  def test_deserialize2 (self):
    self.assertEqual(Flip.deserialize(Flip.NONE.serialize()), Flip.NONE)
    self.assertEqual(Flip.deserialize(Flip.X.serialize()), Flip.X)
    self.assertEqual(Flip.deserialize(Flip.Y.serialize()), Flip.Y)
    self.assertEqual(Flip.deserialize(Flip.XY.serialize()), Flip.XY)
