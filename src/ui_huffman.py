"""This is a preliminary user interface for file compression and decompression."""
from huffman.compress_huffman_coding import HuffmanCodingCompress
from huffman.decompress_huffman_coding import HuffmanCodingDecompress
import os

class UI:
    def __init__(self, text_file_path):
        self.text_file_path = text_file_path
        self.compress()
        self.decompress()

    def compress(self):
        return HuffmanCodingCompress(self.text_file_path)
    
    def decompress(self):
        return HuffmanCodingDecompress(self.text_file_path)


if __name__ == "__main__":
    print("Tämä on Huffmanin algoritmiin perustuva tiedonpakkausohjelma.")
    text_file_path = input("Anna tekstitiedoston polku:")
    ui = UI(text_file_path)
    compressed_file_path = os.path.join(
            os.getcwd(), "compressed.bin")
    decompressed_file_path = os.path.join(
            os.getcwd(), "decompressed.txt")
    print("\n")
    print(f"Kompressoitu tiedosto löytyy polusta {compressed_file_path} ja dekompressoitu polusta {decompressed_file_path}.")