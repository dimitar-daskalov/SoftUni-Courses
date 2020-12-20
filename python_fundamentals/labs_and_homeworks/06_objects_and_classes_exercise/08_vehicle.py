class Vehicle:
    def __init__(self, type_car, model_car, price_car):
        self.type = type_car
        self.model = model_car
        self.price = price_car
        self.owner = None

    def buy(self, money, owner):
        if self.owner is None:
            if money >= self.price:
                self.owner = owner
                return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"

            else:
                return "Sorry, not enough money"

        else:
            return "Car already sold"

    def sell(self):
        if self.owner is not None:
            self.owner = None

        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"

        else:
            return f"{self.model} {self.type} is on sale: {self.price}"