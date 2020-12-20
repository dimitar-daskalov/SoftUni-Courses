integers = [int(integer) for integer in input().split()]

command = input()
while not command == "end":
    command = command.split()
    action = command[0]
    if action == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])
        integers[index_1], integers[index_2] = integers[index_2], integers[index_1]
    elif action == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])
        integers[index_1] = integers[index_1] * integers[index_2]
    elif action == "decrease":
        integers = [(number - 1) for number in integers]
    command = input()

print(", ".join(str(number) for number in integers))