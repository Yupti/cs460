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
	matrixContent = ''
	letters = list(string.ascii_letters)

	letters.remove('j') # removing to simplify matrix, NOT SURE IF LEGAL

	for i in keyword: # creates letters from keyword without duplicates
		if i not in matrixContent:
			matrixContent += i

	remainingSpace = 25 - len(matrixContent)


	print(remainingSpace)

	#print(matrixContent)

if __name__ == '__main__':
	main()