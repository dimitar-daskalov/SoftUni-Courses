import math

numbers = [int(num) for num in input().split(", ")]

max_number_range = math.ceil(max(numbers) / 10)

for index in range(1, max_number_range + 1):
    upper = index * 10
    lower = upper - 10

    current_range = [num for num in numbers if lower < num <= upper]

    print(f"Group of {index * 10}'s: {current_range}")



