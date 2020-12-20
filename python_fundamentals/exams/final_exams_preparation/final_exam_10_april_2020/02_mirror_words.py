import re

text = input()

pattern = r'(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

matches = re.finditer(pattern, text)

valid_pairs = 0
valid_pairs_list = []

for match in matches:
    valid_pairs += 1
    if match.group(2) == match.group(3)[::-1]:
        valid_pairs_list.append(match.group(2))
        valid_pairs_list.append(match.group(3))

if valid_pairs == 0:
    print(f"No word pairs found!")
else:
    print(f"{valid_pairs} word pairs found!")

if len(valid_pairs_list) == 0:
    print(f"No mirror words!")
else:
    print("The mirror words are:")
    for index in range(0, len(valid_pairs_list), 2):
        if index + 1 == len(valid_pairs_list) - 1:
            print(f"{valid_pairs_list[index]} <=> {valid_pairs_list[index + 1]}", end="")
        else:
            print(f"{valid_pairs_list[index]} <=> {valid_pairs_list[index + 1]}, ", end="")