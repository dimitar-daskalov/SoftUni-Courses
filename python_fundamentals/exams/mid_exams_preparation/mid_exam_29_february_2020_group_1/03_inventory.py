collected_items = input().split(", ")

command = input()
while not command == "Craft!":
    command = command.split(" - ")
    action = command[0]
    if action == "Collect":
        item = command[1]
        if item not in collected_items:
            collected_items.append(item)
    elif action == "Drop":
        item = command[1]
        if item in collected_items:
            collected_items.remove(item)
    elif action == "Combine Items":
        old_item, new_item = command[1].split(":")
        if old_item in collected_items:
            old_item_index = collected_items.index(old_item)
            collected_items.insert(old_item_index + 1, new_item)
    elif action == "Renew":
        item = command[1]
        if item in collected_items:
            collected_items.remove(item)
            collected_items.append(item)
    command = input()

print(", ".join(collected_items))