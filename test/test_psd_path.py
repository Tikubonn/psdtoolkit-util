
from unittest import TestCase 
from psdtoolkit_util import PSDPath

class TestPSDPath (TestCase):

  def test_psd_path (self):
    self.assertEqual(PSDPath("a/b/c"), PSDPath("a/b/c"))
    self.assertEqual(PSDPath("a/b/c").parent, PSDPath("a/b"))
    self.assertEqual(PSDPath("a/b/c").parent.parent, PSDPath("a"))
    self.assertEqual(PSDPath("a/b/c").parent.parent.parent, PSDPath())
    self.assertEqual(PSDPath("a/b/c").name, "c")
    self.assertEqual(PSDPath("a/b/c").parent.name, "b")
    self.assertEqual(PSDPath("a/b/c").parent.parent.name, "a")
    self.assertEqual(PSDPath("a/b/c").parent.parent.parent.name, None)

  def test_psd_path2 (self):
    self.assertEqual(PSDPath([ "a", "b", "c" ]), PSDPath([ "a", "b", "c" ]))
    self.assertEqual(PSDPath([ "a", "b", "c" ]).parent, PSDPath([ "a", "b" ]))
    self.assertEqual(PSDPath([ "a", "b", "c" ]).parent.parent, PSDPath([ "a" ]))
    self.assertEqual(PSDPath([ "a", "b", "c" ]).parent.parent.parent, PSDPath())
    self.assertEqual(PSDPath([ "a", "b", "c" ]).name, "c")
    self.assertEqual(PSDPath([ "a", "b", "c" ]).parent.name, "b")
    self.assertEqual(PSDPath([ "a", "b", "c" ]).parent.parent.name, "a")
    self.assertEqual(PSDPath([ "a", "b", "c" ]).parent.parent.parent.name, None)

  def test_str_psd_path (self):
    self.assertEqual(str(PSDPath("a/b/c")), "a/b/c")
    self.assertEqual(str(PSDPath("a/b/c").parent), "a/b")
    self.assertEqual(str(PSDPath("a/b/c").parent.parent), "a")
    self.assertEqual(str(PSDPath("a/b/c").parent.parent.parent), "")
