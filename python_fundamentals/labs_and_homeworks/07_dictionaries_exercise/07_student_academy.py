rows_received = int(input())

student_grades = {}
best_students = {}

for student_grade in range(rows_received):
    student = input()
    grade = float(input())
    if student not in student_grades:
        grade = [grade]
        student_grades[student] = grade
    else:
        student_grades[student].append(grade)

for key, value in student_grades.items():
    average_score = sum(student_grades[key]) / len(student_grades[key])
    if average_score >= 4.50:
        best_students[key] = average_score

ordered_students = dict(sorted(best_students.items(), key=lambda x: -x[1]))

for key, value in ordered_students.items():
    print(f"{key} -> {value:.2f}")