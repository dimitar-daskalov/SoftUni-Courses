rows, columns = [int(number) for number in input().split()]

matrix = [[chr(97+row) + chr(97+col+row) + chr(97+row) for col in range(columns)] for row in range(rows)]

for row in matrix:
    print(*row)