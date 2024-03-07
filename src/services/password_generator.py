import secrets, string


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
        while True:
            if not (
                self.MINIMUM_PASSWORD_LEN
                <= password_length
                <= self.MAXIMUM_PASSWORD_LEN
            ):
                raise ValueError(
                    f"Password lenght must be between {self.MINIMUM_PASSWORD_LEN} and {self.MAXIMUM_PASSWORD_LEN}"
                )

            character_set = string.ascii_lowercase

            if include_uppercase:
                character_set += string.ascii_uppercase
            if include_numbers:
                character_set += string.digits
            if include_special_chars:
                character_set += string.punctuation

            generated_password = "".join(
                secrets.choice(character_set) for _ in range(password_length)
            )

            if (
                (
                    not include_uppercase
                    or any(char.isupper() for char in generated_password)
                )
                and (
                    not include_numbers
                    or any(char.isdigit() for char in generated_password)
                )
                and (
                    not include_special_chars
                    or any(char in string.punctuation for char in generated_password)
                )
            ):
                return generated_password


password_generator = PasswordGenerator()
try:
    print(password_generator.generate())
except ValueError as e:
    print(f"Error: {e}")
