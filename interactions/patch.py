import requests


class Patch(object):
    def __init__(self, url, headers, data):
        self.url = url
        self.headers = headers
        self.data = data

    def patch(self):
        r = requests.patch(self.url, headers=self.headers, json=self.data)
        return r.status_code, {} if r.text == '' else r.json()
