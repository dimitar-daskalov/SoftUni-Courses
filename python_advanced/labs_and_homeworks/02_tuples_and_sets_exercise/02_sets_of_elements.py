n_number, m_number = [int(number) for number in input().split()]

n_number_set = set()
m_number_set = set()

for _ in range(n_number):
    n_number_set.add(input())

for _ in range(m_number):
    m_number_set.add(input())

repeatable_elements = n_number_set.intersection(m_number_set)

for el in repeatable_elements:
    print(el)