n = int(input())
counter = 1
Flag_is_bigger_than_n = False
for rows in range(1, n + 1):
    for columns in range(1, rows + 1):
        if counter > n:
            Flag_is_bigger_than_n = True
            break
        print(str(counter) + " ", end="")
        counter += 1
    if Flag_is_bigger_than_n:
        break
    print()