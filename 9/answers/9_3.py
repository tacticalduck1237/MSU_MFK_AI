import numpy as np
import pandas as pd
s1 = open('input.csv')
c = s1.readline()
c=c.replace('\n', "")
c=c.split(',')
s1.close()
s =np.genfromtxt('input.csv', delimiter=',')
s = np.delete(s, (0), axis=0)
s=s.astype(float)
f=np.sum(s, axis = 0)
f=f.tolist()
def maximum(a, n):
    maxpos = a.index(max(a))
    print(c[maxpos])
maximum(f, len(f))
