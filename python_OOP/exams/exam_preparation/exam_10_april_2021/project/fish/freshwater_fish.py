from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 3, price)

    def eat(self, value=3):
        return super().eat(value)


