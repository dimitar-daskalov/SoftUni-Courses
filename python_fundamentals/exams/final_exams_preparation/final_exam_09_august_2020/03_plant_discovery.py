number_of_plants = int(input())

plants_dict = {}

for plant_received in range(number_of_plants):
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    plants_dict[plant] = {"rarity": rarity, "rating": []}

command = input()
while not command == "Exhibition":
    command = command.split(": ")
    action = command[0]
    if action == "Rate":
        plant, rating = command[1].split(" - ")
        rating = int(rating)
        if plant in plants_dict:
            plants_dict[plant]["rating"].append(rating)
        else:
            print("error")
    elif action == "Update":
        plant, new_rarity = command[1].split(" - ")
        new_rarity = int(new_rarity)
        if plant in plants_dict:
            plants_dict[plant]["rarity"] = new_rarity
        else:
            print("error")
    elif action == "Reset":
        plant = command[1]
        if plant in plants_dict:
            plants_dict[plant]["rating"].clear()
        else:
            print("error")
    command = input()

for plant, value in plants_dict.items():
    if len(value["rating"]) == 0:
        value["rating"] = 0
    else:
        value["rating"] = (sum(value["rating"]) / len(value["rating"]))

sorted_plants_dict = dict(sorted(plants_dict.items(), key=lambda x: (-x[1]["rarity"], -x[1]["rating"])))

print(f"Plants for the exhibition:")
for plant, value in sorted_plants_dict.items():
    print(f"- {plant}; Rarity: {value['rarity']}; Rating: {value['rating']:.2f}")