count_of_days = int(input())
count_of_bakers = int(input())
count_of_cakes = int(input())
count_of_waffles = int(input())
count_of_pancakes = int(input())

cake_price = 45
waffle_price = 5.80
pancake_price = 3.20

cakes_sales_per_day = count_of_cakes * cake_price
waffles_sales_per_day = count_of_waffles * waffle_price
pancakes_sales_per_day = count_of_pancakes * pancake_price
Sales_per_day = (cakes_sales_per_day + waffles_sales_per_day + pancakes_sales_per_day) * count_of_bakers

total_turnover_received = Sales_per_day * count_of_days

print(total_turnover_received - total_turnover_received * 1/8)