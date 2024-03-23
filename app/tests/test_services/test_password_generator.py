import pytest
import string
from app.services.password_generator import PasswordGenerator

pg = PasswordGenerator()


def test_generate_length():
    for pl in range(8, 25):
        password = pg.generate(password_length=pl)

        assert (
            len(password) == pl
        ), f"Password should have {pl} characters, but having {len(password)}."


def test_password_contains_lowercase_letters():
    password = pg.generate(
        include_uppercase=True,
        include_numbers=True,
        include_special_chars=True,
        password_length=8,
    )

    assert any(
        char.islower() for char in password
    ), "Generated password must contain at least one lowercase character."


def test_password_contains_uppercase_letters():
    password = pg.generate(
        include_uppercase=True,
        include_numbers=True,
        include_special_chars=True,
        password_length=8,
    )

    assert any(
        char.isupper() for char in password
    ), "Generated password must contain at least one upercase character."


def test_password_contains_numbers():
    password = pg.generate(
        include_uppercase=True,
        include_numbers=True,
        include_special_chars=True,
        password_length=8,
    )

    assert any(
        char.isdigit() for char in password
    ), "Generated password must contain at least one digit character."


def test_password_contains_punctuation():
    password = pg.generate(
        include_uppercase=True,
        include_numbers=True,
        include_special_chars=True,
        password_length=8,
    )

    assert any(
        char in string.punctuation for char in password
    ), "Generated password must contain at least one punctuation character."


def test_password_contains_all():
    password = pg.generate(
        include_uppercase=True,
        include_numbers=True,
        include_special_chars=True,
        password_length=8,
    )

    assert (
        any(char.islower() for char in password)
        and any(char.isupper() for char in password)
        and any(char.isdigit() for char in password)
        and any(char in string.punctuation for char in password)
    ), "The generated password must contain at least: one lowercase letter, one uppercase letter, one number and one special character."


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
