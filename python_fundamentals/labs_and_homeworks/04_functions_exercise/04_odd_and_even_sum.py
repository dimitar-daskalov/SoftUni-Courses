number_received = input()


def even_and_odd_sum(a):
    odd_sum = 0
    even_sum = 0
    for el in a:
        num = int(el)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


even_and_odd_sum(number_received)