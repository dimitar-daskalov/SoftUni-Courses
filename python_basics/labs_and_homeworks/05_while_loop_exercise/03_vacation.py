money_needed = float(input())
money_available = float(input())
days = 0
spending = 0

while True:
    action = input()
    money = float(input())
    days += 1
    if action == "save":
        money_available += money
        spending = 0
    elif action == "spend":
        money_available -= money
        spending += 1
        if money_available < 0:
            money_available = 0

    if spending == 5:
        print(f"You can't save the money.")
        print(f"{days}")
        break
    if money_available >= money_needed:
        print(f"You saved the money for {days} days.")
        break