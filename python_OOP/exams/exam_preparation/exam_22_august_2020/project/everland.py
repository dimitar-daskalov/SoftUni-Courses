from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        monthly_consumption = 0
        for room in self.rooms:
            monthly_consumption += room.expenses + room.room_cost
        return f"Monthly consumptions: {monthly_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            total_room_expenses = room.expenses + room.room_cost
            if room.budget < total_room_expenses:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
            else:
                result.append(f"{room.family_name} paid {total_room_expenses:.2f}$ and have {room.budget:.2f}$ left.")
                room.budget -= total_room_expenses

        return "\n".join(r for r in result)

    def status(self):
        result = [f"Total population: {sum(room.members_count for room in self.rooms)}"]
        for room in self.rooms:
            result.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            if room.children:
                child_number = 0
                for child in room.children:
                    child_number += 1
                    result.append(f"--- Child {child_number} monthly cost: {child.get_monthly_expense():.2f}$")
                result.append(f"--- Appliances monthly cost: {sum(appliance.get_monthly_expense() for appliance in room.appliances):.2f}$")
            else:
                result.append(f"--- Appliances monthly cost: {room.expenses:.2f}$")

        return "\n".join(r for r in result)
