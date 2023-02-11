from compress_huffman_coding import HuffmanCodingCompress
from decompress_huffman_coding import HuffmanCodingDecompress

class UI:
    def __init__(self, text_file_path):
        HuffmanCodingCompress(text_file_path)
        HuffmanCodingDecompress(text_file_path)


if __name__ == "__main__":
    print("Tämä on Huffmanin algoritmiin perustuva tiedonpakkausohjelma.")
    text_file_path = input("Anna tekstitiedoston polku:")
    UI(text_file_path)
    print("Kompressoitu tiedosto löytyy nimellä compressed.bin ja dekompressoitu nimellä decompressed.txt ohjelman juurikansiosta.")