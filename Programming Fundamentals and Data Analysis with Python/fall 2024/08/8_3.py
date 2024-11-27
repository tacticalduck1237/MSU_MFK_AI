import numpy as np
s = np.genfromtxt('input.csv', delimiter=',')
s[::2,1::2]=s[::2,1::2]/2
s[1::2,::2]=s[1::2,::2]/2
np.savetxt('output.csv', s,fmt='%g', delimiter=',')
