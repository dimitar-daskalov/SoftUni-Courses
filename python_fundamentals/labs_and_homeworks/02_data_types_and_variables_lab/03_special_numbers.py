number = int(input())

for num in range(1, number + 1):
    sum_digits = 0
    digits = str(num)
    for i in range(len(digits)):
        sum_digits += int(digits[i])

    if (sum_digits == 5) or (sum_digits == 7) or (sum_digits == 11):
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")