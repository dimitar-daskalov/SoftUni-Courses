budget = float(input())
price_1_kg_flour = float(input())

price_1_pack_of_eggs = price_1_kg_flour * 0.75
price_1_liter_milk = price_1_kg_flour * 1.25
price_for_250ml_milk = price_1_liter_milk / 4
price_of_one_cozonac = price_1_kg_flour + price_1_pack_of_eggs + price_for_250ml_milk

cozonacs = 0
coloured_eggs = 0

while price_of_one_cozonac <= budget:
    cozonacs += 1
    coloured_eggs += 3
    if cozonacs % 3 == 0:
        coloured_eggs -= cozonacs - 2
    budget -= price_of_one_cozonac


print(f"You made {cozonacs} cozonacs! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")