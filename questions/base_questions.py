
class BaseQuestion:

    @staticmethod
    def is_a_list(response_body):
        if isinstance(response_body, dict):
            valid_list = response_body.get("items", None)
            if isinstance(valid_list, list):
                return True
        return False

    @staticmethod
    def validated_status_code_response(expected_code, current_code):
        return expected_code == current_code

    @staticmethod
    def is_a_empty_list(response_body):
        if isinstance(response_body, dict):
            get_list = response_body.get("items", None)
            if isinstance(get_list, list) and get_list == []:
                return True
        return False
