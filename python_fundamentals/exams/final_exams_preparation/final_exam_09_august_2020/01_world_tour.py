stops = input()

command = input()
while not command == "Travel":
    command = command.split(":")
    action = command[0]
    if action == "Add Stop":
        index = int(command[1])
        string = command[2]
        if index in range(len(stops)):
            stops = stops[:index] + string + stops[index:]
        print(stops)
    elif action == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops.replace(stops[start_index:end_index + 1], "", 1)
        print(stops)
    elif action == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")