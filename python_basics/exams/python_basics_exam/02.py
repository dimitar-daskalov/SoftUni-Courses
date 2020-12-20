sleeve_size = float(input())
front_size = float(input())
material = input()
tie = input()

shirt_size = (((sleeve_size * 2) + (front_size * 2)) + (((sleeve_size * 2) + (front_size * 2)) * 0.10)) / 100

if material == "Linen":
    price = shirt_size * 15
elif material == "Cotton":
    price = shirt_size * 12
elif material == "Denim":
    price = shirt_size * 20
elif material == "Twill":
    price = shirt_size * 16
else:
    price = shirt_size * 11

price = price + 10

if tie == "Yes":
    price = price + (price * 0.20)

print(f"The price of the shirt is: {price:.2f}lv.")