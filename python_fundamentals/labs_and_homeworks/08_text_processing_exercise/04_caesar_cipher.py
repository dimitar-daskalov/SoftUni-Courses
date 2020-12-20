string_received = input()
encrypted_string = ""

for char in string_received:
    character_from_ascii = chr(ord(char) + 3)
    encrypted_string += character_from_ascii

print(encrypted_string)