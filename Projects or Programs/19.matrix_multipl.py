def multiply_matrices(a, b):
  if len(a[0]) != len(b):
    raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")

  # Create the result matrix
  result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

  # Perform matrix multiplication
  for i in range(len(a)):
    for j in range(len(b[0])):
      for k in range(len(b)):
        result[i][j] += a[i][k] * b[k][j]

  return result

# Example matrices
a = [[3, 4, 5]]
b = [[4], [2]]

# Multiply the matrices
result = multiply_matrices(a, b)

# Print the result
print(result)
