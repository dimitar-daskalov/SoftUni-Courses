matrix_size = int(input())
matrix = []


def bombs_damage(func_bomb_rows, func_bomb_cols, modified_matrix):
    bomb_primary_position_value = modified_matrix[func_bomb_rows][func_bomb_cols]
    modified_matrix[func_bomb_rows][func_bomb_cols] = 0
    bombs_damage_squares = [
        (func_bomb_rows, func_bomb_cols - 1),
        (func_bomb_rows - 1, func_bomb_cols - 1),
        (func_bomb_rows - 1, func_bomb_cols),
        (func_bomb_rows - 1, func_bomb_cols + 1),
        (func_bomb_rows, func_bomb_cols + 1),
        (func_bomb_rows + 1, func_bomb_cols + 1),
        (func_bomb_rows + 1, func_bomb_cols),
        (func_bomb_rows + 1, func_bomb_cols - 1),
    ]
    for current_position_damage in bombs_damage_squares:
        if 0 <= current_position_damage[0] <= (len(modified_matrix) - 1) and 0 <= current_position_damage[1] <= (len(modified_matrix) - 1):
            if modified_matrix[current_position_damage[0]][current_position_damage[1]] > 0:
                modified_matrix[current_position_damage[0]][current_position_damage[1]] -= bomb_primary_position_value
    return modified_matrix


for row in range(matrix_size):
    matrix.append([int(el) for el in input().split()])

bomb_coordinates = []
received_coordinates = [el for el in input().split()]
for current_bomb_coordinates in received_coordinates:
    bomb_rows, bomb_cols = [int(el) for el in current_bomb_coordinates.split(",")]
    bomb_coordinates.append([bomb_rows, bomb_cols])


for bomb in bomb_coordinates:
    if matrix[bomb[0]][bomb[1]] > 0:
        matrix = bombs_damage(bomb[0], bomb[1], matrix)

alive_cells = 0
summed_values_alive_cells = 0

for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] > 0:
            alive_cells += 1
            summed_values_alive_cells += matrix[row][col]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {summed_values_alive_cells}")
for row in matrix:
    print(*row)
