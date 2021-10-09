import requests

from urllib.parse import urljoin

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

def get_requset_data():
    """
    Descryption:
        This function will get data from pokemon api 
    Output:
        Type: Dict
        
        Example:
            The output will contain URL values as values and keys as the URL detail name
            {'ability':'https://pokeapi.co/api/v2/ability/',.....}    
    """

    response = requests.get(url=URL)
    json_response = response.json()
    return json_response

def is_validate(validate_input):
    if validate_input in ENDPOINTS:
        return True
    else:
        return False

def get_ability():
    """ Get Abiluty of Pokemon
        
        Descryption:
            This function will get value of the ability key from the json response of
            get_request_data() function and again get the data from ability URL
        Output:
            Type: JSON

    """
    pass


def get_all_names_list(name):
    """
        Descryption:
            This function will get all the names of type you mention if the type is in endpoint
                Type: List
    """
    names_list = []
    if is_validate(name):
        name_url = urljoin(URL, name)

        response = requests.get(url=name_url)
        json_resone = response.json()
        for i in json_resone['results']:
            names_list.append(i['name'])

        return names_list
    else:
        return ValueError("{0} is not a Valid name".format(name))

def get_berry_details(berry_name):
    """This function will retutn berry details """
    berry_to_fetch = 'berry/' + berry_name
    berry_url = urljoin(URL,berry_to_fetch)
    berry_details = {}

    # First I need to get berry response call
    berry_response = requests.get(url=berry_url)

    # Return the response in the form of JSON format
    json_response = berry_response.json()
    # print(json_response)
    berry_attributes = []

    # json_response['flavors'] is a list of dicts with each dict has its name and
    # its APIresouce link of the individual flavir under 'url' key so we are removing
    # url key and adding all names as list to 'flavors'

    # json_response['flavors'] = [x['flavor'] for x in json_response['flavors']]

    for jr in json_response['flavors']:
        jr['flavor'] = jr['flavor']['name']

    # This will loop through the json_response and will check if the value type of a
    # is a dict or not. If it is a dict then then it will only take 'name' value of that
    # and assign it to that key attribute 
    # Example {'attr':{'name':'filiusfall','url':'filiusfall.github.io'}} will be converted
    # to {'attr':'filiusfall'}

    for j in json_response:
        if type(json_response[j]) == dict:
            json_response[j] = json_response[j]['name']
    return json_response


# print(get_berry_details('cheri'))