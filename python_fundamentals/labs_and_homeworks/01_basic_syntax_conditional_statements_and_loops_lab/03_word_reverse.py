word_received = input()

for index in range(len(word_received) - 1, -1, -1):
    print(word_received[index], end="")
