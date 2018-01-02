"""Implementation of Basic KNX 4-Byte."""

import struct
from xknx.exceptions import ConversionError

from .dpt import DPTBase


class DPT4ByteUnsigned(DPTBase):
    """
    Abstraction for KNX 4 Byte "32-bit unsigned".

    DPT 12.x
    """

    value_min = 0
    value_max = 4294967295
    unit = ""
    resolution = 1
    
    _struct_format = ">I"

    @classmethod
    def from_knx(cls, raw):
        """Parse/deserialize from KNX/IP raw data."""
        cls.test_bytesarray(raw, 4)

        try:
            return struct.unpack(cls._struct_format, bytes(raw))[0]
        except struct.error:
            raise ConversionError(raw)

    @classmethod
    def to_knx(cls, value):
        """Serialize to KNX/IP raw data."""
        if not cls._test_boundaries(value):
            raise ConversionError(value)

        try:
            return tuple(struct.pack(cls._struct_format, value))
        except struct.error:
            raise ConversionError(value)

    @classmethod
    def _test_boundaries(cls, value):
        """Test if value is within defined range for this object."""
        return value >= cls.value_min and \
            value <= cls.value_max



class DPT4ByteSigned(DPT4ByteUnsigned):
    """
    Abstraction for KNX 4 Byte "32-bit signed".

    DPT 13.x
    """

    value_min = -2147483648
    value_max =  2147483647
    unit = ""
    resolution = 1

    _struct_format = ">i"

