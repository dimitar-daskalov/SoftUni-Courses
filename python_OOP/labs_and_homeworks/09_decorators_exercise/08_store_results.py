class store_results:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)
        with open("results.txt", "a") as file:
            file.write(f"Function '{self.function.__name__}' was called. Result: {result}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
