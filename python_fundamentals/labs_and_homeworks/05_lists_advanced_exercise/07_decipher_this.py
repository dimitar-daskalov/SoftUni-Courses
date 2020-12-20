def replace_chr(word_received):
    word_received = list(word_received)
    word_received[0], word_received[-1] = word_received[-1], word_received[0]
    word_received = "".join(word_received)
    return word_received


def find_chr_ascii(word_received):
    ascii_code = ""
    for symbol in word_received:
        if symbol.isdigit():
            ascii_code += symbol
    return ascii_code


received_words = input().split()

for word in received_words:
    letter_ascii = find_chr_ascii(word)
    word = word.replace(letter_ascii, "")
    word = replace_chr(word)
    letter = chr(int(letter_ascii))
    word = letter + word
    print(word, end=" ")