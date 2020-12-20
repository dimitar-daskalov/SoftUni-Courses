money_received = input().split(", ")
number_of_beggars = int(input())

numbers = []

for num in money_received:
    numbers.append(int(num))

result_sum = [0] * number_of_beggars

for i in range(len(numbers)):
    index = i % number_of_beggars
    result_sum[index] += numbers[i]

print(result_sum)
