first_employee = int(input())
second_employee = int(input())
third_employee = int(input())

students_count = int(input())
students_per_day = first_employee + second_employee + third_employee
worked_hours = 0

while students_count > 0:
    worked_hours += 1
    if worked_hours % 4 == 0:
        worked_hours += 1
    students_count -= students_per_day

print(f"Time needed: {worked_hours}h.")

