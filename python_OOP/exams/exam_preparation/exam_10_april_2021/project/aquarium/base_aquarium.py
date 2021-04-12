from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: list = []
        self.fish: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([decoration.comfort for decoration in self.decorations])

    def add_fish(self, fish):
        if self.capacity <= len(self.fish):
            return "Not enough capacity."
        if fish.__class__.__name__ == "FreshwaterFish" or fish.__class__.__name__ == "SaltwaterFish":
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\n"
        result += f"Fish: {' '.join(fish.name for fish in self.fish) if self.fish else 'none'}\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}\n"

        return result

