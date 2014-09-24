from p2_cipher import Cipher

def p2_answer():
	aCipher = Cipher()
	aCipher.key = "FDHNE" # the hardcoded key, it comes from p1_ and p_0
	aCipher.processKey()
	aCipher.readIn()
	aCipher.printDecodedMessage()

if __name__ == "__main__":
	p2_answer()