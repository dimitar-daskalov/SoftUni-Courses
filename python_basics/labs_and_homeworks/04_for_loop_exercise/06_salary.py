n = int(input())
salary = int(input())

for i in range(0, n):
    count = input()
    if count == "Facebook":
        salary -= 150
    if count == "Instagram":
        salary -= 100
    if count == "Reddit":
        salary -= 50

    if salary <= 0:
        break
if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")