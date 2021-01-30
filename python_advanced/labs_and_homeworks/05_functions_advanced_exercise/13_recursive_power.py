def recursive_power(number, power):
    if power == 1:
        return number
    number *= recursive_power(number, power - 1)
    return number




