class BaseQuestion:

    @staticmethod
    def is_a_list(response_body):
        if isinstance(response_body, dict):
            valid_list = response_body.get("items", None)
            if isinstance(valid_list, list):
                return True
        return False

    @staticmethod
    def validated_status_code_response(context, expected_code):
        current_status_code_response = context.response_code
        return int(expected_code) == int(current_status_code_response)

    @staticmethod
    def is_a_empty_list(response_body):
        if isinstance(response_body, dict):
            get_list = response_body.get("items", None)
            if isinstance(get_list, list) and get_list == []:
                return True
        return False

    @staticmethod
    def validated_error_message_response(context, expected_message):
        error_message_response = context.response_body['error']['message']
        return str(error_message_response) == str(expected_message)
