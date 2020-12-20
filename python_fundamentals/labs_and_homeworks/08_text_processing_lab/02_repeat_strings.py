string_received = input().split()

concatenated_string = ""

for el in string_received:
    concatenated_string += el * len(el)

print(concatenated_string)