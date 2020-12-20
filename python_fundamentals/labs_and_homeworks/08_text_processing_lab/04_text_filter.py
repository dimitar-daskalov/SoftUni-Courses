ban_list = input().split(", ")
text = input()

for word in ban_list:
    if word in text:
        replaced = len(word) * "*"
        new_text = text.replace(word, replaced)
        text = new_text
print(text)
