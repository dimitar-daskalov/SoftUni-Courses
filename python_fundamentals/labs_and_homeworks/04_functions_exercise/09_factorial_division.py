def factorial_numbers(first_num, second_num):
    first_factorial = 1
    second_factorial = 1

    for factorial_one in range(1, first_num + 1):
        first_factorial = first_factorial * factorial_one

    for factorial_two in range(1, second_num + 1):
        second_factorial = second_factorial * factorial_two

    result = first_factorial / second_factorial
    print(f"{result:.2f}")


number_one = int(input())
number_two = int(input())

factorial_numbers(number_one, number_two)