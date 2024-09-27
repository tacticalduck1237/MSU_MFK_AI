with open('input.csv', mode='r') as f:
	txt=f.readlines()[1:]
s=0
for line in txt:
	a,b,c=map(int, line.split(','))
	a,b,c = sorted([a,b,c])
	s+=a+b>c
print(s)
