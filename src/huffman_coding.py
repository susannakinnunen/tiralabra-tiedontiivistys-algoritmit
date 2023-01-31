""" File compressing and decompressing algorithm"""
import heapq # provides priority queue algorithms

class HuffmanCoding:
    """File compressing and decompressing algorithm"""
    def __init__(self, path):
        self.frequence_table = {}
        self.string = self.get_string_from_file(path)
        self.heap = []

    def get_string_from_file(self, path):
        """Gets a path to a file as a parameter and returns
        a string of the file content"""
        with open(path, "r", encoding="utf-8") as file:
            string = file.read()
            string = string.strip()
        return string

    def create_frequence_table(self, string = None):
        """Creates a frequence table for the characters in a string/text"""
        if string == None:
            string = self.string
        for character in string:
            if not character in self.frequence_table:
                self.frequence_table[character] = 0
            self.frequence_table[character] += 1
        return self.frequence_table

    def create_minimum_heap(self):
        """Creates a minimum heap of the charcters
        in the string according to their frequence."""
        for character in self.frequence_table:
            node = Node(character, self.frequence_table[character])
            heapq.heappush(self.heap, node)

    def create_huffman_tree(self):
        """Creates a Huffman tree by always taking
        two minimum nodes from the minimum heap and merges them."""

    def encode(self):
        """Assigns codes, 0's and 1's, to the nodes in the Huffman tree.
        The codes are then used to write a compressed file."""

class Node:
    """Nodes for the minimum heap
    """
    def __init__(self, character, frequency):
        self.character = character
        self. frequency = frequency

