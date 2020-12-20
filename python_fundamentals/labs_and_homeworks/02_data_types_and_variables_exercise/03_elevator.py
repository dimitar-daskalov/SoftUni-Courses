people = int(input())
capacity = int(input())

courses_1 = people // capacity
courses_2 = people % capacity

if courses_2 != 0:
    print(courses_1 + 1)
else:
    print(courses_1)