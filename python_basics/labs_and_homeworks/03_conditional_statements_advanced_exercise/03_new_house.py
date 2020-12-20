flower_type = input()
flower_count = int(input())
budget = int(input())

price = 0

if flower_type == "Roses":
    if flower_count > 80:
        price = (flower_count * 5) - ((flower_count * 5) * 0.10)
    else:
        price = (flower_count * 5)
elif flower_type == "Dahlias":
    if flower_count > 90:
        price = (flower_count * 3.80) - ((flower_count * 3.80) * 0.15)
    else:
        price = (flower_count * 3.80)
elif flower_type == "Tulips":
    if flower_count > 80:
        price = (flower_count * 2.80) - ((flower_count * 2.80) * 0.15)
    else:
        price = (flower_count * 2.80)
elif flower_type == "Narcissus":
    if flower_count < 120:
        price = (flower_count * 3) + ((flower_count * 3) * 0.15)
    else:
        price = (flower_count * 3)
elif flower_type == "Gladiolus":
    if flower_count < 80:
        price = (flower_count * 2.50) + ((flower_count * 2.50) * 0.2)
    else:
        price = (flower_count * 2.50)

if budget >= price:
    money_left = budget - price
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {money_left:.2f} leva left.")
elif price > budget:
    money_needed = price - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")