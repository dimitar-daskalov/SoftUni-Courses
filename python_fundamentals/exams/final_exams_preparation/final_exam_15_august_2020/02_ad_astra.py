import re

text = input()

pattern = r"(#|\|)(?P<item>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>[0-9][0-9]{0,3}|10000)\1"

matches = re.finditer(pattern, text)
calories_count = 0
items_list = []

for match in matches:
    calories_count += int(match.group("calories"))
    items_list.append([match.group("item"), (match.group("date")), match.group("calories")])

food_for_days = int(calories_count / 2000)
print(f"You have food to last you for: {food_for_days} days!")
for el in items_list:
    print(f"Item: {el[0]}, Best before: {el[1]}, Nutrition: {el[2]}")
