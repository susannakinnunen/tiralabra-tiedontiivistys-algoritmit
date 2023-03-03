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
    
    original_size = os.path.getsize(os.path.join(os.getcwd(), "kalevala.txt"))
    compressed_size = os.path.getsize(os.path.join(os.getcwd(), "lz77_compressed.bin"))
    
    print("\n")
    print(f"-Kompressoitu tiedosto löytyy polusta {compressed_file_path} \n\n-Dekompressoitu tiedosto polusta {decompressed_file_path}")
    print("\n")
    print(f"Kompressoidun tiedoston koko on {round(compressed_size/original_size*100)} % alkuperäisen tiedoston koosta.")