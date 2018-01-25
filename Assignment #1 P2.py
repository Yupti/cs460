import string, random

def main():

	letters = list(string.ascii_lowercase)
	randomKey = []

	while letters:
		size = len(letters)
		randomKey.append(letters.pop(random.randint(0, size - 1)))

	letters = list(string.ascii_lowercase)

	decryptLetters = 'etaoinshrdlcumwfgypbvkjxqc'
	
	# print("Regular: ", letters)
	# print("Key: ", randomKey)

	refDictionary = dict(zip(letters, randomKey))
	plaintext = input("Enter a plaintext to encode: ")
	plaintext = plaintext.lower()

	ciphertext = encrypt(plaintext, refDictionary)

	frequencyAttack(letters, ciphertext, decryptLetters)

def encrypt(text, refDictionary):
	ciphertext = ''
	for i in text:
		for j in refDictionary:
			if i == j:
				ciphertext += refDictionary[j]

	print("Ciphertext:", ciphertext)

	return ciphertext

def frequencyAttack(letters, ciphertext, decryptLetters):
	letterCounter = []
	indexFrequency = []

	for i in letters:
		counter = 0
		for j in ciphertext:
			if i == j:
				counter += 1

		letterCounter.append(counter)

	print(letterCounter)

	while letterCounter:
		maxNumLetters = 0
		letterIndex = 0

		for i in letterCounter:
			if i > maxNumLetters:
				maxNumLetters = i
				letterIndex = letterCounter.index(i)

		letterCounter.pop(letterIndex) # NEEDS TESTING pops the value out of letterCounter

	print(letterIndex) # good

if __name__ == '__main__':
	main()