string_received = input()

new_message = ""
current_message = ""
digit = "0"

for index in range(len(string_received)):
    if string_received[index].isdigit():
        digit += string_received[index]
    else:
        new_message += current_message * int(digit)
        if index > 0 and string_received[index - 1].isdigit():
            current_message = string_received[index].upper()
        else:
            current_message += string_received[index].upper()
        digit = "0"

if len(digit) > 1:
    new_message += current_message * int(digit)

print(f"Unique symbols used: {len(set(new_message))}", f"{new_message}", sep="\n")
