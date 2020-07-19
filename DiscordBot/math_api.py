import requests

URL = 'https://api.mathjs.org/v4/?expr='


def get_math(expr):
    req = requests.get(f'{URL}{expr}')

    return req.text
