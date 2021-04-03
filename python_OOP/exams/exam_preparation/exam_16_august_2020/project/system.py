from project.hardware.hardware import UnsuccessfulInstallException
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def get_obj_by_name(name, obj_list):
        try:
            return [h for h in obj_list if h.name == name][0]
        except IndexError:
            return None

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_software(hardware_name, name, capacity_consumption, memory_consumption, type_software):
        hardware = System.get_obj_by_name(hardware_name, System._hardware)
        if not hardware:
            return "Hardware does not exist"

        software = type_software(name, capacity_consumption, memory_consumption)

        try:
            hardware.install(software)
            System._software.append(software)

        except UnsuccessfulInstallException:
            return 'Software cannot be installed'

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        return System.register_software(hardware_name, name, capacity_consumption, memory_consumption, ExpressSoftware)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        return System.register_software(hardware_name, name, capacity_consumption, memory_consumption, LightSoftware)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware = System.get_obj_by_name(hardware_name, System._hardware)
        software = System.get_obj_by_name(software_name, System._software)

        if not hardware or not software:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        total_memory = sum(hardware.memory for hardware in System._hardware)
        total_used_memory = sum(h.memory_used for h in System._hardware)
        total_used_capacity = sum(h.capacity_used for h in System._hardware)
        total_capacity = sum(h.capacity for h in System._hardware)

        result = f"System Analysis\nHardware Components: {len(System._hardware)}\n" \
                 f"Software Components: {len(System._software)}\n" \
                 f"Total Operational Memory: {total_used_memory} / {total_memory}\n" \
                 f"Total Capacity Taken: {total_used_capacity} / {total_capacity}"

        return result

    @staticmethod
    def system_split():
        result = ""
        for hardware in System._hardware:
            express_soft = len([software for software in hardware.software_components if software.type == "Express"])
            light_soft = len([software for software in hardware.software_components if software.type == "Light"])

            result += f"Hardware Component - {hardware.name}\n"
            result += f"Express Software Components: {express_soft}\n"
            result += f"Light Software Components: {light_soft}\n"
            result += f"Memory Usage: {hardware.memory_used} / {hardware.memory}\n"
            result += f"Capacity Usage: {hardware.capacity_used} / {hardware.capacity}\n"
            result += f"Type: {hardware.type}\n"
            result += f"Software Components: " \
                      f"{', '.join(s.name for s in hardware.software_components) if hardware.software_components else None}"

        return result
