import base64


def build_basic_authorization_header(client_id, secret_key):
    token_plain = "{}:{}".format(client_id, secret_key)
    token = base64.b64encode(token_plain.encode("ascii"))
    return "Basic {}".format(token.decode())


def build_bearer_authorization_header(token):
    return "Bearer {}".format(token)


def build_invalid_authorization_header(token):
    return {"Authorization": "token {}".format(token)}


def get_token_from_auth_response(auth_response):
    if auth_response.get("jwt"):
        return auth_response.get("jwt")
    elif auth_response.get("token"):
        return auth_response.get("token")
    else:
        return None


def build_request_endpoint():
    pass
