food_list = input().split()

food_dict = {}

for el in range(0, len(food_list), 2):
    key = food_list[el]
    value = int(food_list[el + 1])
    food_dict[key] = value

print(food_dict)