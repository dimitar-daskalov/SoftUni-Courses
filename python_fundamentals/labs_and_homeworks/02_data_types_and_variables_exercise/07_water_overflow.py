times_received = int(input())
tank_capacity = 255
filled_liters = 0

for i in range(1, times_received + 1):
    quantities = int(input())
    filled_liters += quantities
    if filled_liters > tank_capacity:
        print("Insufficient capacity!")
        filled_liters -= quantities
print(filled_liters)