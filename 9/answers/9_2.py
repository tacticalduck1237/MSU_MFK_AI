import numpy as np
import pandas as pd
s =np.genfromtxt('input.csv', delimiter=',')
s=s.astype(int)
i=0
j=0
f=np.average(s, axis = 0)
f=f.tolist()
# function to find minimum and maximum position in list
def minimum(a, n):
    minpos = a.index(min(a))
    print(minpos + 1)
minimum(f, len(f))
