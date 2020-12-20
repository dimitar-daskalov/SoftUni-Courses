n1 = int(input())
n2 = int(input())

operator = input()
result = 0
number = ""

if operator == "+":
    result = n1 + n2
elif operator == "-":
    result = n1 - n2
elif operator == "*":
    result = n1 * n2
if result % 2 == 0:
    number = "even"
else:
    number = "odd"
if operator == "/" and n2 != 0:
    result = n1 / n2
elif operator == "%" and n2 != 0:
    result = n1 % n2

if operator == "+" or operator == "-" or operator == "*":
    print(f"{n1} {operator} {n2} = {result} - {number}")
elif operator == "/" and n2 != 0:
    print(f"{n1} / {n2} = {result:.2f}")
elif operator == "%" and n2 != 0:
    print(f"{n1} % {n2} = {result}")
else:
    print(f"Cannot divide {n1} by zero")