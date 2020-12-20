rent = int(input())

cake_price = rent * 0.20
beverages_price = cake_price - cake_price * 0.45
animator = rent / 3

print(rent + cake_price + beverages_price + animator)