num_lines = int(input())
summed_letters = 0

for i in range(num_lines):
    letters = ord(input())
    summed_letters += letters

print(f"The sum equals: {summed_letters}")