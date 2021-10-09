import pytest
from unittest.mock import patch

from poke_api.main import get_requset_data

def test_request_data():

    result = get_requset_data()

    assert result['ability'] == "https://pokeapi.co/api/v2/ability/"