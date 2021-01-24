start = int(input())
end = int(input())


def divisible_number(number):
    divisions = [num for num in range(2, 10 + 1)]
    for numbr in divisions:
        if number % numbr == 0:
            return True
    return False


print([number for number in range(start, end + 1) if divisible_number(number)])