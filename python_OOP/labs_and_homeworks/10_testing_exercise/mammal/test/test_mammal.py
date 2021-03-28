from unittest import TestCase, main

from mammal.project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.test_animal = Mammal("Rijko", "cat", "meow")

    def test_if_mammal_initialised_successfully(self):
        self.assertEqual("Rijko", self.test_animal.name)
        self.assertEqual("cat", self.test_animal.type)
        self.assertEqual("meow", self.test_animal.sound)

    def test_if_mammal_make_sound_successfully(self):
        self.assertEqual("Rijko makes meow", self.test_animal.make_sound())

    def test_if_mammal_get_kingdom_successfully(self):
        self.assertEqual("animals", self.test_animal.get_kingdom())

    def test_if_get_kingdom_is_private(self):
        result = self.test_animal._Mammal__kingdom
        self.assertEqual("animals", result)

    def test_if_mammal_info_successfully(self):
        self.assertEqual("Rijko is of type cat", self.test_animal.info())


if __name__ == '__main__':
    main()