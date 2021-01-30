from functools import reduce

operator_mapper = {
    "+": lambda x, b: x + b,
    "-": lambda x, b: x - b,
    "*": lambda x, b: x * b,
    "/": lambda x, b: x / b,
}


def operate(operator, *numbers):
    return reduce(operator_mapper[operator], numbers)


