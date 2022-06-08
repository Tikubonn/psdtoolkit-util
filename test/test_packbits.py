
import struct 
from unittest import TestCase 
from psdtoolkit_util import encode_packbits, decode_packbits

class TestPackBits (TestCase):

  #0bytes

  def test_encode_packbits (self):
    TEST_DATA = bytes([])
    DESIRABLE_RESULT = bytes([])
    self.assertEqual(list(encode_packbits(TEST_DATA)), list(DESIRABLE_RESULT))
    self.assertEqual(list(decode_packbits(encode_packbits(TEST_DATA))), list(TEST_DATA))

  #1bytes

  def test_encode_packbits2 (self):
    TEST_DATA = bytes([ 0 ])
    DESIRABLE_RESULT = struct.pack("b", -1) + bytes([ 0 ])
    self.assertEqual(list(encode_packbits(TEST_DATA)), list(DESIRABLE_RESULT))
    self.assertEqual(list(decode_packbits(encode_packbits(TEST_DATA))), list(TEST_DATA))

  def test_encode_packbits3 (self):
    TEST_DATA = bytes([ 1 ])
    DESIRABLE_RESULT = struct.pack("b", -1) + bytes([ 1 ])
    self.assertEqual(list(encode_packbits(TEST_DATA)), list(DESIRABLE_RESULT))
    self.assertEqual(list(decode_packbits(encode_packbits(TEST_DATA))), list(TEST_DATA))

  #2bytes 

  def test_encode_packbits4 (self):
    TEST_DATA = bytes([ 0, 0 ])
    DESIRABLE_RESULT = bytes([ 2, 0 ])
    self.assertEqual(list(encode_packbits(TEST_DATA)), list(DESIRABLE_RESULT))
    self.assertEqual(list(decode_packbits(encode_packbits(TEST_DATA))), list(TEST_DATA))

  def test_encode_packbits5 (self):
    TEST_DATA = bytes([ 0, 1 ])
    DESIRABLE_RESULT = struct.pack("b", -2) + bytes([ 0, 1 ])
    self.assertEqual(list(encode_packbits(TEST_DATA)), list(DESIRABLE_RESULT))
    self.assertEqual(list(decode_packbits(encode_packbits(TEST_DATA))), list(TEST_DATA))

  def test_encode_packbits6 (self):
    TEST_DATA = bytes([ 1, 0 ])
    DESIRABLE_RESULT = struct.pack("b", -2) + bytes([ 1, 0 ])
    self.assertEqual(list(encode_packbits(TEST_DATA)), list(DESIRABLE_RESULT))
    self.assertEqual(list(decode_packbits(encode_packbits(TEST_DATA))), list(TEST_DATA))

  def test_encode_packbits7 (self):
    TEST_DATA = bytes([ 1, 1 ])
    DESIRABLE_RESULT = bytes([ 2, 1 ])
    self.assertEqual(list(encode_packbits(TEST_DATA)), list(DESIRABLE_RESULT))
    self.assertEqual(list(decode_packbits(encode_packbits(TEST_DATA))), list(TEST_DATA))

  #3bytes

  def test_encode_packbits8 (self):
    TEST_DATA = bytes([ 0, 0, 0 ])
    DESIRABLE_RESULT = bytes([ 3, 0 ])
    self.assertEqual(list(encode_packbits(TEST_DATA)), list(DESIRABLE_RESULT))
    self.assertEqual(list(decode_packbits(encode_packbits(TEST_DATA))), list(TEST_DATA))

  def test_encode_packbits9 (self):
    TEST_DATA = bytes([ 0, 0, 1 ])
    DESIRABLE_RESULT = bytes([ 2, 0 ]) + struct.pack("b", -1) + bytes([ 1 ])
    self.assertEqual(list(encode_packbits(TEST_DATA)), list(DESIRABLE_RESULT))
    self.assertEqual(list(decode_packbits(encode_packbits(TEST_DATA))), list(TEST_DATA))

  def test_encode_packbits10 (self):
    TEST_DATA = bytes([ 0, 1, 0 ])
    DESIRABLE_RESULT = struct.pack("b", -3) + bytes([ 0, 1, 0 ])
    self.assertEqual(list(encode_packbits(TEST_DATA)), list(DESIRABLE_RESULT))
    self.assertEqual(list(decode_packbits(encode_packbits(TEST_DATA))), list(TEST_DATA))

  def test_encode_packbits11 (self):
    TEST_DATA = bytes([ 0, 1, 1 ])
    DESIRABLE_RESULT = struct.pack("b", -1) + bytes([ 0, 2, 1 ])
    self.assertEqual(list(encode_packbits(TEST_DATA)), list(DESIRABLE_RESULT))
    self.assertEqual(list(decode_packbits(encode_packbits(TEST_DATA))), list(TEST_DATA))

  def test_encode_packbits12 (self):
    TEST_DATA = bytes([ 1, 0, 0 ])
    DESIRABLE_RESULT = struct.pack("b", -1) + bytes([ 1, 2, 0 ])
    self.assertEqual(list(encode_packbits(TEST_DATA)), list(DESIRABLE_RESULT))
    self.assertEqual(list(decode_packbits(encode_packbits(TEST_DATA))), list(TEST_DATA))

  def test_encode_packbits13 (self):
    TEST_DATA = bytes([ 1, 0, 1 ])
    DESIRABLE_RESULT = struct.pack("b", -3) + bytes([ 1, 0, 1 ])
    self.assertEqual(list(encode_packbits(TEST_DATA)), list(DESIRABLE_RESULT))
    self.assertEqual(list(decode_packbits(encode_packbits(TEST_DATA))), list(TEST_DATA))

  def test_encode_packbits14 (self):
    TEST_DATA = bytes([ 1, 1, 0 ])
    DESIRABLE_RESULT = bytes([ 2, 1 ]) + struct.pack("b", -1) + bytes([ 0 ])
    self.assertEqual(list(encode_packbits(TEST_DATA)), list(DESIRABLE_RESULT))
    self.assertEqual(list(decode_packbits(encode_packbits(TEST_DATA))), list(TEST_DATA))

  def test_encode_packbits15 (self):
    TEST_DATA = bytes([ 1, 1, 1 ])
    DESIRABLE_RESULT = bytes([ 3, 1 ])
    self.assertEqual(list(encode_packbits(TEST_DATA)), list(DESIRABLE_RESULT))
    self.assertEqual(list(decode_packbits(encode_packbits(TEST_DATA))), list(TEST_DATA))

  #https://github.com/oov/aviutl_psdtoolkit/blob/d71bb83bc96025fa0e0bd43ca525b63a4ded1280/src/go/img/packbits_test.go

  def test_encode_packbits_with_original_test (self):
    TEST_DATAS = [
      ([], []), 
      ([ 0x03 ], [ 0xff, 0x03 ]), 
      ([ 0x03, 0x03 ], [ 0x02, 0x03 ]), 
      ([ 0x03, 0x04 ], [ 0xfe, 0x03, 0x04 ]), 
      ([ 0x03, 0x03, 0x03 ], [ 0x03, 0x03 ]), 
      ([ 0x03, 0x04, 0x05 ], [ 0xfd, 0x03, 0x04, 0x05 ]), 
      ([ 0x03, 0x03, 0x03, 0x03 ], [ 0x04, 0x03 ]), 
      ([ 0x03, 0x04, 0x05, 0x06 ], [ 0xfc, 0x03, 0x04, 0x05, 0x06 ]), 
      ([ 0x03, 0x03, 0x04 ], [ 0x02, 0x03, 0xff, 0x04 ]), 
      ([ 0x03, 0x04, 0x04 ], [ 0xff, 0x03, 0x02, 0x04 ]), 
      ([ 0x03, 0x03, 0x04, 0x04 ], [ 0x02, 0x03, 0x02, 0x04 ]), 
      ([ 0x03, 0x03, 0x04, 0x05 ], [ 0x02, 0x03, 0xfe, 0x04, 0x05 ]), 
      ([ 0x03, 0x04, 0x05, 0x05 ], [ 0xfe, 0x03, 0x04, 0x02, 0x05 ]), 
      ([ 0x03, 0x04, 0x05, 0x05, 0x06, 0x07 ], [ 0xfe, 0x03, 0x04, 0x02, 0x05, 0xfe, 0x06, 0x07 ]), 
      ([ 0x03, 0x03, 0x04, 0x05, 0x06, 0x06 ], [ 0x02, 0x03, 0xfe, 0x04, 0x05, 0x02, 0x06]), 
    ]
    for TEST_DATA, RESULT_DATA in TEST_DATAS:
      self.assertEqual(list(encode_packbits(TEST_DATA)), list(RESULT_DATA))
      self.assertEqual(list(decode_packbits(encode_packbits(TEST_DATA))), list(TEST_DATA))
