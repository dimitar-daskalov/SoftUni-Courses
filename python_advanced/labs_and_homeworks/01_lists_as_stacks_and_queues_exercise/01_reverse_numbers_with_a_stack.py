numbers_received = [number for number in input().split()]

numbers_in_stack = []

for _ in range(len(numbers_received)):
    numbers_in_stack.append(numbers_received.pop())

print(" ".join(numbers_in_stack))