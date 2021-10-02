from .util import alpha_mod_add, standardize_string

def caesar(pt, shift=3):
	ct = ''

	for i in range(len(pt)):
		if ord('a') <= ord(pt[i]) and ord(pt[i]) <= ord('z'):
			ct += alpha_mod_add(pt[i], shift).upper()
		else:
			ct += pt[i]

	return ct

def vigenere(pt, keyword, skip_nonalpha=True):
	ct = ''
	shifts = []
	mask_idx = 0

	for c in keyword:
		if c.islower():
			shifts.append(ord(c) - ord('a'))
		else:
			shifts.append(ord(c) - ord('A'))

	for i in range(len(pt)):
		if ord('a') <= ord(pt[i]) and ord(pt[i]) <= ord('z'):
			ct += alpha_mod_add(pt[i], shifts[mask_idx%len(shifts)]).upper()
			mask_idx += 1
		else:
			ct += pt[i]

			if not skip_nonalpha:
				mask_idx += 1

	return ct

def atbash(pt):
	ct = ''

	for c in pt:
		if ord('a') <= ord(c) and ord(c) <= ord('z'):
			ct += chr((ord('z') - ord(c)) % 26 + ord('a'))
		else:
			ct += c

	return ct

def substitution(pt, key):
	ct = ''

	for c in pt:
		if c.isalpha():
			if c.islower():
				ct += key[c]
			else:
				ct += key[c.lower()].upper()
		else:
			ct += c

	return ct

def convolution(pt, poly):
	pt_clean = standardize_string(pt)
	pt_clean = pt_clean.lower()
	ct = ''

	for i in range(len(pt_clean)):
		if i - len(poly) < 0:
			pt_buf = pt_clean[i-len(poly)+1:] + pt_clean[:i+1]
		else:
			pt_buf = pt_clean[i-len(poly):i]

		shift = 0

		for j in range(len(poly)):
			shift += (ord(pt_buf[j]) - ord('a'))*int(poly[j])

		ct += alpha_mod_add(pt[i], shift)

	return ct

def direct_numeric(pt):
	ct = ''

	for i in range(len(pt)):
		if ord('a') <= ord(pt[i]) and ord(pt[i]) <= ord('z'):
			ct += str(ord(pt[i]) - ord('a') + 1) + '-'*(1-int(i == len(pt)-1 or not pt[i+1].isalpha()))
		else:
			ct += pt[i]

	return ct