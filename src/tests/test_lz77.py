import unittest
import os
from lz77 import LZ77

class TestLZ77Coding(unittest.TestCase):
    def setUp(self):
        self.lz77 = LZ77()

    def test_get_string_from_file(self):
        """Test get_string_from_file method"""
        with open(os.path.join(os.getcwd(), "test_lz77.txt"), "w") as test_file:
            test_file.write("Test text: \n12368")
        
        path = os.path.join(os.getcwd(), "test_lz77.txt")
        
        string = self.lz77.get_string_from_file(path)

        self.assertEqual(string, "Test text: \n12368")

    



