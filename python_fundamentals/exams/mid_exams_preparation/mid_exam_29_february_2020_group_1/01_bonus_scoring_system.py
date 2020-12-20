import sys

students_count = int(input())
lectures_count = int(input())
initial_bonus_score = int(input())
max_bonus = -sys.maxsize
max_attendances = 0

if lectures_count == 0 or students_count == 0:
    print(f"Max Bonus: {0}.", f"The student has attended {0} lectures.", sep="\n")
else:
    for student in range(1, students_count + 1):
        attendances = int(input())
        total_bonus = attendances / lectures_count * (5 + initial_bonus_score)
        if total_bonus > max_bonus:
            max_bonus = total_bonus
            max_attendances = attendances

    print(f"Max Bonus: {round(max_bonus)}.", f"The student has attended {max_attendances} lectures.", sep="\n")
