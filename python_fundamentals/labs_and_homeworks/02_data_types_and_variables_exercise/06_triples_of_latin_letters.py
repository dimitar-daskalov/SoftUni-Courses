n = int(input())

for i in range(n):
    for k in range(n):
        for m in range(n):
            print(f"{chr(i + 97)}{chr(k + 97)}{chr(m + 97)}")