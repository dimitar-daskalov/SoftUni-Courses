with open("text_files/numbers.txt", "r") as file:
    print(sum([int(el[0]) for el in file.readlines()]))
