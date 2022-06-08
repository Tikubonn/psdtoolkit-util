
import base64
from .packbits import encode_packbits, decode_packbits
from .serializable import Serializable 

class Visibles (list, Serializable):

  def __repr__ (self):
    if self:
      return "{:s}({!r})".format(self.__class__.__name__, list(self))
    else:
      return "{:s}()".format(self.__class__.__name__)

  #https://github.com/oov/aviutl_psdtoolkit/blob/d71bb83bc96025fa0e0bd43ca525b63a4ded1280/src/go/img/serialize.go
  
  def _serialize_as_binary (self):
    header = len(self).to_bytes(2, "little")
    body = bytearray()
    for index, visible in enumerate(self):
      while not (index // 8) < len(body):
        body.append(0)
      body[index // 8] <<= 1
      if visible:
        body[index // 8] |= 1
    return encode_packbits(header + body)

  def serialize (self):
    binary = self._serialize_as_binary()
    return base64.urlsafe_b64encode(binary).decode("ascii").replace("=", "")

  #https://github.com/oov/aviutl_psdtoolkit/blob/d71bb83bc96025fa0e0bd43ca525b63a4ded1280/src/go/img/layermgr.go

  @classmethod
  def _deserialize_from_binary (cls, binary):
    decoded = cls()
    binarydecoded = decode_packbits(binary)
    binarydecodedlen, binarydecodedbody = binarydecoded[:2], binarydecoded[2:]
    bdlen = int.from_bytes(binarydecodedlen, "little")
    for index in range(bdlen):
      decoded.append(bool(binarydecodedbody[index // 8] & 0b10000000 >> (index % 8))) 
    return decoded

  @classmethod
  def deserialize (cls, text):
    te = text + "=" * ((len(text) % 4) and (4 - len(text) % 4))
    binary = base64.urlsafe_b64decode(te)
    return cls._deserialize_from_binary(binary)
