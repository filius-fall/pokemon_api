import pytest
import requests

import responses

from unittest.mock import patch,PropertyMock

from poke_api import Pokemon
from .test_fake_data import FAKE_POKEMON_RESPONSE

@responses.activate
def test_pokemon_attack():

    poke_name = Pokemon('pikachu')
    responses.add(responses.GET,'https://pokeapi.co/api/v2/pokemon/pikachu',json=FAKE_POKEMON_RESPONSE)
    assert_value = poke_name.get_pokemon_details()['types']
    output = ['electric']

    assert assert_value == output




