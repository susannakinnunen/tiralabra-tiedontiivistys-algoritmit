import unittest
import os
from lz77 import LZ77


class TestLZ77Coding(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join(os.getcwd(), "kalevala.txt")
        self.lz77 = LZ77(self.path)

    def test_compress_is_smaller(self):
        """Tests if the compressed file size is at least 60 % smaller than the original file size"""
        original_file_size = os.path.getsize(os.path.join(os.getcwd(), "kalevala.txt"))
        compressed_file_size = os.path.getsize(os.path.join(os.getcwd(), "lz77_compressed.bin"))

        assert compressed_file_size/original_file_size <= 0.70

    def test_decompressed_is_same_as_original(self):
        with open("kalevala.txt", "r", encoding="utf-8")as original_file, open("lz77_decompressed.txt", "r", encoding="utf-8")as decompressed_file:
            original_string = original_file.read()
            decompressed_string = decompressed_file.read()

        assert original_string == decompressed_string