#попробуйте решить через while, мы не придумали как это сделать и сделали через for
a=open('input.txt')
c = a.readlines()
d="/".join(c)
d=d.replace('\n',"")
d=d.split("/")
h=0
i=0
t=0
q=len(d)
for h in d:
    n=int(h)
    if n != 0:
        i+=1
        t+=n
print(i, t)
