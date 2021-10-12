import requests

from urllib.parse import urljoin
from tabulate import tabulate

from .berry import all_pokemon_names

URL = 'https://pokeapi.co/api/v2/'
ENDPOINTS = [
    "ability",
    "berry",
    "berry-firmness",
    "berry-flavor",
    "characteristic",
    "contest-effect",
    "contest-type",
    "egg-group",
    "encounter-condition",
    "encounter-condition-value",
    "encounter-method",
    "evolution-chain",
    "evolution-trigger",
    "gender",
    "generation",
    "growth-rate",
    "item",
    "item-attribute",
    "item-category",
    "item-fling-effect",
    "item-pocket",
    "language",
    "location",
    "location-area",
    "machine",
    "move",
    "move-ailment",
    "move-battle-style",
    "move-category",
    "move-damage-class",
    "move-learn-method",
    "move-target",
    "nature",
    "pal-park-area",
    "pokeathlon-stat",
    "pokedex",
    "pokemon",
    "pokemon-color",
    "pokemon-form",
    "pokemon-habitat",
    "pokemon-shape",
    "pokemon-species",
    "region",
    "stat",
    "super-contest-effect",
    "type",
    "version",
    "version-group",
]


class Pokemon:
    """
    This class will initialise a pokemon and will add features to it
    By using two instances of this class we can battle each other
        
    __str__ attribute returns table of stats
    
    
    """
    def __init__(self,name):
        self.pokemon_list = all_pokemon_names()
        self.name = self.validate_name(name)
        self.health = 10000
    
    def __repr__(self):
        return "<Pokemon:{0}>".format(self.name)

    def __str__(self):
        stats = [[i,self.get_pokemon_details()['stats'][i]] for i in self.get_pokemon_details()['stats']]
        tab = tabulate(stats,headers=['Type','Value'],tablefmt='orgtbl')
        return tab
        

    def attack(self,attack_name,defender_name):
        """This function will give damage to other pokemon that is mentioned """
        
        attack_stats  = self.get_pokemon_details()['stats']['attack']
        damage = self.damage_by_each_move(attack_name) * (attack_stats/2)
        print("damage given by {0} to {1} for {2}".format(self.name,defender_name.name,damage))
        try:
            def_damage = defender_name.damage_taken(damage)
    
        except:
            raise KeyError("check defender name")

    def damage_taken(self,damage):
        """This function will decrease the helath of the pokemon based
            on the damage given by an other pokemon.
            The damage taken will also based on the defense stat of this
            pokemon other than attack power of opponent
        
        """
        stat_defense = self.get_pokemon_details()['stats']['defense']

        # real damage will be reduced according to defence stat of pokemon
        real_damage = damage / (stat_defense/10)
        self.health -= real_damage
        print("{0}'s health = {1}".format(self.name,self.health))

    def validate_name(self,poke_name):
        """ 
            This function will check if the given pokemon name is valid or not
            from the pokemon list and again returns the pokemon name if it is valid
            or it Raises name error if the name doesnt match with the list of pokemone

        """
        print(poke_name)
        if poke_name not in self.pokemon_list:
            raise NameError("Pokemon not found!!!.Check the spelling of name once or try another pokemon")
            return False
        else:
            return poke_name
    
    def damage_by_each_move(self,move_name):
        """ 
            This function will fetch the damage that will be delt by the given
            attack name from the 
        """

        poke_details = self.get_pokemon_details()
        if move_name in poke_details['moves']:
            print(self.move_damages(move_name))
            damage = self.move_damages(move_name)['damage']
            return int(damage) if damage is not None else 0
        else:
            raise NameError("{0} doesnt have this attack".format(self.name))
        

    
    def get_pokemon_details(self):
        """This function will get all the details of given pokemon """
        
        pokemon = 'pokemon/' + str(self.name)
        poke_url = urljoin(URL,pokemon)
        poke_response = requests.get(url=poke_url).json()

        print(poke_response)

        result = {
            'abilities' : [],
            'base_experience': poke_response['base_experience'],
            'height': poke_response['height'],
            'weight': poke_response['weight'],
            'forms' : [],
            'moves':[],
            'types':[],
            'stats' : {}

        }

        for i in poke_response['abilities']:
            result['abilities'].append(i['ability']['name'])
        
        for j in poke_response['moves']:
            result['moves'].append(j['move']['name'])

        for k in poke_response['types'] :
            result['types'].append(k['type']['name'])

        for l in poke_response['stats']:
            # print(l['stat']['name'])
            result['stats'][str(l['stat']['name'])] = l['base_stat']
        
        for m in poke_response['forms']:
            result['forms'].append(m['name'])


        return result


    def move_damages(self,move_name):
        """ 
        This Function will give details of the attack moves
        """

        moves = 'move/' + str(move_name)
        moves_url = urljoin(URL, moves)
        try:
            moves_response = requests.get(url=moves_url).json()
        except:
            raise(ValueError("Move entered is not in the database"))
            return None

        output = {
            'name':move_name, 
            'damage': moves_response['power'],
            "pp" : moves_response['pp']
        
        }

        return output



def battle_areana():
    """ 
    This function is battlefield for two pokemons they battle it out
    by mentioning attacks and opponents and whose health gets below
    their stats hp they loose

    After executing the function you will be prompted to type the pokemon
    names and then you should enter your attack name each time until ones health 
    is below their hp then battle state will be changed to stop and 
    while loop stops
    
    """

    c1_name = input("Contender 1 enter your pokemon name:")
    contender_1 = Pokemon(c1_name)

    c2_name = input("Contender 2 enter your pokemon name:")
    contender_2 = Pokemon(c2_name)

    battle_state = "start"


    while battle_state == 'start':

        print('Contender 1 its your turn.')
        attack_name = input("Enter your attack:")
        contender_1.attack(attack_name,contender_2)

        print('Contender 2 its your turn')
        c2_attack_name = input("Enter your attacj:")
        contender_2.attack(c2_attack_name,contender_1)


        c1_hp = contender_1.get_pokemon_details()['stats']['defense'] * 10
        c2_hp = contender_2.get_pokemon_details()['stats']['defense'] * 10
        if contender_1.health <= c1_hp:
            print("{0} is dead. Contender 2 is winner".format(contender_1.name))
            battle_state = "stop"
        elif contender_2.health <= c2_hp:
            print("{0} is dead. Contender 1 is winner".format(contender_2.name))
            battle_state = "stop"


if __name__ == "__main__":
    ...