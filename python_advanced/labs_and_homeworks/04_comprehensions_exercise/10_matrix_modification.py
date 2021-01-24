size = int(input())

matrix = [[int(el) for el in input().split()] for row in range(size)]


def is_in_range(row, col, dimension):
    if row in range(dimension) and col in range(dimension):
        return True
    return False


command = input()
while not command == "END":
    action, row_received, col_received, value = command.split()
    row_received = int(row_received)
    col_received = int(col_received)
    value = int(value)
    if action == "Add":
        if is_in_range(row_received, col_received, size):
            matrix[row_received][col_received] += value
        else:
            print("Invalid coordinates")
    elif action == "Subtract":
        if is_in_range(row_received, col_received, size):
            matrix[row_received][col_received] -= value
        else:
            print("Invalid coordinates")
    command = input()

for row in matrix:
    print(*row)