def flat_matrix(m):
    return [cell for row in m for cell in row ]

print(flat_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))