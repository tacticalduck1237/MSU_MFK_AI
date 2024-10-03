import numpy as np
s =np.genfromtxt('input.csv', delimiter=',')
s=s.astype(int)
i=0
j=0
f=np.std(s, axis = 1)
f=f.tolist()
for d in range(len(f)):
    if f[int(d)]>4:
        i+=1
    else:
        j+=1
if i>j:
    print('2')
else:
    print('1')
