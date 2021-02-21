def calculator(num_1, num_2, sign):
    operations_mapper = {
        '+': num_1 + num_2,
        '-': num_1 - num_2,
        '*': num_1 * num_2,
        '/': num_1 / num_2,
        '^': num_1 ** num_2,
    }
    return f"{operations_mapper[sign]:.2f}"


