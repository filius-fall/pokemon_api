from poke_api import Pokemon
import requests
k = Pokemon('pikachu')
det = k.get_pokemon_details()

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

l = requests.get(url=url).json()

with open('tes.txt','w+') as t:
    t.write(str(l))