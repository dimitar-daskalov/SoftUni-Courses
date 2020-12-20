numbers_received = input().split(", ")
list_indexes_even = []

for index, number in enumerate(numbers_received):
    if int(number) % 2 == 0:
        list_indexes_even.append(index)

print(list_indexes_even)