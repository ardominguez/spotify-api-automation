from behave import given, when, then, step, use_step_matcher
from facts.authorization_client import get_access_token
from facts.endpoints import BASE_API_SPOTIFY
from facts.rest_client import RestClient
from facts.services import services
from questions.base_questions import BaseQuestion
from task.common_task import call_service_with_variable_path, call_service_with_parameters
from utils.load_json import load_variable_path, load_parameters
from utils.rest_utils import build_bearer_authorization_header

use_step_matcher("parse")


# /auth
@given(u'I get the authorization api access token')
def step_impl(context):
    context.access_token = get_access_token()


# /request
@step(u'I execute a "{method}" request to service "{service}" with path variable "{variable_path}"')
def step_impl(context, method, service, variable_path):
    context.response_code, context.response_body = call_service_with_variable_path(context, method, service, variable_path)


@when(u'I execute a "{method}" request to service "{service}" with path variable "{variable_path}" and parameters "{parameter}"')
def step_impl(context, method, service, variable_path, parameter):
    context.response_code, context.response_body = call_service_with_parameters(method, service, parameter)


# /code response
@step(u'I receive a valid "{code_response}" status response code')
def step_impl(context, code_response):
    assert BaseQuestion.validated_status_code_response(context, code_response)


# /error response message
@step(u'I receive a valid error message "{error_message}"')
def step_impl(context, error_message):
    assert BaseQuestion.validated_error_message_response(context, error_message)
