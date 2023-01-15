from interactions.post import Post
from interactions.get import GetParams
from interactions.delete import DeleteRequest
from interactions.patch import Patch


class RestClient(object):

    def __init__(self, endpoint, auth_token=None):
        self.endpoint = endpoint
        self.headers = {}
        if auth_token is not None:
            self.headers["Authorization"] = auth_token

    def do_request(self, method, path, request_body, parameters):
        if method == "GET":
            return self.do_get(path, parameters)
        elif method == "POST":
            return self.do_post(path, request_body)
        elif method == "DELETE":
            return self.do_delete(path)
        elif method == "PATCH":
            return self.do_patch(path, request_body)

    def do_get(self, path, parameters):
        uri = self.endpoint + path
        request = GetParams(uri, self.headers, parameters)
        return request.get()

    def do_post(self, path, request_body):
        uri = self.endpoint + path
        request = Post(uri, self.headers, request_body)
        return request.post()

    def do_post_data(self, path, form_data):
        uri = self.endpoint + path
        request = Post(uri, self.headers, form_data)
        return request.post_data()

    def do_delete(self, path):
        uri = self.endpoint + path
        request = DeleteRequest(uri, self.headers)
        return request.delete()

    def do_patch(self, path, request_body):
        uri = self.endpoint + path
        request = Patch(uri, self.headers, request_body)
        return request.patch()

    def do_put(self):
        pass
