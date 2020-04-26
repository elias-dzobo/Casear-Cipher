def encrypt(text, shift=3):
	upper_case_text = text.upper()
	encrypted_text = []

	for c in upper_case_text:
		if c == " ":
			encrypted_text.append(" ")
			continue
		x = (((ord(c)-65)+shift)%26) + 65
		encrypted_text.append(chr(x))

	return "".join(encrypted_text)


print(encrypt('0553428198'))


def decrypt(text, shift=3):
	upper_case_text = text.upper()
	decrypted_text = []

	for c in upper_case_text:
		if c == " ":
			decrypted_text.append(c)
			continue
		x = (((ord(c) + 65) - shift) % 26) + 65
		decrypted_text.append(chr(x))

	return "".join(decrypted_text)

print(decrypt('mrrpqounvu'))
