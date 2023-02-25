import cProfile

"""Performance testing for huffman algorithm with Python cProfile library
"""
import os
import heapq # provides priority queue algorithms

class HuffmanCoding:#pylint:disable=too-few-public-methods
    """This class compresses and decompresses a text
    file with an algorithm based on Huffman Coding algorithm"""
    def __init__(self, path, test_small_files = None):
        self.character_codes = {} # Key: character, value: binarycode
        self.reversed_charcter_codes = {} # Key:binarycode, value:character
        self.frequence_table = {}
        self.string = self.get_string_from_file(path)
        self.heap = []
        if test_small_files is None:
            self.compress()
            self.decompress()

    def compress(self):
        """Calls for all the needed functions in the right order
        for file compression."""
        self.create_frequence_table()
        self.create_minimum_heap()
        self.create_huffman_tree()
        self.create_codes()
        encoded_string = self.create_encoded_string()
        compressed_file = self.create_compressed_file(encoded_string)
        return compressed_file

    def get_string_from_file(self, path):
        """Gets a path to a file as a parameter and returns
        a string of the file content"""
        with open(path, "r", encoding="utf-8") as file:
            string = file.read()
        return string

    def create_frequence_table(self):
        """Creates a frequence table for the characters in a string/text"""
        for character in self.string:
            if not character in self.frequence_table:
                self.frequence_table[character] = 0
            self.frequence_table[character] += 1
        return self.frequence_table

    def create_minimum_heap(self):
        """Creates a minimum heap of the charcters
        in the string according to their frequence."""
        for character, frequency in self.frequence_table.items():
            node = Node(character, frequency)
            heapq.heappush(self.heap, node)
        return self.heap

    def create_huffman_tree(self):
        """Creates a Huffman tree by calling
        self.create_merged_node function for
        as long as there are nodes in the self.heap."""
        while len(self.heap) > 1:
            merged_node = self.create_merged_node()
            heapq.heappush(self.heap, merged_node)

        return self.heap

    def create_merged_node(self):
        """Takes two nodes with minimum frequency values from
        the minimum heap and merges them creating a merged node.
        The merged node becomes the parent of the two taken nodes"""
        smallest_node = heapq.heappop(self.heap)
        second_smallest_node = heapq.heappop(self.heap)

        merged_node = Node(
            None,
            smallest_node.frequency + second_smallest_node.frequency
            )
        merged_node.left = smallest_node
        merged_node.right = second_smallest_node

        return merged_node


    def create_codes(self):
        """Initiates variables for the encoding of
        the huffman tree. Calls self.encode() function,
        which startto call itself recursively.
        Returns the self.character_codes-dictionary"""
        root_node = heapq.heappop(self.heap)
        code = ""

        self.encode(root_node, code)

        return self.character_codes

    def encode(self, node, code):
        """Assigns codes, 0's and 1's, to the nodes in the Huffman tree.
        Recursive function."""
        if node is None:
            return
        if node.character is not None:
            self.character_codes[node.character] = code
            self.reversed_charcter_codes[code] = node.character

        self.encode(node.left, code + "0")
        self.encode(node.right, code + "1")

    def create_encoded_string(self):
        """Creates an encoded string from the original string
        """
        encoded_string = ""
        for character in self.string:
            encoded_string += self.character_codes[character]
        return encoded_string

    def create_compressed_file(self, encoded_string):
        """Creates a compressed file"""
        encoded_string_with_filling = self.write_remaining_bits(
            encoded_string
            )
        # fetches the encoded string which is divisble by 8

        byte_list = self.create_byte_list(encoded_string_with_filling)
        # fetches a list of bytes

        with open("huffman_compressed.bin", "wb") as binary_file:
            binary_file.write(byte_list)

        return binary_file

    def write_remaining_bits(self, encoded_string):
        """Makes the encoded string divisible by 8,
        so that it can be later converted into bytes"""
        filling_length = 8 - len(encoded_string) % 8
        # checks if the encoded string is divisible by 8 and
        # calculates the amount that will be added to make it
        # divisible by 8
        encoded_string += filling_length*"0"
        # 0's equal to the amount of filling_length
        # are added to the end of the encoded_string.

        filling_information_binary = "{0:08b}".format(filling_length) #pylint:disable=consider-using-f-string
        #filling is formatted into 8-bits long binary form
        encoded_string = filling_information_binary + encoded_string
        # filling_information is used to tell the decompressing algorithm
        # the lenght of the extra bits in the end.
        return encoded_string

    def create_byte_list(self, encoded_string_with_filling):
        """Creates a list of bytes from the encoded_string_with_filling
        """
        byte_list = bytearray()
        for i in range(0, len(encoded_string_with_filling), 8):
            byte = encoded_string_with_filling[i:i+8]
            byte_list.append(int(byte, 2))
        return byte_list

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
        decompressed_file = self.create_decompressed_file(decoded_string)

        return decompressed_file


    def get_binary_string_from_compressed_file(self):
        """Fetches a binary string from the compressed file"""
        # 1 .read binary file in the given path
        binary_string = ""
        with open(os.path.join(
            os.getcwd(), "huffman_compressed.bin"), "rb"
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
            "huffman_decompressed.txt", "w", encoding="utf-8"
            )as decompressed_file:
            decompressed_file.write(decoded_string)

        return decompressed_file
    

class Node:
    """Nodes for the minimum heap
    """
    def __init__(self, character, frequency):
        self.character = character
        self. frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, comparing_node):
        return self.frequency < comparing_node.frequency

    def __repr__(self):
        return f"{self.character}:{self.frequency}"


if __name__== "__main__":
    huffman  = HuffmanCoding("/home/suskinnu/Desktop/yliopisto/tiralabra/tiralabra-tiedontiivistys-algoritmit/kalevala.txt", True)
    cProfile.run('huffman.compress()')
    cProfile.run('huffman.decompress()')
