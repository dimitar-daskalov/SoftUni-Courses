class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price: int):
        if len(self.animals) < self.__animal_capacity and self.__budget < price:
            return "Not enough budget"
        elif len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            fired_worker = [worker for worker in self.workers if worker.name == worker_name][0]
            self.workers.remove(fired_worker)
            return f"{fired_worker.name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        summed_salaries = sum([worker.salary for worker in self.workers])
        if self.__budget < summed_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= summed_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        summed_tend = sum([animal.get_needs() for animal in self.animals])
        if self.__budget < summed_tend:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= summed_tend
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [animal for animal in self.animals if animal.__class__.__name__ == "Lion"]
        tigers = [animal for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == "Cheetah"]
        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        result += "\n".join(lion.__repr__() for lion in lions)
        result += "\n"
        result += f"----- {len(tigers)} Tigers:\n"
        result += "\n".join(tiger.__repr__() for tiger in tigers)
        result += "\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += "\n".join(cheetah.__repr__() for cheetah in cheetahs)
        return result

    def workers_status(self):
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        vets = [worker for worker in self.workers if worker.__class__.__name__ == "Vet"]
        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += "\n".join(keeper.__repr__() for keeper in keepers)
        result += "\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += "\n".join(caretaker.__repr__() for caretaker in caretakers)
        result += "\n"
        result += f"----- {len(vets)} Vets:\n"
        result += "\n".join(vet.__repr__() for vet in vets)
        return result
