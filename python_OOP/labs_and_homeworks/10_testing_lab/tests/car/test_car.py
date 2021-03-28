from unittest import TestCase, main

from car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.first_car = Car("VW", "Golf", 1, 5)

    def test_if_car_is_initialised_successfully(self):
        self.assertEqual("VW", self.first_car.make)
        self.assertEqual("Golf", self.first_car.model)
        self.assertEqual(1, self.first_car.fuel_consumption)
        self.assertEqual(5, self.first_car.fuel_capacity)

    def test_if_car_make_is_not_initialised_raises(self):
        with self.assertRaises(Exception) as ex:
            self.first_car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_if_car_model_is_not_initialised_raises(self):
        with self.assertRaises(Exception) as ex:
            self.first_car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_if_car_fuel_consumption_is_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.first_car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_if_car_fuel_consumption_is_lower_than_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.first_car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_if_car_fuel_capacity_is_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.first_car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_if_car_fuel_capacity_is_lower_than_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.first_car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_if_car_fuel_amount_is_lower_than_zero(self):
        with self.assertRaises(Exception) as ex:
            self.first_car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_if_car_refuel_amount_is_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.first_car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_if_car_refuel_amount_is_lower_than_zero(self):
        with self.assertRaises(Exception) as ex:
            self.first_car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_if_car_refuel_amount_is_more_than_car_fuel_capacity(self):
        self.first_car.fuel_capacity = 5
        self.first_car.fuel_amount = 0
        self.first_car.refuel(6)
        self.assertEqual(5, self.first_car.fuel_amount)

    def test_if_car_fuel_amount_is_increased_after_refuel(self):
        self.first_car.fuel_capacity = 5
        self.first_car.fuel_amount = 4
        self.first_car.refuel(1)
        self.assertEqual(5, self.first_car.fuel_amount)

    def test_if_drive_needed_fuel_is_higher_than_car_fuel_amount_raises(self):
        self.first_car.fuel_amount = 0
        self.first_car.fuel_consumption = 10
        with self.assertRaises(Exception) as ex:
            self.first_car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_if_fuel_amount_is_decreased_after_drive(self):
        self.first_car.fuel_amount = 5
        self.first_car.fuel_consumption = 10
        self.first_car.drive(10)
        self.assertEqual(4, self.first_car.fuel_amount)


if __name__ == '__main__':
    main()