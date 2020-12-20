import re

list_of_names = input()

regex = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"

matches = re.findall(regex, list_of_names)

print(" ".join(matches))