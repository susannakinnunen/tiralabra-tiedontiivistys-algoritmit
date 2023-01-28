"""
    File compressing and decompressing algorithm
"""
class LZ77:
    """
    File compressing and decompressing algorithm
    """
    def __init__(self):
        """A search window is the list of already seen characters from
        where we are looking for matches for the the characters
        in the look-ahead window. The integers assigned for the variables are
        lengths of the windows in bits. These can be changed later,
        the fixed lengths are just for
        the start of the development project."""
        self.search_window = 1024
        self.lookahead_window = 16


    def get_string_from_file(self, path):
        """Gets a path to a file as a parameter and
        returns a string of the file content"""
        with open(path, "r", encoding="utf-8") as file:
            string = file.read()
            string = string.strip()

        return string

    def search_longest_match(self):
        """Finds the longest match in the search_window for
        the next character(s) in the lookahead_window.
        Returns a triplet (distance, length, character).
        d = The distance to the start of the match,
        l = the lenght of the match,
        c = the next character in the lookahead table that was not
        matched in the search windows."""

    def compress(self):
        """Creates a compressed file. Matching charcter(s) is written
        in the compressed file in the form of information about
        the distance to the start of the match and the lenght of the match"""
