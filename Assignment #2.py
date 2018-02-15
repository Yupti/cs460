import random

def main():
	running = True

	while running:
		choice = int(input("Enter a command:\n(1) manual input for a word\n(2) randomly generated words\n(3) Exit program\nChoice: "))
		if choice == 1:
			manual_input()
		elif choice == 2:
			random_key_generation() #values hold individual hex values
		elif choice == 3:
			print("Thank you for using this program!")
			running = False
		else:
			print("Incorrect choice chose, please try again.\n")
	
def rounds(w0, w1, w2, w3): # Runs the rounds for subkey generation
	aes_round = 1
	round_num = 4
	total_key = w0 + w1 + w2 + w3

	print("Round 0: ")
	print("word 0:", "0x" + w0)
	print("word 1:", "0x" + w1)
	print("word 2:", "0x" + w2)
	print("word 3:", "0x" + w3)
	w3_gee = g_function(w3, aes_round)

	aes_round += 1

	while aes_round <= 11:
		print("Round " + str(aes_round - 1) + ":")
		w0 = hex(int(w0, 16) ^ int(w3_gee, 16))
		w0 = hex_append(w0)
		print("word " + str(round_num) + ": " + w0)
		round_num += 1
		total_key += w0[2:]
		w1 = hex(int(w0, 16) ^ int(w1, 16))
		w1 = hex_append(w1)
		print("word " + str(round_num) + ": " + w1)
		round_num += 1
		total_key += w1[2:]
		w2 = hex(int(w1, 16) ^ int(w2, 16))
		w2 = hex_append(w2)
		print("word " + str(round_num) + ": " + w2)
		round_num += 1
		total_key += w2[2:]
		w3 = hex(int(w2, 16) ^ int(w3, 16))
		w3 = hex_append(w3)
		print("word " + str(round_num) + ": " + w3)
		round_num += 1
		total_key += w3[2:]

		if aes_round < 11:
			w3_gee = g_function(w3[2:], aes_round)

		aes_round += 1

	print("\nTotal Key:") # prints completed key
	for i in range(len(total_key)):
		if i % 32 == 0:
			print("")
		print(total_key[i], end = '')

	print("\n")

def manual_input(): # for manual input of words in rounds
	temp_list = []
	print("When inputting hex values, please enter only 8 hex values like so: (abcd1234)")

	for i in range(4):
		temp_list.append(input("Enter a value for word " + str(i) + ": "))

	rounds(temp_list.pop(0), temp_list.pop(0), temp_list.pop(0), temp_list.pop(0))

def random_key_generation(): # for randomly generated words in rounds
	hex_values = '0123456789abcdef'
	w1 = ''; w2 = ''; w3 = ''; w4 = ''
	word_matrix = [] 

	for i in range(16):
		indiv_values = (random.choice(hex_values), random.choice(hex_values))
		word_matrix.append(indiv_values)

	for i in range(len(word_matrix)):
		val = word_matrix[i]
		if i % 4 == 0:
			w1 += val[0]
			w1 += val[1]
		elif i % 4 == 1:
			w2 += val[0]
			w2 += val[1]
		elif i % 4 == 2:
			w3 += val[0]
			w3 += val[1]
		else:
			w4 += val[0]
			w4 += val[1]

	rounds(w1, w2, w3, w4)

def g_function(word, round): # g function for translating word 3 for continuous rounds
	new_word = '0x'
	Sbox = (
            0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
            0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
            0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
            0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
            0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
            0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
            0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
            0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
            0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
            0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
            0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
            0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
            0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
            0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
            0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
            0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
            )

	shifted = word[2:] + word[:2] # byte shift left
	int_values = []
	int_values.extend(shifted)

	while int_values: # for locating the values in the S-box
		temp = int(int_values.pop(0), 16)
		temp2 = int(int_values.pop(0), 16)
		temp *= 16
		temp += temp2 # gets location in Sbox 

		value = str(hex(Sbox[temp]))
		new_word += s_box_extract(value)

	rc_value = rc_extract(round) # determines Round Constant value to use based on current round
	final_word = hex(int(new_word, 16) ^ int(rc_value, 16))

	return final_word[2:]

def s_box_extract(hex1): # properly generates hex values from S-box
	if len(hex1) == 3:
		return "0" + hex1[2]
	else:
		return hex1[2:]

def rc_extract(round): # generates Round Constant based on current round
	RC = (0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36)
	value = str(hex(RC[round - 1]))
	if len(value) == 1: 
		return "0" + value + "000000"
	else:
		return value + "000000"

def hex_append(hex_val): # fixes gaps in hex values
	if len(hex_val) != 10:
		while len(hex_val) != 10:
			hex_val += "0"
	return hex_val

if __name__ == "__main__":
	main()