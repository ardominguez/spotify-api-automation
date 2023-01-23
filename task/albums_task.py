from facts.endpoints import BASE_API_SPOTIFY
from facts.rest_client import RestClient
from facts.services import services
from utils.load_json import load_variable_path
from utils.rest_utils import build_bearer_authorization_header


def get_market(context):
    context.execute_steps(u"""
        When I execute a "GET" request to service "albums" with path variable "valid_album_id"
    """)
    get_available_market = context.response_body['available_markets'][0]
    return {'market': get_available_market}


def build_request_by_market(context, method, service, variable_path, parameter):
    auth_bearer_header = build_bearer_authorization_header(context.access_token)
    rest_client = RestClient(BASE_API_SPOTIFY, auth_bearer_header)
    variable = load_variable_path(services[service]["folder_name"], variable_path)
    context.path_variable_id = variable['id']

    path = services[service]["base_path"] + context.path_variable_id
    loaded_body = None
    return rest_client.do_request(method, path, loaded_body, parameter)

