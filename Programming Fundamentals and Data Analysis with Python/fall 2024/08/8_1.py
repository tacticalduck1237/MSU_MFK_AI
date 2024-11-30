import numpy as np

# Read the matrix from the input file
matrix = np.loadtxt('input.txt', dtype=float)

# Transpose the matrix
matrix_t = matrix.T

# Print the transposed matrix in the required format
print("[", end="")
for i, row in enumerate(matrix_t):
    if i > 0:
        print(" ", end="")
    print("[" + " ".join(f"{x: .1f}" for x in row) + "]", end="")
    if i != len(matrix_t) - 1:
        print()
print("]")
