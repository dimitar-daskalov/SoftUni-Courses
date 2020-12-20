fire = input().split("#")

water = int(input())
effort = 0
total_fire = 0

print(f"Cells:")

for level_of_fire in fire:
    fire_parts = level_of_fire.split(" = ")
    if fire_parts[0] == "High":
        if 81 <= int(fire_parts[1]) <= 125:
            total_fire += int(fire_parts[1])
            if total_fire <= water:
                effort += int(fire_parts[1]) * 0.25
                print(f" - {int(fire_parts[1])}")
            else:
                total_fire -= int(fire_parts[1])
    elif fire_parts[0] == "Medium":
        if 51 <= int(fire_parts[1]) <= 80:
            total_fire += int(fire_parts[1])
            if total_fire <= water:
                effort += int(fire_parts[1]) * 0.25
                print(f" - {int(fire_parts[1])}")
            else:
                total_fire -= int(fire_parts[1])
    elif fire_parts[0] == "Low":
        if 1 <= int(fire_parts[1]) <= 50:
            total_fire += int(fire_parts[1])
            if total_fire <= water:
                effort += int(fire_parts[1]) * 0.25
                print(f" - {int(fire_parts[1])}")
            else:
                total_fire -= int(fire_parts[1])


print(f"Effort: {effort:.2f}", f"Total Fire: {total_fire}", sep="\n")