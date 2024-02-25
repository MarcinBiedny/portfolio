import secrets, string


class PasswordGenerator:
    def __init__(self):
        pass

    def generate_password(self, lenght=8):
        return "".join(
            (
                secrets.choice(
                    string.ascii_letters + string.punctuation + string.digits
                )
                for _ in range(lenght)
            )
        )


password_generator = PasswordGenerator()
new_password = password_generator.generate_password()
print(new_password)
