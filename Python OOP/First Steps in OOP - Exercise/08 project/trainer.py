
from pokemon import Pokemon

class Trainer:
     
    def __init__(self, name: str) -> None:
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon : Pokemon):
        if pokemon not in self.pokemons:

            self.pokemons.append(pokemon)

            return f"Caught {pokemon.name} with health {pokemon.health}"
        else:
            return f"This pokemon is already caught"
    
    def release_pokemon(self, pokemon_name):

        for i in self.pokemons:
  
            if pokemon_name == i.name:
                self.pokemons.remove(i)
                return f"You have released {pokemon_name}"

            else: 
                return "Pokemon is not caught"
        
    
    def trainer_data(self):
        output = [f"Pokemon Trainer {self.name}",f"Pokemon count {len(self.pokemons)}"]
        for i in self.pokemons:
            output.append(f"- {i.pokemon_details()}")
        return "\n".join(output)

             

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
