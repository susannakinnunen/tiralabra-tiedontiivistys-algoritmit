import unittest
import os
from huffman_coding import HuffmanCoding

class TestHuffmanCodingKalevala(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join(os.getcwd(), "kalevala.txt")
        self.huffman_compress = HuffmanCoding(self.path)
    
    def test_compress_is_smaller(self):
        """Tests if the compressed file size is at least 60 % smaller than the original file size"""
        original_file_size = os.path.getsize(os.path.join(os.getcwd(), "kalevala.txt"))
        compressed_file_size = os.path.getsize(os.path.join(os.getcwd(), "huffman_compressed.bin"))

        assert compressed_file_size/original_file_size <= 0.60
    
    def test_decompress_returns_original_file_content(self):
        HuffmanCoding(self.path)
        with open("kalevala.txt", "r", encoding="utf-8")as original_file, open("huffman_decompressed.txt", "r", encoding="utf-8")as decompressed_file:
            original_string = original_file.read()
            decompressed_string = decompressed_file.read()

        assert original_string == decompressed_string
