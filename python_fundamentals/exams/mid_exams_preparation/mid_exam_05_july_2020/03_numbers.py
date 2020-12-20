integers = [int(number) for number in input().split()]

average = sum(integers) / len(integers)

greater_numbers = [number for number in integers if number > average]
greater_numbers.sort()

if len(greater_numbers) == 0:
    print("No")
else:
    if len(greater_numbers) < 5:
        greater_numbers.sort(reverse=True)
    else:
        greater_numbers = greater_numbers[-5:]
        greater_numbers.sort(reverse=True)

print(" ".join(str(number) for number in greater_numbers))