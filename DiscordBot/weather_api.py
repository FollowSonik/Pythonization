import requests

URL = 'https://customapi.aidenwallis.co.uk/api/v1/misc/weather'


def get_weather(city):
    req = requests.get(f'{URL}/{city}')

    return req.text
