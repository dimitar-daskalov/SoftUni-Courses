from math_operator.calculating_operator import calculator

first_number, mathematical_sign, second_number = input().split()

print(calculator(float(first_number), int(second_number), mathematical_sign))