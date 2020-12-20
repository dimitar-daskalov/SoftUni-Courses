city = input()
sales = float(input())

price = 0

is_valid = False

if city == "Sofia":
    if 0 <= sales <= 500:
        price -= sales * 0.05
    elif 500 < sales <= 1000:
        price -= sales * 0.07
    elif 1000 < sales <= 10000:
        price -= sales * 0.08
    elif sales > 10000:
        price -= sales * 0.12
    else:
        is_valid = True
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        price -= sales * 0.055
    elif 500 < sales <= 1000:
        price -= sales * 0.08
    elif 1000 < sales <= 10000:
        price -= sales * 0.12
    elif sales > 10000:
        price -= sales * 0.145
    else:
        is_valid = True
elif city == "Varna":
    if 0 <= sales <= 500:
        price -= sales * 0.045
    elif 500 < sales <= 1000:
        price -= sales * 0.075
    elif 1000 < sales <= 10000:
        price -= sales * 0.1
    elif sales > 10000:
        price -= sales * 0.13
    else:
        is_valid = True
else:
    is_valid = True

if is_valid == True:
    print("error")
else:
    print(f"{(abs(price)):.2f}")