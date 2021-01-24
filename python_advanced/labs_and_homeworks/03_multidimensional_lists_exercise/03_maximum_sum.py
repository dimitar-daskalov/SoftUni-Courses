from sys import maxsize
rows, columns = [int(el) for el in input().split()]

matrix = []
max_sum = -maxsize
max_summed_square = []

for row in range(rows):
    current_row = [int(el) for el in input().split()]
    matrix.append(current_row)

for row in range(rows - 2):
    for col in range(columns - 2):
        square_3 = [
            [matrix[row][col],
            matrix[row][col + 1],
            matrix[row][col + 2]],
            [matrix[row + 1][col],
            matrix[row + 1][col + 1],
            matrix[row + 1][col + 2]],
            [matrix[row + 2][col],
            matrix[row + 2][col + 1],
            matrix[row + 2][col + 2]],
        ]
        current_sum = sum([sum(el) for el in square_3])
        if current_sum > max_sum:
            max_sum = current_sum
            max_summed_square = square_3

print(f"Sum = {max_sum}")
for row in max_summed_square:
    print(*row)
