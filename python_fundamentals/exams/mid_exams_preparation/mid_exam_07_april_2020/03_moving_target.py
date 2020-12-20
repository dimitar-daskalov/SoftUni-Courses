targets = [int(target) for target in input().split()]

command = input()
while not command == "End":
    command = command.split()
    action = command[0]
    index = command[1]
    index = int(index)
    if action == "Shoot":
        power = int(command[2])
        if index in range(len(targets)):
            targets[index] -= power
            if targets[index] <= 0:
                targets.remove(targets[index])
    elif action == "Add":
        value = int(command[2])
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        radius = int(command[2])
        if index in range(len(targets)) and (index + radius) in range(len(targets)) and (index - radius) in range(
                len(targets)):
            del targets[(index - radius):(index + radius + 1)]
        else:
            print("Strike missed!")
    command = input()

print(f"{'|'.join(str(target) for target in targets)}")