numbers_received = input().split()
alphabet_positions = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10',
                      'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19',
                      't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}

total_sum = 0

for el in numbers_received:
    number = int(el[1: -1])
    if el[0].isupper():
        total_sum += number / int(alphabet_positions[el[0].lower()])
    elif el[0].islower():
        total_sum += number * int(alphabet_positions[el[0].lower()])
    if el[-1].isupper():
        total_sum -= int(alphabet_positions[el[-1].lower()])
    elif el[-1].islower():
        total_sum += int(alphabet_positions[el[-1].lower()])

total_sum = round(total_sum, 2)

print(f"{total_sum:.2f}")