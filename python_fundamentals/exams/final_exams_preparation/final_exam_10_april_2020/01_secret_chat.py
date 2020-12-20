secret_message = input()

command = input()
while not command == "Reveal":
    command = command.split(":|:")
    action = command[0]
    if action == "InsertSpace":
        index = int(command[1])
        secret_message = secret_message[:index] + " " + secret_message[index:]
        print(secret_message)
    elif action == "Reverse":
        substring = command[1]
        if substring in secret_message:
            secret_message = secret_message.replace(substring, "", 1)
            substring = substring[::-1]
            secret_message = secret_message + substring
            print(secret_message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        if substring in secret_message:
            secret_message = secret_message.replace(substring, replacement)
        print(secret_message)
    command = input()

print(f"You have a new text message: {secret_message}")