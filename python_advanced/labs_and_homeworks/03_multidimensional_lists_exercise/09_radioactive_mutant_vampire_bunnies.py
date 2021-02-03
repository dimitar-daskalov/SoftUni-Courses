def is_in_range(current_pos, row_received, col_received):
    current_row_pos, current_col_pos = current_pos[0], current_pos[1]
    if 0 <= current_row_pos < row_received and 0 <= current_col_pos < col_received:
        return True
    return False


def find_bunnies(row_received, col_received, changed_matrix):
    bunny_positions = []
    for row_index in range(row_received):
        for col_index in range(col_received):
            if changed_matrix[row_index][col_index] == "B":
                bunny_positions.append((row_index, col_index))
    for bunny_position in bunny_positions:
        changed_matrix = bunnies_expand(bunny_position[0], bunny_position[1], changed_matrix, row_received, col_received)
    return changed_matrix


def bunnies_expand(bunny_row, bunny_col, changed_matrix, row_received, col_received):
    expand_positions = [
        (bunny_row + 1, bunny_col),
        (bunny_row - 1, bunny_col),
        (bunny_row, bunny_col + 1),
        (bunny_row, bunny_col - 1),
        ]
    for position in expand_positions:
        if is_in_range(position, row_received, col_received) and changed_matrix[position[0]][position[1]] != "B":
            changed_matrix[position[0]][position[1]] = "B"

    return changed_matrix


rows, columns = [int(el) for el in input().split()]

matrix = []
for _ in range(rows):
    row = [el for el in input()]
    matrix.append(row)

starting_player_position = 0
for current_row in range(rows):
    for current_col in range(columns):
        current_position = (current_row, current_col)
        if matrix[current_row][current_col] == "P":
            matrix[current_row][current_col] = "."
            starting_player_position = current_position


commands = input()
game_won = False
game_over = False

for command in commands:
    matrix = find_bunnies(rows, columns, matrix)
    if command == "R":
        needed_position = (starting_player_position[0], starting_player_position[1] + 1)
        if is_in_range(needed_position, rows, columns):
            if matrix[needed_position[0]][needed_position[1]] == "B":
                game_over = True
                starting_player_position = needed_position
                break
            starting_player_position = needed_position
        else:
            game_won = True
            break
    elif command == "L":
        needed_position = (starting_player_position[0], starting_player_position[1] - 1)
        if is_in_range(needed_position, rows, columns):
            if matrix[needed_position[0]][needed_position[1]] == "B":
                game_over = True
                starting_player_position = needed_position
                break
            starting_player_position = needed_position
        else:
            game_won = True
            break
    elif command == "U":
        needed_position = (starting_player_position[0] - 1, starting_player_position[1])
        if is_in_range(needed_position, rows, columns):
            if matrix[needed_position[0]][needed_position[1]] == "B":
                game_over = True
                starting_player_position = needed_position
                break
            starting_player_position = needed_position
        else:
            game_won = True
            break
    elif command == "D":
        needed_position = (starting_player_position[0] + 1, starting_player_position[1])
        if is_in_range(needed_position, rows, columns):
            if matrix[needed_position[0]][needed_position[1]] == "B":
                game_over = True
                starting_player_position = needed_position
                break
            starting_player_position = needed_position
        else:
            game_won = True
            break

for row in matrix:
    print("".join(row))
if game_won:
    print(f"won: {starting_player_position[0]} {starting_player_position[1]}")
elif game_over:
    print(f"dead: {starting_player_position[0]} {starting_player_position[1]}")