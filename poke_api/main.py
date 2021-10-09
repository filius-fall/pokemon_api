import requests

URL = 'https://pokeapi.co/api/v2'

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