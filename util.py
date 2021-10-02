import re

def standardize_string(in_str):
	out_str = in_str.replace(' ', '')
	out_str = re.sub(r'\W+', '', out_str)

	return out_str

def alpha_mod_add(l, shift):
	l_lwr = l.lower()

	return chr((ord(l_lwr) - ord('a') + shift) % 26 + ord('a')*l.islower() + ord('A')*l.isupper())

def fix_fw_sub_key(fw_key):
	pretty_key = {}

	for k, v in fw_key.items():
		pretty_key[k.lower()] = v.upper()

	return pretty_key