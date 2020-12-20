first_list = input().split(", ")
second_string = input()

unique_elements = []

for el in first_list:
    print(second_string.find(el))
    if second_string.find(el) != -1:
        unique_elements.append(el)

print(unique_elements)