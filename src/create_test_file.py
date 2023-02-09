from random import sample

class FileForTesting:
    def __init__(self):
        self.string = ""
        self.a = "a"
        self.B = "B"
        self.c = "c"
        self.d = "d"
        self.e = "e"
        self.F = "F"
        self.g = "g"
        self.h = "h"
        self.i = "i"
        self.J = "J"
        self.k = "k"
        self.l = "l"
        self.m = "m"
        self.n = "n"
        self.O = "O"
        self.w = "w"
        self.Ä = "Ä"
        self.å = "å"
        self.quotation_mark = '"'
        self.parenthesis = "("
        self.space = " "
        self.new_line = '\n'
        self.et = "&"
        self.curlybracket = "{"

        self.generate_string()
        self.generate_file()

    def generate_string(self):
        self.a = self.a * 30000
        self.B = self.B * 15000
        self.c = self.c * 857000
        self.d = self.d * 765432
        self.e = self.e * 456777
        self.F = self.F * 6762
        self.g = self.g * 95463
        self.Ä = self.Ä * 68
        self.å = self.å * 73
        self.quotation_mark = self.quotation_mark * 3
        self.parenthesis = self.parenthesis * 1
        self.space = self.space * 20034
        self.new_line = self.new_line * 100
        self.et = self.et * 778276
        self.curlybracket = self.curlybracket * 81

        self.string = str(self.a) + str(self.B) + str(self.c) + str(self.d) + str(self.e) + str(self.Ä) + str(self.å) + str(self.quotation_mark) + str(self.parenthesis) + str(self.space) + str(self.new_line) + str(self.et) + str(self.curlybracket)
        self.string = ''.join(sample(self.string, len(self.string)))
        return self.string

    def generate_file(self):
        with open("test_file.txt", "w", encoding="utf-8") as testfile:
            testfile.write(self.string)
   
        return testfile
       
"""
if __name__ == "__main__":
    testi_tiedosto = TestFile()
    testi_tiedosto.generate_string()
    a = testi_tiedosto.generate_file()
    print(a)

        self.h = 
        self.i = 
        self.J = 
        self.k = 
        self.l = 
        self.m = 
        self.n = 
        self.O = 
        self.w = 
    """