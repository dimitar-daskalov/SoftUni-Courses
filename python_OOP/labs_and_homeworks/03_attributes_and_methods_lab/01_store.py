class Store:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

    @classmethod
    def from_size(cls, name: str, type: str, size: int):
        capacity = size // 2
        return cls(name, type, capacity)

    @staticmethod
    def summed_values(items_dict: dict):
        sum_values = sum(items_dict.values())
        return sum_values

    def can_remove(self, item_name: str, amount: int):
        return item_name in self.items and self.items[item_name] >= amount

    def add_item(self, item_name: str):
        if self.capacity <= self.summed_values(self.items):
            return "Not enough capacity in the store"
        elif item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name: str, amount: int):
        if not self.can_remove(item_name, amount):
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        return f"{amount} {item_name} removed from the store"


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))
