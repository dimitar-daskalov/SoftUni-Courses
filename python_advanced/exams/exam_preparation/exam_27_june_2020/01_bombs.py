from collections import deque

bomb_effects = deque(int(el) for el in input().split(", "))
bomb_casings = [int(el) for el in input().split(", ")]

bomb_values = {40: "datura_bomb", 60: "cherry_bomb", 120: "smoke_decoy_bomb"}
bombs_count = {"datura_bomb": 0, "cherry_bomb": 0, "smoke_decoy_bomb": 0}
bomb_pouch_filled = False

while bomb_effects and bomb_casings:
    current_sum = bomb_effects[0] + bomb_casings[-1]
    if bombs_count["datura_bomb"] >= 3 and bombs_count["cherry_bomb"] >= 3 and bombs_count["smoke_decoy_bomb"] >= 3:
        bomb_pouch_filled = True
        break
    elif current_sum in bomb_values:
        current_bomb_created = bomb_values[current_sum]
        bombs_count[current_bomb_created] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

if bomb_pouch_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {'empty' if not bomb_effects else ', '.join(map(str, bomb_effects))}")
print(f"Bomb Casings: {'empty' if not bomb_casings else ', '.join(map(str, bomb_casings))}")

print(f"Cherry Bombs: {bombs_count['cherry_bomb']}",
      f"Datura Bombs: {bombs_count['datura_bomb']}",
      f"Smoke Decoy Bombs: {bombs_count['smoke_decoy_bomb']}", sep="\n")