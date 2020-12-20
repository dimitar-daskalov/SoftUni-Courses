import re

text = input()

pattern = r'>>(?P<product>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)'
total_spend = 0

print(f"Bought furniture:")
while not text == "Purchase":
    match = re.fullmatch(pattern, text)

    if match is None:
        text = input()
        continue

    print(match.group("product"))
    price = float(match.group("price"))
    quantity = int(match.group("quantity"))
    total_spend += price * quantity
    text = input()

print(f"Total money spend: {total_spend:.2f}")
