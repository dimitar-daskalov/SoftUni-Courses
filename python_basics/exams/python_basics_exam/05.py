count_sea_excursions = int(input())
count_mountain_excursion = int(input())
profit = 0

packet_name = input()
while packet_name != "Stop":
    if packet_name == "sea" and count_sea_excursions > 0:
        count_sea_excursions -= 1
        profit += 680
    elif packet_name == "mountain" and count_mountain_excursion > 0:
        count_mountain_excursion -= 1
        profit += 499
    if count_sea_excursions == 0 and count_mountain_excursion == 0:
        break
    packet_name = input()

if count_sea_excursions == 0 and count_mountain_excursion == 0:
    print("Good job! Everything is sold.")
    print(f"Profit: {profit} leva.")
else:
    print(f"Profit: {profit} leva.")