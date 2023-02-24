"""This is a preliminary user interface for file compression and decompression."""
from lz77 import LZ77
import os

class UI:
    def __init__(self, text_file_path):
        self.text_file_path = text_file_path
        LZ77(self.text_file_path)




if __name__ == "__main__":
    print("\n")
    print("Tämä on LZ77 algoritmiin perustuva tiedonpakkausohjelma.")
    text_file_path = input("Anna tekstitiedoston polku:")
    ui = UI(text_file_path)
    compressed_file_path = os.path.join(
            os.getcwd(), "lz77_compressed.bin")
    decompressed_file_path = os.path.join(os.getcwd(), "lz77_decompressed.txt")
    print("\n")
    print(f"Kompressoitu tiedosto löytyy polusta {compressed_file_path} ja dekompressoitu polusta {decompressed_file_path}")