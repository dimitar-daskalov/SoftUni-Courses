from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        capacity_consumption_sum = sum(
            [software_component.capacity_consumption for software_component in self.software_components])
        memory_consumption_sum = sum(
            [software_component.memory_consumption for software_component in self.software_components])

        if self.capacity < (software.capacity_consumption + capacity_consumption_sum)\
                or self.memory < (software.memory_consumption + memory_consumption_sum):
            raise Exception("Software cannot be installed")

        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
