staying_period = int(input()) - 1
staying_place = input()
grade = input()

price = 0

if staying_place == "apartment":
    if staying_period < 10:
        price = (25 * staying_period) - ((25 * staying_period) * 0.30)
    elif 10 <= staying_period <= 15:
        price = (25 * staying_period) - ((25 * staying_period) * 0.35)
    elif staying_period > 15:
        price = (25 * staying_period) - ((25 * staying_period) * 0.50)
elif staying_place == "president apartment":
    if staying_period < 10:
        price = (35 * staying_period) - ((35 * staying_period) * 0.10)
    elif 10 <= staying_period <= 15:
        price = (35 * staying_period) - ((35 * staying_period) * 0.15)
    elif staying_period > 15:
        price = (35 * staying_period) - ((35 * staying_period) * 0.20)
elif staying_place == "room for one person":
    price = (18 * staying_period)

if grade == "positive":
    price += price * 0.25
elif grade == "negative":
    price = price - (price * 0.10)

print(f"{price:.2f}")