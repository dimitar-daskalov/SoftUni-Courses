lost_fight_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

shield_broken = 0
money_spent = 0

for battle in range(1, lost_fight_count + 1):
    if battle % 2 == 0:
        money_spent += helmet_price
    if battle % 3 == 0:
        money_spent += sword_price
    if battle % 6 == 0:
        shield_broken += 1
        money_spent += shield_price
        if shield_broken % 2 == 0:
            money_spent += armor_price

print(f"Gladiator expenses: {money_spent:.2f} aureus")