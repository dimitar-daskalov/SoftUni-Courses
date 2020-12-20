neighbourhood_houses = [int(house) for house in input().split("@")]
command = input()
current_position = 0
last_position = 0

while not command == "Love!":
    split_command = command.split()
    current_position = int(split_command[1]) + last_position

    if current_position > len(neighbourhood_houses) - 1:
        current_position = 0
    last_position = current_position
    if neighbourhood_houses[current_position] <= 0:
        print(f"Place {current_position} already had Valentine's day.")
    else:
        neighbourhood_houses[current_position] -= 2
        if neighbourhood_houses[current_position] <= 0:
            print(f"Place {current_position} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {last_position}.")

if sum(neighbourhood_houses) > 0:
    count_houses = 0
    for el in neighbourhood_houses:
        if el > 0:
            count_houses += 1
    print(f"Cupid has failed {count_houses} places.")
else:
    print("Mission was successful.")
