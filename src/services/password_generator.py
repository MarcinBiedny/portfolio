import secrets, string


class PasswordGenerator:
    MINIMUM_PASSWORD_LEN = 8
    MAXIMUM_PASSWORD_LEN = 24

    def __init__(self):
        pass

    def generate(
        self,
        include_upercase: bool = True,
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

        character_set = (
            string.ascii_lowercase
            + (string.ascii_uppercase if include_upercase else "")
            + (string.digits if include_numbers else "")
            + (string.punctuation if include_special_chars else "")
        )

        return "".join(secrets.choice(character_set) for _ in range(password_length))


password_generator = PasswordGenerator()
try:
    print(password_generator.generate())
except ValueError as e:
    print(f"Error: {e}")
