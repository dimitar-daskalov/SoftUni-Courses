class ValueCannotBeNegative(Exception):
    pass


while True:
    number = int(input())
    if number > 0:
        number = int(input())
    else:
        raise ValueCannotBeNegative

