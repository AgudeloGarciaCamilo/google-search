from constants.app_config import SEARCH_TERM_INPUT_MESSAGE


class CustomInput:
    def get_user_input(self, input_message) -> str:
        print("\n")
        user_input = input(input_message)
        print("\n")

        return user_input
