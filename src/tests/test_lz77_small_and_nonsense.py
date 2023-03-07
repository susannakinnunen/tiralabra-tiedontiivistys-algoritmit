import unittest
import os
from lz77 import LZ77
from tests.create_test_file import FileForTesting

with open(os.path.join(os.getcwd(), "test_lz77.txt"), "w") as test_file:
        test_file.write("ABBAABBABB")

class TestLZ77Coding(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join(os.getcwd(), "test_lz77.txt")
        self.lz77 = LZ77(self.path, True)
        self.compressed_info_list = self.lz77.compress()

    def test_get_string_from_file(self):
        """Test get_string_from_file method"""     
        string = self.lz77.get_string_from_file(self.path)

        self.assertEqual(string, "ABBAABBABB")

    def test_compress_and_search_longest_match(self):
        self.assertEqual(self.compressed_info_list, [(0, 1,"A"), (0, 1,"B"), (0, 1,"B"), (0, 1,"A"), (4, 4, 0), (3, 2, 0)])


    def test_compress_and_convert_into_tuples_to_bit_string(self):
        bit_string = self.lz77.convert_into_bit_string(self.compressed_info_list)

        self.assertEqual(bit_string, "0000000001000001000000000100001000000000010000100000000001000001100000000010001000000000100000000001100100000000")

    
    def test_convert_into_bytes(self):
        bit_string = self.lz77.convert_into_bit_string(self.compressed_info_list)
        byte_list = self.lz77.convert_into_bytes(bit_string)

        self.assertEqual(bit_string, "0000000001000001000000000100001000000000010000100000000001000001100000000010001000000000100000000001100100000000")

        self.assertEqual(str(byte_list), 'bytearray(b\'\\x00A\\x00B\\x00B\\x00A\\x80"\\x00\\x80\\x19\\x00\')')


