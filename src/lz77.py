"""
    File compressing and decompressing algorithm based on LZ77 algorithm
"""

import os

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
            self.decompress()


    def get_string_from_file(self, path):
        """Gets a path to a file as a parameter and
        returns a string of the file content"""
        with open(path, "r", encoding="utf-8") as file:
            string = file.read()

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

        Character is given fifteen bits if there wasn't a match.
        If there was a match, character is given 7 bits.

        If distance is equal to 0,
        only the character is added to the bit string with 15 bits.
        """

        bit_string = ""

        for element in list_of_tuples:
            distance, length, character = element
            if distance == 0:
                # if distance == 0,
                # it means the character did not have a match
                # --> bitstring will start with "0"
                bit_string = bit_string + "0" + str(bin(ord(character)))[2:].zfill(15)#pylint:disable=line-too-long
                # [2:] <- when converting to bits python adds 0b in front,
                # so that needs to be ignored
            else:
                # character had a match and
                # the following bit string starts with "1",
                # to distinguish from a non-match.
                bit_string = bit_string + "1" \
                + str(bin(distance))[2:].zfill(12) \
                + str(bin(length))[2:].zfill(4) \
                + str(bin(character))[2:].zfill(7)

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

    def decompress(self):
        """Calls for all the methods needed for decompressing a binaryfile."""
        # 1 .read and save binary file in the given path
        binary_string = self.get_binary_string_from_compressed_file()
        # 2. decode the string
        decoded_string = self.decode_bit_string(binary_string)
        # 3. save the decoded string
        decompressed_file = self.create_decompressed_file(decoded_string)

        return decompressed_file

    def get_binary_string_from_compressed_file(self):
        """Fetches a binary string from the compressed file"""
        # 1 .read binary file in the given path
        binary_string = ""
        with open(os.path.join(
            os.getcwd(), "lz77_compressed.bin"), "rb"
            ) as file:
            row_from_file = file.read(1)
            while len(row_from_file) > 0:
                row_from_file = ord(row_from_file)
                bits = bin(row_from_file)[2:].rjust(8, "0")
                binary_string += bits
                row_from_file = file.read(1)
        return binary_string

    def decode_bit_string(self, binary_string):
        """Decodes bitstring into characters"""
        tuples_list = self.get_tuples(binary_string)

        decompressed_string = ""
        for element in tuples_list:
            distance, length, character = element
            if distance == 0:
                decompressed_string += character
            else:
                matching_characters = decompressed_string[-(distance):]
                matching_characters = matching_characters[:length]
                decompressed_string += matching_characters

        return decompressed_string

    def get_tuples(self, binary_string):
        """Creates a list of (distance, length, character)
        tuples from the binarystring"""
        self.compressed_info_list = []
        i = 0
        while i < len(binary_string) - 1:
            short_string = binary_string[i+1:i+16]
            # Short string is a seven bits long string
            # cut from the binary string
            if binary_string[i] == "0":
            # if binary_string[i] == "0", it means this character
            # did not have a match
            # to understand better see function convert_into_bit_string
                distance = 0
                length = 1
                character_int = int(short_string, 2)
                # short_string is converted into an integer
                # which works as Unicode code integer
                character = chr(character_int)
                # chr() returns a character from the code integer
                i += 16
                # a bitstring with
                # no match is 16 bits long altogether with the first bit "0"
                # in the beginning, thus we can now move 16 bits forward in
                # the binary_string
                self.compressed_info_list.append((distance, length, character))
            else:
                # this means binary_string[i] == "1"
                # thus there's distance and length in
                # the following 24 bits
                # distance has 12 bits, length 4 and
                # character has 8 zeros to signal the charcter(s) is found
                # with the help of distance and length
                # (in the decode_bit_string function)
                distance = int(binary_string[i+1:i+13], 2)
                length = int(binary_string[i+13:i+17], 2)
                character = ""
                i += 24
                self.compressed_info_list.append((distance, length, character))
        return self.compressed_info_list

    def create_decompressed_file(self, decoded_string):
        """Writes the decoded string into lz77_decompressed.txt file."""
        with open(
            "lz77_decompressed.txt", "w", encoding="utf-8"
            )as decompressed_file:
            decompressed_file.write(decoded_string)

        return decompressed_file
