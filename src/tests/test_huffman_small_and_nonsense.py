import unittest
import os
import heapq
from huffman_coding import HuffmanCoding
from tests.create_test_file import FileForTesting

with open(os.path.join(os.getcwd(), "test_small.txt"), "w") as test_file:
    test_file.write("AAABBC") # Creates a very small test file



class TestHuffmanCodingSmallFiles(unittest.TestCase):
    def setUp(self):
        # testing with short strings and small files
        self.path_small = os.path.join(os.getcwd(), "test_small.txt")
        self.huffman_small = HuffmanCoding(self.path_small, "test")


        FileForTesting() # Creates a bit bigger test_file.txt
        self.path_big_nonsense = os.path.join(os.getcwd(), "test_big_nonsense.txt")
        self.huffman_big_nonsense = HuffmanCoding(self.path_big_nonsense, "test")

#From here tests are done with the big nonsense file.
    def test_frequency_table(self):
        """Test create_frequency_table method"""
        frequence_table = self.huffman_big_nonsense.create_frequence_table()
        self.assertEqual(frequence_table, {"a":30000, "B":15000, "c":857000, "d":765432, "e":456777, "Ä":68, "å":73, '"':3, "(":1, " ":20034, "\n":100, "&":778276, "{":81})

    def test_create_minimum_heap(self):
        "Test if create_mimum_heap works as expected"
        self.huffman_big_nonsense.create_frequence_table()
        self.huffman_big_nonsense.create_minimum_heap()
        self.assertEqual(str(heapq.heappop(self.huffman_big_nonsense.heap)), "(:1")
        self.assertEqual(str(heapq.heappop(self.huffman_big_nonsense.heap)), '":3')
        self.assertEqual(str(heapq.heappop(self.huffman_big_nonsense.heap)), "Ä:68")


    def test_create_a_merged_node(self):
        self.huffman_big_nonsense.create_frequence_table()
        self.huffman_big_nonsense.create_minimum_heap()
        merged_node = self.huffman_big_nonsense.create_merged_node()

        self.assertEqual(str(merged_node), "None:4")

    def test_create_huffman_tree(self):
        """This test ensures that there is only one node left in the
        huffman tree with the sum of all the nodes"""
        self.huffman_big_nonsense.create_frequence_table()
        self.huffman_big_nonsense.create_minimum_heap()
        huffman_tree = self.huffman_big_nonsense.create_huffman_tree()

        self.assertEqual(str(huffman_tree), "[None:2922845]")
      
#From here tests are done with a very short strings (very small files).
    def test_create_codes(self):
        """This test ensures that the characters 
        get correct codes according to their frequency."""
        self.huffman_small.create_frequence_table()
        self.huffman_small.create_minimum_heap()
        self.huffman_small.create_huffman_tree()

        codes = self.huffman_small.create_codes()

        self.assertEqual(str(codes), "{'A': '0', 'C': '10', 'B': '11'}")

    def test_create_encoded_string(self):
        """Tests if the create_encoded_string_function works as expected."""
        self.huffman_small.create_frequence_table()
        self.huffman_small.create_minimum_heap()
        self.huffman_small.create_huffman_tree()
        self.huffman_small.create_codes()
        encoded_string = self.huffman_small.create_encoded_string()

        self.assertEqual(str(encoded_string), "000111110")
    
    def test_binary_file_length_and_correctness(self):
        """At the moment tests if the function returns a file of whose lenght is divisible by 8. Also tests if the returned binary string is correct."""
        self.huffman_small.create_frequence_table()
        self.huffman_small.create_minimum_heap()
        self.huffman_small.create_huffman_tree()
        self.huffman_small.create_codes()
        encoded_string = self.huffman_small.create_encoded_string()
        binary_string = self.huffman_small.write_remaining_bits(encoded_string)
        divisible_by_eight = len(binary_string) % 8
        
        self.assertEqual(str(divisible_by_eight), "0")
        self.assertEqual(str(binary_string),"000001110001111100000000")
  
    def test_remove_filling_bits(self):
        self.huffman_small.create_frequence_table()
        self.huffman_small.create_minimum_heap()
        self.huffman_small.create_huffman_tree()
        self.huffman_small.create_codes()
        binary_string_before_compression = self.huffman_small.create_encoded_string()
        binary_string_after_compression_filling = self.huffman_small.get_binary_string_from_compressed_file()

        binary_string_after_compression_no_filling = self.huffman_small.remove_filling_bits(binary_string_after_compression_filling)

        self.assertEqual(binary_string_after_compression_no_filling, binary_string_before_compression)

    def test_decode_string(self):
        self.huffman_small.compress()
        
        binary_string_after_compression_filling = self.huffman_small.get_binary_string_from_compressed_file()
        binary_string_after_compression_no_filling = self.huffman_small.remove_filling_bits(binary_string_after_compression_filling)
        string = self.huffman_small.decode_string(binary_string_after_compression_no_filling)

        self.assertEqual(string, "AAABBC")

