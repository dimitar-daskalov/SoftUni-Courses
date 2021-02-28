from pokemon_battle_06.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name in self.pokemon:
            return f"This pokemon is already caught"

        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        if pokemon_name not in [pokemon.name for pokemon in self.pokemon]:
            return f"Pokemon is not caught"

        self.pokemon = [pokemon for pokemon in self.pokemon if not pokemon.name == pokemon_name]
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n" + f"Pokemon count {len(self.pokemon)}\n"
        for pokemon in self.pokemon:
            result += f"- {pokemon.pokemon_details()}\n"
        return result


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
