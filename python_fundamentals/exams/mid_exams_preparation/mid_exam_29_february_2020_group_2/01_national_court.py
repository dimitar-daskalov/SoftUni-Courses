first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
hours = 0

people_per_hour = first_employee + second_employee + third_employee

people_to_serve = int(input())

while people_to_serve > 0:
    hours += 1
    people_to_serve -= people_per_hour
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")