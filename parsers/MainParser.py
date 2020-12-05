import requests
from bs4 import BeautifulSoup

class Parser:

    def __init__(self, url, **kwargs):
        if kwargs:
            self.url = url.replace(kwargs)
        else:
            self.url = url

    def get_data(self, selector=None):
        req = requests.get(self.url)
        if not selector:
            return req.text
        else:
            soup = BeautifulSoup(req.text)
            results = soup.select(selector)
            return results

