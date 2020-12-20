string_received = input()
dict_string_received = {}
quantity = 1

for char in string_received:
    key = char
    value = quantity
    if char in dict_string_received:
        dict_string_received[key] += 1
    else:
        dict_string_received[key] = value

for key, value in dict_string_received.items():
    if key != " ":
        print(f"{key} -> {value}")