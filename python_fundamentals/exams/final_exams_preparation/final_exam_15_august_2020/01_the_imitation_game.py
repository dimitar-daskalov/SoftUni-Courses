encrypted_message = input()

command = input()
while not command == "Decode":
    command = command.split("|")
    action = command[0]
    if action == "Move":
        number_of_letters = int(command[1])
        letters_to_move = encrypted_message[:number_of_letters]
        encrypted_message = encrypted_message[number_of_letters:] + letters_to_move
    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {encrypted_message}")