from math import floor


def is_in_range(moving_position_row, moving_position_col, size):
    if 0 <= moving_position_row < size and 0 <= moving_position_col < size:
        return True
    return False


matrix_size = int(input())
coins = 0
matrix = []
player = "P"
player_starting_position = 0
POSITIONS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for row_index in range(matrix_size):
    current_row = list(input().split())
    if player in current_row:
        player_starting_position = (row_index, current_row.index(player))
    matrix.append(current_row)

path = []
current_player_position = player_starting_position
while coins < 100:
    command = input()
    if command in POSITIONS:
        possible_moving_position = (POSITIONS[command][0] + current_player_position[0],
                                    POSITIONS[command][1] + current_player_position[1])
        if is_in_range(possible_moving_position[0], possible_moving_position[1], matrix_size):
            if matrix[possible_moving_position[0]][possible_moving_position[1]] == "X":
                if coins:
                    coins = floor(coins / 2)
                break
            else:
                coins += int(matrix[possible_moving_position[0]][possible_moving_position[1]])
                path.append([possible_moving_position[0], possible_moving_position[1]])
                current_player_position = possible_moving_position
        else:
            if coins:
                coins = floor(coins / 2)
            break

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")
for el in path:
    print(el)