import re

text = input()
pattern = r'(w{3}.[A-Za-z0-9]+([-\.][A-Za-z0-9]+)*(\.[a-z]+))'
matched_sites = []

while True:
    if not text:
        break
    else:
        matched_sites += re.findall(pattern, text)
        text = input()

for site in matched_sites:
    print(site[0])