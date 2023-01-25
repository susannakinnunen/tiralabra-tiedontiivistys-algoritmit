import unittest
from huffman_coding import HuffmanCoding

class TestHuffmanCoding(unittest.TestCase):
    def setUp(self):
        self.huffman_coding = HuffmanCoding() 

    def test_frequency_table(self):
        string = "AABC"
        frequence_table = self.huffman_coding.create_frequence_table(string)
        self.assertEqual(frequence_table, {"A":2, "B":1, "C":1})
