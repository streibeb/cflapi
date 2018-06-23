from test import *

PLAYER_ID = 159141

def test_get_players(response_keys):
    api = CFLApi(API_KEY)
    response = api.getPlayers()

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"

def test_get_player(response_keys):
    api = CFLApi(API_KEY)
    response = api.getPlayer(PLAYER_ID)

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    assert response['data'][0]['cfl_central_id'] == PLAYER_ID

def test_get_player_include_seasons(response_keys):
    api = CFLApi(API_KEY)
    response = api.getPlayer(PLAYER_ID, include='seasons')

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    assert response['data'][0]['cfl_central_id'] == PLAYER_ID
    assert isinstance(response['data'][0]['seasons'], dict)

def test_get_player_include_game_by_game(response_keys):
    api = CFLApi(API_KEY)
    response = api.getPlayer(PLAYER_ID, include='game_by_game')

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    assert response['data'][0]['cfl_central_id'] == PLAYER_ID
    assert isinstance(response['data'][0]['game_by_game'], dict)

def test_get_player_include_seasons_and_game_by_game(response_keys):
    api = CFLApi(API_KEY)
    response = api.getPlayer(PLAYER_ID, include=['seasons','game_by_game'])

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    assert response['data'][0]['cfl_central_id'] == PLAYER_ID
    assert isinstance(response['data'][0]['seasons'], dict)
    assert isinstance(response['data'][0]['game_by_game'], dict)

def test_get_players_sort_by_birth_date_asc(response_keys):
    api = CFLApi(API_KEY)
    response = api.getPlayers(sort='birth_date')

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    
    firstGame, lastGame = response['data'][0], response['data'][-1]
    assert firstGame['birth_date'] <= lastGame['birth_date']

def test_get_players_sort_by_height_desc(response_keys):
    api = CFLApi(API_KEY)
    response = api.getPlayers(sort='-height')

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    
    firstGame, lastGame = response['data'][0], response['data'][-1]
    assert firstGame['height'] >= lastGame['height']

def test_get_players_filter_by_position_abbreviation(response_keys):
    api = CFLApi(API_KEY)
    response = api.getPlayers(filter={'position_abbreviation': {'eq': 'QB'}})

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    for player in response['data']:
        assert player['position']['abbreviation'] == 'QB'
