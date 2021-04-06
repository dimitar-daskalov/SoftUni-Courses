from project.appliances.appliance import Appliance


class Room:
    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.__expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    @staticmethod
    def calculate_expenses(*args):
        total_cost = 0
        for arg in args:
            for el in arg:
                if isinstance(el, Appliance):
                    total_cost += el.get_monthly_expense()
                else:
                    total_cost += el.month_cost

        return total_cost
