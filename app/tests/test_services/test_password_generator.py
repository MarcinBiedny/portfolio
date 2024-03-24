import pytest
import string
from app.services.password_generator import PasswordGenerator

pg = PasswordGenerator()


def test_password_contains_only_lower():
    for pl in range(8, 25):
        password = pg.generate(
            include_uppercase=False,
            include_numbers=False,
            include_special_chars=False,
            password_length=pl,
        )

        assert_password_correct_len(password=password, expected_len=pl)

        assert all(
            char.islower() for char in password
        ), "The generated password should contain only 'lowercase' characters"


def test_password_contains_lower_and_special():
    for pl in range(8, 25):
        password = pg.generate(
            include_uppercase=False,
            include_numbers=False,
            include_special_chars=True,
            password_length=pl,
        )

        assert_password_correct_len(password=password, expected_len=pl)

        assert (
            any(char.islower() for char in password)
            and not any(char.isupper() for char in password)
            and not any(char.isdigit() for char in password)
            and any(char in string.punctuation for char in password)
        ), "The generated password should not contain 'uppercase' or 'digit' characters."


def test_password_does_not_contain_upper():
    for pl in range(8, 25):
        password = pg.generate(
            include_uppercase=False,
            include_numbers=True,
            include_special_chars=True,
            password_length=pl,
        )

        assert_password_correct_len(password=password, expected_len=pl)

        assert (
            any(char.islower() for char in password)
            and not any(char.isupper() for char in password)
            and any(char.isdigit() for char in password)
            and any(char in string.punctuation for char in password)
        ), "The generated password should not contain 'uppercase' characters."


def test_password_contains_all():
    for pl in range(8, 25):
        password = pg.generate(
            include_uppercase=True,
            include_numbers=True,
            include_special_chars=True,
            password_length=pl,
        )

        assert_password_correct_len(password=password, expected_len=pl)

        assert (
            any(char.islower() for char in password)
            and any(char.isupper() for char in password)
            and any(char.isdigit() for char in password)
            and any(char in string.punctuation for char in password)
        ), "The generated password must contain at least:one lowercase letter, one uppercase letter, one number and one special character."


def test_password_length_error():
    with pytest.raises(ValueError) as e:
        pg.generate(password_length=7)

    assert (
        str(e.value) == "Password lenght must be between 8 and 24"
    ), "Incorrect error message."

    with pytest.raises(ValueError) as e:
        pg.generate(password_length=25)

    assert (
        str(e.value) == "Password lenght must be between 8 and 24"
    ), "Incorrect error message."


# ================== support functions


def assert_password_correct_len(password: str, expected_len: int) -> bool:
    assert (
        len(password) == expected_len
    ), f"Password should have {expected_len} characters, but having {len(password)}."
