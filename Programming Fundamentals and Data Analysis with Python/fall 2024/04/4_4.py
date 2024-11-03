s=open('input.txt')
a=s.readlines()
n=len(a)
i=0
minlist=[]
while i<n:
    b=a[i].strip()
    b=b.split(" ")
    i+=1
    minimal=float(min(b))
    minlist.append(minimal)
    maximum=max(minlist)
print(f"{maximum:.3f}")
s.close