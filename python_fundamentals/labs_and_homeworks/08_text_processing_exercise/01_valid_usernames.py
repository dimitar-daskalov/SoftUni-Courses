strings_received = input().split(", ")
correct_words = []

for word in strings_received:
    if 3 <= len(word) <= 16:
        is_correct = True
        for c in word:
            if c.isdigit() is False and c.isalpha() is False and c != "_" and c != "-":
                is_correct = False
                break
        if is_correct:
            correct_words.append(word)

for word in correct_words:
    print(word)
