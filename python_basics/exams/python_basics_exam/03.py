import math

cat_breed = input()
cat_sex = input()

if cat_breed == "British Shorthair":
    if cat_sex == "m":
        months = (13 * 12) / 6
    else:
        months = (14  * 12) / 6
elif cat_breed == "Siamese":
    if cat_sex == "m":
        months = (15 * 12) / 6
    else:
        months = (16 * 12) / 6
elif cat_breed == "Persian":
    if cat_sex == "m":
        months = (14 * 12) / 6
    else:
        months = (15 * 12) / 6
elif cat_breed == "Ragdoll":
    if cat_sex == "m":
        months = (16 * 12) / 6
    else:
        months = (17 * 12) / 6
elif cat_breed == "American Shorthair":
    if cat_sex == "m":
        months = (12 * 12) / 6
    else:
        months = (13 * 12) / 6
elif cat_breed == "Siberian":
    if cat_sex == "m":
        months = (11 * 12) / 6
    else:
        months = (12 * 12) / 6
else:
    print(f"{cat_breed} is invalid cat!")

if cat_breed == "British Shorthair" or cat_breed == "Siamese" or cat_breed == "Persian" or cat_breed == "Ragdoll" or cat_breed == "American Shorthair" or cat_breed == "Siberian":
    print(f"{math.floor(months)} cat months")