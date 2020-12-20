change = float(input())

counter_coins = 0

change_in_coins = change * 100

while True:
    counter_coins += 1

    if change_in_coins >= 200:
        change_in_coins -= 200
    elif change_in_coins >= 100:
        change_in_coins -= 100
    elif change_in_coins >= 50:
        change_in_coins -= 50
    elif change_in_coins >= 20:
        change_in_coins -= 20
    elif change_in_coins >= 10:
        change_in_coins -= 10
    elif change_in_coins >= 5:
        change_in_coins -= 5
    elif change_in_coins >= 2:
        change_in_coins -= 2
    elif change_in_coins >= 1:
        change_in_coins -= 1

    if change_in_coins < 1:
        break
print(counter_coins)