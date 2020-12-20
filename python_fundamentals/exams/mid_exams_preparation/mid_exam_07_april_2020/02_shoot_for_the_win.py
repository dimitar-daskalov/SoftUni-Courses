targets = [int(target) for target in input().split()]

command = input()
count_shot = 0
while not command == "End":
    index = int(command)
    if index in range(len(targets)):
        old_value = targets[index]
        targets[index] = -1
        count_shot += 1
        for target_index in range(len(targets)):
            if not targets[target_index] == -1:
                if targets[target_index] > old_value:
                    targets[target_index] -= old_value
                else:
                    targets[target_index] += old_value
    command = input()

print(f"Shot targets: {count_shot} -> {' '.join([str(target)for target in targets])}")
