# Input matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input matrix elements
print("Enter the elements row by row:")
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Element [{i}][{j}]: "))
        row.append(val)
    matrix.append(row)

# Display original matrix
print("\nOriginal Matrix:")
for row in matrix:
    print(row)

# Diagonal sum (only for square matrices)
if rows == cols:
    diagonal_sum = 0
    for i in range(rows):
        diagonal_sum += matrix[i][i]
    print("Sum of main diagonal elements:", diagonal_sum)
else:
    print("Not a square matrix, so diagonal sum is not defined.")

# Transpose of matrix
transpose = []
for j in range(cols):
    row = []
    for i in range(rows):
        row.append(matrix[i][j])
    transpose.append(row)

# Display transpose
print("\nTranspose of the Matrix:")
for row in transpose:
    print(row)
