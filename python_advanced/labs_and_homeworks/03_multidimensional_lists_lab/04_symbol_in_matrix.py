size_of_the_matrix = int(input())

matrix = []

for _ in range(size_of_the_matrix):
    line = list("".join(input()))
    matrix.append(line)

needed_symbol = input()
is_available = False
for column_index in range(size_of_the_matrix):
    if is_available:
        break
    for row_index in range(size_of_the_matrix):
        if matrix[column_index][row_index] == needed_symbol:
            print((column_index, row_index))
            is_available = True
            break

if not is_available:
    print(f"{needed_symbol} does not occur in the matrix")