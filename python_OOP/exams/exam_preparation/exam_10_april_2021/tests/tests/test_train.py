import unittest

from tests.project.train.train import Train


class TestTrain(unittest.TestCase):
    def setUp(self):
        self.test_train = Train("TestTrain", 5)

    def test_if_train_init_successfully(self):
        self.assertEqual("TestTrain", self.test_train.name)
        self.assertEqual(5, self.test_train.capacity)
        self.assertEqual([], self.test_train.passengers)
        self.assertEqual("Train is full", self.test_train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.test_train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.test_train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.test_train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.test_train.PASSENGER_REMOVED)
        self.assertEqual(0, self.test_train.ZERO_CAPACITY)

    def test_if_train_add_successfully(self):
        self.assertEqual("Added passenger Ivan", self.test_train.add("Ivan"))
        self.assertEqual(1, len(self.test_train.passengers))

    def test_if_train_add_raises_on_full_capacity(self):
        self.test_train.add("Ivan")
        self.test_train.add("Viktor")
        self.test_train.add("Yosif")
        self.test_train.add("Test")
        self.test_train.add("Test2")
        with self.assertRaises(ValueError) as ex:
            self.test_train.add("Pesho")
        self.assertEqual("Train is full", str(ex.exception))

    def test_if_train_add_raises_if_passenger_already_added(self):
        self.test_train.add("Ivan")
        with self.assertRaises(ValueError) as ex:
            self.test_train.add("Ivan")
        self.assertEqual("Passenger Ivan Exists", str(ex.exception))

    def test_if_train_remove_invalid_passenger_raises(self):
        self.test_train.add("Ivan")
        with self.assertRaises(ValueError) as ex:
            self.test_train.remove("Pesho")
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_if_train_remove_successfully(self):
        self.test_train.add("Ivan")
        self.assertEqual("Removed Ivan", self.test_train.remove("Ivan"))
        self.assertEqual([], self.test_train.passengers)


