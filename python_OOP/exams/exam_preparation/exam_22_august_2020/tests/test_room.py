import unittest

from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.test_room = Room("Johnsons", 400, 2)

    def test_room_init_if_initialized_successfully(self):
        self.assertEqual("Johnsons", self.test_room.family_name)
        self.assertEqual(400, self.test_room.budget)
        self.assertEqual(2, self.test_room.members_count)
        self.assertEqual([], self.test_room.children)
        self.assertTrue(hasattr(self.test_room, "expenses"))

    def test_room_expenses_lower_than_0_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.test_room.expenses = -1
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_room_expenses_0_successfully(self):
        self.test_room.expenses = 0
        self.assertEqual(0, self.test_room.expenses)


if __name__ == '__main__':
    unittest.main()