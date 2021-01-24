size = int(input())

matrix = [[int(num) for num in input().split()] for row in range(size)]

summed_primary_diagonal = sum([matrix[num][num] for num in range(size)])
summed_secondary_diagonal = sum([matrix[num][size - num - 1] for num in range(size)])

all_summed = abs(summed_primary_diagonal - summed_secondary_diagonal)

print(all_summed)