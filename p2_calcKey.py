import sys

# the variable, number, will always be a whole number. No need to deal with negatives!
# this function sums all digits within itself until it only has one digit
def sum_digits(number):
	if number<10:
		return number
	else:
		x = str(number)
		sum = 0
		for val in x:
			sum += int(val)
		return sum_digits(sum)

def castToLetter(num):
	toMap = str(num%26)  #letters 

	#As 6 maps to F, I map 0 to Z to deal with the corner case of num being zero or if there are numbers bigger than 25
	mapToAlphabet = {}
	mapToAlphabet['0'] = 'Z'
	mapToAlphabet['1'] = 'A'
	mapToAlphabet['2'] = 'B'
	mapToAlphabet['3'] = 'C'
	mapToAlphabet['4'] = 'D'
	mapToAlphabet['5'] = 'E'
	mapToAlphabet['6'] = 'F'
	mapToAlphabet['7'] = 'G'
	mapToAlphabet['8'] = 'H'
	mapToAlphabet['9'] = 'I'
	mapToAlphabet['10'] = 'J'
	mapToAlphabet['11'] = 'K'
	mapToAlphabet['12'] = 'L'
	mapToAlphabet['13'] = 'M'
	mapToAlphabet['14'] = 'N'
	mapToAlphabet['15'] = 'O'
	mapToAlphabet['16'] = 'P'
	mapToAlphabet['17'] = 'Q'
	mapToAlphabet['18'] = 'R'
	mapToAlphabet['19'] = 'S'
	mapToAlphabet['20'] = 'T'
	mapToAlphabet['21'] = 'U'
	mapToAlphabet['22'] = 'V'
	mapToAlphabet['23'] = 'W'
	mapToAlphabet['24'] = 'X'
	mapToAlphabet['25'] = 'Y'

	return mapToAlphabet[toMap]

## Answer from Task 1: 
#  Repeatedly sum the digits of the number until only a single digit remains.
# The key begins with that letter of the English alphabet.
#    ex: 78 -> 15 -> 6 -> F
def p0_buildcipher(number):
	x = sum_digits(number) 
	return castToLetter(x)

## Answer from Task 2:
#  Cast the absolute value of each of the two numbers to a letter in the 
# English alphabet. The letter is already a letter (or letters).
#    ex: 4 -8 NE -> 4 8 NE -> D H NE
def p1_buildcipher(string):
	stringSet = string.split(' ')
	stringSet[0] = castToLetter( abs(int(stringSet[0]) ) )
	stringSet[1] = castToLetter( abs(int(stringSet[1]) ) )
	return stringSet

def printKey(p0_num,p1_string):
	p0_char = p0_buildcipher(p0_num)
	p1_stringset = p1_buildcipher(p1_string)
	p1_newString = ''.join(p1_stringset)

	print 'This is your key: ' + p0_char + p1_newString

if __name__ == "__main__":
	print 'Type a whole number -- from part 0: '
	p0_num = int( sys.stdin.readline().rstrip('\n') )
	print 'Type two integers followed by an abbreviation of a direction -- from part 1: '
	p1_string = sys.stdin.readline().rstrip('\n')
	printKey(p0_num,p1_string) 