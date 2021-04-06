from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = ""
        for room in self.rooms:
            if room.budget >= room.expenses:
                total_expenses = room.expenses + room.room_cost
                new_budget = room.budget - total_expenses
                result += f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.\n"
                room.budget = new_budget
            else:
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(room)
        return result[:-1]

    def status(self):
        result = f"Total population: {sum([room.members_count for room in self.rooms])}\n"
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if room.children:
                child_number = 1
                for child in room.children:
                    result += f"--- Child {child_number} monthly cost: {child.month_cost:.2f}$\n"
                    child_number += 1
            if room.appliances:
                appliances_cost = sum([appliance.get_monthly_expense() for appliance in room.appliances])
                result += f"--- Appliances monthly cost: {appliances_cost:.2f}$\n"
        return result[:-1]
