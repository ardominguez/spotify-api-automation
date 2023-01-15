from behave import given, when, then, step, use_step_matcher
from questions.base_questions import BaseQuestion


# /artists steps
@step(u'The artist "{artist_type}" should be "{artist}"')
def step_impl(context, artist_type, artist):
    current_artist = context.response_body[type]
    expected_artist_information = str(artist)
    assert current_artist == expected_artist_information
