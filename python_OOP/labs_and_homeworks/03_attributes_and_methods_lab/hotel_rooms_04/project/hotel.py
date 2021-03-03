class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def get_room_number(self, room_number):
        current_number = [room for room in self.rooms if room.number == room_number][0]
        return current_number

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        current_room = self.get_room_number(room_number)
        result = current_room.take_room(people)
        if result:
            return result
        self.guests += people

    def free_room(self, room_number):
        current_room = self.get_room_number(room_number)
        current_guests = current_room.guests
        result = current_room.free_room()
        if result:
            return result
        self.guests -= current_guests

    def print_status(self):
        free_rooms = ", ".join(str(room.number) for room in self.rooms if not room.is_taken)
        taken_rooms = ", ".join(str(room.number) for room in self.rooms if room.is_taken)

        print(f"Hotel {self.name} has {self.guests} total guests")
        if free_rooms:
            print(f"Free rooms: {free_rooms}")
        if taken_rooms:
            print(f"Taken rooms: {taken_rooms}")


from project.room import Room

hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

hotel.print_status()

