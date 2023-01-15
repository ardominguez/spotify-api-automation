import requests


class DeleteRequest(object):
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def delete(self):
        r = requests.delete(f'{self.url}', headers=self.headers)
        return r.status_code, {} if r.text == '' else r.json()