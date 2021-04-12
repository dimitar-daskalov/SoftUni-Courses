import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):

    def setUp(self):
        self.test_hardware = Hardware("HDD", "Heavy", 200, 200)
        self.test_software = Software("Linux", "Express", 60, 100)

    def test_if_hardware_initialised_successfully(self):
        self.assertEqual("HDD", self.test_hardware.name)
        self.assertEqual("Heavy", self.test_hardware.type)
        self.assertEqual(200, self.test_hardware.capacity)
        self.assertEqual(200, self.test_hardware.memory)
        self.assertListEqual([], self.test_hardware.software_components)

    def test_if_hardware_install_raises_when_capacity_higher_than_hardware_capacity(self):
        self.test_software.capacity_consumption = 201
        with self.assertRaises(Exception) as ex:
            self.test_hardware.install(self.test_software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_if_hardware_install_raises_when_memory_higher_than_hardware_memory(self):
        self.test_software.memory_consumption = 201
        with self.assertRaises(Exception) as ex:
            self.test_hardware.install(self.test_software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_if_hardware_install_successfully_increase_the_software_comp(self):
        self.test_hardware.software_components = []
        self.test_hardware.install(self.test_software)
        self.assertListEqual([self.test_software], self.test_hardware.software_components)

    def test_if_hardware_uninstall_successfully_decrease_the_software_comp(self):
        self.test_hardware.install(self.test_software)
        self.test_hardware.uninstall(self.test_software)
        self.assertListEqual([], self.test_hardware.software_components)


if __name__ == '__main__':
    unittest.main()
