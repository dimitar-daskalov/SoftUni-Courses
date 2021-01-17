number_of_students = int(input())
student_grades_dict = {}

for student in range(number_of_students):
    student_name, grade = input().split()
    grade = float(grade)
    if student_name not in student_grades_dict:
        student_grades_dict[student_name] = [grade]
    else:
        student_grades_dict[student_name].append(grade)

for key, value in student_grades_dict.items():
    average_grade = sum(value) / len(value)
    print(f"{key} -> {' '.join(f'{el:.2f}' for el in value)} (avg: {average_grade:.2f})")
