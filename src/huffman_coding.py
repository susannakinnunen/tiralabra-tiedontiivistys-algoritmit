class HuffmanCoding:
    def __init__(self):
        self.frequence_table = {}

    def create_frequence_table(self, string):
        """Creates a frequence table for the characters in a string/text"""
        for character in string:
            if not character in self.frequence_table:
                self.frequence_table[character] = 0
            self.frequence_table[character] += 1
        return self.frequence_table