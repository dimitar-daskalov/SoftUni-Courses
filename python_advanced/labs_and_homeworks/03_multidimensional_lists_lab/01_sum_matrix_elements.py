rows, columns = [int(x) for x in input().split(", ")]

matrix = []

total_sum = 0
for row_index in range(rows):
    element = [int(i) for i in input().split(", ")]
    matrix.append(element)
    total_sum += sum(element)
print(total_sum, matrix, sep="\n")