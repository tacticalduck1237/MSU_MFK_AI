s = open('input.txt')
c = s.readline()
a = c.split( )
nw = [i [:: - 1] for i in a]
d = ' '.join(nw)
print(d)
s.close()
