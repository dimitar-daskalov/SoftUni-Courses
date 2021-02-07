def is_in_range(row_received, col_received, size):
    if 0 <= row_received < size and 0 <= col_received < size:
        return True
    return False


matrix_size = int(input())
matrix = [[0] * matrix_size for _ in range(matrix_size)]

MOVES = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
    "left_upper": (-1, -1),
    "right_upper": (-1, 1),
    "left_lower": (1, -1),
    "right_lower": (1, 1),
}
number_of_bombs = int(input())
bombs_coordinates = []

for _ in range(number_of_bombs):
    bombs_coordinates.append(input().strip("()").split(", "))

for bomb_coords in bombs_coordinates:
    bomb_col, bomb_row = int(bomb_coords[0]), int(bomb_coords[1])
    matrix[bomb_col][bomb_row] = "*"

for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == "*":
            for direction in MOVES:
                direction_row, direction_col = MOVES[direction][0], MOVES[direction][1]
                if is_in_range(row + direction_row, col + direction_col, matrix_size):
                    if not matrix[row + direction_row][col + direction_col] == "*":
                        matrix[row + direction_row][col + direction_col] += 1

for row in matrix:
    print(*row)

