list_commands = []
dict_commands = {}

command = input()
while not command == "stop":
    list_commands.append(command)
    command = input()

for index in range(0, len(list_commands), 2):
    key = list_commands[index]
    value = int(list_commands[index + 1])
    if key in dict_commands:
        dict_commands[key] += value
    else:
        dict_commands[key] = value

for key, value in dict_commands.items():
    print(f"{key} -> {value}")