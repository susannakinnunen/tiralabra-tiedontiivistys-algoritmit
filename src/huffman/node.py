"""Node creating module"""

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
