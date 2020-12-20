import re

received_numbers = input()

pattern = r"(\+359\s2\s\d{3}\s\d{4}|\+359\-2\-\d{3}\-\d{4})\b"

matches = re.findall(pattern, received_numbers)

print(", ".join(matches))