command = input()

cities_dict = {}
while not command == "Sail":
    city, population, gold = command.split("||")
    population = int(population)
    gold = int(gold)
    if city in cities_dict:
        cities_dict[city]["population"] += population
        cities_dict[city]["gold"] += gold
    else:
        cities_dict[city] = {"population": population, "gold": gold}
    command = input()

lines = input()
while not lines == "End":
    lines = lines.split("=>")
    action = lines[0]
    if action == "Plunder":
        town = lines[1]
        people = int(lines[2])
        gold = int(lines[3])
        cities_dict[town]["population"] -= people
        cities_dict[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities_dict[town]["population"] == 0 or cities_dict[town]["gold"] == 0:
            del cities_dict[town]
            print(f"{town} has been wiped off the map!")
    elif action == "Prosper":
        town = lines[1]
        gold = int(lines[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities_dict[town]["gold"] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {cities_dict[town]["gold"]} gold.')
    lines = input()

sorted_cities_dict = dict(sorted(cities_dict.items(), key=lambda x: (-x[1]["gold"], x[0])))

if len(sorted_cities_dict) == 0:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(sorted_cities_dict.keys())} wealthy settlements to go to:")
    for city, values in sorted_cities_dict.items():
        print(f"{city} -> Population: {values['population']} citizens, Gold: {values['gold']} kg")