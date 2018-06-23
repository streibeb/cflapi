from test import *

GAME_ID = 2221
SEASON = 2015

def test_get_games(response_keys):
    api = CFLApi(API_KEY)
    response = api.getGames()

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"

def test_get_games_by_season(response_keys):
    api = CFLApi(API_KEY)
    response = api.getGamesBySeason(SEASON)

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    assert response['data'][0]['season'] == SEASON

def test_get_game(response_keys):
    api = CFLApi(API_KEY)
    response = api.getGame(SEASON, GAME_ID)

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    assert response['data'][0]['game_id'] == GAME_ID
    assert response['data'][0]['season'] == SEASON

def test_get_game_include_boxscore(response_keys):
    api = CFLApi(API_KEY)
    response = api.getGame(SEASON, GAME_ID, include='boxscore')

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    game = response['data'][0]
    assert game['game_id'] == GAME_ID
    assert game['season'] == SEASON
    assert isinstance(game['boxscore'], dict)

def test_get_game_include_play_by_play(response_keys):
    api = CFLApi(API_KEY)
    response = api.getGame(SEASON, GAME_ID, include='play_by_play')

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    game = response['data'][0]
    assert game['game_id'] == GAME_ID
    assert game['season'] == SEASON
    assert isinstance(game['play_by_play'], list)

def test_get_game_include_boxscore_and_play_by_play(response_keys):
    api = CFLApi(API_KEY)
    response = api.getGame(SEASON, GAME_ID, include=['boxscore','play_by_play'])

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    game = response['data'][0]
    assert game['game_id'] == GAME_ID
    assert game['season'] == SEASON
    assert isinstance(game['boxscore'], dict)
    assert isinstance(game['play_by_play'], list)

def test_get_games_sort_by_date_start_asc(response_keys):
    api = CFLApi(API_KEY)
    response = api.getGames(sort='date_start')

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    
    firstGame, lastGame = response['data'][0], response['data'][-1]
    assert firstGame['date_start'] <= lastGame['date_start']

def test_get_games_sort_by_date_start_desc(response_keys):
    api = CFLApi(API_KEY)
    response = api.getGames(sort='-date_start')

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    
    firstGame, lastGame = response['data'][0], response['data'][-1]
    assert firstGame['date_start'] >= lastGame['date_start']

def test_get_games_filter_by_event_type_id(response_keys):
    api = CFLApi(API_KEY)
    response = api.getGames(filter={'event_type_id': {'eq': 3}})

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    for game in response['data']:
        assert game['event_type']['event_type_id'] == 3

def test_get_games_filter_by_event_type_id_and_season(response_keys):
    api = CFLApi(API_KEY)
    response = api.getGames(filter=[{'event_type_id': {'eq': 3}},{'season': {'eq': 2016}}])

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    assert len(response['data']) == 1
    assert response['data'][0]['season'] == 2016
    assert response['data'][0]['event_type']['event_type_id'] == 3

def test_get_games_10_per_page(response_keys):
    api = CFLApi(API_KEY)
    response = api.getGames(pageSize=10)

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"
    assert len(response['data']) == 10

def test_get_games_page_2(response_keys):
    api = CFLApi(API_KEY)

    response1 = api.getGames(pageSize=10)
    assert isinstance(response1, dict)
    assert set(response_keys).issubset(response1.keys()), "All keys should be in the response"
    assert len(response1['data']) == 10

    response2 = api.getGames(pageNumber=2,pageSize=10)
    assert isinstance(response2, dict)
    assert set(response_keys).issubset(response2.keys()), "All keys should be in the response"
    assert len(response2['data']) == 10

    assert response1['data'][0]['game_id'] != response2['data'][0]['game_id']

def test_get_games_filter_by_event_type_id_sort_by_attendance_desc(response_keys):
    api = CFLApi(API_KEY)
    response = api.getGames(filter={'event_type_id': {'eq': 3}}, sort='-attendance')

    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys()), "All keys should be in the response"

    firstGame, lastGame = response['data'][0], response['data'][-1]
    assert firstGame['attendance'] >= lastGame['attendance']
    for game in response['data']:
        assert game['event_type']['event_type_id'] == 3