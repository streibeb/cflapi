# CFLApi - a Python client for The Canadian Football League statistics API

## Description

CFLApi is a lightweight client library for the CFL statistics API

## Documentation

- [Official API Documentation](http://api.cfl.ca/docs)

## Installation

TODO

## Dependencies

- [Requests](https://github.com/kennethreitz/requests)

## API Key
You will need an API key to access the CFL API. To obtain a key, submit a [API key request](http://api.cfl.ca/key-request)

## Example

```python
import cflapi
api = cflapi.CFLApi(YOUR API KEY HERE)

response = api.getGamesBySeason(2018, filter={'team': {'eq': 'SSK'}})
for game in response['data']:
    print(game['date_start'], game['team_1']['nickname'], '@', game['team_2']['nickname'])
```

## Support
If you find an bug, have any questions or have suggestions for improvements then feel free to file an issue on the Github project page [here](https://github.com/streibeb/cflapi/issues).
