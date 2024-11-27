import numpy as np
a=open('input.txt')
q=[]
b=a.readlines()
b=[x.strip() for x in b]
for line in b:
    q.append( [x for x in line.split(' ') ] )
matrix = np.array(q)
matrix_t=matrix.transpose()
print(matrix_t)
a.close()