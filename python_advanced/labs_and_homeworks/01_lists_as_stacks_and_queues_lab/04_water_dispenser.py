from collections import deque

people_who_want_water = deque()

water_liters = int(input())

person = input()
while not person == "Start":
    people_who_want_water.append(person)
    person = input()

command = input()
while not command == "End":
    if command.startswith("refill"):
        refillable_liters = int(command.split()[1])
        water_liters += refillable_liters
    else:
        liters_spent = int(command)
        if people_who_want_water:
            if water_liters >= liters_spent:
                water_liters -= liters_spent
                print(f"{people_who_want_water.popleft()} got water")
            else:
                print(f"{people_who_want_water.popleft()} must wait")
    command = input()

print(f"{water_liters} liters left")