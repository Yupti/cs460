import string

def main():

	#caesarStart()
	#caesarEncryptDecrypt("zzz", 2)
	# test = "hello"
	# s = ''
	# for i in test:
	# 	if i not in s:
	# 		s += i
	# print(len(s))
	playfairCipher("test", "tester", 2)
	# letters = string.ascii_lowercase
	# test = 'test'
	# print(letters)
	# for i in range(25 - len(test)):
	# 	test += letters[i]
	# print(test)


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
	letters = list(string.ascii_lowercase)

	letters.remove('j') # removing to simplify matrix, NOT SURE IF LEGAL
	print("Letters: ", letters)

	for i in keyword: # creates letters from keyword without duplicates
		if i not in matrixContent:
			matrixContent.append(i)

	for i in range(25): # creates all needed letters for matrix
		singleLetter = letters[i]
		if singleLetter not in matrixContent:
			matrixContent.append(singleLetter)

	matrix = [] # creates empty list to fill with the letters

	for i in range(5):
		row = []
		for j in range(5):
			row.append(matrixContent.pop(0)) 
		matrix.append(row)

	print(matrix)


if __name__ == '__main__':
	main()