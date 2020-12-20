number = int(input())
positive_integers = []
negative_integers = []

for i in range(number):
    received_integer = int(input())
    if received_integer >= 0:
        positive_integers.append(received_integer)
    else:
        negative_integers.append(received_integer)

print(positive_integers, negative_integers, sep="\n")
print(f"Count of positives: {len(positive_integers)}. Sum of negatives: {sum(negative_integers)}")