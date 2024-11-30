import numpy as np

# Read the input file
with open('input.txt') as a:
    q = []
    b = a.readlines()
    b = [x.strip() for x in b]
    for line in b:
        q.append([float(x) for x in line.split()])  # Convert to float for numerical data

# Convert to NumPy array
matrix = np.array(q)

# Transpose the matrix
matrix_t = matrix.transpose()

# Print the transposed matrix in the desired format
print("[", end="")
for row in matrix_t:
    print("[" + " ".join(f"{x:.1f}" for x in row) + "]", end="")
print("]")