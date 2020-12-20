import re

text = input()
word_given = input()
pattern = fr'\b{word_given}\b'

matches = re.findall(pattern, text, re.IGNORECASE)

print(len(matches))