number_of_names = int(input())

unique_names_set = set()

for _ in range(number_of_names):
    unique_names_set.add(input())

for name in unique_names_set:
    print(name)
