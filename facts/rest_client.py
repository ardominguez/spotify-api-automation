from facts.services import services
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
            return self.do_get(path)
        elif method == "POST":
            return self.do_post(path, request_body)
        elif method == "DELETE":
            return self.do_delete(path)
        elif method == "PATCH":
            return self.do_patch(path, request_body)

    def do_request1(self, method, service, data_file):
        base_path = services[service]["base_path"]
        full_url = self.build_full_url(base_path, data_file)
        request_body = self.get_optional_attribute(data_file, "request_body")

        if method == "GET":
            return self.do_get(full_url)
        elif method == "POST":
            return self.do_post(full_url, request_body)
        elif method == "DELETE":
            return self.do_delete(full_url)
        elif method == "PATCH":
            return self.do_patch(full_url, request_body)

    def do_get(self, path):
        uri = self.endpoint + path
        request = GetParams(uri, self.headers)
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

    def build_full_url(self, base_path, data_file):
        full_url = base_path + data_file["operation_url"]
        path_variables = self.get_optional_attribute(data_file, "path_variables")
        query_params = self.get_optional_attribute(data_file, "query_params")

        if path_variables is not None:
            for key, value in path_variables.items():
                full_url = full_url.replace(f":{key}", value)

        params = ""
        if query_params is not None:
            for key, value in query_params.items():
                params = params + ("?" if params == "" else "&") + f"{key}={value}"

        return full_url + params

    def get_optional_attribute(self, obj, attributeName):
        try:
            return obj[attributeName]
        except Exception:
            return None
