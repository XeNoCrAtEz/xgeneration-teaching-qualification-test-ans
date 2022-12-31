import requests

# This is a code to get you started.
# Feel free to add any additional helper function(s) or variable(s)
# to make your work easier
# Note: Please make your code readable
class Pokedex:
    def __init__(self, pokemon):
        response = requests.get('https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1154')
        data = response.json()['results']

        # [{'name': 'bulbasaur', 'url': 'https://pokeapi.co/api/v2/pokemon/1'}, ...] 
        # count: 1154
        # self.data contains an array of dictionary with the format above with 1154
        # dictionaries inside the array.
        self.data = data

        self.name = pokemon

        for i in range(len(self.data)):
            if self.data[i]['name'] == self.name.lower():
                response = requests.get(self.data[i]['url'])
                pokemon_data = response.json()
                break
        try:
            pokemon_data
        except NameError:
            raise ValueError(f"Pokemon named {pokemon} not found!")

        self.id = int(pokemon_data['id'])

        self.abilities = []
        for ability in pokemon_data['abilities']:
            self.abilities.append(ability['ability']['name'].title())

        self.types = []
        for pkmn_type in pokemon_data['types']:
            self.types.append(pkmn_type['type']['name'].title())
        
    # This function returns the pokemon ID 
    def pokemon_id(self):
        return self.id

    # This function returns the pokemon type(s)
    def pokemon_type(self):
        return " / ".join(self.types)

    # This function returns the pokemon ability/abilities
    def pokemon_ability(self):
        return ", ".join(self.abilities)

    # Returns the summary of the pokemon below:
    # ID: 1
    # Name: Bulbasaur
    # Type(s): Grass / Poison
    def __str__(self):
        # Note: String format should be similar (i.e. uppercase and lowercase should be in the same format)
        return f"ID: {self.pokemon_id()}\n" \
             + f"Name: {self.name}\n" \
             + f"Type(s): {self.pokemon_type()}"

###########################################################
# Do not modify the code below here
def pokemon_summary(pokemons):
    for pkmn in pokemons:
        print(pkmn + " Summary:")
        print(Pokedex(pkmn))

if __name__ == "__main__":
    pokemon_summary(["Arceus", "Charizard", "Greninja", "Tyranitar"])