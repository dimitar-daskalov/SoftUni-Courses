steps_needed = 10000
sum_steps_made = 0

while sum_steps_made < steps_needed:
    command = input()
    if command == "Going home":
        steps_home = int(input())
        sum_steps_made += steps_home
        if sum_steps_made < steps_needed:
            diff = steps_needed - sum_steps_made
            print(f"{diff} more steps to reach goal.")
        break
    steps_made = int(command)
    sum_steps_made += steps_made

    if sum_steps_made >= steps_needed:
        break
if sum_steps_made >= steps_needed:
    diff = sum_steps_made - steps_needed
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")