"""Parent class for other codes.
Read class docstring for more information."""

class HuffmanCodingInitial:#pylint:disable=too-few-public-methods
    """This class is inherited by HuffmanCodingCompressor and
    HuffmanCodingDecompressor by inheriting HuffmanCodingCompressor.
    Has the needed common attributes for both subclasses."""
    def __init__(self):
        self.character_codes = {} # Key: character, value: binarycode
        self.reversed_charcter_codes = {} # Key:binarycode, value:character
        self.frequence_table = {}
