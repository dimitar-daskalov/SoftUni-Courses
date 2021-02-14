from collections import deque
firework_effects = deque(int(el) for el in input().split(", ") if int(el) > 0)
explosive_power = [int(el) for el in input().split(", ") if int(el) > 0]

fireworks = {"Palm Firework": 0, "Willow Firework": 0, "Crossette Firework": 0}
is_full = False

while firework_effects and explosive_power:
    current_sum = firework_effects[0] + explosive_power[-1]
    if current_sum % 3 == 0 and current_sum % 5 == 0:
        fireworks["Crossette Firework"] += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif current_sum % 3 == 0 and current_sum % 5 != 0:
        fireworks["Palm Firework"] += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif current_sum % 5 == 0 and current_sum % 3 != 0:
        fireworks["Willow Firework"] += 1
        firework_effects.popleft()
        explosive_power.pop()
    else:
        firework_effects[0] -= 1
        if firework_effects[0] <= 0:
            firework_effects.popleft()
        else:
            firework_effects.append(firework_effects.popleft())
    if fireworks["Crossette Firework"] >= 3 and fireworks["Willow Firework"] >= 3 and fireworks["Palm Firework"] >= 3:
        is_full = True
        break

if is_full:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(str(effect) for effect in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(power) for power in explosive_power)}")
print(f"Palm Fireworks: {fireworks['Palm Firework']}",
      f"Willow Fireworks: {fireworks['Willow Firework']}",
      f"Crossette Fireworks: {fireworks['Crossette Firework']}", sep="\n")