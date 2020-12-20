month = input()
count_of_nights = int(input())

studio_price = 0
apartment_price = 0
total_sum_studio = 0
total_sum_apartment = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < count_of_nights <= 14:
        total_sum_studio = (studio_price * count_of_nights) - ((studio_price * count_of_nights) * 0.05)
    elif count_of_nights > 14:
        total_sum_studio = (studio_price * count_of_nights) - ((studio_price * count_of_nights) * 0.30)
    else:
        total_sum_studio = (studio_price * count_of_nights)
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if count_of_nights > 14:
        total_sum_studio = (studio_price * count_of_nights) - ((studio_price * count_of_nights) * 0.20)
    else:
        total_sum_studio = studio_price * count_of_nights
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    total_sum_studio = studio_price * count_of_nights
if count_of_nights > 14:
    total_sum_apartment = (apartment_price * count_of_nights) - ((apartment_price * count_of_nights) * 0.10)
else:
    total_sum_apartment = apartment_price * count_of_nights

print(f"Apartment: {total_sum_apartment:.2f} lv.")
print(f"Studio: {total_sum_studio:.2f} lv.")