quantity_per_type = int(input())
days_left_until_christmas = int(input())

ornament_set = 2
tree_skirt_per_peace = 5
tree_garlands_per_peace = 3
tree_lights_per_peace = 15

christmas_spirit = 0
budget = 0

for days in range(1, days_left_until_christmas + 1):
    if days % 11 == 0:
        quantity_per_type += 2
    if days % 2 == 0:
        budget += ornament_set * quantity_per_type
        christmas_spirit += 5
    if days % 3 == 0:
        budget += tree_skirt_per_peace * quantity_per_type
        budget += tree_garlands_per_peace * quantity_per_type
        christmas_spirit += 13
    if days % 5 == 0:
        budget += tree_lights_per_peace * quantity_per_type
        christmas_spirit += 17
        if days % 3 == 0:
            christmas_spirit += 30
    if days % 10 == 0:
        christmas_spirit -= 20
        budget += tree_skirt_per_peace * 1
        budget += tree_garlands_per_peace * 1
        budget += tree_lights_per_peace * 1
if days_left_until_christmas % 10 == 0:
    christmas_spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")