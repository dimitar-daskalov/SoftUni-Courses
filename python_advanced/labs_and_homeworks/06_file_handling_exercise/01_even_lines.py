import re


with open("exercises_test_files/text.txt", "r") as file:
    file = file.readlines()
    result = ([file[line_index] for line_index in range(len(file)) if line_index % 2 == 0])
    for line in result:
        line = re.sub(r"[-,.!,?]", "@", line)
        line = ' '.join(line.split()[::-1])
        print(line)

