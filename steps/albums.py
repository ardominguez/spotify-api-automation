from behave import given, when, then, step, use_step_matcher


# /albums steps
from facts.endpoints import BASE_API_SPOTIFY
from facts.rest_client import RestClient
from utils.load_json import load_variable_path
from utils.rest_utils import build_bearer_authorization_header


@given('I get an available market for an album')
def step_impl(context):
    context.execute_steps(u"""
        When I execute a "GET" request to endpoint path "/albums/" with path variable "valid_album_id"
    """)
    get_available_market = context.response_body['available_markets'][0]
    context.available_market = {'market': get_available_market}


@when(u'I execute a "{method}" request to "{endpoint_path}" with path variable "{variable_path}" for an available market')
def step_impl(context, method, endpoint_path, variable_path):
    auth_bearer_header = build_bearer_authorization_header(context.access_token)

    rest_client = RestClient(BASE_API_SPOTIFY, auth_bearer_header)
    variable = load_variable_path(context.data_folder, variable_path)
    context.path_variable_id = variable['id']

    path = endpoint_path + context.path_variable_id
    loaded_body = None
    context.response_code, context.response_body = rest_client.do_request(method, path, loaded_body, context.available_market)






