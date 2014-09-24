import sys

class Cipher(object):
    def __init__(self):
        self.key = ''
        self.value = ''
        self.message = ''
        self.cipherMapping = {}
        self.dupHashMap = {}
    def readIn(self):
        self.message = sys.stdin.readline().rstrip('\n')

    # removes duplicate characters from self.value, the string created from self.key by adding the alphabet
    def removeDups(self): 
        self.dupHashMap["A"] = False
        self.dupHashMap["B"] = False
        self.dupHashMap["C"] = False 
        self.dupHashMap["D"] = False
        self.dupHashMap["E"] = False
        self.dupHashMap["F"] = False
        self.dupHashMap["G"] = False
        self.dupHashMap["H"] = False
        self.dupHashMap["I"] = False
        self.dupHashMap["J"] = False
        self.dupHashMap["K"] = False
        self.dupHashMap["L"] = False
        self.dupHashMap["M"] = False
        self.dupHashMap["N"] = False
        self.dupHashMap["O"] = False
        self.dupHashMap["P"] = False
        self.dupHashMap["Q"] = False
        self.dupHashMap["R"] = False
        self.dupHashMap["S"] = False
        self.dupHashMap["T"] = False
        self.dupHashMap["U"] = False
        self.dupHashMap["V"] = False
        self.dupHashMap["W"] = False
        self.dupHashMap["X"] = False
        self.dupHashMap["Y"] = False
        self.dupHashMap["Z"] = False
        self.dupHashMap[" "] = False

        length = len(self.value)
        index = 0
        while index < length:
            val = self.value[index]
            if self.dupHashMap[val]:
                self.value = self.value[:index] + self.value[index+1:]
                length -= 1
            else:
                self.dupHashMap[val] = True
                index += 1
    def printDecodedMessage(self):
        codedMessage = ''
        for char in self.message:
            codedMessage += self.cipherMapping[char]
        print codedMessage
    def processKey(self):
        self.value =  self.key + " ZYXWVUTSRQPONMLKJIHGFEDCBA"
        self.removeDups()

        #create decoding mapping
        self.cipherMapping[ self.value[0] ] = "A"
        self.cipherMapping[ self.value[1] ] = "B" 
        self.cipherMapping[ self.value[2] ] = "C" 
        self.cipherMapping[ self.value[3] ] = "D"
        self.cipherMapping[ self.value[4] ] = "E"
        self.cipherMapping[ self.value[5] ] = "F"
        self.cipherMapping[ self.value[6] ] = "G"  
        self.cipherMapping[ self.value[7] ] = "H"
        self.cipherMapping[ self.value[8] ] = "I"
        self.cipherMapping[ self.value[9] ] = "J"
        self.cipherMapping[ self.value[10]] = "K"
        self.cipherMapping[ self.value[11]] = "L"
        self.cipherMapping[ self.value[12]] = "M"
        self.cipherMapping[ self.value[13]] = "N"
        self.cipherMapping[ self.value[14]] = "O"
        self.cipherMapping[ self.value[15]] = "P" 
        self.cipherMapping[ self.value[16]] = "Q"
        self.cipherMapping[ self.value[17]] = "R"
        self.cipherMapping[ self.value[18]] = "S"
        self.cipherMapping[ self.value[19]] = "T"
        self.cipherMapping[ self.value[20]] = "U"
        self.cipherMapping[ self.value[21]] = "V"
        self.cipherMapping[ self.value[22]] = "W"
        self.cipherMapping[ self.value[23]] = "X"
        self.cipherMapping[ self.value[24]] = "Y" 
        self.cipherMapping[ self.value[25]] = "Z"
        self.cipherMapping[ self.value[26]] = " "
