product_received = input()

quantity_received = int(input())


def total_cost(product, quantity):
    result = 0
    if product == "coffee":
        result = quantity * 1.50
    elif product == "water":
        result = quantity * 1.00
    elif product == "coke":
        result = quantity * 1.40
    elif product == "snacks":
        result = quantity * 2.00

    return format(result, ".2f")


print(total_cost(product_received, quantity_received))


