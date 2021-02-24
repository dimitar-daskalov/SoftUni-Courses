class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        if not milliliters <= self.status():
            return
        self.quantity += milliliters

    def status(self):
        space_left = self.size - self.quantity
        return space_left


cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
