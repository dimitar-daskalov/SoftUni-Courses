import sys

n = int(input())
max_number = -sys.maxsize
total = 0

for i in range(0, n):
    number = int(input())
    if number > max_number:
        max_number = number
    total += number

total -= max_number

if total == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {(abs(max_number - total))}")