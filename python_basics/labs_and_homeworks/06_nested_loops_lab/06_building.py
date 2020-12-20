count_floors = int(input())
count_rooms = int(input())

for floors in range(count_floors, 0, - 1):
    for rooms in range(count_rooms):
        if floors == count_floors:
            print(f'L{floors}{rooms}', end=" ")
        if floors % 2 == 0 and count_floors != floors:
            print(f'O{floors}{rooms}', end=" ")
        elif floors % 2 != 0 and count_floors != floors:
            print(f'A{floors}{rooms}', end=" ")
    print()