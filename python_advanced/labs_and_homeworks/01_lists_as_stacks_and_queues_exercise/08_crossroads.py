from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
cars_queue = deque()
passed = 0
are_safe = True

command = input()
while not command == "END":
    current_green_light_duration = green_light_duration
    current_free_window_duration = free_window_duration
    if command == "green":
        while current_green_light_duration > 0:
            if cars_queue:
                current_car = cars_queue[0]
                cars_queue.popleft()
                current_green_light_duration -= len(current_car)
                if current_green_light_duration >= 0:
                    passed += 1
                elif current_green_light_duration <= 0:
                    current_free_window_duration -= abs(current_green_light_duration)
                    if current_free_window_duration >= 0:
                        passed += 1
                    else:
                        print(f"A crash happened!", f"{current_car} was hit at {current_car[current_free_window_duration]}.", sep="\n")
                        are_safe = False
                        break
            else:
                are_safe = True
                break
    else:
        car = command
        cars_queue.append(car)
    if not are_safe:
        break
    command = input()

if are_safe:
    print(f"Everyone is safe.", f"{passed} total cars passed the crossroads.", sep="\n")