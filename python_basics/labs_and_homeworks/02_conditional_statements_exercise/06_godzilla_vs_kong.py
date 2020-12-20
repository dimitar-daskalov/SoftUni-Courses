movie_budget = float(input())
count_of_stunts = int(input())
cost_of_1_clothing = float(input())
decor = movie_budget * 0.10
cost_of_clothing = count_of_stunts * cost_of_1_clothing
total_cost = cost_of_clothing + decor
if count_of_stunts > 150:
    total_cost = (cost_of_clothing - (cost_of_clothing * 0.10)) + decor
if total_cost > movie_budget:
    money_needed = abs(total_cost - movie_budget)
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
elif total_cost <= movie_budget:
    money_left = abs(total_cost - movie_budget)
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")