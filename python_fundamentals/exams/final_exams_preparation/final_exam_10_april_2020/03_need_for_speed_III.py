number_of_cars = int(input())

cars_dict = {}

for cars_characteristics in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    cars_dict[car] = {"mileage": mileage, "fuel": fuel}

command = input()
while not command == "Stop":
    command = command.split(" : ")
    action = command[0]
    if action == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if cars_dict[car]["fuel"] >= fuel:
            cars_dict[car]["mileage"] += distance
            cars_dict[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_dict[car]["mileage"] >= 100000:
                del cars_dict[car]
                print(f"Time to sell the {car}!")
        else:
            print(f"Not enough fuel to make that ride")
    elif action == "Refuel":
        car = command[1]
        fuel = int(command[2])
        if cars_dict[car]["fuel"] + fuel > 75:
            current_fuel = cars_dict[car]["fuel"]
            print(f"{car} refueled with {75 - current_fuel} liters")
            cars_dict[car]["fuel"] = 75
        else:
            cars_dict[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif action == "Revert":
        car = command[1]
        kilometers = int(command[2])
        cars_dict[car]["mileage"] -= kilometers
        if cars_dict[car]["mileage"] <= 10000:
            cars_dict[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input()

sorted_cars_dict = dict(sorted(cars_dict.items(), key=lambda x: (-x[1]["mileage"], x[0])))

for key, value in sorted_cars_dict.items():
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")


