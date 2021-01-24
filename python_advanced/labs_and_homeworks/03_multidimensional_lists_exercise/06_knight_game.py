size = int(input())

matrix = []
for row in range(size):
    current_row = [ch for ch in input()]
    matrix.append(current_row)


def steps_available(current_row, current_col, size, matrix):
    current_value = 0
    positions = [
        (current_row - 1, current_col - 2),
        (current_row + 1, current_col - 2),
        (current_row - 1, current_col + 2),
        (current_row + 1, current_col + 2),
        (current_row + 2, current_col - 1),
        (current_row + 2, current_col + 1),
        (current_row - 2, current_col - 1),
        (current_row - 2, current_col + 1),
    ]
    for position in positions:
        if 0 <= position[0] <= (size - 1) and 0 <= position[1] <= (size - 1):
            if matrix[position[0]][position[1]] == "K":
                current_value += 1
    return current_value


knights_removed = 0
while True:
    max_value = 0
    killer_position = []
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                current_knight = matrix[row][col]
                current_value = steps_available(row, col, size, matrix)
                if current_value > max_value:
                    max_value = current_value
                    killer_position = [row, col]
    if killer_position:
            matrix[killer_position[0]][killer_position[1]] = "0"
            knights_removed += 1
    else:
        break

print(knights_removed)

