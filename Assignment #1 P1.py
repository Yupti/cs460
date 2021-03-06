import string

def main():

	active = True
	while active:
		active = menu()
	print("Thank you for using this program!")

def menu():
	continueChoice = 0
	compressString = '' # when user enters a plain/ciphertext to work on, compresses letters without whitespace and stores here
	choice = int(input("Choices\n1.) Caesar Cipher\n2.) Playfair Cipher\n3.) Vignere Cipher\n4.) Exit\nChoose a number: "))
	if choice == 1: # caesar cypher
		text = input("Enter a word or sentence you wish to encrypt/decrypt: ")
		text = text.lower()
		choice2 = int(input("Enter the number for desired action: (1) Encrypt (2) Decrypt: "))

		compressString = wordCompress(text)

		caesarEncryptDecrypt(compressString, choice2) 

	elif choice == 2: # playfair cypher
		text = input("Enter a word or sentence you wish to encrypt/decrypt: ")
		text = text.lower()
		keyword = input("Enter a keyword to use for encryption/decryption: ")
		choice2 = int(input("Enter the number for desired action: (1) Encrypt (2) Decrypt: ")) 

		compressString = wordCompress(text)

		playfairCipher(compressString, keyword, choice2)

	elif choice == 3:
		print("NOTE: word/sentence to encrypt/decrypt MUST be longer than keyword")
		text = input("Enter a word or sentence you wish to encrypt/decrypt: ")
		text = text.lower()
		keyword = input("Enter a keyword to use for encryption/decryption: ")
		choice2 = int(input("Enter the number for desired action: (1) Encrypt (2) Decrypt: ")) 

		compressString = wordCompress(text)

		if len(compressString) < len(keyword):
			print("Unable to encrypt/decrypt, keyword is longer than the plain/ciphertext.")
		else:
			vigenereEncryptDecrypt(compressString, keyword, choice2)
	elif choice == 4:
		return False
	else:
		continueChoice = int(input("Incorrect choice selected, would you like to retry or exit the program?\n1.) Exit\n2.) Retry\n(If invalid choice chosen, retries by default.): "))

	if continueChoice == 1: 
		return False
	else: 
		return True 

def wordCompress(text):
	compressedWord = ''
	for i in text:
		if ord(i) != 32:
			compressedWord += i

	return compressedWord

def caesarEncryptDecrypt(text, selection): 
	text = text.lower()
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

	elif selection == 2: # for decryption
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

	else:
		print("Invalid choice, returning to main menu.")

def playfairCipher(text, keyword, selection): 
	if selection == 1 or selection == 2:
		matrixContent = []
		matrix = [] # creates empty list to fill with the letters
		extra = '' # holds letter if the pair is a duplicate, uses for next pair if available
		finalText = '' # for holding plain/ciphertext when finished
		letters = list(string.ascii_lowercase)
		size = len(text)

		letters.remove('j') # removing to simplify matrix

		for i in keyword: # creates letters from keyword without duplicates
			letterTemp = i
			if letterTemp == 'j': 
				letterTemp = 'i'
			if letterTemp not in matrixContent:
				matrixContent.append(letterTemp)

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
	
		print("Matrix:") # only for show, will remove later
		for i in matrix:
			print(i)

		while textLetters: # separate text 2 by 2, placing duplicate pairs in 'extras'
			letter1 = ''
			letter2 = ''
			location1 = [] # holds (x,y) for letter1
			location2 = [] # holds (x,y) for letter2
			pointer1 = 0 # pointers to use for locating the encrypted/decrypted letter to use
			pointer2 = 0

			if letter1 == 'j': 
				letter1 = 'i'
			if letter2 == 'j':
				letter2 = 'i'

			if extra: # checks 'extra' contains a letter
				letter1 = extra
				extra = '' # resets to empty
			else:
				letter1 = textLetters.pop(0)

			if textLetters: # checks if contains letters
				letter2 = textLetters.pop(0)
			else:
				letter2 = 'x'

			if letter1 == letter2: # checks if pair is duplicate or not
				extra = letter2
				letter2 = 'x' # the default letter if pair is duplicates

			for i in range(5):
				for j in range(5):
					if matrix[i][j] == letter1:
						location1.extend([i,j]) # holds coordinates
					if matrix[i][j] == letter2:
						location2.extend([i,j]) # same as above comment

			if selection == 1: # FOR ENCRYPTION
				if location1[0] == location2[0]: # case where they are in same row
					pointer1 = location1[1] + 1
					pointer2 = location2[1] + 1 

					if pointer1 > 4: # to the right is out of bounds, resets to 0
						pointer1 = 0

					if pointer2 > 4: # same comments as above
						pointer2 = 0

					finalText += matrix[location1[0]][pointer1] 
					finalText += matrix[location2[0]][pointer2]

				elif location1[1] == location2[1]: # case where they are in same column
					pointer1 = location1[0] + 1
					pointer2 = location2[0] + 1 # encrypt +1, decrypt -1

					if pointer1 > 4: # to the right is out of bounds, resets to 0
						pointer1 = 0

					if pointer2 > 4: # same comments as above
						pointer2 = 0

					finalText += matrix[pointer1][location1[1]]
					finalText += matrix[pointer2][location2[1]]

				else: # case of different rows, different columns
					finalText += matrix[location1[0]][location2[1]]
					finalText += matrix[location2[0]][location1[1]]

			elif selection == 2: # FOR DECRYPTION
				if location1[0] == location2[0]: # case where they are in same row
					pointer1 = location1[1] - 1
					pointer2 = location2[1] - 1 

					if pointer1 < 0: # to the right is out of bounds, resets to 0
						pointer1 = 4

					if pointer2 < 0: # same comments as above
						pointer2 = 4

					finalText += matrix[location1[0]][pointer1] 
					finalText += matrix[location2[0]][pointer2]

				elif location1[1] == location2[1]: # case where they are in same column
					pointer1 = location1[0] - 1
					pointer2 = location2[0] - 1 # encrypt +1, decrypt -1

					if pointer1 < 0: # to the right is out of bounds, resets to 0
						pointer1 = 4

					if pointer2 < 0: # same comments as above
						pointer2 = 4

					finalText += matrix[pointer1][location1[1]]
					finalText += matrix[pointer2][location2[1]]

				else: # case of different rows, different columns
					finalText += matrix[location1[0]][location2[1]]
					finalText += matrix[location2[0]][location1[1]]

		if selection == 1:
			print("Plaintext:", text, "\nKeyword:", keyword, "\nCiphertext:", finalText)
		else:	
			print("Cyphertext:", text, "\nKeyword:", keyword, "\nPlaintext:", finalText)
	else:
		print("Invalid choice, returning to main menu.")


def vigenereEncryptDecrypt(text, keyword, selection): # NOTE: keyword should be shorter than text
	allLetters = string.ascii_lowercase
	letters = []
	numbers = []
	textToNumbers = []
	keywordToNumbers = []
	ciphertextNumbers = []
	keyLength = len(keyword)
	keywordCounter = 0
	finalText = ''

	for i in range(26):
		letters.append(allLetters[i])
		numbers.append(i)

	vigenere = dict(zip(letters, numbers)) # dictionary holding values for each letter

	for i in text: # holds numbers for text
		for j in vigenere:
			if i == j:
				textToNumbers.append(vigenere[j])

	for i in keyword: # holds numbers for keyword
		for j in vigenere:
			if i == j:
				keywordToNumbers.append(vigenere[j])

	if selection == 1: # for encryption
		for i in range(len(text)): # for iterating through entire list of text
			if keywordCounter == keyLength:
				keywordCounter = 0
			ciphertextNumbers.append((textToNumbers[i] + keywordToNumbers[keywordCounter]) % 26)
			keywordCounter += 1

		# print("Keyword:", keywordToNumbers)
		# print("Text:", textToNumbers)
		# print("Result:", ciphertextNumbers)

		for i in ciphertextNumbers:
			for j in vigenere:
				if i == vigenere[j]:
					finalText += j

		print("Plaintext:", text, "\nKeyword:", keyword, "\nCiphertext:", finalText)

	elif selection == 2: # for decryption
		for i in range(len(text)): # for iterating through entire list of text
			if keywordCounter == keyLength:
				keywordCounter = 0
			ciphertextNumbers.append((textToNumbers[i] - keywordToNumbers[keywordCounter]) % 26)
			keywordCounter += 1

		for i in ciphertextNumbers:
			for j in vigenere:
				if i == vigenere[j]:
					finalText += j

		print("Plaintext:", text, "\nKeyword:", keyword, "\nCiphertext:", finalText)
	else:
		print("Invalid choice, returning to main menu.")
 

if __name__ == '__main__':
	main()