import requests
from random import choice
from .models import CatchPokemon

class Pokemon_data():
    """
    FYI methods: name, id, sprite, cartoon, abilities, ability, moves, stats, hp, attack, defense, pokedex
    """
    def __init__(self, name):
        self.name = name.title()
        # url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        # response = requests.get(url)
        # if response.ok:
        #     data = response.json()
    
    def test_data(self):
        url = (f"https://pokeapi.co/api/v2/pokemon/{self.name.lower()}/")
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return data
        else:
            print("The name specified is not in the Pokemon database")

    def id(self):
        # self.test_data()
        data = self.test_data()
        pokemon_id = data["id"]
        return pokemon_id

# capture sprite URL
# sprite = data["sprites"]["front_shiny"]
    def sprite(self):
        # self.test_data()
        data = self.test_data()
        sprite = data["sprites"]["front_default"]
        return sprite
    
    def cartoon(self):
        # self.test_data()
        data = self.test_data()
        cartoon = data["sprites"]["other"]["dream_world"]["front_default"]
        return cartoon

# capture pokemon's name
# pokemon_name = data["name"].title()
    def pokemon_name(self):
        # self.test_data()
        data = self.test_data()
        pokemon_name = data["name"].title()
        return f"*This Pokemon's name is: {pokemon_name}*"

# capture pokemon's XP
# pokemon_xp = data["base_experience"]
    def exp(self):
        # self.test_data()
        data = self.test_data()
        pokemon_xp = data["base_experience"]
        return f"This Pokemon's XP is: {pokemon_xp}"

    def abilities(self):
        # self.test_data()
        data = self.test_data()
        abilities = {}
        try:
            # abilities key is a list of indices > indices dict first key ability > ability dict {name: "", url: ""}
            for k in range(2):
                ability_name = data["abilities"][int(k)]["ability"]["name"].title()
                # response2 = url link to ability's details
                response2 = requests.get(data["abilities"][int(k)]["ability"]["url"])
                if response2.ok:
                    data2 = response2.json()
                    effect = data2["effect_entries"][1]["effect"]
                    abilities[ability_name] = effect
        except:
            ability_name = data["abilities"][0]["ability"]["name"].title()
            response2 = requests.get(data["abilities"][0]["ability"]["url"])
            if response2.ok:
                data2 = response2.json()
                effect = data2["effect_entries"][1]["effect"]
                abilities[ability_name] = effect
        return abilities
    
    def ability(self):
        # self.test_data()
        data = self.test_data()
        ability = {}
        # abilities key is a list of indices > indices dict first key ability > ability dict {name: "", url: ""}
        ability_name = data["abilities"][0]["ability"]["name"].title()
        # response2 = url link to ability's details
        response2 = requests.get(data["abilities"][0]["ability"]["url"])
        if response2.ok:
            data2 = response2.json()
            effect = data2["effect_entries"][1]["effect"]
            ability[ability_name] = effect
        return ability
    
    def moves(self):
        # self.test_data()
        data = self.test_data()
        moves = {}
        move_list = data["moves"]
        for k in range(4):
            try:
                move_name = move_list[int(k)]["move"]["name"].title()
                response2 = requests.get(move_list[int(k)]["move"]["url"])
                if response2.ok:
                    data2 = response2.json()
                    move_power = data2["power"]
                    moves[move_name] = move_power
            except:
                move_name = move_list[0]["move"]["name"].title()
                response2 = requests.get(move_list[0]["move"]["url"])
                if response2.ok:
                    data2 = response2.json()
                    move_power = data2["power"]
                    moves[move_name] = move_power
        return moves
    
    def stats(self):
        # self.test_data()
        data = self.test_data()
        stats = {}
        stats_list = data["stats"]
        stats["hp"] = stats_list[0]["base_stat"]
        stats["attack"] = stats_list[1]["base_stat"]
        stats["defense"] = stats_list[2]["base_stat"]
        return stats
    
    def hp(self):
        return self.stats()["hp"]
    
    def attack(self):
        return self.stats()["attack"]
    
    def defense(self):
        return self.stats()["defense"]

    def pokedex(self):
        """
        dict w/keys: name, id, sprite, cartoon, abilities, ability, moves, moves1, moves2
        """
        all_dict = {}
        print(self.pokemon_name())
        all_dict["name"] = self.name
        all_dict["id"] = self.id()
        all_dict["sprite"] = self.sprite()
        all_dict["cartoon"] = self.cartoon()
        all_dict["abilities"] = self.abilities()
        all_dict["ability"] = self.ability()
        all_dict["moves"] = self.moves()
        all_dict["moves1"] = {}
        all_dict["moves2"] = {} 
        count = 0
        for k,v in self.moves().items():
            if count < 2:
                all_dict["moves1"][k] = v
            else:
                all_dict["moves2"][k] = v
            count += 1
        all_dict["stats"] = self.stats()
        return all_dict
    
# def get_data(url):
#     response = requests.get(url)
#     data = response.json()
#     return data

def pokemon_pull():
    def get_data(url):
        response = requests.get(url)
        data = response.json()
        return data

    num = choice(range(1,152))
    num -= 1
    set = num // 20
    offset = set*20
    num -= offset
    data = get_data(f"https://pokeapi.co/api/v2/pokemon/?offset={offset}&limit=20")
    return data["results"][num]["name"]
    

def addPokemon(arr):
    """
    Takes in list object - loops through all pokemon names in list and adds to the CatchPokemon table
    """
    for name in arr:
        pokemon = Pokemon_data(name)
        p = pokemon.pokedex()
        catch = CatchPokemon(p["name"], p["stats"]["hp"], p["stats"]["attack"], p["stats"]["defense"], p["sprite"], p["cartoon"])
        catch.catch_pokemon()
    print("All done")


class Battle():

    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.winner = ""
        self.difference = 0
        self.xp = 0


    def run(self):
        """
        returns dict: 
            arg1: damage points
            arg2: damage points
            difference: difference of damage points
            winner: (arg that one)
        """
        dp_dict = {}
        dp1 = self.team1["attack"]*100 // (self.team2["hp"]*(1+self.team2["defense"] // 100))
        dp2 = self.team2["attack"]*100 // (self.team1["hp"]*(1+self.team1["defense"] // 100))
        luck1 = choice([n for n in range(-3,4)])
        luck2 = choice([n for n in range(-3,4)])
        dp1 += luck1
        dp2 += luck2
        if dp1 == dp2:
            dp1 += 1
        dp_dict[self.team1["name"]] = dp1
        dp_dict[self.team2["name"]] = dp2
        dp_dict["difference"] = abs(dp1 - dp2)
        if dp1 > dp2:
            dp_dict["winner"] = self.team1["name"]
        else:
            dp_dict["winner"] = self.team2["name"]
        self.winner = dp_dict["winner"]
        self.difference = dp_dict["difference"]
        if self.difference < 10:
            self.xp = 99 // dp_dict["difference"] + dp_dict["difference"]
        else:
            self.xp = 99 // dp_dict["difference"] + dp_dict["difference"] // 10
        return dp_dict

    # def winner(self):
    #     winner = self.dp()["winner"]
    #     return winner

    # def difference(self):
    #     difference = self.dp()["difference"]
    #     return difference

    # def xp(self):
    #     xp = 100 // self.difference()
    #     return xp



# def dp(team1, team2):
#     """
#     returns dict: 
#         arg1: damage points
#         arg2: damage points
#         difference: difference of damage points
#         winner: (arg that one)
#     """
#     dp_dict = {}
#     dp1 = team1["attack"]*100 // (team2["hp"]*(1+team2["defense"] // 100))
#     dp2 = team2["attack"]*100 // (team1["hp"]*(1+team1["defense"] // 100))
#     luck1 = choice([n for n in range(-3,4)])
#     luck2 = choice([n for n in range(-3,4)])
#     dp1 += luck1
#     dp2 += luck2
#     if dp1 == dp2:
#         dp1 += 1
#     dp_dict[team1["name"]] = dp1
#     dp_dict[team2["name"]] = dp2
#     dp_dict["difference"] = abs(dp1 - dp2)
#     if dp1 > dp2:
#         dp_dict["winner"] = team1["name"]
#     else:
#         dp_dict["winner"] = team2["name"]
#     return dp_dict

def check_pokemon(pokemon_name):
    response= requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/")
    if response.ok:
        return True
    return False

