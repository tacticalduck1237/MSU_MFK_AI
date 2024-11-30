import numpy as np

a = open('input.txt')
q = []
b = a.readlines()
b = [x.strip() for x in b]
for line in b:
    q.append([x for x in line.split(' ')])

matrix = np.array(q, dtype=float)  # Ensure data is treated as floats
matrix_t = matrix.transpose()

# Print the matrix in the desired format
print("[", end="")
for i, row in enumerate(matrix_t):
    if i > 0:
        print(" ", end="")
    print("[" + " ".join(f"{x: .1f}" for x in row) + "]", end="")
    if i != len(matrix_t) - 1:
        print()
print("]")
a.close()