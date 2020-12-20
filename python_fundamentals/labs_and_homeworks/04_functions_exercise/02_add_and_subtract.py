number_one = int(input())
number_two = int(input())
number_three = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(c, result):
    return result - c


def add_and_subtract(a, b, c):
    result = sum_numbers(a, b)
    subtract_result = subtract(c, result)

    print(subtract_result)


add_and_subtract(number_one, number_two, number_three)