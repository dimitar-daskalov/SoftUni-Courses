cars_number = int(input())

cars_set = set()

for _ in range(cars_number):
    command, car_number = input().split(", ")
    if command == "IN":
        cars_set.add(car_number)
    else:
        if cars_set:
            cars_set.remove(car_number)
if cars_set:
    for car_number in cars_set:
        print(car_number)
else:
    print(f"Parking Lot is Empty")