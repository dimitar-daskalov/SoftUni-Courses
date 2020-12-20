word_received = input()

while not word_received == "end":
    reversed_word = word_received[::-1]
    print(f"{word_received} = {reversed_word}")
    word_received = input()