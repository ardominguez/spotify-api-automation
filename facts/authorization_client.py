import os

from facts.rest_client import RestClient
from facts.endpoints import BASE_AUTH_SPOTIFY
from utils.rest_utils import build_basic_authorization_header


def get_access_token():
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    refresh_token = os.getenv("REFRESH_TOKEN")
    basic_auth_header = build_basic_authorization_header(client_id, client_secret)
    rest_client = RestClient(BASE_AUTH_SPOTIFY, basic_auth_header)
    form_body = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    auth_code, auth_response = rest_client.do_post_data("/api/token", form_body)
    return auth_response['access_token']


def build_invalid_access_token():
    return get_access_token() + "testing"
