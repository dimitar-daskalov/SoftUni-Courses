budget_of_the_group = int(input())
season = input()
count_fishermen = int(input())

rent = 0

if season == "Spring":
    rent = 3000
    if count_fishermen <= 6:
        rent = rent - (rent * 0.10)
    elif 7 <= count_fishermen <= 11:
        rent = rent - (rent * 0.15)
    elif count_fishermen >= 12:
        rent = rent - (rent * 0.25)
elif season == "Summer" or season == "Autumn":
    rent = 4200
    if count_fishermen <= 6:
        rent = rent - (rent * 0.10)
    elif 7 <= count_fishermen <= 11:
        rent = rent - (rent * 0.15)
    elif count_fishermen >= 12:
        rent = rent - (rent * 0.25)
elif season == "Winter":
    rent = 2600
    if count_fishermen <= 6:
        rent = rent - (rent * 0.10)
    elif 7 <= count_fishermen <= 11:
        rent = rent - (rent * 0.15)
    elif count_fishermen >= 12:
        rent = rent - (rent * 0.25)
if (count_fishermen % 2 == 0) and (season != "Autumn"):
    rent = rent - (rent * 0.05)
if budget_of_the_group >= rent:
    money_left = budget_of_the_group - rent
    print(f"Yes! You have {money_left:.2f} leva left.")
elif budget_of_the_group < rent:
    money_needed = rent - budget_of_the_group
    print(f"Not enough money! You need {money_needed:.2f} leva.")