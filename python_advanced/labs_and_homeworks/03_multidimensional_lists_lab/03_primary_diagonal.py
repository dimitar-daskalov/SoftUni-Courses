size_of_square_matrix = int(input())

matrix = []

for _ in range(size_of_square_matrix):
    row = [int(x) for x in input().split()]
    matrix.append(row)

summed_primary_diagonal = 0
current_index = 0
for column_index in range(size_of_square_matrix):
    if current_index == size_of_square_matrix:
        break
    summed_primary_diagonal += matrix[column_index][current_index]
    current_index += 1

print(summed_primary_diagonal)