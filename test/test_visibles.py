
from unittest import TestCase 
from psdtoolkit_util import Visibles

class TestVisibles (TestCase):

  #https://seiga.nicovideo.jp/seiga/im5342445
  #f="...\\SDゆかり.psd";l="L.0 V.9E0AwmIBIEwMAQYIAA";

  def test_serialize (self):
    TEST_DATA = [True, True, False, False, False, False, True, False, False, True, True, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, True, False, False, True, True, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False]
    visibles = Visibles(TEST_DATA)
    self.assertEqual(visibles.serialize(), "9E0AwmIBIEwMAQYIAA")

  #https://seiga.nicovideo.jp/seiga/im6232152
  #f="...\\結月ゆかりさん2.psd";l="L.0 V._LgAPv0CgPY-GCAJnCIIAO5AAg75YEEAwETALw";

  def test_serialize2 (self):
    TEST_DATA = [False, False, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, True, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, True, True, False, False, True, True, True, False, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, True, True, True, False, False, True, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, True, True, True, False, False, True, True, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, True, False, False, False, True, False, False, True, True, False, False, False, False, False, False, False, False, True, False, True, True, True, True]
    visibles = Visibles(TEST_DATA)
    self.assertEqual(visibles.serialize(), "_LgAPv0CgPY-GCAJnCIIAO5AAg75YEEAwETALw")

  #https://seiga.nicovideo.jp/seiga/im5342445
  #f="...\\SDゆかり.psd";l="L.0 V.9E0AwmIBIEwMAQYIAA";

  def test_deserialize (self):
    TEST_DATA = [True, True, False, False, False, False, True, False, False, True, True, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, True, False, False, True, True, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False]
    visibles = Visibles(TEST_DATA)
    self.assertEqual(Visibles.deserialize(visibles.serialize()), TEST_DATA)

  #https://seiga.nicovideo.jp/seiga/im6232152
  #f="...\\結月ゆかりさん2.psd";l="L.0 V._LgAPv0CgPY-GCAJnCIIAO5AAg75YEEAwETALw";

  def test_deserialize2 (self):
    TEST_DATA = [False, False, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, True, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, True, True, False, False, True, True, True, False, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, True, True, True, False, False, True, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, True, True, True, False, False, True, True, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, True, False, False, False, True, False, False, True, True, False, False, False, False, False, False, False, False, True, False, True, True, True, True]
    visibles = Visibles(TEST_DATA)
    self.assertEqual(Visibles.deserialize(visibles.serialize()), TEST_DATA)
