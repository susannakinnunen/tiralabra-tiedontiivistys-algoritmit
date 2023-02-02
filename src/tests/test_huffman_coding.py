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
    
    def test_frequency_table_where_string_None(self):
        string = None
        frequence_table = self.huffman_coding.create_frequence_table(string)
        self.assertEqual(
            frequence_table,
            {'T': 1, 'e': 2, 's': 1, 't': 3, ' ': 2, 'x': 1, ':': 1, '\n': 1, '1': 1, '2': 1, '3': 1, '6': 1, '8': 1}
            )

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

    def test_create_encoded_string(self):
        """Tests if the create_encoded_string_function works as expected."""
        string = "AAABBC"
        self.huffman_coding.create_frequence_table(string)
        self.huffman_coding.create_minimum_heap()
        self.huffman_coding.create_huffman_tree()
        self.huffman_coding.create_codes()
        encoded_string = self.huffman_coding.create_encoded_string(string)

        self.assertEqual(str(encoded_string), "000111110")

    def test_binary_file_length_and_correctness(self):
        """At the moment tests if the function returns a file of whose lenght is divisible by 8. Also tests if the returned binary string is correct."""
        string = "AAABBC"
        self.huffman_coding.create_frequence_table(string)
        self.huffman_coding.create_minimum_heap()
        self.huffman_coding.create_huffman_tree()
        self.huffman_coding.create_codes()
        encoded_string = self.huffman_coding.create_encoded_string(string)
        binary_string = self.huffman_coding.create_compressed_file(encoded_string)
        divisible_by_eight = len(binary_string) % 8
        
        self.assertEqual(str(divisible_by_eight), "0")

        self.assertEqual(str(binary_string),"000001110001111100000000")

    def test_binary_file_length_if_string_divisible_by_8(self):
        string = "ABCD"
        self.huffman_coding.create_frequence_table(string)
        self.huffman_coding.create_minimum_heap()
        self.huffman_coding.create_huffman_tree()
        self.huffman_coding.create_codes()
        encoded_string = self.huffman_coding.create_encoded_string(string)
        binary_string = self.huffman_coding.create_compressed_file(encoded_string)
        divisible_by_eight = len(binary_string) % 8
        
        self.assertEqual(str(divisible_by_eight), "0")

        self.assertEqual(str(binary_string),"0000000000100111")       
