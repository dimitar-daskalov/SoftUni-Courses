def list_manipulator(numbers_list, first_action, second_action, *args):
    numbers_received = list(args)
    if first_action == "add" and second_action == "beginning":
        numbers_list = numbers_received + numbers_list

    elif first_action == "add" and second_action == "end":
        numbers_list = numbers_list + numbers_received

    elif first_action == "remove" and second_action == "beginning":
        if numbers_received:
            numbers_received = int(numbers_received[0])
            numbers_list = numbers_list[numbers_received:]
        else:
            numbers_list = numbers_list[1:]
    elif first_action == "remove" and second_action == "end":
        if numbers_received:
            numbers_received = int(numbers_received[0])
            numbers_list = numbers_list[:-numbers_received]
        else:
            numbers_list = numbers_list[:-1]
    return numbers_list
