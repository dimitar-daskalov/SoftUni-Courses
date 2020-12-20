price_of_strawberries_per_kg = float(input())
quantity_of_bananas_per_kg = float(input())
quantity_of_oranges_per_kg = float(input())
quantity_of_raspberries_per_kg = float(input())
quantity_of_strawberries_per_kg = float(input())

price_of_raspberries_per_kg = (price_of_strawberries_per_kg / 2)
price_of_oranges_per_kg = price_of_raspberries_per_kg - (price_of_raspberries_per_kg * 0.40)
price_of_bananas_per_kg = price_of_raspberries_per_kg - (price_of_raspberries_per_kg * 0.80)

total_price_for_strawberries = price_of_strawberries_per_kg * quantity_of_strawberries_per_kg
total_price_for_bananas = price_of_bananas_per_kg * quantity_of_bananas_per_kg
total_price_for_oranges = price_of_oranges_per_kg * quantity_of_oranges_per_kg
total_price_for_raspberries = price_of_raspberries_per_kg * quantity_of_raspberries_per_kg

total_price = (total_price_for_strawberries + total_price_for_bananas + total_price_for_oranges + total_price_for_raspberries)

print(total_price)