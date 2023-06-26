from models import User, CatchPokemon, catches
from myfunctions import Pokemon_data

# name, hp, attack, defense, sprite, cartoon

def addPokemon(arr):
    for name in arr:
        pokemon = Pokemon_data(name)
        p = pokemon.pokedex()
        catch = CatchPokemon(p["name"], p["stats"]["hp"], p["stats"]["attack"], p["stats"]["defense"], p["sprite"], p["cartoon"])
        catch.catch_pokemon()
    print("All done")

print(addPokemon(['bulbasaur','ivysaur', 'venusaur']))