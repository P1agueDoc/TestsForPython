def get_matrix (n, m, value):
    matrix=[]
    for matrix_c1 in range(n):
        matrix_add=[]
        for matrix_d2 in range(m):
            matrix_add.append(value)
        matrix.append(matrix_add)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)