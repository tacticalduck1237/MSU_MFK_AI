with open('input.txt') as file:
	for s in file:
		g = s.split()
		print(" ".join(g[::2]))
close(file)