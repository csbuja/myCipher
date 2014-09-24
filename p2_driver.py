from p2_cipher import Cipher

def p2_answer():
	aCipher = Cipher()
	aCipher.key = "BLUE" # the hardcoded key, it comes from p1_ and p_0
	aCipher.processKey() # make a deduped string 
	aCipher.readIn() # reads the message in
	aCipher.printDecodedMessage() #prints the decoded message

if __name__ == "__main__":
	p2_answer()