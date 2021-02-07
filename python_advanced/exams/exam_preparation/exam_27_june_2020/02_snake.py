def is_in_range(row_received, col_received, size):
    if 0 <= row_received < size and 0 <= col_received < size:
        return True
    return False


matrix_size = int(input())
matrix = [[el for el in input()] for _ in range(matrix_size)]

MOVES = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
snake_position = 0
burrow_positions = []
for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == "S":
            snake_position = (row, col)
        elif matrix[row][col] == "B":
            burrow_positions.append((row, col))

received_moves = []
food_quantity = 0
is_failed = False
current_snake_position = snake_position
while True:
    if food_quantity == 10:
        break
    command = input()
    possible_move_position = (MOVES[command][0] + current_snake_position[0],
                              MOVES[command][1] + current_snake_position[1])
    if is_in_range(possible_move_position[0], possible_move_position[1], matrix_size):
        matrix[current_snake_position[0]][current_snake_position[1]] = "."
        current_snake_position = possible_move_position
        if matrix[possible_move_position[0]][possible_move_position[1]] == "*":
            matrix[possible_move_position[0]][possible_move_position[1]] = "S"
            food_quantity += 1
        elif matrix[possible_move_position[0]][possible_move_position[1]] == "B":
            matrix[possible_move_position[0]][possible_move_position[1]] = "."
            exit_burrow_position = burrow_positions[1]
            matrix[exit_burrow_position[0]][exit_burrow_position[1]] = "S"
            current_snake_position = exit_burrow_position
        elif matrix[possible_move_position[0]][possible_move_position[1]] == "-":
            matrix[possible_move_position[0]][possible_move_position[1]] = "S"
    else:
        matrix[current_snake_position[0]][current_snake_position[1]] = "."
        is_failed = True
        break


if is_failed:
    print("Game over!", f"Food eaten: {food_quantity}", sep="\n")
else:
    print("You won! You fed the snake.", f"Food eaten: {food_quantity}", sep="\n")
for row in matrix:
    print("".join(row))