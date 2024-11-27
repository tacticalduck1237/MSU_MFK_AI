import numpy as np
s =np.genfromtxt('input.csv', delimiter=',')
i=s[:,0].sum()
j=s[:,1].sum()
k=s[:,2].sum()
def maximum(a, b, c):
    if (a >= b) and (a >= c):
        return 1
    elif (b >= a) and (b >= c):
        return 2
    else:
        return 3
print(maximum(i, j, k))
