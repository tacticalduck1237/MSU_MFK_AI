import numpy as np
data = np.genfromtxt('input.csv', delimiter=',')
avg_wins = np.mean(data, axis=0)
data[0, :] = np.floor(avg_wins * 1.5)
np.savetxt('output.csv', data, fmt="%g", delimiter=',')
