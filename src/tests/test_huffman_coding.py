import unittest
import os
from huffman_coding import HuffmanCoding
import heapq
from create_test_file import FileForTesting

with open(os.path.join(os.getcwd(), "test.txt"), "w") as test_file:
    test_file.write("Test text: \n12368")

class TestHuffmanCoding(unittest.TestCase):
    def setUp(self):

        # testing with short strings and small files (insuficcient)
        self.path = os.path.join(os.getcwd(), "test.txt")
        self.huffman_coding = HuffmanCoding(self.path, "test")
        
        ## testing with bigger files
        FileForTesting() # Creates test_file.txt
        path = os.path.join(os.getcwd(), "test_file.txt")
        self.huffman = HuffmanCoding(path, "test")

    def test_frequency_table(self):
        """Test create_frequency_table method"""
        frequence_table = self.huffman.create_frequence_table()
        self.assertEqual(frequence_table, {"a":30000, "B":15000, "c":857000, "d":765432, "e":456777, "Ä":68, "å":73, '"':3, "(":1, " ":20034, "\n":100, "&":778276, "{":81})
   
    def test_create_minimum_heap(self):
        "Test if create_mimum_heap works as expected"
        self.huffman.create_frequence_table()
        minimumheap = self.huffman.create_minimum_heap()
        print(minimumheap)
        self.assertEqual(str(heapq.heappop(self.huffman.heap)), "(:1")
        self.assertEqual(str(heapq.heappop(self.huffman.heap)), '":3')
        self.assertEqual(str(heapq.heappop(self.huffman.heap)), "Ä:68")


    def test_create_a_merged_node(self):
        self.huffman.create_frequence_table()
        self.huffman.create_minimum_heap()
        merged_node = self.huffman.create_merged_node()

        self.assertEqual(str(merged_node), "None:4")

    def test_create_huffman_tree(self):
        """This test ensures that there is only one node left in the
        huffman tree with the sum of all the nodes"""
        self.huffman.create_frequence_table()
        self.huffman.create_minimum_heap()
        huffman_tree = self.huffman.create_huffman_tree()

        self.assertEqual(str(huffman_tree), "[None:2922845]")

    def test_get_binary_string_from_file(self):
        self.huffman_coding.compress()

        self.huffman_coding.create_frequence_table()
        self.huffman_coding.create_minimum_heap()
        self.huffman_coding.create_huffman_tree()
        self.huffman_coding.create_codes()
        binary_string_before_compression = self.huffman_coding.create_encoded_string()
        binary_string_before_compression = self.huffman_coding.write_remaining_bits(binary_string_before_compression)
        binary_string_after_compression = self.huffman_coding.get_binary_string_from_compressed_file()
        self.assertEqual(binary_string_after_compression, binary_string_before_compression)
    
    def test_remove_filling_bits(self):
        self.huffman_coding.create_frequence_table()
        self.huffman_coding.create_minimum_heap()
        self.huffman_coding.create_huffman_tree()
        self.huffman_coding.create_codes()
        binary_string_before_compression = self.huffman_coding.create_encoded_string()
        binary_string_after_compression_filling = self.huffman_coding.get_binary_string_from_compressed_file()

        binary_string_after_compression_no_filling = self.huffman_coding.remove_filling_bits(binary_string_after_compression_filling)

        self.assertEqual(binary_string_after_compression_no_filling, binary_string_before_compression)

    def test_decode_string(self):
        self.huffman_coding.compress()
        
        binary_string_after_compression_filling = self.huffman_coding.get_binary_string_from_compressed_file()
        binary_string_after_compression_no_filling = self.huffman_coding.remove_filling_bits(binary_string_after_compression_filling)
        string = self.huffman_coding.decode_string(binary_string_after_compression_no_filling)

        self.assertEqual(string, "Test text: \n12368")
"""
    def test_create_codes(self):
        """"""This test ensures that the characters 
        get correct codes according to their frequency.""""""
        string = "AAABBC"
        self.huffman_coding.create_frequence_table(string)
        self.huffman_coding.create_minimum_heap()
        self.huffman_coding.create_huffman_tree()

        codes = self.huffman_coding.create_codes()

        self.assertEqual(str(codes), "{'A': '0', 'C': '10', 'B': '11'}")

    def test_create_encoded_string(self):
        """"""Tests if the create_encoded_string_function works as expected.""""""
        string = "AAABBC"
        self.huffman_coding.create_frequence_table(string)
        self.huffman_coding.create_minimum_heap()
        self.huffman_coding.create_huffman_tree()
        self.huffman_coding.create_codes()
        encoded_string = self.huffman_coding.create_encoded_string()

        self.assertEqual(str(encoded_string), "000111110")

    def test_binary_file_length_and_correctness(self):
        """"""At the moment tests if the function returns a file of whose lenght is divisible by 8. Also tests if the returned binary string is correct.""""""""
        string = "AAABBC"
        self.huffman_coding.create_frequence_table(string)
        self.huffman_coding.create_minimum_heap()
        self.huffman_coding.create_huffman_tree()
        self.huffman_coding.create_codes()
        encoded_string = self.huffman_coding.create_encoded_string()
        binary_string = self.huffman_coding.write_remaining_bits(encoded_string)
        divisible_by_eight = len(binary_string) % 8
        
        self.assertEqual(str(divisible_by_eight), "0")

        self.assertEqual(str(binary_string),"000001110001111100000000")

    def test_binary_file_length_if_string_divisible_by_8(self):
        string = "ABCD"
        self.huffman_coding.create_frequence_table(string)
        self.huffman_coding.create_minimum_heap()
        self.huffman_coding.create_huffman_tree()
        self.huffman_coding.create_codes()
        encoded_string = self.huffman_coding.create_encoded_string()
        binary_string = self.huffman_coding.write_remaining_bits(encoded_string)
        divisible_by_eight = len(binary_string) % 8
        
        self.assertEqual(str(divisible_by_eight), "0")

        self.assertEqual(str(binary_string),"0000000000100111")

    def test_create_byte_list(self):
        """"""Tests if the byte list created is correct""""""
        path = os.path.join(os.getcwd(), "loremipsum.txt")
        string = self.huffman_coding.get_string_from_file(path)
        self.huffman_coding.create_frequence_table(string)
        self.huffman_coding.create_minimum_heap()
        self.huffman_coding.create_huffman_tree()
        self.huffman_coding.create_codes()
        encoded_string = self.huffman_coding.create_encoded_string()
        binary_string = self.huffman_coding.write_remaining_bits(encoded_string)
        byte_list = self.huffman_coding.create_byte_list(binary_string)

        self.assertEqual(byte_list, bytearray(b'\x05k\xa2\xbf\xcc[y\xe6dB+\x9c\xde\xae}\xb5\xfd\x08\x8b\xfc/\xeeWS\x0be\xe0E\x1d\xe0m\xaf\xe7\xf6fGy\x97\xe4Y\xaf\xf8\xdcW\x11\x81ad\x8d\xe9\xbc\x14\x84W\xf7\xdedB+\xfb\x94\x88\xd6\xa0)Mw\x9a\xd5\xe6\xe2\xb7f\xe2\xb8>:\xb3\rs<@\x0c\r\xcb\x08\xf7\xba\xa0R\x9a\xe6\x9b\xcd\xc5n\xcd\xc5p|uf\x1a\xe6x\x80\x18\x1b\x96\x11\xd7\xfcn+\x8b;\xcd"\xe1\x9e^\x05\xb3z\x98[/\x02(\xe4\n\x1e,\x9eo{\xd2\x16\xa6\x07\xdf\xbc\xd6\x94kB"\xc3\xcf\x1b\x9enU\xd9|\xdf\x80x\xdf\xbaS\xf8\xb3\tC\xaf\\V\xe2\xb8\xb3\xbd\xd4\xec1\xd7\xfcn+\xa2\xb09\x94\xd9B_HZ\x98{\xe28\xd4$\x0b\xe1\x91\x87y\xa5 \x15\x9b\xeb\xa5\xfbZ\xcc5\xcc\xe6\xf5s\xef\tp\xcf/\x02\xd9\xbdL-\x97\x81\x14{\xcdS\xbd\x1f\xbd\xca\x95/\x9b\xeb\xa5\xfbZ\xdfzB\xd4\xc3\xdf\x0f\xa5?\xa2\xa3K\xfd\xe6\x95sP\x14\xa6\xb9\x9f\xf9\xbe\xf5\xc5n+\xa1\x11\x7fJj\xf1gy\xa9%\xf9\x16`\xa8\x115\xaa\xf2R_)y|\xfe\xcc\x9c\x83su\x7f\xa2\xc3\x1d7\xdek\xd1[\x8a\xe6\xe2\xf3\xeb\xfa\xa1\xa6\xf4"/\xe9M_{\xaa\xb0\x9d\xd3\xe0_ P\xf1d\xf3M\xebR\xf6R\x9f\xdf}\xe6\xa2?xda\x9e\x1e\x1e\xa5\xd2\x9f\xc9\x94\xfdV\xb7*T\xbe#\xa8\nS\\\xcf\xfc\xdd*E\x12\x01]\xee\x8f\xd7\x11\x84\xbe\xf7\xbc\xdf\x80x\xdf\xbaS\xfb\xc0\xde\x90\n\xe4"\xad\xfa\xe6\x14D\xbb\x9eh->\xb20,\x91\xbe\xf3C\xfc\xc3 \x15\x9b\xeb\xa5\xfbZ\xcc5\xcc\xe6\xf5s\xef\tp\xcf/\x02\xd9\xbdL-\x97\x81\x14{\xcd/\xb9}\xf7\xb9A\xef4\xca\xdd5\xcf}P\xd7*\xd9~\xf7Q\x11\xf8o\x13\xcc\xc3\\\xc9\xc877W\xfao7\xd7K\xf6\xb5\x9c\xde\xae}\xf7\xd0\xe8u%\xa4\xcb+%%\xf2\x01B\xc3z\xe5[/\xa1*\xf2\xf8\x8e\xeb\xa8n\xba@\xdd;\xfel*\xfe\xbb\xcd\x04\x97J\x7fz>\xf7O\x98k\x98\x8e\xa5\x84\xe8J\xbc\xbfy\xa8\x06\xf3~\x01\xe3~\xe9O\xee\xba@\xdd\r\xeeEP:\xd4\xbd\x94\xa7\xf3\xf8\xfc._}\xe1\xfb\x97\xef5\x950(K\xe7\x87\x87\xa9t\xa7\xf7\x87\x9e\x9f\x16fD~\x19\xb5\xfb3\xcc\x9c\x83su\x7f\xdeh}\x98>\x17/\x93\xf7\xb2\x84\x84\xf3r\xae\xcb\xe9\x00\xaeB*\xdf\xaeO\xc0\xde\x7ff\x90\n\xe4"\xad\xfa\xeeEP=\xee\xaf>\xf7)\xde\xb2f\xeb\xf5\xc5n+\xa1\x11a\xe7\x8d\xcf0T\x08\x9a\xc9I~\xf7G\xeb\x88\xc2_2!\x15\xcd\xca\xcb\xe1\x88\xef\x13\xcc\xda\xd7\xbf\x8d\xef\x0f\xe7\x8d\xcf7M@\x81r\xf8>=\xe6\x8d\x9a\x12\xaf/\xb9\xf7/\xa8\nS\\\xde\x1ez|Y\xde\xe8\x97\xec\xcf7L\xbc?\x16d\xfc\r\xe9\xbdq[\x8a\xe6\xd7\xec\xcf2e?U\xac\xf2\xed\xf8\xb0\xbb\xfen7\xe3g\xbc\xd6\xc2\x85\x86\xf5\x01Jk\x9b\xec\xd77\xad^O\xc0\xdexxz\x97J\x7f\x11\xcc0\xb9\xe7y\xab\x10\x02\xfa\x80\xa55\xcd7\x9b\x8a\xdd\x9b\x8a\xe0\xf8\xea\xcc5\xcc\xf1\x0007,#\xdek\xde\x01/\x88\xee\xba\x86\xeb\xa4\r\xd3\xbf\xe6\xc2\xaf\xeb0\xc2\xe7\x8f}\xf4:\r\x04\xd72r\r\xcd\xd5\xfeaDK\xb9\xe6yv\xfcX]\xff\x11\xde\xf7\xa8o\xf1\x1c%\x0e\xbd\xca\x95/\xde\xe8\x97\xec\xcf0|._%5\xccY\x83\xe3\x88\xf7\xba\xbc\xfb\xca^_\x0c\x80W7\xa3\xf7\xba|\x0b\xefG\xef\x0c\x8c;\xcdX\xaa\x07Y\x18\x16H\xde\x8a\x8d/\xeeS\xbdoG\xefz>\xf7O\x9b\x95\x97\xef4\xa4\x02\xb9\xbd\x1f\xbd\xd3\xe0_z?xda\x82(El\xbe\xe5]\x97\xd4\x05)\xaen\x9a\x98\x14%\xfb\xcd\x14y\xc8\xb2;\xc0\xde\xab\xc7\x8d\xfa\xb0\xfd\xe6I\xef5b\xa8\x1c1\x1dK\t\xca^_%%\xf2t\xa6_%5\xcc\x94\x97J\x7f\xbc\xd0I}\x08\xf3\x91dtXc\xab\xc7\xe8s\xfb50\xb6^\x04Q\xcc5\xce\xf3Q\x1f{\xa7\xcc\x93\x8b4Ti\x7fR\xc2tXc\xdek>Q5x\x8e\xa1\xbf\xdc\xfb\x97\xcc0\xb9\xe6\xab\xd7\xfcn+\xa1\x1er,\x8e\x90\n\xe4"\xad\xfa\xea\xefue\x19\xfc>\x94\xfeEi2\xca\xc4wO\xaf<ny\xbe\xf3\xc4\x00\xc0\xdc\xb0\x8e\xa8h\xac\x0eo\xae\x9f\xc0%\xfb\xcd\x18\xdf\xa3\xeb\xb9A\xef4\xca\xc3#\x0c\x9f\x86R\xf2\xfa\x11\xe7"\xc8\xe4\xca~\xab[\x95\xf0\xf1\xa7\xd5\x08O\x1e\x87\x05B_\xbc\xd3)\xfa\xada\xae`(z\xc7td\xbd\xc7\x05E\x7f\xef9\xbd\\\xfb\xd0\x95y|\xe6\xf5s\xef\xbd\xd4I\xc9\x94\xeb\x92\xfa\x96\x13\xba|\x0b\xe4\n\x1e,\x9ei\xbdj^\xcaS\xfb\xef\xbc\xd4\xbc?r\xfb\xefr\x83\xdei\x95\xbak\x9e\xfa\xa1\xaeU\xb2\xfd\xe6\xba+\xfc\xcf\xec\xca^_HZ\x98\x1f}j^\xcaS\xfd\xe6\x89i\xf3r\t\x91\xa5\xdc\xab\xb2\xf8da\x9f\xd9\x90\n\x16\x1b\xc0P\xf5\x8eN!6\xdd^\x7fg{\xa8\x92\xfa\xd4\xbd\x94\xa7\xf3\xc4\x00\xc0\xdc\xb0\x8e\x12\x87^sz\xb9\xf7\xa1\x1er,\x8f}\x0e\x87F\xf8\xb1}M\xe6D"\xbb\x94\x88\xd6\xf4~\xf7\xbd\xf7\xba\x83\\\xcc\x88\xfc50\xb6^\x04Q\xd6\xa5\xec\xa5?\x94\xbc\xbe\x1f\x86\xe9\xf9D\xd5\xe2=\xee\xac5\xc5n+\x98Q\x12\xeey\xa1\x11N\x80\x0b\xea\xf1\xfa\x1d\xf7\xae+q]W\x94\xbc\xbf{\xab\r\x16\x18\xeb\xfe7\x15\xd1X\x1c\xcal\xa1/\xa4-L=\xf1\x1cj\x12\x05\xfb\xddM/q\xc1Q_\xfb\xceoW>\xf4%^_\xbd\xd5\xbd*5\xa1\x11a\xe7\x8d\xcf7*\xec\xbeo\xc0<o\xdd)\xfe\xf3[\n\x16\x1b\xc9\xc4&\xdb\xab\xdc\xaf\x87\x8d>N!6\xdd^@(XoP\x14\xa6\xb9\xbe\xcdsz\xd5\xe4\xfc\r\xe7\x87\x87\xa9t\xa7\xfb\xcd\x12\xd3\xe6\xe4\x13#K\xb9We\xf0\xc8\xc3?\xb3 \x14,7\x80\xa1\xeb\x1c\x9cBm\xba\xbe\xf3L\xa7\xea\xb5\xb9R\xa5\xf1\x1d@R\x9a\xe6\x7f\xe7y\xa3\x1d~\x01/\x88\xdf\xa3\xeb\xba~Q5y\xe1\xe1\xea])\xfc\x9d)\x97\xdc\x8a\xa0{\xcdX\x80\x17\xc3#\x0c\xfe\xccY\x9f\xf8\xdf\xafy\xae\xa8\xaf\xfd\xe1\x88\xe8J\xd2\x06\xe5r+I\x96V\xa5\x84\xea\x86\xb8\xad\xc5s\n"]\xcf4")\xd0\x01}^?C\xdek\xa2\x84V\xcb\xee\x9f\x94M^L\xa7\\\x97\xd5z\xa5\x19\xfd\xe8\xfd\xeaXNa\x85\xcf2t\xa6_2K\xf7\xba\xab\t\xd0\x95y|\x99\xba\xfd\x08\x8a3\xfb\x95*_/\\F\x12\xfa\xbc~\x87\'\xe1\xbc\r\xe7\x87\x87\xa9t\xa7\xfb\xe8t:/\x00\xf1\xbft\xa7\xf0\xfc0\xd75\x01Jk\x99\xff\x9b\xef\xbc\xd4G\xef2!\x15\xdc\x8a\xa0p\xc4u,\')y|\x94\x97\xc9\xd2\x99|\x94\xd72R])\xfe\xf7W\xc7\xe8w\xde\xb8\xad\xc5u^R\xf2\xf92\x9f\xaa\xd6\xa6\x16\xcb\xc0\x8a:\xaf\xbc\xd0\x9b\xd5\xcf\xbd\xefy\xb0\xa8z\xd5\xe2=\xe6\xadJ\x97\xd5(\xcf\xe1\xf4\xa7\xf2+I\x96V#\xba}y\xe3s\xcd\xf7\xde\xeaKI\x96V\xa5\x84\xea\x86\xb8\xad\xc5s\n"]\xcf4")\xd0\x01}^?C\xbe\xf5\xc5n+\xdei\x94\xeb\x92\xfa\x96\x13\xba|\x0b\xe4\n\x1e,\x9ei\xbdj^\xcaS\xfd\xee\xa7a\x8e\xf9\xdd?(\x9a\xbc\xda\xfd\x99\xe6\x12\x87^-\xbc\xf3B"\xfe\x94\xd5\xe1.\x19?\x0e\xf7E\xd7K\xf6\xb5\xbe\xf4\x85\xa9\x87\xbe\x1fJ\x7fEF\x97\xfb\xcd9\x06\xe6\xea\xff0\xa2%\xdc\xf3<\xbb~,.\xff\x88\xef{\xd47\xf8\x8e\x12\x87^\xe5J\x97\xd0\x95y~\xf3H\xb8k#\x02\xc9\x1b\xde\x8f\xde\x19\x00\xaea\x88\xe1.w\xbd\xe77\xdej\xcb\xeeT\xa9|\x99\xba\xfd!j`}\xf0|q\x1b\xf4}w(=\xe6\x99Xda\x93\xf0\xca^_\xbc\xd4\x9dr\xad\x97\xde\x8f\xbd\xd3\xe6\xd7\xec\xcf5x\xfd\x0eo\xae\x97\xedkr\x91\x1a\xd5\x0e\xf3L\xdd~\x19\x18g\xf6d\xfc\r\xe6\x14D\xbb\x9ew\x9a\xcf\x02\xfb\xd1\xfb\xc3#\x0c\x11B+e\xf7*\xec\xbe\xa0)Mst\xd4\xc0\xa1/\x9b\x95\x97\xef5\x950(K\xeb\x95l\xbe#\xbew\x0e@\xa1\xe2\xc9\xe7y\xa7\xefe\t\t\xe6^\xb8\x8c%\xf7\xbd\xe6\xfc\x03\xc6\xfd\xd2\x9f\xde\x06\xfb\xddP)Msr\x83\xdei\x95\x90(x\xb2y\xa9a93u\xfb\xc3\xf9\xe3s\xcd\tZ@\xdc\xaeL\xdd\x7f`'))

    def test_compressed_file_is_smaller(self):
        path = os.path.join(os.getcwd(), "loremipsum.txt")
        string = self.huffman_coding.get_string_from_file(path)
        self.huffman_coding.create_frequence_table(string)
        self.huffman_coding.create_minimum_heap()
        self.huffman_coding.create_huffman_tree()
        self.huffman_coding.create_codes()
        encoded_string = self.huffman_coding.create_encoded_string()
        self.huffman_coding.create_compressed_file(encoded_string)

        original_file_size = os.path.getsize(os.path.join(os.getcwd(), "loremipsum.txt"))
        compressed_file_size = os.path.getsize(os.path.join(os.getcwd(), "compressed.bin"))

        self.assertLess(compressed_file_size,original_file_size)
"""
