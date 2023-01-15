from behave import given, when, then, step, use_step_matcher

from facts import rest_client
from facts.authorization_client import get_access_token
from facts.endpoints import BASE_API_SPOTIFY
from facts.rest_client import RestClient
from questions.base_questions import BaseQuestion
from utils.load_json import load_variable_path, load_parameters
from utils.rest_utils import build_basic_authorization_header, build_bearer_authorization_header

use_step_matcher("parse")


# /auth
@given(u'I get the authorization api access token for execute endpoint "{endpoint_folder}"')
def step_impl(context, endpoint_folder):
    context.access_token = get_access_token()
    context.data_folder = endpoint_folder


# /request
@step(u'I execute a "{method}" request to endpoint path "{endpoint_path}" with path variable "{variable_path}"')
def step_impl(context, method, endpoint_path, variable_path):
    variable = load_variable_path(context.data_folder, variable_path)
    context.path_variable_id = variable['id']
    auth_bearer_header = build_bearer_authorization_header(context.access_token)
    path = endpoint_path + context.path_variable_id
    rest_client = RestClient(BASE_API_SPOTIFY, auth_bearer_header)
    context.response_code, context.response_body = rest_client.do_request(method, path, None, None)


@when(u'I execute a "{method}" request to "{endpoint_path}" with path variable "{variable_path}" and parameters "{parameter}"')
def step_impl(context, method, endpoint_path, variable_path, parameter):
    auth_bearer_header = build_bearer_authorization_header(context.access_token)

    rest_client = RestClient(BASE_API_SPOTIFY, auth_bearer_header)
    variable = load_variable_path(context.data_folder, variable_path)
    context.path_variable_id = variable['id']

    loaded_params = load_parameters(context.data_folder, parameter)

    path = endpoint_path + context.path_variable_id
    loaded_body = None
    context.response_code, context.response_body = rest_client.do_request(method, path, loaded_body, loaded_params)


# /code response
@step(u'I receive a valid "{code_response}" status response code')
def step_impl(context, code_response):
    current_status_code_response = context.response_code
    expected_code_response = int(code_response)
    assert BaseQuestion.validated_status_code_response(expected_code_response, current_status_code_response)


# /error response message
@step(u'I receive a valid error message "{error_message}"')
def step_impl(context, error_message):
    error_message_response = context.response_body['error']['message']
    expected_error = str(error_message)
    assert error_message_response == expected_error
