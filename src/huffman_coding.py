""" File compressing and decompressing algorithm"""
import heapq # provides priority queue algorithms
#import os needed when debugging

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
        if string is None:
            string = self.string
        for character in string:
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
        The merged node becomes the parent of the merged nodes"""
        smallest_node = heapq.heappop(self.heap)
        second_smallest_node = heapq.heappop(self.heap)

        merged_node = Node(
            None,
            smallest_node.frequency + second_smallest_node.frequency
            )
        merged_node.left = smallest_node
        merged_node.right = second_smallest_node

        return merged_node


    def encode(self):
        """Assigns codes, 0's and 1's, to the nodes in the Huffman tree.
        The codes are then used to write a compressed file."""

class Node:
    """Nodes for the minimum heap
    """
    def __init__(self, character, frequency):
        self.character = character
        self. frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __repr__(self):
        return f"{self.character}:{self.frequency}"

#"""
#For debugging:
#if __name__ == "__main__":
    #string = "AAABBC"
    #with open(os.path.join(os.getcwd(), "temporary.txt"), "w") as test_file:
        #test_file.write("AAABBC")
    #path = os.path.join(os.getcwd(), "temporary.txt")
    #huffman = HuffmanCoding(path)
    #huffman.create_frequence_table(string)
    #huffman.create_minimum_heap()
   #print(huffman.create_huffman_tree())
#"""
