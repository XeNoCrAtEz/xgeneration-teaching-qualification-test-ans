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
        
    # This function returns the pokemon ID 
    def pokemon_id(self):
        pass

    # This function returns the pokemon type(s)
    def pokemon_type(self):
        pass

    # This function returns the pokemon ability/abilities
    def pokemon_ability(self):
        pass

    # Returns the summary of the pokemon below:
    # ID: 1
    # Name: Bulbasaur
    # Type(s): Grass / Poison
    def __str__(self):
        # Note: String format should be similar (i.e. uppercase and lowercase should be in the same format)
        pass

###########################################################
# Do not modify the code below here
def pokemon_summary(pokemons):
    for pkmn in pokemons:
        print(pkmn + " Summary:")
        print(Pokedex(pkmn))

if __name__ == "__main__":
    pokemon_summary(["Arceus", "Charizard", "Greninja", "Tyranitar"])