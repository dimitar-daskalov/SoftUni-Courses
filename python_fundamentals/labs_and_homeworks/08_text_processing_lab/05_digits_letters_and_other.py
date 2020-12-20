string_received = input()

digits = ""
letters = ""
other = ""
for el in string_received:
    if el.isdigit():
        digits += el
    elif el.isalpha():
        letters += el
    else:
        other += el

print(digits, letters, other, sep="\n")