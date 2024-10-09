''' TODO '''
from sc_python import sc_api
import pytest
import json

def log_json(obj):
    print(json.dumps(obj, indent=2))

@pytest.fixture
def api():
    return sc_api.ScApi()

def test_sc_api_is_valid(api):
    ''' TODO '''
    assert api.is_valid()

def test_sc_api_user_groups():
    ''' TODO '''
    user_groups = api.get_user_groups()
    log_json(user_groups)

    assert not user_groups is None