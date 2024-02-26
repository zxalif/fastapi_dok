import requests


def api():
    return requests.get('http://api.myip.com/').json()
