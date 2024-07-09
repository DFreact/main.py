def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
            # value += 1


    return matrix

print(get_matrix(8,1,0))