from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 5, price)

    def eat(self, value=2):
        return super().eat(value)
