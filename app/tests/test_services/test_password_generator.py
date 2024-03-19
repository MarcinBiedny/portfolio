import pytest
import string
from app.services.password_generator import PasswordGenerator

pg = PasswordGenerator()


def test_generate_length1():
    for p_l in range(8, 25):
        password = pg.generate(password_length=p_l)

        assert len(password) == p_l


def test_generate_length2():
    password = pg.generate(password_length=10)

    assert len(password) == 10, "Generated password must have 10 characters."


def test_password_contains_lowercase_letters():
    password = pg.generate()

    assert any(
        char.islower() for char in password
    ), "Generated password must contain at least one lowercase character."


def test_password_contains_uppercase_letters():
    password = pg.generate(include_uppercase=True)

    assert any(
        char.isupper() for char in password
    ), "Generated password must contain at least one upercase character."


def test_password_contains_numbers():
    password = pg.generate(include_numbers=True)

    assert any(
        char.isdigit() for char in password
    ), "Generated password must contain at least one digit character."


def test_password_contains_punctuation():
    password = pg.generate(include_special_chars=True)

    assert any(
        char in string.punctuation for char in password
    ), "Generated password must contain at least one punctuation character."


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
