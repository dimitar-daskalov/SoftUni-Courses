import unittest

from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.test_room = Room("TestRoom", 100, 2)

    def test_if_test_room_initialised_successfully(self):
        self.assertEqual("TestRoom", self.test_room.family_name)
        self.assertEqual(100, self.test_room.budget)
        self.assertEqual(2, self.test_room.members_count)
        self.assertListEqual([], self.test_room.children)
        self.assertEqual(0, self.test_room.expenses)

    def test_if_test_room_expenses_value_less_than_0_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.test_room.expenses = -10
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_if_test_room_expenses_return_successfully(self):
        self.test_room.expenses = 50
        self.assertEqual(50, self.test_room.expenses)

