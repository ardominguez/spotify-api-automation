import json
import os


def load_request_body(folder, data_json):
    return load_json(folder, "{}_request_body.json".format(data_json))


def load_parameters(folder, data_json):
    return load_json(folder, "{}_parameters.json".format(data_json))


def load_json(folder, data_json):
    with open("{}/data/{}/{}".format(os.getcwd(), folder, data_json)) as json_file:
        return json.loads(json_file.read())


def load_variable_path(folder, data_json):
    return load_json(folder, "{}_variable_path.json".format(data_json))
