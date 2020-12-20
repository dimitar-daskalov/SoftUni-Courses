import sys

n = int(input())
minimum = sys.maxsize
maximum = -sys.maxsize

for i in range(0, n):
    number = int(input())
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number
print(f"Max number: {maximum}")
print(f"Min number: {minimum}")
