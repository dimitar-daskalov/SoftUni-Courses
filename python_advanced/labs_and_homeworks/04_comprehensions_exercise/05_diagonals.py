size = int(input())

matrix = [[int(el) for el in input().split(",")] for row in range(size)]
print(f'First diagonal: {", ".join([str(matrix[i][i]) for i in range(len(matrix))])}. Sum: {sum([matrix[i][i] for i in range(size)])}')
print(f'Second diagonal: {", ".join([str(matrix[i][size - i - 1]) for i in range(len(matrix))])}. Sum: {sum([matrix[i][size - i - 1] for i in range(len(matrix))])}')