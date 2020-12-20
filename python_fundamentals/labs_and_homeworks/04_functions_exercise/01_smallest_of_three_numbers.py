number_one = int(input())
number_two = int(input())
number_three = int(input())


def smallest_number(one, two, three):
    result = min(one, two, three)

    return result


print(smallest_number(number_one, number_two, number_three))