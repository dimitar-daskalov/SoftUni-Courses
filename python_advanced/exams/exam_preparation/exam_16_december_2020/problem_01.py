from collections import deque

males = [int(el) for el in input().split() if int(el) > 0]
females = deque(int(el) for el in input().split() if int(el) > 0)

matches_count = 0
while males and females:
    if females[0] % 25 == 0:
        females.popleft()
        if len(females) > 0:
            females.popleft()
    elif males[-1] % 25 == 0:
        males.pop()
        if len(males) > 0:
            males.pop()
    elif males[-1] == females[0]:
        males.pop()
        females.popleft()
        matches_count += 1
    else:
        females.popleft()
        males[-1] -= 2
        if males[-1] <= 0:
            males.pop()

print(f"Matches: {matches_count}")
if males:
    print(f"Males left: {', '.join(str(el) for el in males[::-1])}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(str(el) for el in females)}")
else:
    print(f"Females left: none")

