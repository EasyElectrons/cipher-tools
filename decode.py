import re
from .util import fix_fw_sub_key, standardize_string, alpha_mod_add

def caesar(ct, orig_shift=3):
	pt = ''

	for i in range(0, len(ct)):
		if ord('A') <= ord(ct[i]) and ord(ct[i]) <= ord('Z'):
			pt += alpha_mod_add(ct[i], -orig_shift).lower()
		else:
			pt += ct[i]

	return pt

def vigenere(ct, keyword, skip_nonalpha=True):
	pt = ''
	shifts = []
	mask_idx = 0

	for c in keyword:
		if c.islower():
			shifts.append(ord(c) - ord('a'))
		else:
			shifts.append(ord(c) - ord('A'))

	for i in range(len(ct)):
		if ord('A') <= ord(ct[i]) and ord(ct[i]) <= ord('Z'):
			pt += alpha_mod_add(ct[i], -shifts[mask_idx%len(shifts)]).lower()
			mask_idx += 1
		else:
			pt += ct[i]

			if not skip_nonalpha:
				mask_idx += 1

	return pt

def atbash(ct):
	pt = ''

	for c in ct:
		if ord('A') <= ord(c) and ord(c) <= ord('Z'):
			pt += chr((ord('Z') - ord(c)) % 26 + ord('A')).lower()
		else:
			pt += c

	return pt

def substitution(ct, fw_key):
	fw_key = fix_fw_sub_key(fw_key)
	pt = ''

	rv_key = {}

	for k, v in fw_key.items():
		rv_key[v] = k

	for c in ct:
		if c.isalpha() and c in rv_key.keys():
			pt += rv_key[c]
		else:
			pt += c

	return pt

def convolution(ct, poly):
	ct_clean = standardize_string(ct)
	ct_clean = ct_clean.upper()
	pt = ''

	for i in range(len(ct_clean)):
		if i - len(poly) < 0:
			ct_buf = ct_clean[i-len(poly)+1:] + ct_clean[:i+1]
		else:
			ct_buf = ct_clean[i-len(poly):i]

		shift = 0

		for j in range(len(poly)):
			shift -= (ord(ct_buf[j]) - ord('A'))*int(poly[j])

		pt += alpha_mod_add(ct[i], shift).lower()

	return pt

def direct_numeric(ct):
	pt = ''
	chars = re.split('(\W)', ct)
	
	for c in chars:
		if c.isdigit():
			pt += chr(int(c) + ord('a') - 1)
		elif c == '-':
			pass
		else:
			pt += c

	return pt