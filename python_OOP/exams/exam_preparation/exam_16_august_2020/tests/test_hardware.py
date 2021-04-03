from unittest import TestCase, main
from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(TestCase):
    def setUp(self):
        self.test_hardware = Hardware("SSD", "Power", 200, 400)
        self.test_software = Software("Daemon_Tools", "Light", 100, 50)

    def test_if_hardware_initialised_successfully(self):
        self.assertEqual("SSD", self.test_hardware.name)
        self.assertEqual("Power", self.test_hardware.type)
        self.assertEqual(200, self.test_hardware.capacity)
        self.assertEqual(400, self.test_hardware.memory)
        self.assertEqual([], self.test_hardware.software_components)

    def test_if_hardware_empty_software_components__install_not_enough_memory_raises(self):
        self.test_software.memory_consumption = 500
        with self.assertRaises(Exception) as ex:
            self.test_hardware.install(self.test_software)
        self.assertEqual('Software cannot be installed', str(ex.exception))

    def test_if_hardware_not_empty_software_components__install_not_enough_memory_raises(self):
        self.test_hardware.memory_used = 200
        self.test_software.memory_consumption = 300
        with self.assertRaises(Exception) as ex:
            self.test_hardware.install(self.test_software)
        self.assertEqual('Software cannot be installed', str(ex.exception))

    def test_if_hardware_empty_software_components__install_not_enough_capacity_raises(self):
        self.test_software.capacity_consumption = 300
        with self.assertRaises(Exception) as ex:
            self.test_hardware.install(self.test_software)
        self.assertEqual('Software cannot be installed', str(ex.exception))

    def test_if_hardware_not_empty_software_components__install_not_enough_capacity_raises(self):
        self.test_hardware.capacity_used = 100
        self.test_software.capacity_consumption = 200
        with self.assertRaises(Exception) as ex:
            self.test_hardware.install(self.test_software)
        self.assertEqual('Software cannot be installed', str(ex.exception))

    def test_if_hardware_install_successfully_increased_software_components(self):
        self.test_hardware.install(self.test_software)
        software_names = [soft.name for soft in self.test_hardware.software_components]
        self.assertEqual(["Daemon_Tools"], software_names)

    def test_if_hardware_install_successfully_increased_memory_used(self):
        self.test_hardware.install(self.test_software)
        self.assertEqual(50, self.test_hardware.memory_used)

    def test_if_hardware_install_successfully_increased_capacity_used(self):
        self.test_hardware.install(self.test_software)
        self.assertEqual(100, self.test_hardware.capacity_used)

    def test_if_hardware_uninstall_successfully_removed_software_component(self):
        self.test_hardware.install(self.test_software)
        self.test_hardware.uninstall(self.test_software)
        self.assertEqual([], self.test_hardware.software_components)

    def test_if_hardware_uninstall_successfully_decreased_memory_used(self):
        self.test_hardware.install(self.test_software)
        self.test_hardware.uninstall(self.test_software)
        self.assertEqual(0, self.test_hardware.memory_used)

    def test_if_hardware_uninstall_successfully_decreased_capacity_used(self):
        self.test_hardware.install(self.test_software)
        self.test_hardware.uninstall(self.test_software)
        self.assertEqual(0, self.test_hardware.capacity_used)


if __name__ == '__main__':
    main()