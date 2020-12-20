import sys

numbers_received = input().split()
numbers_we_should_remove = int(input())
numbers = []
min_number = sys.maxsize

for number in numbers_received:
    numbers.append(int(number))

for _ in range(numbers_we_should_remove):
    for num in numbers:
        if num < min_number:
            min_number = num
    numbers.remove(min_number)
    min_number = sys.maxsize

print(numbers)

