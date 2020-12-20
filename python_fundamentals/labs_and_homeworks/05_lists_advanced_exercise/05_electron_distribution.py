number_of_electrons = int(input())
result = []
n = 0

while number_of_electrons > sum(result):
    n += 1
    formula = 2 * n ** 2
    electrons_left = number_of_electrons - sum(result)
    if electrons_left > formula:
        result.append(formula)
    else:
        result.append(electrons_left)

print(result)