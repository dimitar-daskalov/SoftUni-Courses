inventory = input().split(", ")

command = input()
while not command == "Craft!":
    split_command = command.split(" - ")
    if split_command[0] == "Collect":
        if split_command[1] not in inventory:
            inventory.append(split_command[1])
    elif split_command[0] == "Drop":
        if split_command[1] in inventory:
            inventory.remove(split_command[1])
    elif split_command[0] == "Combine Items":
        second = "".join(split_command[1]).split(":")
        if second[0] in inventory:
            for index in range(len(inventory)):
                if inventory[index] == second[0]:
                    inventory.insert(index + 1, second[1])
                    break
    elif split_command[0] == "Renew":
        if split_command[1] in inventory:
            for index, item in enumerate(inventory):
                if split_command[1] == item:
                    item_removed = inventory.pop(index)
                    inventory.append(item_removed)

    command = input()

if command == "Craft!":
    print(", ".join(inventory))


