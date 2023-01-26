import unittest
import os
from huffman_coding import HuffmanCoding

class TestHuffmanCoding(unittest.TestCase):
    def setUp(self):
        self.huffman_coding = HuffmanCoding() 

    def test_frequency_table(self):
        """Test create_frequency_table method"""
        string = "AABC"
        frequence_table = self.huffman_coding.create_frequence_table(string)
        self.assertEqual(frequence_table, {"A":2, "B":1, "C":1})

    def test_get_string_from_file(self):
        """Test get_string_from_file method"""
        with open(os.path.join(os.getcwd(), "test.txt"), "w") as test_file:
            test_file.write("Test text: \n12368")
        
        path = os.path.join(os.getcwd(), "test.txt")
        
        string = self.huffman_coding.get_string_from_file(path)

        self.assertEqual(string, "Test text: \n12368")