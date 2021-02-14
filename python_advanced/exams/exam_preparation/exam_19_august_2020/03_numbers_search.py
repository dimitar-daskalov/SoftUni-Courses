def numbers_searching(*numbers):
    numbers = sorted(numbers)
    smallest_number = min(numbers)
    biggest_number = max(numbers)
    duplicates = sorted(set([x for x in numbers if numbers.count(x) > 1]))
    numbers_set = set(range(smallest_number, biggest_number + 1))
    missing_numbers = set(numbers) ^ numbers_set
    return [max(missing_numbers), duplicates]

