n = int(input())
l = int(input())

for i in range(1, n + 1):
    for m in range(1, n + 1):
        for s in range(97, 97 + l):
            for w in range(97, 97 + l):
                for r in range(1, n + 1):
                    if r > i and r > m:
                        print(f"{i}{m}{chr(s)}{chr(w)}{r}", end=" ")