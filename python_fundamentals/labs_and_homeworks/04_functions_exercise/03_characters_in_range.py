character_one = input()
character_two = input()


def ascii_characters(a, b):
    for char in range(ord(a) + 1, ord(b)):
        print(chr(char), end=" ")


ascii_characters(character_one, character_two)