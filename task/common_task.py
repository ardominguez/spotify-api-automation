from facts.endpoints import BASE_API_SPOTIFY
from facts.rest_client import RestClient
from facts.services import services
from utils.load_json import load_variable_path, load_parameters, load_request_body, load_data_file
from utils.rest_utils import build_bearer_authorization_header


def call_service_with_variable_path(context, method, service, data_file):
    request_body = None
    request_params = None
    return call_service(context, method, service, data_file)


def call_service_with_parameters(context, method, service, variable_path, parameter):
    request_body = None
    request_params = load_parameters(get_folder_data_location(service), parameter)
    #return call_service(context, method, service, variable_path, request_body, request_params)


def call_service_with_body(context, method, service, variable_path, body_data_name, parameter_data_name):
    folder_data_location = get_folder_data_location(service)
    request_body = load_request_body(folder_data_location, body_data_name)
    request_params = load_parameters(folder_data_location, parameter_data_name)
    #return call_service(context, method, service, variable_path, request_body, request_params)


def call_service(context, method, service, data_file):
    auth_bearer_header = build_bearer_authorization_header(context.access_token)
    rest_client = RestClient(BASE_API_SPOTIFY, auth_bearer_header)

    data_file = load_data_file(service, data_file)

    return rest_client.do_request1(method, service, data_file)


def get_folder_data_location(service):
    return services[service]["folder_name"]

