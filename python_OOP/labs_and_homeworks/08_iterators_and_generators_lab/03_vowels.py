class vowels:
    VOWELS = ["a", "e", "i", "o", "u", "y"]

    def __init__(self, string_received: str):
        self.string_received = string_received
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.string_received):
            raise StopIteration
        character = self.string_received[self.index]
        self.index += 1
        if character.lower() in self.VOWELS:
            return character
        return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
