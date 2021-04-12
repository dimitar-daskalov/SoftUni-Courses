from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: list = []

    def find_aquarium_by_name(self, aquarium_name):
        try:
            return [aquarium for aquarium in self.aquariums if aquarium.name == aquarium_name][0]
        except IndexError:
            pass

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
        elif aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
        else:
            return f"Invalid aquarium type."
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            self.decorations_repository.add(Ornament())
        elif decoration_type == "Plant":
            self.decorations_repository.add(Plant())
        else:
            return f"Invalid decoration type."
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium_needed = self.find_aquarium_by_name(aquarium_name)
        decoration_needed = self.decorations_repository.find_by_type(decoration_type)
        if decoration_needed == "None":
            return f"There isn't a decoration of type {decoration_type}."
        if not aquarium_needed:
            return
        aquarium_needed.add_decoration(decoration_needed)
        is_removed = self.decorations_repository.remove(decoration_needed)
        if is_removed:
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == "SaltwaterFish":
            fish = SaltwaterFish(fish_name, fish_species, price)
        else:
            return f"There isn't a fish of type {fish_type}."
        aquarium_needed = self.find_aquarium_by_name(aquarium_name)
        if fish and aquarium_needed:
            if (fish.__class__.__name__ == "FreshwaterFish" and aquarium_needed.__class__.__name__ == "FreshwaterAquarium") or (fish.__class__.__name__ == "SaltwaterFish" and aquarium_needed.__class__.__name__ == "SaltwaterAquarium"):
                return aquarium_needed.add_fish(fish)
            else:
                return f"Water not suitable."

    def feed_fish(self, aquarium_name: str):
        aquarium_needed = self.find_aquarium_by_name(aquarium_name)
        if aquarium_needed:
            aquarium_needed.feed()
            return f"Fish fed: {len(aquarium_needed.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium_needed = self.find_aquarium_by_name(aquarium_name)
        if aquarium_needed:
            decorations_price = sum([decoration.price for decoration in aquarium_needed.decorations])
            fish_price = sum([fish.price for fish in aquarium_needed.fish])
            return f"The value of Aquarium {aquarium_name} is {decorations_price + fish_price:.2f}."

    def report(self):
        result = ""
        for aquarium in self.aquariums:
            result += aquarium.__str__()

        return result

