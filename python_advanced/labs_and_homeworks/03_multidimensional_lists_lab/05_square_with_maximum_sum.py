rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)

biggest_sum = 0
biggest_num_1 = 0
biggest_num_2 = 0
biggest_num_3 = 0
biggest_num_4 = 0

for row_index in range(rows - 1):
    current_sum = 0
    for col_index in range(columns - 1):
        current_number = matrix[row_index][col_index]
        second_number = matrix[row_index][col_index + 1]
        third_number = matrix[row_index + 1][col_index]
        forth_number = matrix[row_index + 1][col_index + 1]
        current_sum = current_number + second_number + third_number + forth_number
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            biggest_num_1 = current_number
            biggest_num_2 = second_number
            biggest_num_3 = third_number
            biggest_num_4 = forth_number

print(biggest_num_1, biggest_num_2)
print(biggest_num_3, biggest_num_4)
print(biggest_sum)
