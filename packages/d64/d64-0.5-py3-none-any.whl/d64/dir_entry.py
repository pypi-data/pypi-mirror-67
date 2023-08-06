import struct

from .block import Block


class DirEntry(object):
    ENTRY_SIZE = 0x20
    FTYPE_STR = ('DEL', 'SEQ', 'PRG', 'USR', 'REL', '???', '???', '???')

    def __init__(self, image, entry_start):
        self.image = image
        self.entry_start = entry_start

    def _file_type(self):
        return self.image.map[self.entry_start+2]

    def first_block(self):
        """Return the first block containing file data."""
        return Block(self.image, *self.start_ts)

    def reset(self, first_block):
        """Reset an entry for reuse."""
        self.file_type = 0
        self.size = 1
        self.start_ts = (first_block.track, first_block.sector)

    @property
    def is_deleted(self):
        """Return `True` if this entry is no longer in use."""
        return self._file_type() == 0

    @property
    def file_type(self):
        return self.FTYPE_STR[self._file_type() & 7]

    @property
    def protected(self):
        return bool(self._file_type() & 0x40)

    @property
    def closed(self):
        return bool(self._file_type() & 0x80)

    @property
    def start_ts(self):
        return struct.unpack('<BB', self.image.map[self.entry_start+3:self.entry_start+5])

    @property
    def name(self):
        name = self.image.map[self.entry_start+5:self.entry_start+0x15]
        return name.rstrip(b'\xa0')

    @property
    def size(self):
        size, = struct.unpack('<H', self.image.map[self.entry_start+0x1e:self.entry_start+0x20])
        return size

    @file_type.setter
    def file_type(self, ftype):
        if isinstance(ftype, str):
            if ftype.upper() not in self.FTYPE_STR:
                raise ValueError("Unknown file type, "+ftype)
            ftype = self.FTYPE_STR.index(ftype.upper()) | 0x80

        self.image.map[self.entry_start+2] = ftype

    @protected.setter
    def protected(self, prot):
        val = 0x40 if prot else 0
        old = self.image.map[self.entry_start+2]
        self.image.map[self.entry_start+2] = old & 0xbf | val

    @closed.setter
    def closed(self, clsd):
        val = 0x80 if clsd else 0
        old = self.image.map[self.entry_start+2]
        self.image.map[self.entry_start+2] = old & 0x7f | val

    @start_ts.setter
    def start_ts(self, ts):
        self.image.map[self.entry_start+3:self.entry_start+5] = struct.pack('<BB', *ts)

    @name.setter
    def name(self, name):
        self.image.map[self.entry_start+5:self.entry_start+0x15] = name.ljust(16, b'\xa0')

    @size.setter
    def size(self, size):
        self.image.map[self.entry_start+0x1e:self.entry_start+0x20] = struct.pack('<H', size)
