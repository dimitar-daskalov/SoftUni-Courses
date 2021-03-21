def squares(n: int):
    return (x * x for x in range(1, n + 1))


print(list(squares(5)))
