name = input()
total_grade = 0.0
excluded = 0
year = 1

while year <= 12:
    grade = float(input())

    if grade < 4.0:
        excluded += 1

        if excluded == 2:
            break
    else:
        total_grade += grade
        year += 1

if excluded == 2:
    print(f"{name} has been excluded at {year} grade")
else:
    year -= 1
    print(f"{name} graduated. Average grade: {(total_grade / year):.2f}")