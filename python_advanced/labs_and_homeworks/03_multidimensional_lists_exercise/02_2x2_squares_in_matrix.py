rows, columns = [int(el) for el in input().split()]

matrix = [[el for el in input().split()] for row in range(rows)]
are_same = False
equals = 0
for row in range(rows - 1):
    for col in range(columns - 1):
        square = [matrix[row][col],
                  matrix[row][col + 1],
                  matrix[row + 1][col],
                  matrix[row + 1][col + 1],
                  ]
        for el in range(len(square) - 1):
            if square[el] == square[el + 1]:
                are_same = True
            else:
                are_same = False
                break
        if are_same:
            equals += 1
print(equals)