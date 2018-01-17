import string

def main():

	#caesarStart()
	#caesarEncryptDecrypt("zzz",1)
	# test = "hello"
	# s = ''
	# for i in test:
	# 	if i not in s:
	# 		s += i
	# print(len(s))
	playfairCipher("test", "tester", 2)
	# letters = string.ascii_lowercase
	# test = ''
	# test2 = []
	# if test:
	# 	print("a")
	# else:
	# 	print("b")
	# print(letters)
	# for i in range(25 - len(test)):
	# 	test += letters[i]
	print('hello')


def caesarStart(): #text can be either plaintext or ciphertext
	cipher = list(string.ascii_lowercase)
	for i in range(3): # creates list for caesar cipher
		cipher.append(cipher.pop(0))
	print(cipher)
	cipher.remove('j')
	print(cipher)

def caesarEncryptDecrypt(text, selection): #if greater than 120, minus 23
	if selection == 1: # for encryption
		ciphertext = ''
		for i in text:
			i = ord(i)
			if i >= 120:
				i -= 23
			else:
				i += 3
			i = chr(i) 
			ciphertext += i

		print("Plaintext:", text, "\nCiphertext:", ciphertext)

	else: # for decryption
		plaintext = ''
		for i in text:
			i = ord(i)
			if i <= 97:
				i += 23
			else:
				i -= 3
			i = chr(i)
			plaintext += i

		print("Ciphertext:", text, "\nPlaintext:", plaintext)

def playfairCipher(text, keyword, selection): #IN PROGRESS
	matrixContent = []
	matrix = [] # creates empty list to fill with the letters
	extra = '' # holds letter if the pair is a duplicate, uses for next pair if available
	finalText = '' # for holding plain/ciphertext when finished
	letters = list(string.ascii_lowercase)
	size = len(text)

	letters.remove('j') # removing to simplify matrix, NOT SURE IF LEGAL
	print("Letters: ", letters)

	for i in keyword: # creates letters from keyword without duplicates
		if i not in matrixContent:
			matrixContent.append(i)

	for i in range(25): # creates all needed letters for matrix
		singleLetter = letters[i]
		if singleLetter not in matrixContent:
			matrixContent.append(singleLetter)

	for i in range(5):
		row = []
		for j in range(5):
			row.append(matrixContent.pop(0)) 
		matrix.append(row)

	textLetters = [i for i in text] # holds all letters of plain/ciphertext
	
	print("Matrix:")
	for i in matrix:
		print(i)

	while textLetters: # separate text 2 by 2, placing duplicate pairs in 'extras'
		letter1 = ''
		letter2 = ''
		location1 = [] # holds (x,y) for letter1
		location2 = [] # holds (x,y) for letter2

		if extra: # checks if list is empty
			letter1 = extra
		else:
			letter1 = textLetters.pop(0)
		letter2 = textLetters.pop(0)

		if letter1 == letter2: # checks if pair is duplicate or not
			extra = letter2
			letter2 = 'x' # the default letter if pair is duplicates

		# print("Letter1:", letter1)
		# print("Letter2:", letter2)

		for i in range(5):
			for j in range(5):
				if matrix[i][j] == letter1:
					location1.extend([i,j]) # holds coordinates
				if matrix[i][j] == letter2:
					location2.extend([i,j]) # same as above comment

		# print("Coordinates1:", location1[0], " ", location1[1])
		# print("Coordinates2:", location2[0], " ", location2[1])

		

if __name__ == '__main__':
	main()