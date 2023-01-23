from facts.endpoints import BASE_API_SPOTIFY
from facts.rest_client import RestClient
from facts.services import services
from utils.load_json import load_variable_path, load_parameters, load_request_body
from utils.rest_utils import build_bearer_authorization_header


def call_service_with_variable_path(context, method, service, variable_path):
    request_body = None
    request_params = None
    call_service(context, method, service, variable_path, request_body, request_params)


def call_service_with_parameters(context, method, service, variable_path, parameter):
    request_body = None
    request_params = load_parameters(get_folder_data_location(service), parameter)
    call_service(context, method, service, variable_path, request_body, request_params)


def call_service_with_body(context, method, service, variable_path, body_data_name, parameter_data_name):
    folder_data_location = get_folder_data_location(service)
    request_body = load_request_body(folder_data_location, body_data_name)
    request_params = load_parameters(folder_data_location, parameter_data_name)
    call_service(context, method, service, variable_path, request_body, request_params)


def call_service(context, method, service, variable_path, request_body, request_parameters):
    variable = load_variable_path(get_folder_data_location(service), variable_path)
    context.path_variable_id = variable['id']
    path = services[service]["base_path"] + context.path_variable_id

    auth_bearer_header = build_bearer_authorization_header(context.access_token)

    rest_client = RestClient(BASE_API_SPOTIFY, auth_bearer_header)
    return rest_client.do_request(method, path, request_body, request_parameters)


def get_folder_data_location(service):
    return services[service]["folder_name"]