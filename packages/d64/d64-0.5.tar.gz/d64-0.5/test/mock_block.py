class MockBlock(object):
    SECTOR_SIZE = 256

    def __init__(self, _=None, track=1, sector=0):
        self.track = track
        self.sector = sector
        self.data = b''
        self.data_size = 0
        self.start = 0
        self.is_final = True
        self._next_block = None

    def get(self, start, end):
        return self.data[start:end]

    def set(self, start, new):
        self.data[start:start+len(new)] = new

    def _set_data(self, data):
        self.data = data
        self.data_size = len(data)-2

    def set_next_block(self, block):
        self._next_block = block
        self.is_final = False

    def next_block(self):
        return self._next_block
