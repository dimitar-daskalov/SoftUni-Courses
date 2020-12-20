import re

text = input()

pattern = r"\b_([A-Za-z0-9]+)\b"

matches = re.finditer(pattern, text)
resulted_matches = []

for match in matches:
    resulted_matches.append(match[1])

print(",".join(resulted_matches))