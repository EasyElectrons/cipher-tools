from .util import standardize_string

def gram_freq(ct, gram_length=1):
	"""!
	@details Determines the frequencies of the present n-gram.
	An n-gram is a set of consecutive letters (in English, most common monogram is 'e', bigram 'th', trigram 'the')

	@arg ct: input ciphertext
	@arg gram_length (optional): what length of n-gram to analyze, default 1
	"""
	ct = standardize_string(ct)
	ct_upr = ct.upper()
	counts = {}

	for i in range(len(ct_upr)-gram_length):
		g = ct_upr[i:i+gram_length]

		if g in counts.keys():
			counts[g] += 1
		else:
			counts[g] = 1

	return counts

def rowize(string, len_row, only_alpha=True):
	if only_alpha:
		string = standardize_string(string)

	rows = []

	for i in range(0, len(string), len_row):
		rows.append(string[i:i+len_row])

	return rows

def columnize(string, num_cols, only_alpha=True):
	if only_alpha:
		string = standardize_string(string)

	rows = rowize(string, num_cols)
	cols = []
	
	for c in range(num_cols):
		col = ''

		for r in rows:
			try:
				col += r[c]
			except:
				pass

		cols.append(col)

	return cols

def kasiski(ct, group_size=3, only_alpha=True):
	if only_alpha:
		ct = standardize_string(ct)

	prob_lens = {}
	groups = []

	for i in range(len(ct)-group_size):
		groups.append(ct[i:i+group_size])

	for i in range(len(groups)-group_size):
		for j in range(i+group_size, len(groups)):
			if groups[i] == groups[j]:
				diff = j - i
				
				if diff > 17:
					check_range = 17
				else:
					check_range = diff

				for k in range(3, check_range):
					if diff % k == 0 and k in prob_lens.keys():
						prob_lens[k] += 1
					elif diff % k == 0 and k not in prob_lens.keys():
						prob_lens[k] = 1

	return prob_lens