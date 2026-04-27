def dec2bin(val, n=8, absolute = True):
	if val < 0:
		if absolute:
			val = abs(val)
		else:
			raise ValueError('Negative value')
	if val > (2**n - 1):
		if absolute:
			val = 0
		else:
			raise ValueError('Very big value')
	return [int(x) for x in bin(val)[2:].zfill(n)]