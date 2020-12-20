items_with_prices = input().split("|")

budget = float(input())
new_prices = []
sum_of_new_prices = 0
profit = 0
money_spend = 0

is_in_budget = False

for item in items_with_prices:
    item_and_price = item.split("->")
    item = item_and_price[0]
    price = float(item_and_price[1])

    if item == "Clothes" and price <= 50.00 and price <= (budget - money_spend):
        is_in_budget = True
    elif item == "Shoes" and price <= 35.00 and price <= (budget - money_spend):
        is_in_budget = True
    elif item == "Accessories" and price <= 20.50 and price <= (budget - money_spend):
        is_in_budget = True
    else:
        is_in_budget = False

    if is_in_budget:
        money_spend += price
        new_price = price * 0.40 + price
        new_prices.append(round(new_price, 2))

profit = money_spend * 0.40
money_collected = (budget - money_spend) + sum(new_prices)

for i in new_prices:
    print(f"{i:.2f}", end=" ")
print()

print(f"Profit: {profit:.2f}")

if money_collected >= 150:
    print("Hello, France!")
else:
    print("Time to go.")