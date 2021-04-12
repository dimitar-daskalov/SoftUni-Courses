from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors: list = []
        self.supplies: list = []
        self.medicine: list = []

    @property
    def food(self):
        food = [food for food in self.supplies if food.__class__.__name__ == "FoodSupply"]
        if not food:
            raise IndexError("There are no food supplies left!")
        return food

    @property
    def water(self):
        water = [water for water in self.supplies if water.__class__.__name__ == "WaterSupply"]
        if not water:
            raise IndexError("There are no water supplies left!")
        return water

    @property
    def painkillers(self):
        painkillers = [painkiller for painkiller in self.medicine if painkiller.__class__.__name__ == "Painkiller"]
        if not painkillers:
            raise IndexError("There are no painkillers left!")
        return painkillers

    @property
    def salves(self):
        salves = [salve for salve in self.medicine if salve.__class__.__name__ == "Salve"]
        if not salves:
            raise IndexError("There are no salves left!")
        return salves

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            needed_index = [medicine_index for medicine_index, medicine in enumerate(self.medicine) if
                            medicine.__class__.__name__ == medicine_type][-1]
            medicine = self.medicine.pop(needed_index)
            medicine.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            needed_index = [supply_index for supply_index, supply in enumerate(self.supplies) if
                            supply.__class__.__name__ == sustenance_type][-1]
            supply = self.supplies.pop(needed_index)
            supply.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")
