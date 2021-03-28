from unittest import TestCase, main

from extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.first_list = IntegerList(1, 2, 3, 4, 5, "Test")

    def test_if_the_int_list_is_initialised_successfully(self):
        self.assertEqual(5, len(self.first_list.get_data()))

    def test_if_the_int_list_add_not_int_element_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.first_list.add("six")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_if_the_int_list_add_int_element_successfully(self):
        self.first_list.get_data().append(6)
        self.assertEqual([1, 2, 3, 4, 5, 6], self.first_list.get_data())

    def test_if_the_int_list_remove_index_out_of_range_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.first_list.remove_index(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_if_the_int_list_remove_index_successfully(self):
        res = self.first_list.get_data()[4]
        self.first_list.remove_index(4)
        self.assertEqual(5, res)

    def test_if_the_int_list_get_out_of_range_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.first_list.get(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_if_the_int_list_get_successfully(self):
        res = self.first_list.get(4)
        self.assertEqual(5, res)
        self.assertEqual(self.first_list.get(4), self.first_list.get_data()[4])

    def test_if_the_int_list_insert_out_of_range_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.first_list.insert(5, 6)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_if_the_int_list_insert_not_int_element_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.first_list.insert(4, "six")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_if_the_int_list_insert_successfully(self):
        self.first_list = IntegerList(1, 2, 3, 4, 6)
        self.first_list.insert(4, 5)
        self.assertEqual([1, 2, 3, 4, 5, 6], self.first_list.get_data())

    def test_if_the_int_list_get_biggest_successfully(self):
        self.first_list = IntegerList(1, 2, 55, 3, 4, 5)
        self.assertEqual(55, self.first_list.get_biggest())

    def test_if_the_int_list_get_index_successfully(self):
        self.first_list = IntegerList(1, 2, 3, 4, 5, 55)
        self.assertEqual(5, self.first_list.get_index(55))


if __name__ == '__main__':
    main()

