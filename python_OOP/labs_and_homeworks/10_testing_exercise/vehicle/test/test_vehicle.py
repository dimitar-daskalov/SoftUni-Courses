from unittest import TestCase, main

from vehicle.project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.test_vehicle = Vehicle(50, 100)

    def test_if_vehicle_initialised_successfully(self):
        self.assertEqual(50, self.test_vehicle.fuel)
        self.assertEqual(50, self.test_vehicle.capacity)
        self.assertEqual(100, self.test_vehicle.horse_power)
        self.assertEqual(1.25, self.test_vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_if_vehicle_drive_not_have_enough_fuel_raises(self):
        self.test_vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.drive(5)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_if_vehicle_drive_successfully(self):
        self.test_vehicle.fuel = 20
        self.test_vehicle.drive(4)
        self.assertEqual(15, self.test_vehicle.fuel)

    def test_if_vehicle_refuel_more_fuel_than_capacity_raises(self):
        self.test_vehicle.fuel = 50
        self.test_vehicle.capacity = 55
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.refuel(20)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_if_vehicle_refuel_successfully(self):
        self.test_vehicle.fuel = 25
        self.test_vehicle.capacity = 30
        self.test_vehicle.refuel(5)
        self.assertEqual(30, self.test_vehicle.fuel)

    def test_if_vehicle_str_successfully(self):
        result = f"The vehicle has 100 " \
               f"horse power with 50 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, self.test_vehicle.__str__())


if __name__ == '__main__':
    main()