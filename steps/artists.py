from behave import given, when, then, step, use_step_matcher
from questions import artist_questions


# /artists steps
@step(u'The artist "{artist_information}" should be "{artist_value}"')
def step_impl(context, artist_information, artist_value):
    assert artist_questions.validated_artist_information(context, artist_information, artist_value)
