import requests


class Post(object):
    def __init__(self, url, headers, data):
        self.url = url
        self.headers = headers
        self.data = data

    def post(self):
        if "file" in self.data.keys():
            request_params = []
            for key_name in self.data.keys():
                if key_name == 'file':
                    file_location = self.data["file"]["location"]
                    file_name = file_location.split("/")[-1]
                    file_media_type = self.data["file"]["media_type"]
                    multipart_key = self.data.get("multipart_key", 'file')
                    file_content = open(file_location, 'rb')

                    request_params.append((multipart_key, (file_name, file_content, file_media_type)))
                else:
                    request_params.append((key_name, (None, self.data[key_name])))

            request_multipart_headers = {
                "Authorization": self.headers["Authorization"]
            }

            r = requests.post('{}'.format(self.url),
                              headers=request_multipart_headers, files=request_params)
        else:
            r = requests.post('{}/'.format(self.url),
                              headers=self.headers, json=self.data)
        return r.status_code, {} if r.text == '' else r.json()

    def post_data(self):
        r = requests.post(
            '{}/'.format(self.url),
            headers=self.headers,
            data=self.data
        )
        return r.status_code, {} if r.text == '' else r.json()
