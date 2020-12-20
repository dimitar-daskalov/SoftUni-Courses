age = float(input())
sex = input()

if age >= 16 and sex == "m":
    print("Mr.")
elif age < 16 and sex == "m":
    print("Master")
elif age >= 16 and sex == "f":
    print("Ms.")
elif age < 16 and sex == "f":
    print("Miss")