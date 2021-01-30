def even_odd(*numbers):
    command = numbers[-1]
    mapper = {
        "even": filter(lambda x: x % 2 == 0, numbers[:-1]),
        "odd": filter(lambda x: x % 2 != 0, numbers[:-1]),
    }
    return list(mapper[command])
