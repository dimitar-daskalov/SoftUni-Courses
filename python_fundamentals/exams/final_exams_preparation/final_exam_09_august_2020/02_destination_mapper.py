import re

text = input()

pattern = r'(=|/)(?P<destination>[A-Z][A-Za-z]{2,})\1'

matches = re.finditer(pattern, text)

travel_points = 0

valid_destinations = []

for match in matches:
    travel_points += len(match.group("destination"))
    valid_destinations.append(match.group("destination"))

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {travel_points}")