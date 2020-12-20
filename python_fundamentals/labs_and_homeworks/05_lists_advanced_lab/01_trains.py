wagons = int(input())
wagons_list = []
for i in range(wagons):
    wagons_list.append(0)

command = input()
while command != "End":
    split_command = command.split()
    action = split_command[0]
    if action == "add":
        wagons_list[-1] += int(split_command[1])
    elif action == "insert":
        wagons_list[int(split_command[1])] += int(split_command[2])
    elif action == "leave":
        wagons_list[int(split_command[1])] -= int(split_command[2])

    command = input()

if command == "End":
    print(wagons_list)