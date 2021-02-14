def get_magic_triangle(number_received):
    matrix = [[1], [1, 1]]
    for index in range(3, number_received + 1):
        current_row = [1] * index
        matrix.append(current_row)

    for row in range(2, len(matrix)):
        for col in range(1, row):
            matrix[row][col] = matrix[row-1][col-1] + matrix[row-1][col]
    return matrix
