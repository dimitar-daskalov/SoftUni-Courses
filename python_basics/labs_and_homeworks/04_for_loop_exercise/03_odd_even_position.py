import sys

n = int(input())

even_minimum_number = sys.maxsize
even_maximum_number = -sys.maxsize
odd_minimum_number = sys.maxsize
odd_maximum_number = -sys.maxsize
odd_sum = 0
even_sum = 0

for i in range(1, n+1):
    number = float(input())
    if i % 2 == 0:
        even_sum += number
        if number > even_maximum_number:
            even_maximum_number = number
        if number < even_minimum_number:
            even_minimum_number = number
    else:
        odd_sum += number
        if number > odd_maximum_number:
            odd_maximum_number = number
        if number < odd_minimum_number:
            odd_minimum_number = number
print(f"OddSum={odd_sum:.2f},")
if n == 0:
    print("OddMin=No,")
    print("OddMax=No,")
else:
    print(f"OddMin={odd_minimum_number:.2f},")
    print(f"OddMax={odd_maximum_number:.2f},")
print(f"EvenSum={even_sum:.2f},")
if n == 1 or n == 0:
    print("EvenMin=No,")
    print("EvenMax=No")
else:
    print(f"EvenMin={even_minimum_number:.2f},")
    print(f"EvenMax={even_maximum_number:.2f}")