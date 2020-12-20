number_of_heroes = int(input())

MAX_HP = 100
MAX_MP = 200
heroes_dict = {}

for hero_index in range(number_of_heroes):
    hero_name, health_points, mana_points = input().split()
    health_points = int(health_points)
    mana_points = int(mana_points)
    heroes_dict[hero_name] = {"HP": health_points, "MP": mana_points}

command = input()
while not command == "End":
    command = command.split(" - ")
    action = command[0]
    if action == "CastSpell":
        hero_name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes_dict[hero_name]["MP"] >= mp_needed:
            heroes_dict[hero_name]["MP"] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes_dict[hero_name]["HP"] -= damage
        if heroes_dict[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name]['HP']} HP left!")
        else:
            del heroes_dict[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    elif action == "Recharge":
        hero_name = command[1]
        amount = int(command[2])
        if heroes_dict[hero_name]["MP"] + amount > MAX_MP:
            mana_recovered = MAX_MP - heroes_dict[hero_name]["MP"]
            heroes_dict[hero_name]["MP"] = MAX_MP
            print(f"{hero_name} recharged for {mana_recovered} MP!")
        else:
            heroes_dict[hero_name]["MP"] += amount
            print(f"{hero_name} recharged for {amount} MP!")
    elif action == "Heal":
        hero_name = command[1]
        amount = int(command[2])
        if heroes_dict[hero_name]["HP"] + amount > MAX_HP:
            health_recovered = MAX_HP - heroes_dict[hero_name]["HP"]
            heroes_dict[hero_name]["HP"] = MAX_HP
            print(f"{hero_name} healed for {health_recovered} HP!")
        else:
            heroes_dict[hero_name]["HP"] += amount
            print(f"{hero_name} healed for {amount} HP!")
    command = input()

sorted_heroes_dict = dict(sorted(heroes_dict.items(), key=lambda x: (-x[1]["HP"], x[0])))

for key, value in sorted_heroes_dict.items():
    print(key)
    print(f"  HP: {value['HP']}")
    print(f"  MP: {value['MP']}")
