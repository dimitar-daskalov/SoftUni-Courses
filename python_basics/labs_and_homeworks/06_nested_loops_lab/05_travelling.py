while True:
    destination = input()

    if destination == "End":
        break
    minimal_money = float(input())

    money_collected = 0

    while money_collected < minimal_money:
        money = float(input())
        money_collected += money

    print(f"Going to {destination}!")