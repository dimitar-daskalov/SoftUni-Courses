from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware: list = []
    _software: list = []

    @staticmethod
    def get_hardware_by_name(hardware_name, hardware_list):
        try:
            return [hardware for hardware in hardware_list if hardware.name == hardware_name][0]
        except IndexError:
            pass

    @staticmethod
    def get_software_by_name(software_name, software_list):
        try:
            return [software for software in software_list if software.name == software_name][0]
        except IndexError:
            pass

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.get_hardware_by_name(hardware_name, System._hardware)
        if not hardware:
            return f"Hardware does not exist"
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(express_software)
        except Exception:
            return f"Software cannot be installed"
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.get_hardware_by_name(hardware_name, System._hardware)
        if not hardware:
            return f"Hardware does not exist"
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(light_software)
        except Exception:
            return f"Software cannot be installed"
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.get_hardware_by_name(hardware_name, System._hardware)
        software = System.get_software_by_name(software_name, System._software)
        if not hardware or not software:
            return f"Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        result = "System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        total_memory = sum([hardware.memory for hardware in System._hardware])
        total_used_memory = sum(
            [software_component.memory_consumption for hardware in System._hardware
             for software_component in hardware.software_components])
        result += f"Total Operational Memory: {total_used_memory} / {total_memory}\n"
        total_capacity = sum([hardware.capacity for hardware in System._hardware])
        total_used_capacity = sum(
            [software_component.capacity_consumption for hardware in System._hardware
             for software_component in hardware.software_components])
        result += f"Total Capacity Taken: {total_used_capacity} / {total_capacity}"

        return result

    @staticmethod
    def system_split():
        result = ""
        for hardware in System._hardware:
            result += f"Hardware Component - {hardware.name}\n"
            result += f"Express Software Components: {len([s for s in hardware.software_components if s.type == 'Express'])}\n"
            result += f"Light Software Components: {len([s for s in hardware.software_components if s.type == 'Light'])}\n"
            result += f"Memory Usage: {sum(s.memory_consumption for s in hardware.software_components)} / {hardware.memory}\n"
            result += f"Capacity Usage: {sum(s.capacity_consumption for s in hardware.software_components)} / {hardware.capacity}\n"
            result += f"Type: {hardware.type}\n"
            result += f"Software Components: {', '.join(s.name for s in hardware.software_components) if hardware.software_components else None}"

        return result
