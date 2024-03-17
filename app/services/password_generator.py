import secrets, string
from random import shuffle


class PasswordGenerator:
    MINIMUM_PASSWORD_LEN = 8
    MAXIMUM_PASSWORD_LEN = 24

    def __init__(self):
        pass

    def generate(
        self,
        include_uppercase: bool = True,
        include_numbers: bool = True,
        include_special_chars: bool = True,
        password_length: int = 8,
    ) -> str:
        if not (
            self.MINIMUM_PASSWORD_LEN <= password_length <= self.MAXIMUM_PASSWORD_LEN
        ):
            raise ValueError(
                f"Password lenght must be between {self.MINIMUM_PASSWORD_LEN} and {self.MAXIMUM_PASSWORD_LEN}"
            )

        password_prefix = secrets.choice(string.ascii_lowercase)
        character_set = string.ascii_lowercase
        if include_uppercase == True:
            password_prefix += secrets.choice(string.ascii_uppercase)
            character_set += string.ascii_uppercase
        if include_numbers == True:
            password_prefix += secrets.choice(string.digits)
            character_set += string.digits
        if include_special_chars == True:
            password_prefix += secrets.choice(string.punctuation)
            character_set += string.punctuation

        password_suffix = "".join(
            secrets.choice(character_set)
            for _ in range(password_length - len(password_prefix))
        )

        password = password_prefix + password_suffix
        password_as_list = list(password)
        shuffle(password_as_list)

        return "".join(password_as_list)
