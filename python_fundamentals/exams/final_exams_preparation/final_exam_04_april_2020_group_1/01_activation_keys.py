raw_activation_key = input()

command = input()
while not command == "Generate":
    command = command.split(">>>")
    action = command[0]
    if action == "Contains":
        substring = command[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print(f"Substring not found!")
    elif action == "Flip":
        upper_or_lower = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        if upper_or_lower == "Upper":
            string_to_be_changed = raw_activation_key[start_index:end_index].upper()
            raw_activation_key = raw_activation_key[:start_index] + string_to_be_changed + raw_activation_key[end_index:]
        elif upper_or_lower == "Lower":
            string_to_be_changed = raw_activation_key[start_index:end_index].lower()
            raw_activation_key = raw_activation_key[:start_index] + string_to_be_changed + raw_activation_key[end_index:]
        print(raw_activation_key)
    elif action == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        raw_activation_key = raw_activation_key.replace(raw_activation_key[start_index:end_index], "")
        print(raw_activation_key)
    command = input()

print(f"Your activation key is: {raw_activation_key}")