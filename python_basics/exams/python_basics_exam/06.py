import math
count_airlines = int(input())
airline_passengers = 0
max_count_passengers = 0
name_of_the_biggest_company = ""

for days in range(1, count_airlines + 1):
    name_of_the_company = input()
    count_passengers = 0
    airline_passengers = 0
    count_flights = 0
    while name_of_the_company != "Finish":
        count_passengers = input()
        if count_passengers == "Finish":
            break
        count_flights += 1

        count_passengers = int(count_passengers)
        airline_passengers += count_passengers
    count_passengers = airline_passengers / count_flights
    if count_passengers > max_count_passengers:
        max_count_passengers = count_passengers
        name_of_the_biggest_company = name_of_the_company
    print(f"{name_of_the_company}: {math.floor(count_passengers)} passengers.")
print(f"{name_of_the_biggest_company} has most passengers per flight: {math.floor(max_count_passengers)}")