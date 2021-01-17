from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())

bullets_stack = [int(bullet) for bullet in input().split()]
locks_queue = deque(int(bullet) for bullet in input().split())

intelligence_bounty = int(input())
is_succeeded = False
current_barrel_size = gun_barrel_size

while bullets_stack:
    current_lock = locks_queue[0]
    if bullets_stack[-1] <= current_lock:
        print("Bang!")
        locks_queue.popleft()
    else:
        print("Ping!")
    bullets_stack.pop()
    current_barrel_size -= 1
    if len(bullets_stack) > 0:
        if current_barrel_size == 0:
            print("Reloading!")
            current_barrel_size = gun_barrel_size
    intelligence_bounty -= bullet_price
    if len(locks_queue) == 0:
        is_succeeded = True
        break

if is_succeeded:
    print(f"{len(bullets_stack)} bullets left. Earned ${intelligence_bounty}")
else:
    print(f"Couldn't get through. Locks left: {len(locks_queue)}")