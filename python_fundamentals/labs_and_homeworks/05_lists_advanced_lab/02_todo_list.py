command = input()
notes = [0] * 10

while command != "End":
    split_command = command.split("-")
    priority = int(split_command[0]) - 1
    note = split_command[1]
    if priority <= 10:
        notes.insert(priority, note)

    command = input()

result = []
for element in notes:
    if element != 0:
        result.append(element)

print(result)

