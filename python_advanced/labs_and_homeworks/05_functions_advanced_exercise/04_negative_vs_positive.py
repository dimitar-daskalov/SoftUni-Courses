numbers = [int(el) for el in input().split()]

negatives = sum(filter(lambda x: x <= 0, numbers))
positives = sum(filter(lambda x: x > 0, numbers))

print(negatives, positives, sep="\n")
if abs(negatives) > positives:
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")