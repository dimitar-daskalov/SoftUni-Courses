def concatenate(*args):
    result = []
    result += [arg for arg in args]
    return "".join(el for el in result)

