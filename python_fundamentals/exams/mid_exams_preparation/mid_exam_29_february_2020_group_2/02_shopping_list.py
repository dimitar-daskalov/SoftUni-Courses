groceries = input().split("!")

command = input()
while not command == "Go Shopping!":
    command = command.split()
    action = command[0]
    if action == "Urgent":
        item = command[1]
        if item not in groceries:
            groceries.insert(0, item)
    elif action == "Unnecessary":
        item = command[1]
        if item in groceries:
            groceries.remove(item)
    elif action == "Correct":
        old_item, new_item = command[1], command[2]
        if old_item in groceries:
            index_old_item = groceries.index(old_item)
            groceries[index_old_item] = new_item
    elif action == "Rearrange":
        item = command[1]
        if item in groceries:
            item_index = groceries.index(item)
            groceries.pop(item_index)
            groceries.append(item)
    command = input()

print(", ".join(groceries))
