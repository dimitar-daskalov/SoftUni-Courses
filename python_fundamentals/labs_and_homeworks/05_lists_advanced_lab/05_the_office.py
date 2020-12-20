employees_happiness = input().split()
happiness_factor = int(input())
happy_employees = 0
sum_average_happiness = 0

for employee in employees_happiness:
    sum_average_happiness += (int(employee) * happiness_factor)

average_happiness = sum_average_happiness / len(employees_happiness)

for employee in employees_happiness:
    if (int(employee) * happiness_factor) >= average_happiness:
        happy_employees += 1

if happy_employees >= len(employees_happiness) / 2:
    print(f"Score: {happy_employees}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_employees}/{len(employees_happiness)}. Employees are not happy!")
