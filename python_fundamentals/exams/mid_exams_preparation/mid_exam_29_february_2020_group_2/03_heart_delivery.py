neighbourhood = [int(house) for house in input().split("@")]

position = 0
command = input()
while not command == "Love!":
    length = int(command.split()[1])
    position += length
    if position in range(len(neighbourhood)):
        if neighbourhood[position] == 0:
            print(f"Place {position} already had Valentine's day.")
        elif neighbourhood[position] >= 2:
            neighbourhood[position] -= 2
            if neighbourhood[position] == 0:
                print(f"Place {position} has Valentine's day.")
    else:
        position = 0
        if neighbourhood[position] == 0:
            print(f"Place {position} already had Valentine's day.")
        elif neighbourhood[position] >= 2:
            neighbourhood[position] -= 2
            if neighbourhood[position] == 0:
                print(f"Place {position} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {position}.")

if sum(neighbourhood) == 0:
    print(f"Mission was successful.")
else:
    counter = [house for house in neighbourhood if house > 0]
    print(f"Cupid has failed {len(counter)} places.")