import math

income = float(input())
average_grade = float(input())
minimal_salary = float(input())

social_scholarship = 0
perfect_grade_scholarship = 0

if income < minimal_salary and average_grade > 4.50:
    social_scholarship = math.floor(minimal_salary * 0.35)
if average_grade >= 5.50:
    perfect_grade_scholarship = math.floor(average_grade * 25)
if social_scholarship == 0 and perfect_grade_scholarship == 0:
    print("You cannot get a scholarship!")

if perfect_grade_scholarship != 0 or social_scholarship != 0:
    if social_scholarship <= perfect_grade_scholarship:
        print(f"You get a scholarship for excellent results {perfect_grade_scholarship} BGN")
    elif social_scholarship > perfect_grade_scholarship:
        print(f"You get a Social scholarship {social_scholarship} BGN")