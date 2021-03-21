def is_prime(num):
    if num <= 1:
        return False

    for number in range(2, num):
        if (num % number) == 0:
            return False
    return True


def get_primes(list_of_numbers: list):
    for num in list_of_numbers:
        if is_prime(num):
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))


