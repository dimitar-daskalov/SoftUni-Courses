def is_in_range(size_received, position_parameter):
    if 0 <= position_parameter[0] < size_received and 0 <= position_parameter[1] < size_received:
        return True
    return False


string_received = input()
size = int(input())

positions = {"up": (-1, 0), "down": (+1, 0), "left": (0, -1), "right": (0, +1)}

matrix = []
for _ in range(size):
    row = [el for el in input()]
    matrix.append(row)

is_found = False
start_position = 0
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "P":
            start_position = (row, col)
            is_found = True
            break
    if is_found:
        break

player_current_position = start_position
commands_number = int(input())
for _ in range(commands_number):
    current_command = input()
    movable_parameters = positions[current_command]
    possible_moving_position = (player_current_position[0] + movable_parameters[0],
                                player_current_position[1] + movable_parameters[1])
    if is_in_range(size, possible_moving_position):
        matrix[player_current_position[0]][player_current_position[1]] = "-"
        player_current_position = possible_moving_position
        if matrix[possible_moving_position[0]][possible_moving_position[1]].isalpha():
            string_received += matrix[possible_moving_position[0]][possible_moving_position[1]]
        matrix[possible_moving_position[0]][possible_moving_position[1]] = "P"
    else:
        if string_received:
            string_received = string_received[:-1]

print(string_received)
for row in matrix:
    print("".join(row))