import pytest
import requests
from unittest.mock import patch,PropertyMock
from poke_api.main import get_requset_data,get_all_names_list,get_berry_details

BERRY_TEST_NAMES = ['cheri', 'chesto', 'pecha', 'rawst', 'aspear', 'leppa', 'oran', 'persim', 'lum', 'sitrus', 'figy', 'wiki', 'mago', 'aguav', 'iapapa', 'razz', 'bluk', 'nanab', 'wepear', 'pinap']
TEST_BERRY = [{'name': 'cheri', 'url': 'https://pokeapi.co/api/v2/berry/1/'}, {'name': 'chesto', 'url': 'https://pokeapi.co/api/v2/berry/2/'}, {'name': 'pecha', 'url': 'https://pokeapi.co/api/v2/berry/3/'}, {'name': 'rawst', 'url': 'https://pokeapi.co/api/v2/berry/4/'}, {'name': 'aspear', 'url': 'https://pokeapi.co/api/v2/berry/5/'}, {'name': 'leppa', 'url': 'https://pokeapi.co/api/v2/berry/6/'}, {'name': 'oran', 'url': 'https://pokeapi.co/api/v2/berry/7/'}, {'name': 'persim', 'url': 'https://pokeapi.co/api/v2/berry/8/'}, {'name': 'lum', 'url': 'https://pokeapi.co/api/v2/berry/9/'}, {'name': 'sitrus', 'url': 'https://pokeapi.co/api/v2/berry/10/'}, {'name': 'figy', 'url': 'https://pokeapi.co/api/v2/berry/11/'}, {'name': 'wiki', 'url': 'https://pokeapi.co/api/v2/berry/12/'}, {'name': 'mago', 'url': 'https://pokeapi.co/api/v2/berry/13/'}, {'name': 'aguav', 'url': 'https://pokeapi.co/api/v2/berry/14/'}, {'name': 'iapapa', 'url': 'https://pokeapi.co/api/v2/berry/15/'}, {'name': 'razz', 'url': 'https://pokeapi.co/api/v2/berry/16/'}, {'name': 'bluk', 'url': 'https://pokeapi.co/api/v2/berry/17/'}, {'name': 'nanab', 'url': 'https://pokeapi.co/api/v2/berry/18/'}, {'name': 'wepear', 'url': 'https://pokeapi.co/api/v2/berry/19/'}, {'name': 'pinap', 'url': 'https://pokeapi.co/api/v2/berry/20/'}]




def test_request_data():

    result = get_requset_data()

    assert result['ability'] == "https://pokeapi.co/api/v2/ability/"



def test_get_all_names_list():

    test_name = 'berry'

    t = {'results':TEST_BERRY}

    with patch('requests.get') as patched_get:
        type(requests.get).json = PropertyMock(return_value=t)
    
    re = get_all_names_list(test_name)
    if 'cheri' in re and 'leppa' in re and 'oran' in re:
        assert True
    else:
        assert False

@pytest.mark.parametrize('test_data',[('fake_name1'),('fake_name_2')])
def test_fail_get_all_names_list(test_data):

    test_names = ['fake_name_1','fake_name_2']
    t = {'results':TEST_BERRY}

    with patch('requests.get') as patched_get:
        type(requests.get).json = PropertyMock(return_value=t)
    
    re = get_all_names_list('berry')

    if test_data in re:
        assert False
    else:
        assert True

@pytest.mark.parametrize('test_data',[[{'flavor': 'spicy', 'potency': 10}, {'flavor': 'dry', 'potency': 0}, {'flavor': 'sweet', 'potency': 0}, {'flavor': 'bitter', 'potency': 0}, {'flavor': 'sour', 'potency': 0}]])    
def test_get_berry_details(test_data):

    t = {'firmness': {'name': 'soft', 'url': 'https://pokeapi.co/api/v2/berry-firmness/2/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 10}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 0}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 0}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 0}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 0}], 'growth_time': 3, 'id': 1, 'item': {'name': 'cheri-berry', 'url': 'https://pokeapi.co/api/v2/item/126/'}, 'max_harvest': 5, 'name': 'cheri', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'fire', 'url': 'https://pokeapi.co/api/v2/type/10/'}, 'size': 20, 'smoothness': 25, 'soil_dryness': 15}



    with patch('requests.get') as patched_get:
        type(requests.get).json = PropertyMock(return_value=t)

    result = get_berry_details('cheri')

    print(test_data,result['name'])


    if test_data == result['flavors']:
        assert True
    else:
        raise AssertionError("Test Failed")