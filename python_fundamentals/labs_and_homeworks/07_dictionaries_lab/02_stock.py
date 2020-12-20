products_stock = input().split()
products_needed = input().split()

products_stock_dict = {}

for index in range(0, len(products_stock), 2):
    key = products_stock[index]
    value = int(products_stock[index + 1])
    products_stock_dict[key] = value
for product in products_needed:
    if product in products_stock_dict:
        print(f"We have {products_stock_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")



