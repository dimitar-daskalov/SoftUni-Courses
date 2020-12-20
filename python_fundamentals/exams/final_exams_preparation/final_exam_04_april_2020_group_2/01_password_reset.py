raw_password = input()
new_raw_password = ""
command = input()
while not command == "Done":
    command = command.split()
    action = command[0]
    if action == "TakeOdd":
        for ch_index in range(len(raw_password)):
            if ch_index % 2 != 0:
                new_raw_password += raw_password[ch_index]
        raw_password = new_raw_password
        print(raw_password)
    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        string_to_cut = raw_password[index: index + length]
        raw_password = raw_password.replace(string_to_cut, "", 1)
        print(raw_password)
    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in raw_password:
            raw_password = raw_password.replace(substring, substitute)
            print(raw_password)
        else:
            print(f"Nothing to replace!")
    command = input()

print(f"Your password is: {raw_password}")