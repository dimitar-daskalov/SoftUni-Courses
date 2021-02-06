def get_magic_triangle(number):
    matrix = [[1], [1, 1]]
    for row_index in range(3, number + 1):
        row = [1] * row_index
        matrix.append(row)
    for row_i in range(2, number):
        for col_i in range(1, row_i):
            matrix[row_i][col_i] = matrix[row_i - 1][col_i - 1] + matrix[row_i - 1][col_i]

    return matrix

