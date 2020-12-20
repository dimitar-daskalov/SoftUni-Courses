string_received = input()
total_strength = 0
index = 0

while index < len(string_received):
    ch = string_received[index]
    if ch == ">":
        strength = int(string_received[index + 1])
        total_strength += strength
    else:
        if total_strength > 0:
            string_received = string_received[:index] + string_received[index + 1:]
            index -= 1
            total_strength -= 1
    index += 1

print(string_received)
