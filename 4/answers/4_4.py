s=open('input.txt')
c = s.read()
d=c.split(" ")
b1=float(d[0])
q=float(d[1])
a=float(d[2])
n=1
t=b1
while a>t:
    n+=1
    t=b1*q**(n-1)
print(n)
s.close()
