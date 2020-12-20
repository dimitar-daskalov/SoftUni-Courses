command = input()
courses = {}
while not command == "end":
    course, student = command.split(" : ")
    if course not in courses:
        student = [student]
        courses[course] = student
    else:
        courses[course].append(student)
    command = input()

sorted_courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))

for course, values in sorted_courses.items():
    print(f"{course}: {len(courses[course])}")
    for value in sorted(values):
        print(f"-- {value}")