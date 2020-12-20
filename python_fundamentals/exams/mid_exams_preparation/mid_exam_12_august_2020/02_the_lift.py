people_waiting = int(input())

wagons_available = [int(wagon) for wagon in input().split()]

people_on_the_current_wagon = 0
people_on_the_lift = 0
no_people_left = False

for index in range(len(wagons_available)):
    while 0 <= wagons_available[index] < 4:
        people_on_the_current_wagon += 4 - wagons_available[index]
        wagons_available[index] += 4 - wagons_available[index]
        if people_on_the_current_wagon + people_on_the_lift > people_waiting:
            people_on_the_current_wagon -= 4
            people_on_the_current_wagon += (people_waiting - people_on_the_lift)
            wagons_available[index] -= 4
            wagons_available[index] += (people_waiting - people_on_the_lift)
        if people_on_the_lift + people_on_the_current_wagon == people_waiting:
            no_people_left = True
            break

    people_on_the_lift += people_on_the_current_wagon
    if no_people_left:
        break
    people_on_the_current_wagon = 0

if people_waiting > people_on_the_lift:
    print(f"There isn't enough space! {people_waiting - people_on_the_lift} people in a queue!"
          , " ".join([str(el) for el in wagons_available]), sep="\n")

elif people_on_the_lift == people_waiting and sum(wagons_available) < 4 * len(wagons_available):
    print("The lift has empty spots!", " ".join([str(el) for el in wagons_available]), sep="\n")

elif people_on_the_lift == people_waiting and sum(wagons_available) == 4 * len(wagons_available):
    print(" ".join([str(el) for el in wagons_available]))




