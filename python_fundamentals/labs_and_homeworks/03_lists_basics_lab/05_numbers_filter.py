n = int(input())
even_integers = []
odd_integers = []
negative_integers = []
positive_integers = []

for i in range(n):
    received_integer = int(input())
    if received_integer % 2 == 0:
        even_integers.append(received_integer)
    if received_integer % 2 != 0:
        odd_integers.append(received_integer)
    if received_integer < 0:
        negative_integers.append(received_integer)
    if received_integer >= 0:
        positive_integers.append(received_integer)

command = input()
if command == "even":
    print(even_integers)
elif command == "odd":
    print(odd_integers)
elif command == "negative":
    print(negative_integers)
elif command == "positive":
    print(positive_integers)
