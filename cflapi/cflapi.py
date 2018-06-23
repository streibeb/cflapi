import requests
from urllib.parse import urljoin, urlencode
from .utils import flatten

class APIKeyMissingError(Exception):
    pass

class CFLApi(object):
    def __init__(self, apiKey, baseUri='http://api.cfl.ca'):
        if apiKey == None:
            raise APIKeyMissingError(
                "An API Key is required. Request one at the following URL: "
                "http://api.cfl.ca/key-request "
            )

        self._baseUri = baseUri

        self._session = requests.Session()
        self._session.params = {}
        self._session.params['key'] = apiKey
    
    def __buildParams(self, kwargs):
        params = []

        if 'include' in kwargs:
            params.append(self.__parseIncludeParams(kwargs['include']))
        if 'sort' in kwargs:
            params.append(self.__parseSortParams(kwargs['sort']))
        if 'filter' in kwargs:
            params.append(self.__parseFilterParams(kwargs['filter']))
        if 'pageNumber' in kwargs:
            params.append('page[number]={num}'.format(num=kwargs['pageNumber']))
        if 'pageSize' in kwargs:
            params.append('page[size]={size}'.format(size=kwargs['pageSize']))

        return '?' + '&'.join(params)

    def __parseIncludeParams(self, args):
        params = 'include='
        if type(args) == list:
            params += ','.join(args)
        else:
            params += args
        return params

    def __parseSortParams(self, args):
        params = 'sort='
        if type(args) == list:
            params += ','.join(args)
        else:
            params += args
        return params

    def __parseFilterParams(self, args):
        filters = []
        if type(args) == list:
            for f in args:
                filters.append(flatten(f, 'filter'))
            return '&'.join(filters)
        else:
            return flatten(args, 'filter')

    def getGames(self, **kwargs):
        url = urljoin(self._baseUri, '/v1/games')
        response = self._session.get(url + self.__buildParams(kwargs))
        return response.json()

    def getGamesBySeason(self, season, **kwargs):
        url = urljoin(self._baseUri, '/v1/games/{season}'
                .format(season=season))
        response = self._session.get(url + self.__buildParams(kwargs))
        return response.json()

    def getGame(self, season, gameId, **kwargs):
        url = urljoin(self._baseUri, '/v1/games/{season}/game/{gameId}'
                .format(season=season, gameId=gameId))
        response = self._session.get(url + self.__buildParams(kwargs))
        return response.json()

    def getPlayers(self, **kwargs):
        url = urljoin(self._baseUri, '/v1/players')
        response = self._session.get(url + self.__buildParams(kwargs))
        return response.json()

    def getPlayer(self, playerId, **kwargs):
        url = urljoin(self._baseUri, '/v1/players/{playerId}'
                .format(playerId=playerId))
        response = self._session.get(url + self.__buildParams(kwargs))
        return response.json()

    def getLeaders(self, season, category, **kwargs):
        url = urljoin(self._baseUri, '/v1/leaders/{season}/category/{category}'
                .format(season=season, category=category))
        response = self._session.get(url + self.__buildParams(kwargs))
        return response.json()

    def getTeamLeaders(self, season, category, **kwargs):
        url = urljoin(self._baseUri, '/v1/team_leaders/{season}/category/{category}'
                .format(season=season, category=category))
        response = self._session.get(url + self.__buildParams(kwargs))
        return response.json()

    def getStandings(self, season):
        url = urljoin(self._baseUri, '/v1/standings/{season}'
                .format(season=season))
        response = self._session.get(url)
        return response.json()

    def getCrossoverStandings(self, season):
        url = urljoin(self._baseUri, '/v1/standings/crossover/{season}'
                .format(season=season))
        response = self._session.get(url)
        return response.json()

    def getTeams(self):
        url = urljoin(self._baseUri, '/v1/teams')
        response = self._session.get(url)
        return response.json()