years = int(input())

drink = ""

if years <= 14:
    drink = "toddy"
elif 14 < years <= 18:
    drink = "coke"
elif 18 < years <= 21:
    drink = "beer"
elif years > 21:
    drink = "whisky"

print(f"drink {drink}")