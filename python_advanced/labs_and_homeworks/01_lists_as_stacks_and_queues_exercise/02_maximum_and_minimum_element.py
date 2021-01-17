manipulation_stack = []

commands_number = int(input())

for _ in range(commands_number):
    command = input()
    if command.startswith("1"):
        element = int(command.split()[1])
        manipulation_stack.append(element)
    elif command == "2":
        if manipulation_stack:
            manipulation_stack.pop()
    elif command == "3":
        if manipulation_stack:
            print(max(manipulation_stack))
    elif command == "4":
        if manipulation_stack:
            print(min(manipulation_stack))

manipulation_stack = [str(el) for el in manipulation_stack][::-1]
print(", ".join(manipulation_stack))