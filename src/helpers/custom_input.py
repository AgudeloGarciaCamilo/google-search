from constants.app_config import USER_PROMPT_INPUT_MESSAGE


class CustomInput:
    def __init__(self):
        self.input_message = USER_PROMPT_INPUT_MESSAGE

    def get_user_input(self) -> str:
        print("\n")
        user_input = input(self.input_message)
        print("\n")

        return user_input

