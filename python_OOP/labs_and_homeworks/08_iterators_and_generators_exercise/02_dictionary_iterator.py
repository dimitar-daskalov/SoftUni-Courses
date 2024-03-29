class dictionary_iter:
    def __init__(self, dictionary_obj):
        self.dictionary = dictionary_obj
        self.keys = list(self.dictionary.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.dictionary):
            raise StopIteration
        key = self.keys[self.index]
        value = self.dictionary[key]
        self.index += 1
        return key, value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

