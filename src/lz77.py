"""
    File compressing and decompressing algorithm
"""
class LZ77:
    """
    File compressing and decompressing algorithm
    """
    def __init__(self, path, test = False):
        """A search window is the list of already seen characters from
        where we are looking for matches for the the characters
        in the look-ahead window. The integers assigned for the variables are
        the sizes of the windows. This means, that there is
        4095 characters in the search_window and 15 in the lookahead_window.
        """
        self.search_window = 4095
        self.lookahead_window = 15
        self.path = path
        self.string = self.get_string_from_file(path)
        self.compressed_info_list = []
        # list containing information
        # about compressed characters and matches
        if test is False:
            self.compress()


    def get_string_from_file(self, path):
        """Gets a path to a file as a parameter and
        returns a string of the file content"""
        with open(path, "r", encoding="utf-8") as file:
            string = file.read()
            string = string.strip()

        return string

    def compress(self):
        """Goes through the to be compressed string and
        calls for all the methods needed for the string's compression.
        """
        i = 0
        while i < len(self.string):
            longest_match = self.search_longest_match(i)
            self.compressed_info_list.append(longest_match)
            i += longest_match[1]

        bit_string = self.convert_into_bit_string(self.compressed_info_list)
        byte_list = self.convert_into_bytes(bit_string)
        self.create_compressed_file(byte_list)

        return self.compressed_info_list
        # returns the list for testing purposes

    def search_longest_match(self, current_index):
        """Finds the longest match in the search_window for
        the characters in the lookahead_window.
        Returns a tuple = (d, l, c).
        d = The distance to the start of the match,
        l = the lenght of the match,
        c = the next character in the lookahead table that was not
        matched in the search windows."""
        match = (0,0,0)

        # here, start indexes for the search and lookahead windows are found
        # also the last index of the lookahead window
        search_window_start_index = max(0, current_index - self.search_window)
        start_index_of_lookahead = current_index
        last_index_of_lookahead = min(
                                    current_index + self.lookahead_window,
                                    len(self.string) + 1
                                    )


        for i in range(
            start_index_of_lookahead + 3, last_index_of_lookahead + 1):
            # We are looking for matches at least 3 characters long
            # that's why start_index_of_lookahead + 3 is done
            match_start_index = self.string[
                search_window_start_index:start_index_of_lookahead].rfind(
                self.string[start_index_of_lookahead:i]
                )
                #rfind returns the start index of the match
            if match_start_index != -1:
                #rfind() returns -1 if no matches were found
                match = (
                    start_index_of_lookahead -
                    (search_window_start_index + match_start_index),
                    min(i - start_index_of_lookahead,
                        len(self.string[start_index_of_lookahead:i])),
                    0
                    )
            else:
                break
        if match[1] == 0:
            match = (0,1, self.string[start_index_of_lookahead])

        return match

    def convert_into_bit_string(self, list_of_tuples):
        """This method converts the compressed information
        from the tuples (d, l, c) into a string of bits.

        Distance will be given 12 bits, because 2^12 = 4096
        and the size of the search window is 4095 characters.
        This means the match can be found from up to 4095 characters away.

        Length  will be given 4 bits, 2^4 = 16. The
        lookahead window is 15 characters, so the maximum
        match of 15 characters will fit in that amount.

        Character is given seven bits.

        If distance is equal to 0,
        only a next character is added to the bit string.
        """

        bit_string = ""

        for element in list_of_tuples:
            distance, length, character = element
            if distance == 0:
                bit_string = bit_string + "0" + str(bin(ord(character)))[2:].zfill(7)#pylint:disable=line-too-long
                # [2:] <- when converting to bits python adds 0b in front,
                # so that needs to be ignored
            else:
                bit_string = bit_string + "1" + str(bin(distance))[2:].zfill(12) + str(bin(length))[2:].zfill(4) + str(bin(character))[2:].zfill(7)#pylint:disable=line-too-long
                # didn't know how to divide those operations to separate rows,
                # that's why pylint-disable used

        return bit_string

    def convert_into_bytes(self, bit_string):
        """Creates a list of bytes from the bit_string
        """
        byte_list = bytearray()
        for i in range(0, len(bit_string), 8):
            byte = bit_string[i:i+8]
            byte_list.append(int(byte, 2))
        return byte_list

    def create_compressed_file(self, byte_list):
        """Writes the the compressed information to a .bin file"""
        with open("lz77_compressed.bin", "wb") as binary_file:
            binary_file.write(byte_list)

        return binary_file
