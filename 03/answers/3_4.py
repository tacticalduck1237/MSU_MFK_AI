s = open('input.txt')
c = s.readlines()
d="/".join(c)
d=d.replace('\n',"")
d=d.split("/")
n=int(c[0])
a=d[1:n+1]
b=d[n+1:]
g=""
q=open("output.txt", "a")
for x, y in zip(a, b):
    q.write(str(x))
    q.write("\t")
    q.write(str(y))
    q.write("\n")
s.close()
q.close()
