string_one, string_two = input().split()
string_one_digits = []
string_two_digits = []
difference = []
total_sum = 0
for char in string_one:
    char = ord(char)
    string_one_digits.append(char)
for char in string_two:
    char = ord(char)
    string_two_digits.append(char)

products = sum(a * b for a, b in zip(string_one_digits, string_two_digits))

if len(string_one_digits) > len(string_two_digits):
    difference = string_one_digits[-(len(string_one_digits) - len(string_two_digits)):]
    total_sum = products + sum(difference)
elif len(string_one_digits) < len(string_two_digits):
    difference = string_two_digits[-(len(string_two_digits) - len(string_one_digits)):]
    total_sum = products + sum(difference)
else:
    total_sum = products

print(total_sum)
