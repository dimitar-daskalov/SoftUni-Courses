price_without_taxes = 0
total_amount_of_taxes = 0
total_price_with_taxes = 0

prices_received = input()

while not prices_received == "special" and not prices_received == "regular":
    prices_received = float(prices_received)
    if prices_received < 0:
        print("Invalid price!")
    else:
        price_without_taxes += prices_received
        total_amount_of_taxes += prices_received * 0.20
    prices_received = input()
total_price_with_taxes = price_without_taxes + total_amount_of_taxes
if not total_price_with_taxes == 0:
    print("Congratulations you've just bought a new computer!", f"Price without taxes: {price_without_taxes:.2f}$", f"Taxes: {total_amount_of_taxes:.2f}$", sep="\n")
if prices_received == "special":
    total_price_with_taxes = (price_without_taxes + total_amount_of_taxes) - ((price_without_taxes + total_amount_of_taxes) * 0.10)
if not total_price_with_taxes == 0:
    print("-----------", f"Total price: {total_price_with_taxes:.2f}$", sep="\n")
if total_price_with_taxes == 0:
    print("Invalid order!")