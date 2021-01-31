try:
    with open("text_files/text.txt") as file:
        print("File found")
except FileNotFoundError:
    print("File not found")

