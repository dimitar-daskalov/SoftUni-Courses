number_of_words = int(input())

words_received_dict = {}

for el in range(number_of_words):
    word = input()
    synonym = input()
    if word not in words_received_dict:
        words_received_dict[word] = []
    words_received_dict[word].append(synonym)

for word in words_received_dict:
    print(f"{word} - {', '.join(words_received_dict[word])}")