import urllib.parse

tests = [
    'http://softuni.bg/',
    'https://softuni.bg:447/search?Query=pesho&Users=true#go',
    'http://google:443/',
]

for test in tests:
    actual = urllib.parse.urlsplit(test)
    if "." not in actual.hostname:
        print('Invalid URL')
        break
    elif not actual.query:
        print(f"""Protocol: {actual.scheme}
Host: {actual.hostname}
Port: {actual.port if actual.port else 80}
Path: {actual.path}
""")
    else:
        print(f"""Protocol: {actual.scheme}
Host: {actual.hostname}
Port: {actual.port if actual.port else 80}
Path: {actual.path}
Query: {actual.query}
Fragment: {actual.fragment}
    """)
