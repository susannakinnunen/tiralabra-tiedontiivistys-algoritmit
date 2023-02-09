from huffman_coding import HuffmanCoding

class UI:
    def __init__(self, compressor):
        self.compressor = compressor
        self.compressor.compress()

if __name__ == "__main__":
    text_file_path = input("Anna tekstitiedoston polku:")
    compressor = HuffmanCoding(text_file_path, "compress")
    UI(compressor)
    print("Tiedosto on kompressoitu samaan kansioon kuin missä olet nimellä comprsesed.bin")