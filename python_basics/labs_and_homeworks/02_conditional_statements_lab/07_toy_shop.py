price_of_the_tour = float(input())
count_of_puzzles = int(input())
count_of_talking_dolls = int(input())
count_of_fluffy_bears = int(input())
count_of_minions = int(input())
count_of_trucks = int(input())

puzzle = 2.60
talking_doll = 3
fluffy_bear = 4.10
minion = 8.20
truck = 2

puzzles_total_price = puzzle * count_of_puzzles
talking_dolls_total_price = talking_doll * count_of_talking_dolls
fluffy_bears_total_price = fluffy_bear * count_of_fluffy_bears
minions_total_price = minion * count_of_minions
trucks_total_price = truck * count_of_trucks

total_price = (puzzles_total_price + talking_dolls_total_price \
              + fluffy_bears_total_price + minions_total_price + trucks_total_price) * 0.9

total_count_of_toys = count_of_puzzles + count_of_talking_dolls \
                      + count_of_fluffy_bears + count_of_minions + count_of_trucks

if total_count_of_toys >= 50:
    discount = total_price * 0.25
    total_price = total_price - discount

if total_price >= price_of_the_tour:
    money_left = total_price - price_of_the_tour
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = abs(total_price - price_of_the_tour)
    print(f"Not enough money! {money_needed:.2f} lv needed.")