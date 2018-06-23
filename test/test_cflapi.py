from test import *

def test_get_leaders(response_keys):
    api = CFLApi(API_KEY)
    response = api.getLeaders(2015, 'converts')

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"

def test_get_team_leaders(response_keys):
    api = CFLApi(API_KEY)
    response = api.getTeamLeaders(2015, 'total_yards')

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"

def test_get_standings(response_keys):
    api = CFLApi(API_KEY)
    response = api.getStandings(2015)

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"

def test_get_teams(response_keys):
    api = CFLApi(API_KEY)
    response = api.getTeams()

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"