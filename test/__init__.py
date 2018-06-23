from pytest import fixture
from cflapi import CFLApi
from os import environ

API_KEY = # YOUR API KEY HERE

@fixture
def response_keys():
    return ['data', 'errors', 'meta']