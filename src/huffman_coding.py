class HuffmanCoding:
    """File compressing algorithm"""
    def __init__(self):
        self.frequence_table = {}
    
    def get_string_from_file(self, path):
        """Gets a path to a file as a parameter and returns a string of the file content"""
        with open(path, "r") as file:
            string = file.read()
            string = string.strip()

        return string

    def create_frequence_table(self, string):
        """Creates a frequence table for the characters in a string/text"""
        for character in string:
            if not character in self.frequence_table:
                self.frequence_table[character] = 0
            self.frequence_table[character] += 1
        return self.frequence_table

    def create_minimum_heap(self):
        """Creates a minimum_heap"""
        pass

    def create_huffman_tree(self):
        """Creates a Huffman tree"""
        pass