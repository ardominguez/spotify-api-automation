import requests


class Put(object):
    def __init__(self, url, headers, data):
        self.url = url
        self.headers = headers
        self.data = data

    def put(self):
        r = requests.put(self.url, headers=self.headers, json=self.data)
        return r.status_code, {} if r.text == '' else r.json()
