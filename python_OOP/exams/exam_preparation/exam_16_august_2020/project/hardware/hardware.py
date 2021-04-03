class UnsuccessfulInstallException(Exception):
    pass


class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.capacity_used = 0
        self.memory_used = 0

    def install(self, software):
        if self.capacity < self.capacity_used + software.capacity_consumption \
                or self.memory < self.memory_used + software.memory_consumption:
            raise UnsuccessfulInstallException('Software cannot be installed')

        self.software_components.append(software)
        self.capacity_used += software.capacity_consumption
        self.memory_used += software.memory_consumption

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)
            self.capacity_used -= software.capacity_consumption
            self.memory_used -= software.memory_consumption
