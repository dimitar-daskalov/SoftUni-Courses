import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.test_paint_factory = PaintFactory("TestPainFactory", 50)

    def test_if_paint_factory_initialised_successfully(self):
        self.assertEqual("TestPainFactory", self.test_paint_factory.name)
        self.assertEqual(50, self.test_paint_factory.capacity)
        self.assertDictEqual({}, self.test_paint_factory.ingredients)
        self.assertDictEqual({}, self.test_paint_factory.products)
        self.assertListEqual(["white", "yellow", "blue", "green", "red"], self.test_paint_factory.valid_ingredients)

    def test_if_paint_factory_add_invalid_ingredient_raises(self):
        self.test_paint_factory.ingredients = {}
        with self.assertRaises(TypeError) as ex:
            self.test_paint_factory.add_ingredient("test", 10)
        self.assertEqual("Ingredient of type test not allowed in PaintFactory", str(ex.exception))

    def test_if_paint_factory_add_invalid_quantity_raises(self):
        self.test_paint_factory.capacity = 40
        with self.assertRaises(ValueError) as ex:
            self.test_paint_factory.add_ingredient("blue", 50)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_if_paint_factory_add_successfully(self):
        self.test_paint_factory.capacity = 50
        self.test_paint_factory.add_ingredient("blue", 50)
        self.assertDictEqual({"blue": 50}, self.test_paint_factory.ingredients)

    def test_if_paint_factory_remove_invalid_ingredient_raises(self):
        self.test_paint_factory.add_ingredient("blue", 40)
        with self.assertRaises(KeyError) as ex:
            self.test_paint_factory.remove_ingredient("yellow", 30)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_if_paint_factory_remove_invalid_quantity_raises(self):
        self.test_paint_factory.add_ingredient("blue", 40)
        with self.assertRaises(ValueError) as ex:
            self.test_paint_factory.remove_ingredient("blue", 50)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_if_paint_factory_remove_ingredient_successfully_and_decreased_quantity(self):
        self.test_paint_factory.add_ingredient("blue", 40)
        self.test_paint_factory.add_ingredient("yellow", 10)
        self.test_paint_factory.remove_ingredient("blue", 40)
        self.assertDictEqual({"blue": 0, "yellow": 10}, self.test_paint_factory.products)

    def test_if_paint_factory_products_return_successfully(self):
        self.test_paint_factory.add_ingredient("blue", 40)
        self.test_paint_factory.add_ingredient("yellow", 10)
        self.assertEqual({"blue": 40, "yellow": 10}, self.test_paint_factory.products)

    def test_if_paint_factory_can_add_return_true(self):
        self.assertTrue(self.test_paint_factory.can_add(40))

    def test_if_paint_factory_can_add_return_false(self):
        self.assertFalse(self.test_paint_factory.can_add(51))
