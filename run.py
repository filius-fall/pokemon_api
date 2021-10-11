from poke_api.main import battle_areana


def run_battle():

    response = requests.get(url=URL).ok
    if response:
        battle_areana()

if __name__ == "__main__":
    run_battle()