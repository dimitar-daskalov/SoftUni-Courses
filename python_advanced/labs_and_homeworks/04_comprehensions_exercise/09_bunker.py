categories_received = {category: [] for category in input().split(", ")}

lines_received = int(input())
quantity = 0
quality = 0

for _ in range(lines_received):
    category, item_name, quantity_and_quality = input().split(" - ")
    quantity_value, quality_value = quantity_and_quality.split(";")
    quantity_value = int(quantity_value.split(":")[1])
    quality_value = int(quality_value.split(":")[1])
    quantity += quantity_value
    quality += quality_value
    categories_received[category].append(item_name)

print(f"Count of items: {quantity}")
print(f"Average quality: {(quality / len(categories_received)):.2f}")
for key, value in categories_received.items():
    print(f"{key} -> {', '.join(el for el in value)}")