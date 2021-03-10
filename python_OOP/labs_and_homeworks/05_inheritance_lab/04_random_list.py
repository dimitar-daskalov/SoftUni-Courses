import random


class RandomList(list):

    def get_random_element(self):
        random_el_index = random.randint(0, len(self) - 1)
        random_el = self[random_el_index]
        self.pop(random_el_index)
        return random_el

