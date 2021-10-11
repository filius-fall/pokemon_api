import requests
from poke_api import battle_areana,URL


def run_battle():

    response = requests.get(url=URL).ok
    if response:
        battle_areana()

if __name__ == "__main__":
    run_battle()