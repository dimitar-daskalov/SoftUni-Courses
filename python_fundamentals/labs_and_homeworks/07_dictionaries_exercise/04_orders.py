dict_products_prices = {}
dict_products_quantity = {}


command = input()
while not command == "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in dict_products_prices:
        dict_products_quantity[name] = quantity
    else:

        dict_products_quantity[name] += quantity
    dict_products_prices[name] = price
    command = input()

for key in dict_products_prices:
    total_price = dict_products_prices[key] * dict_products_quantity[key]
    print(f"{key} -> {total_price:.2f}")