from collections import deque
rows, columns = [int(el) for el in input().split()]

string = deque(input())

matrix = []
appended = 1
for row in range(rows):
    current_row = []
    for index_ch in range(columns):
        current_ch = string.popleft()
        current_row += current_ch
        string.append(current_ch)
    if appended % 2 == 0:
        matrix.append(current_row[::-1])
    elif appended % 2 != 0:
        matrix.append(current_row)
    appended += 1
for row in matrix:
    print("".join(ch for ch in row))
