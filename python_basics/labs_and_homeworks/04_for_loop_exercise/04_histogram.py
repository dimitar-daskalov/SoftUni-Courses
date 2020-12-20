n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

for position in range(0, n):
    number = int(input())
    if number < 200:
        count_p1 += 1
        p1 = (count_p1 / n) * 100
    elif 200 <= number <= 399:
        count_p2 += 1
        p2 = (count_p2 / n) * 100
    elif 400 <= number <= 599:
        count_p3 += 1
        p3 = (count_p3 / n) * 100
    elif 600 <= number <= 799:
        count_p4 += 1
        p4 = (count_p4 / n) * 100
    else:
        count_p5 += 1
        p5 = (count_p5 / n) * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")