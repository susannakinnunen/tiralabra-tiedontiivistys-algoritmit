import unittest
import os
from lz77 import LZ77

with open(os.path.join(os.getcwd(), "test_lz77.txt"), "w") as test_file:
        test_file.write("Test text: \n12368")

class TestLZ77Coding(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join(os.getcwd(), "test_lz77.txt")
        self.lz77 = LZ77(self.path)

    def test_get_string_from_file(self):
        """Test get_string_from_file method"""     
        string = self.lz77.get_string_from_file(self.path)

        self.assertEqual(string, "Test text: \n12368")

    



