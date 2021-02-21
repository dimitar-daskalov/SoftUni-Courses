from .function_print import triangle_print


def triangle_calculation(number):
    [triangle_print(1, num + 1) for num in range(number)]
    [triangle_print(1, num + 1) for num in range(number - 2, -1, -1)]
