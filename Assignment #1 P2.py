import string, random

def main():

	letters = list(string.ascii_lowercase)
	randomKey = []

	while letters:
		size = len(letters)
		randomKey.append(letters.pop(random.randint(0, size - 1)))

	letters = list(string.ascii_lowercase)

	decryptLetters = 'etaoinshrdlcumwfgypbvkjxqc'
	
	print("Randomized key used:", randomKey)

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
	plaintext = '' 
	letterCounter = []
	newOrderLetters = []

	for i in letters:
		counter = 0
		for j in ciphertext:
			if i == j:
				counter += 1

		letterCounter.append(counter)

	letterCounterList = dict(zip(letters, letterCounter))

	decryptLettersList = list(decryptLetters)


	while letterCounterList:
		highestFrequency = 0
		letterIndex = ''
		newLetter = ''
		counter = 0

		for i in letterCounterList:
			if letterCounterList[i] > highestFrequency:
				highestFrequency = letterCounterList[i]
				letterIndex = counter # to remove letter with this index later
				newLetter = i # to hold letter to add to newOrderLetters
			counter += 1

		if highestFrequency == 0: # case where all other letters have frequency of 0
			letterIndex = 0
			newLetter = next(iter(letterCounterList))


		newOrderLetters.append(newLetter)
		del letterCounterList[newLetter] 

	convertList = dict(zip(newOrderLetters, decryptLettersList))

	for i in ciphertext:
		for j in convertList:
			if i == j:
				plaintext += convertList[j]

	print("Plaintext:", plaintext)

if __name__ == '__main__':
	main()