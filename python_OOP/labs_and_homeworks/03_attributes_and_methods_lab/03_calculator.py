class Calculator:

    @staticmethod
    def add(*args: int):
        return sum(args)

    @staticmethod
    def multiply(*args: int):
        multiplied = 1
        for el in args:
            multiplied *= el
        return multiplied

    @staticmethod
    def divide(*args: int):
        divided = args[0]
        for el in args[1:]:
            divided /= el
        return divided

    @staticmethod
    def subtract(*args: int):
        subtracted = args[0]
        for el in args[1:]:
            subtracted -= el
        return subtracted


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
