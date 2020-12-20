cards_received = input().split()
shuffles_made = int(input())
deck_middle = int(len(cards_received) / 2)

for _ in range(shuffles_made):
    result = []
    for index in range(deck_middle):
        first = cards_received[index]
        second = cards_received[index + deck_middle]

        result.append(first)
        result.append(second)

    cards_received = result

print(result)