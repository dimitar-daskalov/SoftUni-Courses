first_number = int(input())
second_number = int(input())

magical_number = int(input())
sum_numbers = 0
counter_position = 0

is_found = False

for i in range(first_number, second_number + 1):
    for j in range(first_number, second_number + 1):
        sum_numbers = i + j
        counter_position += 1

        if sum_numbers == magical_number:
            first_number = i
            second_number = j
            is_found = True
            break

    if is_found:
        break

if sum_numbers == magical_number:
    print(f"Combination N:{counter_position} ({first_number} + {second_number} = {magical_number})")
else:
    print(f"{counter_position} combinations - neither equals {magical_number}")