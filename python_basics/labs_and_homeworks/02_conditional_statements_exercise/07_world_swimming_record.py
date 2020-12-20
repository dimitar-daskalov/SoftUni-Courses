import math

record = float(input())
distance_in_meters = float(input())
time_in_second_for_1_m = float(input())

distance_and_time = distance_in_meters * time_in_second_for_1_m

time_in_seconds = (math.floor(distance_in_meters / 15)) * 12.5

total_time_spent = (distance_and_time + time_in_seconds)

if total_time_spent >= record:
    seconds_needed = total_time_spent - record
    print(f"No, he failed! He was {seconds_needed:.2f} seconds slower.")
elif total_time_spent < record:
    print(f"Yes, he succeeded! The new world record is {total_time_spent:.2f} seconds.")