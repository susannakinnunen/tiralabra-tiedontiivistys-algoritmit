class LZ77:
    """File compressing algorithm"""
    
    def __init__(self):
        """A search window is the list of already seen characters from 
        where we are looking for matches for the the characters
        in the look-ahead window. The integers assigned for the variables are 
        lengths of the windows in bits. These can be changed later, the fixed lengths are just for 
        the start of the development project."""
        self.search_window = 1024
        self.lookahead_window = 16

        

