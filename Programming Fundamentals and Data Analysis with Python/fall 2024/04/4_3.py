#s=open('input.txt')
s=str(input())
#c = s.read()
#d=c.split(" ")
d=s.split(" ")
b1=float(d[0])
q=float(d[1])
n=int(d[2])
t=b1
t1=0
a=0
while a<n:
    a+=1
    t=b1*q**(a-1)
    t1+=t
print(f"{t1:.3f}")
#s.close()
#закомментирован ввод через файл, если хотите его-надо раскомментировать и стереть строку 5