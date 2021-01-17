chemical_elements_received = int(input())

unique_ch_elements = set()

for _ in range(chemical_elements_received):
    command = input().split()
    for el in command:
        unique_ch_elements.add(el)

for el in unique_ch_elements:
    print(el)