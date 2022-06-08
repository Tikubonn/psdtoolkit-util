
import struct 
import itertools

#https://github.com/oov/aviutl_psdtoolkit/blob/d71bb83bc96025fa0e0bd43ca525b63a4ded1280/src/go/img/packbits.go

class PackBitsPart:

  def __init__ (self):
    self._values = bytearray()

  def __iter__ (self):
    return iter(self._values)

  def can_add (self, value, nextvalue=None):
    if 2 <= len(self._values):
      if self._values[0] == self._values[1]:
        return self._values[-1] == value 
      else:
        return self._values[-1] != value != nextvalue 
    elif 1 <= len(self._values):
      return self._values[-1] == value or self._values[-1] != value != nextvalue
    else:
      return True 

  def add (self, value, nextvalue=None):
    if 2 <= len(self._values):
      if self._values[0] == self._values[1]:
        if self._values[-1] == value:
          self._values.append(value)
        else:
          raise ValueError("")
      else:
        if self._values[-1] != value != nextvalue:
          self._values.append(value)
        else:
          raise ValueError("")
    elif 1 <= len(self._values):
      if self._values[-1] == value or self._values[-1] != value != nextvalue:
        self._values.append(value)
      else:
        raise ValueError("")
    else:
      self._values.append(value)

  def encode (self):
    if len(self._values) == 0:
      return bytes()
    elif len(self._values) == 1:
      return bytes(struct.pack("b", -1) + self._values)
    else:
      encoded = bytearray()
      if self._values[0] == self._values[1]:
        index = 0
        while index < len(self._values):
          ln = min(len(self._values) - index, 127)
          encoded.append(ln)
          encoded.append(self._values[0])
          index += ln
      else:
        index = 0
        while index < len(self._values):
          ln = min(len(self._values) - index, 128)
          encoded.extend(struct.pack("b", -ln))
          encoded.extend(self._values[index: index + ln])
          index += ln
      return bytes(encoded)

def encode_packbits (binary):
  pbparts = [ PackBitsPart() ]
  for a, b in itertools.zip_longest(binary, binary[1:]):
    if not pbparts[-1].can_add(a, b):
      pbparts.append(PackBitsPart())
    pbparts[-1].add(a)
  encoded = bytearray()
  for pbpart in pbparts:
    encoded.extend(pbpart.encode())
  return encoded

def decode_packbits (binary):
  decoded = bytearray()
  index = 0
  while index < len(binary):
    b, = struct.unpack_from("b", binary, index)
    if b < 0:
      decoded.extend(binary[index +1: index + abs(b) +1])
      index += 1 + abs(b)
    else:
      decoded.extend([ binary[index +1] ] * b)
      index += 2
  return bytes(decoded)
