string_received = input()

char_dict = {}

for ch in string_received:
    if ch not in char_dict:
        char_dict[ch] = 1
    else:
        char_dict[ch] += 1

for key in sorted(char_dict):
    print(f"{key}: {char_dict[key]} time/s")