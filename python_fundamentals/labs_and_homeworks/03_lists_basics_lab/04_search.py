n = int(input())
word = input()
list_strings = []

for i in range(n):
    string_received = input()
    list_strings.append(string_received)

print(list_strings)

for j in range(len(list_strings) - 1, -1, -1):
    element = list_strings[j]
    if word not in element:
        list_strings.remove(element)

print(list_strings)
