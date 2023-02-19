import unittest
import os
from lz77 import LZ77

with open(os.path.join(os.getcwd(), "test_lz77.txt"), "w") as test_file:
        test_file.write("ABBAABBABB")

class TestLZ77Coding(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join(os.getcwd(), "test_lz77.txt")
        self.lz77 = LZ77(self.path, True)

    def test_get_string_from_file(self):
        """Test get_string_from_file method"""     
        string = self.lz77.get_string_from_file(self.path)

        self.assertEqual(string, "ABBAABBABB")

    def test_compress_and_search_longest_match(self):
        compressed_info_list = self.lz77.compress()

        self.assertEqual(compressed_info_list, [(0, 1,"A"), (0, 1,"B"), (0, 1,"B"), (0, 1,"A"), (4, 4, 0), (3, 2, 0)])


