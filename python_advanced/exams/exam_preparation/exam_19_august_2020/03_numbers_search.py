def numbers_searching(*numbers):
    num_list = sorted(numbers)
    duplicates = sorted(set([x for x in num_list if num_list.count(x) > 1]))
    values = set(range(num_list[0], (num_list[-1]+1)))
    missing = sorted(set(num_list) ^ values)
    return [missing, duplicates]

