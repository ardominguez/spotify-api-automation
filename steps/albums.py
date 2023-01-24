from behave import given, when, then, step, use_step_matcher


# /albums steps
from task.albums_task import get_market, build_request_by_market


@given('I get an available market for an album')
def step_impl(context):
    context.available_market = get_market(context)


@when(u'I execute a "{method}" request to service "{service}" with path variable "{variable_path}" for an available market')
def step_impl(context, method, service, variable_path):
    context.response_code, context.response_body = build_request_by_market(context, method, service, variable_path, context.available_market)

