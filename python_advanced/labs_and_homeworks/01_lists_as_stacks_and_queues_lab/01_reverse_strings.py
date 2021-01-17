text_received = list(input())

stack_used = []

for _ in range(len(text_received)):
    stack_used.append(text_received.pop())

print("".join(stack_used))