failed_threshold = int(input())
failed_grades = 0
counter_grades = 0
sum_grades = 0
last_problem = ""
is_enough = False

while failed_grades < failed_threshold:
    problem_name = input()
    if problem_name == "Enough":
        is_enough = True
        break
    grade = int(input())
    counter_grades += 1
    sum_grades += grade
    last_problem = problem_name

    if grade <= 4:
        failed_grades += 1

if is_enough == True:
    print(f"Average score: {(sum_grades / counter_grades):.2f}")
    print(f"Number of problems: {counter_grades}")
    print(f"Last problem: {last_problem}")
if failed_grades == failed_threshold:
    print(f"You need a break, {failed_grades} poor grades.")