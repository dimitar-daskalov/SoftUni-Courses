age_of_lilly = int(input())
cost_of_washing_machine = float(input())
price_of_toy = int(input())
money_per_birthday = 0
count_of_toys = 0
money_collected = 0
counter = 0
for i in range(1, age_of_lilly+1):
    if i % 2 == 0:
        money_per_birthday += 10
        money_collected += money_per_birthday
        counter += 1
    else:
        count_of_toys += 1

total_collected = money_collected + (count_of_toys * price_of_toy) - counter

if total_collected >= cost_of_washing_machine:
    print(f"Yes! {total_collected - cost_of_washing_machine:.2f}")
else:
    print(f"No! {cost_of_washing_machine - total_collected:.2f}")