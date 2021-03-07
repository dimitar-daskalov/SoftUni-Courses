from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    @staticmethod
    def is_smaller(first_param, second_param):
        return first_param < second_param

    def current_customer(self, customer_id):
        return [customer for customer in self.customers if customer.id == customer_id][0]

    def current_dvd(self, dvd_id):
        return [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

    def add_customer(self, customer):
        if self.is_smaller(len(self.customers), self.customer_capacity()):
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if self.is_smaller(len(self.dvds), self.dvd_capacity()):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_customer = self.current_customer(customer_id)
        current_dvd = self.current_dvd(dvd_id)
        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"
        elif current_dvd.is_rented:
            return "DVD is already rented"
        elif current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"
        current_customer.rented_dvds.append(current_dvd)
        current_dvd.is_rented = True
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        current_customer = self.current_customer(customer_id)
        current_dvd = self.current_dvd(dvd_id)
        if current_dvd not in current_customer.rented_dvds:
            return f"{current_customer.name} does not have that DVD"
        current_customer.rented_dvds.remove(current_dvd)
        current_dvd.is_rented = False
        return f"{current_customer.name} has successfully returned {current_dvd.name}"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += f"{customer.__repr__()}\n"
        for dvd in self.dvds:
            result += f"{dvd.__repr__()}\n"

        return result


c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)
