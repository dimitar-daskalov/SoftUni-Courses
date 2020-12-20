rooms = int(input())
counter_free_chairs = 0
successful_room = 0

for room in range(1, rooms + 1):
    chairs_available = input().split()
    free_chairs = chairs_available[0]
    expected_people = chairs_available[1]
    spaces = list(free_chairs).count("X")
    if spaces < int(expected_people):
        print(f"{int(expected_people) - spaces} more chairs needed in room {room}")
    else:
        successful_room += 1
        counter_free_chairs += (spaces - int(expected_people))

if successful_room == rooms:
    print(f"Game On, {counter_free_chairs} free chairs left")
