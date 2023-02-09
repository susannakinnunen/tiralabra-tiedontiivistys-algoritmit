""" File compressing and decompressing algorithm"""
import heapq # provides priority queue algorithms
import os

class HuffmanCoding:
    """File compressing and decompressing algorithm"""
    def __init__(self, path, command = None):
        self.frequence_table = {}
        self.string = self.get_string_from_file(path)
        self.heap = []
        self.character_codes = { }#Individual characters and their binarycodes
        self.path = path
        if command == "compress":
            self.compress()
        elif command == "decompress":
            self.decompress()
        else:
            return

    def compress(self):
        """A service function to take care of the compression"""
        self.create_frequence_table()
        self.create_minimum_heap()
        self.create_huffman_tree()
        self.create_codes()
        encoded_string = self.create_encoded_string()
        self.create_compressed_file(encoded_string)

    def get_string_from_file(self, path):
        """Gets a path to a file as a parameter and returns
        a string of the file content"""
        with open(path, "r", encoding="utf-8") as file:
            string = file.read()
            string = string.strip()
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

        with open("compressed.bin", "wb") as binary_file:
            binary_file.write(byte_list)

        return binary_file
    def write_remaining_bits(self, encoded_string):
        """Makes the encoded string divisible by 8,
        so that it can be later converted into bytes"""
        modulus = len(encoded_string) % 8
        filling_length = modulus
        #checks if the encoded string is divisible by 8
        if modulus != 0:
            filling_length = 8 - modulus # the modulus is subtracted from 8
            # in order to know how many bits to add to the encoded_string
            for index in range(filling_length): #pylint:disable=unused-variable
                # the remainder in filling_length is
                # added to the end of the encoded_string
                encoded_string += "0"

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
        """Decompresses the compressed file"""
         # 1 .read and save binary file in the given path
        self.get_binary_string_from_file()
        # 2. find out the amount of filling bits and remove them
        # 3. decode the string ->
        # replace the codes with the help of self.character codes
        # 4. save the decoded string

    def get_binary_string_from_file(self):
        """Fetches a binary string from the compressed file"""
        # 1 .read binary file in the given path
        with open(os.path.join(
            os.getcwd(), "compressed.bin"), "rb", encoding="utf-8"
            ) as file:
            binary_string = file.read()
            binary_string = binary_string.strip()
        return binary_string

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
