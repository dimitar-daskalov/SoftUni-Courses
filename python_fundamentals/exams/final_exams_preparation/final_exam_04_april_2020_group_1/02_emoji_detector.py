import re

text = input()

pattern = r'(([:]{2})([A-Z][a-z]{2,})([:]{2}))|(([*]{2})([A-Z][a-z]{2,})([*]{2}))'

matches = re.finditer(pattern, text)

cool_threshold = 1
for ch in text:
    if ch.isdigit():
        cool_threshold *= int(ch)
print(f"Cool threshold: {cool_threshold}")

valid_emojis = 0
matches_found = []
emoji_coolness_count = {}
for match in matches:
    valid_emojis += 1
    current_coolness = 0
    for ch in match[0]:
        if ch.isalpha():
            current_coolness += ord(ch)
        emoji_coolness_count[match[0]] = current_coolness

print(f"{valid_emojis} emojis found in the text. The cool ones are:")

for emoji, coolness in emoji_coolness_count.items():
    if coolness >= cool_threshold:
        print(emoji)
