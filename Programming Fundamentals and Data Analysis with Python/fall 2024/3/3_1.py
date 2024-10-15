s = open('input.txt')
c = s.readlines()
b = ''.join(c)
a = b.split( )
nw = [i [:: - 1] for i in a]
d = ' '.join(nw)
print(d)
s.close()
