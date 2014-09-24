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
    def removeDups(self): # removes duplicate characters from self.value, the string created from self.key by adding the alphabet
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
        print self.value
    def printCodedMessage(self):
        codedMessage = ''
        for char in self.message:
            codedMessage += self.cipherMapping[char]
        print codedMessage
    def processKey(self):
        self.value =  self.key + " ZYXWVUTSRQPONMLKJIHGFEDCBA"
        self.removeDups()
        
        print len(self.value)

        #create mapping
        self.cipherMapping["A"] = self.value[0]
        self.cipherMapping["B"] = self.value[1]
        self.cipherMapping["C"] = self.value[2]
        self.cipherMapping["D"] = self.value[3]
        self.cipherMapping["E"] = self.value[4]
        self.cipherMapping["F"] = self.value[5]
        self.cipherMapping["G"] = self.value[6]
        self.cipherMapping["H"] = self.value[7]
        self.cipherMapping["I"] = self.value[8]
        self.cipherMapping["J"] = self.value[9]
        self.cipherMapping["K"] = self.value[10]
        self.cipherMapping["L"] = self.value[11]
        self.cipherMapping["M"] = self.value[12]
        self.cipherMapping["N"] = self.value[13]
        self.cipherMapping["O"] = self.value[14]
        self.cipherMapping["P"] = self.value[15]
        self.cipherMapping["Q"] = self.value[16]
        self.cipherMapping["R"] = self.value[17]
        self.cipherMapping["S"] = self.value[18]
        self.cipherMapping["T"] = self.value[19]
        self.cipherMapping["U"] = self.value[20]
        self.cipherMapping["V"] = self.value[21]
        self.cipherMapping["W"] = self.value[22]
        self.cipherMapping["X"] = self.value[23]
        self.cipherMapping["Y"] = self.value[24]
        self.cipherMapping["Z"] = self.value[25]
        self.cipherMapping[" "] = self.value[26]






