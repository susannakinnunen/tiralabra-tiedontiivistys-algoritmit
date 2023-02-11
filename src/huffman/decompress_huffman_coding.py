"""This module holds a class for decompressing"""
import os
from huffman.compress_huffman_coding import HuffmanCodingCompress

class HuffmanCodingDecompress(HuffmanCodingCompress):
    """This class decompresses a compressed file.
        It inherits the class HuffmanCodingCompress,
        and thus takes the textfilepath,
        although it doesn't really needed. To be changed."""
    def __init__(self, text_file_path):
        super().__init__(text_file_path)

        self.decompress()

    def decompress(self):
        """Calls for all the methods needed for decompressing a binaryfile."""
        # 1 .read and save binary file in the given path
        binary_string = self.get_binary_string_from_compressed_file()
        # 2. find out the amount of filling bits and remove them
        binary_string = self.remove_filling_bits(binary_string)
        # 3. decode the string ->
        # replace the codes with the help of self.character codes
        decoded_string = self.decode_string(binary_string)
        # 4. save the decoded string
        self.create_decompressed_file(decoded_string)


    def get_binary_string_from_compressed_file(self):
        """Fetches a binary string from the compressed file"""
        # 1 .read binary file in the given path
        binary_string = ""
        with open(os.path.join(
            os.getcwd(), "compressed.bin"), "rb"
            ) as file:
            byte_from_file = file.read(1)
            while len(byte_from_file) > 0:
                byte_from_file = ord(byte_from_file)
                bits = bin(byte_from_file)[2:].rjust(8, "0")
                binary_string += bits
                byte_from_file = file.read(1)

        return binary_string

    def remove_filling_bits(self, binary_string):
        """Removes filling bits from the bitstring"""
        filling_information_binary = binary_string[:8]
        filling_length = int(filling_information_binary, 2)

        binary_string_filling = binary_string[8:]
        binary_string_no_filling = binary_string_filling[:-1*filling_length]

        return binary_string_no_filling

    def decode_string(self, binary_string):
        """Decodes bitstring into characters"""
        code = ""
        decoded_string = ""
        for bit in binary_string:
            code += bit
            if code in self.reversed_charcter_codes:
                decoded_string += self.reversed_charcter_codes[code]
                code = ""

        return decoded_string

    def create_decompressed_file(self, decoded_string):
        """Writes the decoded string into decompressed.txt file."""
        with open(
            "decompressed.txt", "w", encoding="utf-8"
            )as decompressed_file:
            decompressed_file.write(decoded_string)

        return decompressed_file
