from unittest import TestCase, main

# from cat import Cat


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Rijko")

    def test_if_cat_size_increase_successfully_after_eating(self):
        # Cat's size is increased after eating
        self.cat.size = 0
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_if_cat_is_fed_after_eating(self):
        # Cat is fed after eating
        self.cat.fed = False
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_if_cat_cannot_eat_after_fed_raises(self):
        # Cat cannot eat if already fed, raises an error
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_if_cat_cannot_fall_asleep_if_not_fed_raises(self):
        # Cat cannot fall asleep if not fed, raises an error
        self.cat.fed = False
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_if_cat_is_not_sleepy_after_sleep(self):
        # Cat is not sleepy after sleeping
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()