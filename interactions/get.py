import requests


class Get(object):
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get(self):
        r = requests.get(f'{self.url}', headers=self.headers)
        if r.headers.get("content-type", "").strip().startswith("application/json"):
            response = r.json()
        else:
            response = r.text
        return r.status_code, response


def build_request_param(param_key, param_value):
    value = param_value
    if isinstance(param_value, list):
        value = ",".join(param_value)

    return "{}={}&".format(param_key, value)


class GetParams(object):
    def __init__(self, url, headers, params):
        self.url = url
        self.headers = headers
        self.params = params

    def get(self):
        url_params = ""
        if self.params is not None:
            url_params = "?"
            for param_key, param_value in self.params.items():
                url_params += build_request_param(param_key, param_value)

        r = requests.get(f'{self.url}{url_params[:-1]}', headers=self.headers)
        if r.headers.get("content-type", "").strip().startswith("application/json"):
            response = r.json()
        else:
            response = r.text
        return r.status_code, response
