import unittest
import os
from huffman_coding import HuffmanCoding
import heapq

with open(os.path.join(os.getcwd(), "test.txt"), "w") as test_file:
    test_file.write("Test text: \n12368")

class TestHuffmanCoding(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join(os.getcwd(), "test.txt")
        self.huffman_coding = HuffmanCoding(self.path)

    def test_frequency_table(self):
        """Test create_frequency_table method"""
        string = "AABC"
        frequence_table = self.huffman_coding.create_frequence_table(string)
        self.assertEqual(frequence_table, {"A":2, "B":1, "C":1})

    def test_get_string_from_file(self):
        """Test get_string_from_file method""" 
        string = self.huffman_coding.get_string_from_file(self.path)

        self.assertEqual(string, "Test text: \n12368")

    def test_create_minimum_heap(self):
        "Test if create_mimum_heap works as expected"
        string = "AAABBC"
        self.huffman_coding.create_frequence_table(string)
        self.huffman_coding.create_minimum_heap()
        
        self.assertEqual(str(heapq.heappop(self.huffman_coding.heap)), "C:1")
        self.assertEqual(str(heapq.heappop(self.huffman_coding.heap)), "B:2")
        self.assertEqual(str(heapq.heappop(self.huffman_coding.heap)), "A:3")

    def test_create_a_merged_node(self):
        string = "AAABBC"
        self.huffman_coding.create_frequence_table(string)
        self.huffman_coding.create_minimum_heap()
        merged_node = self.huffman_coding.create_merged_node()

        self.assertEqual(str(merged_node), "None:3")

    def test_create_huffman_tree(self):
        """This test ensures that there is only one node left in the
        huffman tree with the sum of all the nodes"""
        string = "AAABBC"
        self.huffman_coding.create_frequence_table(string)
        self.huffman_coding.create_minimum_heap()
        huffman_tree = self.huffman_coding.create_huffman_tree()

        self.assertEqual(str(huffman_tree), "[None:6]")

    def test_create_codes(self):
        """This test ensures that the characters 
        get correct codes according to their frequency."""
        string = "AAABBC"
        self.huffman_coding.create_frequence_table(string)
        self.huffman_coding.create_minimum_heap()
        self.huffman_coding.create_huffman_tree()

        codes = self.huffman_coding.create_codes()

        self.assertEqual(str(codes), "{'A': '0', 'C': '10', 'B': '11'}")
