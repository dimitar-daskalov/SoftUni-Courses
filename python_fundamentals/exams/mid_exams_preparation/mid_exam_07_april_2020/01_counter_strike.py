energy = int(input())
won_battles = 0

command = input()
while energy >= 0:
    if command == "End of battle":
        break
    else:
        distance = int(command)
    if energy >= distance:
        energy -= distance
        won_battles += 1
    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        break
    if won_battles % 3 == 0:
        energy += won_battles

    command = input()

if command == "End of battle" and energy >= 0:
    print(f"Won battles: {won_battles}. Energy left: {energy}")