from collections import deque

cups_queue = deque(int(cup) for cup in input().split())
bottles_list = [int(bottle) for bottle in input().split()]

wasted_water = 0
are_filled = True

current_cup = cups_queue[0]

while cups_queue:
    current_bottle = bottles_list[-1]
    if current_bottle - current_cup >= 0:
        wasted_water += current_bottle - current_cup
    bottles_list.pop()
    current_cup -= current_bottle
    if current_cup <= 0:
        cups_queue.popleft()
        if cups_queue:
            current_cup = cups_queue[0]
    if len(bottles_list) == 0:
        are_filled = False
        break

if are_filled:
    print(f"Bottles: {' '.join(str(bottle) for bottle in bottles_list)}")
else:
    print(f"Cups: {' '.join(str(cup) for cup in cups_queue)}")
print(f"Wasted litters of water: {wasted_water}")