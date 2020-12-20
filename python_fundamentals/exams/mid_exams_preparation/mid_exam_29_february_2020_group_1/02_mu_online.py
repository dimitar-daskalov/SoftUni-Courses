dungeon_rooms = input().split("|")
health_points = 100
collected_bitcoins = 0
rooms = 0

for room in dungeon_rooms:
    command, value = room.split()
    value = int(value)
    rooms += 1
    if command == "potion":
        if health_points < 100:
            health_points += value
            if health_points > 100:
                healed_points = value - (health_points - 100)
                health_points = 100
                print(f"You healed for {healed_points} hp.", f"Current health: {health_points} hp.", sep="\n")
            else:
                print(f"You healed for {value} hp.", f"Current health: {health_points} hp.", sep="\n")
    elif command == "chest":
        print(f"You found {value} bitcoins.")
        collected_bitcoins += value
    else:
        health_points -= value
        if health_points > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {rooms}")
            break
if health_points > 0:
    print(f"You've made it!", f"Bitcoins: {collected_bitcoins}", f"Health: {health_points}", sep="\n")