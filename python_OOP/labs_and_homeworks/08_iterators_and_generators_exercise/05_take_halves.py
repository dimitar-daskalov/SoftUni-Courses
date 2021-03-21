def solution():
    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        numbers_list = []
        for num in seq:
            if len(numbers_list) == n:
                return numbers_list
            numbers_list.append(num)

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
