import pytest
from sc_python import sc_statuspage_api

def test_sc_impact_status():
    assert sc_statuspage_api.ScImpactStatus.CRITICAL == 'critical'

def test_sc_endpoint():
    ''' init testing '''
    v2_endpoint = 'https://sonarcloud.statuspage.io/api/v2'
    api = sc_statuspage_api.ScStatusPageApi()
    assert api.endpoint == v2_endpoint

    v1_endpoint = 'https://sonarcloud.statuspage.io/api/v2'
    api = sc_statuspage_api.ScStatusPageApi(endpoint=v1_endpoint)
    assert api.endpoint == v1_endpoint

@pytest.mark.skip('TODO')
def test_sc_components():
    pass

def test_sc_status():
    api = sc_statuspage_api.ScStatusPageApi()
    status = api.get_status()['status']['indicator']
    assert status in [ x.value for x in sc_statuspage_api.ScImpactStatus ] 