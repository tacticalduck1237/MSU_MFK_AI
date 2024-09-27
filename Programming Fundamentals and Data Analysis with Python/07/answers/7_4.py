import numpy as np
data = np.loadtxt('input.txt') 
start, end, lenght = data 
lenght = int(lenght) 
profit = np.linspace(start, end, lenght) 
mon, fri = np.ones(lenght), np.ones(lenght) 
mon[::7], fri[4::7] = 3, 2 
np.savetxt('output.txt', profit / mon * fri, fmt='%.2f')
