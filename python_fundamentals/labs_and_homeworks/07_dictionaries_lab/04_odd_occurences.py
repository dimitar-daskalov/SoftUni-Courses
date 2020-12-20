occurences_list = input().split()

occurences_dict = {}
quantity = 1

for el in occurences_list:
    el = el.lower()
    if el in occurences_dict:
        occurences_dict[el] += 1
    else:
        occurences_dict[el] = quantity

for value in occurences_dict:
    if not occurences_dict[value] % 2 == 0:
        print(value, end=" ")


