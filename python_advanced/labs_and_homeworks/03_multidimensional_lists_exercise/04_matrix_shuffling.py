rows, cols = [int(el) for el in input().split()]

matrix = []

for row in range(rows):
    current_row = [el for el in input().split()]
    matrix.append(current_row)


def is_command_valid(received_command):
    if received_command.startswith("swap") and len(received_command.split()) == 5:
        return True
    return False


def is_command_in_range(first_row, first_column, second_row, second_column, rows, columns):
    if 0 <= first_row <= rows and 0 <= second_row <= rows and 0 <= first_column <= columns and 0 <= second_column <= columns:
        return True
    return False


command = input()
while not command == "END":
    if is_command_valid(command):
        row_1, column_1, row_2, column_2 = [int(el) for el in command.split()[1:]]
        if is_command_in_range(row_1, column_1, row_2, column_2, rows, cols):
            matrix[row_1][column_1], matrix[row_2][column_2] = matrix[row_2][column_2], matrix[row_1][column_1]
            for row in matrix:
                print(*row)
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    command = input()