budget = float(input())
season = input()
place = ""
money_spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        money_spent = budget * 0.30
    if season == "winter":
        place = "Hotel"
        money_spent = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        money_spent = budget * 0.40
    if season == "winter":
        place = "Hotel"
        money_spent = budget * 0.80
else:
    destination = "Europe"
    place = "Hotel"
    money_spent = budget * 0.90
print(f"Somewhere in {destination}")
print(f"{place} - {money_spent:.2f}")