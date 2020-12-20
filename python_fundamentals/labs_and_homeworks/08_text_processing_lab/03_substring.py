word_to_remove = input()
word_received = input()

while word_to_remove in word_received:
    new_word_received = word_received.replace(word_to_remove, "")
    word_received = new_word_received

print(word_received)