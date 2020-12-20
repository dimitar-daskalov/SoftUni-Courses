bed_price = float(input())

toilet_cat_price = float(input())

food_per_month = toilet_cat_price + (toilet_cat_price * 0.25)

toys_per_month = food_per_month - (food_per_month * 0.50)

veterinarian_month = toys_per_month + (toys_per_month * 0.10)

total_expenses_per_month = (toilet_cat_price + food_per_month + toys_per_month + veterinarian_month)

additional_expenses = total_expenses_per_month * 0.05

total_expenses_per_year = bed_price + (total_expenses_per_month * 12) + (additional_expenses * 12)

print(f"{total_expenses_per_year:.2f} lv.")