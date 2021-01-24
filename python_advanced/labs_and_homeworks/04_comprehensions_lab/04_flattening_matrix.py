size = int(input())

matrix = [[int(num)for num in input().split(", ")] for row in range(size)]

print([x for row in matrix for x in row])