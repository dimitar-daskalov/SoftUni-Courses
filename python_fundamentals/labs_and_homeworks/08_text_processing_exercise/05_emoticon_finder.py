string_received = input()

el_needed = ":"
emoticons = ""

for char in range(len(string_received)):
    if string_received[char] == el_needed:
        if char + 1 == len(string_received) - 1:
            emoticons += string_received[char]
            emoticons += string_received[char + 1]
        else:
            emoticons += string_received[char]
            emoticons += string_received[char + 1]
            emoticons += ","

emoticons = emoticons.split(",")
for emoticon in emoticons:
    print(emoticon)
