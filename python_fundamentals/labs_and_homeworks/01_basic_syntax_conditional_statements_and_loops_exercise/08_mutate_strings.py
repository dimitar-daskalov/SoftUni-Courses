first_string = input()
second_string = input()

for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        for second_str_index in range(0, i + 1):
            print(second_string[second_str_index], end="")

        for first_str_index in range(i + 1, len(second_string)):
            print(first_string[first_str_index], end="")

        print()