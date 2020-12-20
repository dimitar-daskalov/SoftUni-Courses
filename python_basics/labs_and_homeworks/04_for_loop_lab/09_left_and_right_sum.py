n = int(input())
left_sum = 0
right_sum = 0

for position in range(0, n):
    number = int(input())
    left_sum += number
for position in range(0, n):
    number = int(input())
    right_sum += number

if left_sum == right_sum:
    print(f"Yes, sum = {right_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")