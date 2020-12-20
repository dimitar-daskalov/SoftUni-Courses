day_events = input().split("|")
initial_energy = 100
initial_coins = 100

for event in day_events:
    event_received = event.split("-")
    current_event_ingredient = event_received[0]
    value_number = int(event_received[1])

    if current_event_ingredient == "rest":
        if (value_number + initial_energy) > 100:
            print("You gained 0 energy.")
            print(f"Current energy: {initial_energy}.")
        else:
            initial_energy += value_number
            print(f"You gained {value_number} energy.")
            print(f"Current energy: {initial_energy}.")
    elif current_event_ingredient == "order":
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += value_number
            print(f"You earned {value_number} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        initial_coins -= value_number
        if initial_coins > 0:
            print(f"You bought {current_event_ingredient}.")
        else:
            print(f"Closed! Cannot afford {current_event_ingredient}.")
            break

if initial_coins > 0:
    print(f"Day completed!", f"Coins: {initial_coins}", f"Energy: {initial_energy}", sep="\n")

