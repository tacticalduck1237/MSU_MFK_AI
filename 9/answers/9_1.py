for i in range(8):
	x1, x2, x3 = bool(i & 4), bool(i & 2), bool(i & 1)
	if (not x1 and x2 and not x3) or (not x1 and x2 and x3) or (x1 and not x2 and not x3):
		print(x1, x2, x3)
