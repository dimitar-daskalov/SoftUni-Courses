number_of_names = int(input())

odd_numbers_set = set()
even_numbers_set = set()

current_line = 0
for _ in range(number_of_names):
    current_line += 1
    name = input()
    summed_values = 0
    for ch in name:
        summed_values += ord(ch)
    divided_values = summed_values // current_line
    if divided_values % 2 != 0:
        odd_numbers_set.add(divided_values)
    else:
        even_numbers_set.add(divided_values)

if sum(odd_numbers_set) == sum(even_numbers_set):
    union_values = odd_numbers_set.union(even_numbers_set)
    print(f"{', '.join([str(number) for number in union_values])}")
elif sum(odd_numbers_set) > sum(even_numbers_set):
    difference_values = odd_numbers_set.difference(even_numbers_set)
    print(f"{', '.join([str(number) for number in difference_values])}")
elif sum(even_numbers_set) > sum(odd_numbers_set):
    symmetric_difference_values = odd_numbers_set.symmetric_difference(even_numbers_set)
    print(f"{', '.join([str(number) for number in symmetric_difference_values])}")