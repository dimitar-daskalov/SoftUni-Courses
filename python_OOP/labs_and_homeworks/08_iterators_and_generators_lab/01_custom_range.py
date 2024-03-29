class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.value = start

    def __iter__(self):
        return self

    def __next__(self):
        value = self.value
        if value == self.end + 1:
            raise StopIteration
        self.value += 1
        return value


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
