from copy import copy

field_size = int(input())
moves = input().split()
collected_coals = 0


def is_in_range(position_0, position_1, size_field):
    if 0 <= position_0 <= (size_field - 1) and 0 <= position_1 <= (size_field - 1):
        return True
    return False


def available_moves(start_position, moves_available, f_size):
    positions_done = []
    curr_position = start_position
    for move in moves_available:
        if move == "left":
            movable_position = (curr_position[0], curr_position[1] - 1)
            if is_in_range(movable_position[0], movable_position[1], f_size):
                curr_position = movable_position
                positions_done.append(curr_position)
            else:
                curr_position = curr_position
        elif move == "right":
            movable_position = (curr_position[0], curr_position[1] + 1)
            if is_in_range(movable_position[0], movable_position[1], f_size):
                curr_position = movable_position
                positions_done.append(curr_position)
            else:
                curr_position = curr_position
        elif move == "up":
            movable_position = (curr_position[0] - 1, curr_position[1])
            if is_in_range(movable_position[0], movable_position[1], f_size):
                curr_position = movable_position
                positions_done.append(curr_position)
            else:
                curr_position = curr_position
        elif move == "down":
            movable_position = (curr_position[0] + 1, curr_position[1])
            if is_in_range(movable_position[0], movable_position[1], f_size):
                curr_position = movable_position
                positions_done.append(curr_position)
            else:
                curr_position = curr_position
    return positions_done


matrix = []
for _ in range(field_size):
    current_row = input().split()
    matrix.append(current_row)

starting_position = 0
all_coals_positions = []
exit_position = 0

for row in range(field_size):
    for col in range(field_size):
        if matrix[row][col] == "s":
            starting_position = (row, col)
        elif matrix[row][col] == "c":
            all_coals_positions.append((row, col))
        elif matrix[row][col] == "e":
            exit_position = (row, col)

all_moves = available_moves(starting_position, moves, field_size)
removed_coals = copy(all_coals_positions)

is_over = False
for position_index in range(len(all_moves)):
    for coal in all_coals_positions:
        if all_moves[position_index] == coal:
            collected_coals += 1
            if coal in removed_coals:
                removed_coals.remove(coal)
        elif all_moves[position_index] == exit_position:
            print(f"Game over! {exit_position}")
            is_over = True
            break
    if len(removed_coals) == 0:
        print(f"You collected all coals! {all_moves[position_index]}")
        break

if len(removed_coals) > 0 and not is_over:
    last_position = all_moves[-1]
    print(f"{len(removed_coals)} coals left. {last_position}")
