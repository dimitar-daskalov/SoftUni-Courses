class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.index = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.number:
            raise StopIteration

        char_received = self.sequence[self.index]
        self.index += 1

        if self.index == len(self.sequence):
            self.index = 0

        self.counter += 1
        return char_received


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
