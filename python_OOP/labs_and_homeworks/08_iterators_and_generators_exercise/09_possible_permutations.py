from itertools import permutations


def possible_permutations(numbers: list):
    for p in permutations(numbers):
        yield list(p)


[print(n) for n in possible_permutations([1, 2, 3])]