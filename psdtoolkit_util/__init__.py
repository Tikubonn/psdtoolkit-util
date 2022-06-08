
from .flip import Flip
from .params import Params 
from .visibles import Visibles 
from .packbits import encode_packbits, decode_packbits
from .psd_visibles import PSDPath, PSDVisibles
from .serializable import Serializable, serialize
from .duplicatable_dict import DuplicatableDict 

Params.serialization_type_table = Params.serialization_type_table | {
  "L.": Flip,
  "V.": Visibles,
}
