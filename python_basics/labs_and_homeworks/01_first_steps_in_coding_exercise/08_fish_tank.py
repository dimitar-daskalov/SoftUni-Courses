length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percent_of_volume_filled = float(input())

volume = int(length_in_cm * width_in_cm * height_in_cm)
all_liters = volume * 0.001
percent = percent_of_volume_filled * 0.01

liters_of_water = all_liters * (1 - percent)
print(liters_of_water)