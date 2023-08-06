import unittest

from d64 import DiskImage


class TestDirRead(unittest.TestCase):

    def test_read_entry(self):
        with DiskImage('test/data/test.d64') as image:
            e = image.path("CATACOMBS")
            self.assertEqual(e.size_blocks, 16)
            self.assertEqual(e.size_bytes, 3813)

    def test_iter(self):
        with DiskImage('test/data/test.d64') as image:
            entries = [e for e in image.iterdir()]
            self.assertEqual(len(entries), 28)
            entries = [e for e in image.iterdir(include_deleted=True)]
            self.assertEqual(len(entries), 32)
            entries = [e for e in image.glob("T*")]
            self.assertEqual(len(entries), 3)
            entries = [e for e in image.glob("T*", include_deleted=True)]
            self.assertEqual(len(entries), 4)
            entries = [e for e in image.glob("*=S")]
            self.assertEqual(len(entries), 1)


if __name__ == '__main__':
    unittest.main()
