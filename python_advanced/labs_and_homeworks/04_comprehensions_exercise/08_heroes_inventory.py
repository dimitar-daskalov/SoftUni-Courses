heroes = {hero_name: [] for hero_name in input().split(", ")}

command = input()
while not command == "End":
    hero_name, item, cost = command.split("-")
    if item not in heroes[hero_name]:
        heroes[hero_name].append(item)
        heroes[hero_name].append(cost)
    command = input()
    
for key, value in heroes.items():
    price = [int(value) for value in value if value.isdecimal()]
    print(f'{key} -> Items: {len(heroes[key]) // 2}, Cost: {sum(price)}')
