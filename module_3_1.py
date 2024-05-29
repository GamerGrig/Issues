def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for k in range(m):
            row.append(value)
        matrix.append(row)

    return matrix


print(get_matrix(3, 4, 500))
