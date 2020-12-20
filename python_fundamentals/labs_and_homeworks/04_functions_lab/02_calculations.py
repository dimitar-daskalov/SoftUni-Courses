operator = input()
first_number = int(input())
second_number = int(input())


def operations(operate, first_num, second_num):
    if operate == "subtract":
        return int(first_num - second_num)
    elif operate == "add":
        return int(first_num + second_num)
    elif operate == "divide":
        return int(first_num / second_num)
    elif operate == "multiply":
        return int(first_num * second_num)


print(operations(operator, first_number, second_number))
