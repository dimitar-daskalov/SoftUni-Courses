string_received = input()
current_char = ""
last_char = ""
new_string_received = ""
for index_char in range(len(string_received)):
    current_char = string_received[index_char]
    if not current_char == last_char:
        new_string_received += current_char
    last_char = current_char
print(new_string_received)