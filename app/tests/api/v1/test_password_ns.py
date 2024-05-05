from flask.testing import FlaskClient
from string import punctuation
import pytest

"""
Test Matrix:

METHOD | includeUppercase | includeNumbers | includeSpecialChars | passwordLength | Test Name
  POST          -                  -                  -                  -          test_wrong_method
  GET           -                  -                  -                  -          test_get_without_data
  GET           -                  -                  -                [7, 25]      test_incorrect_password_lengths
  GET       [True, False]    [True, False]      [True, False]          [8 - 24]     test_all_possible_positive_requests
"""


PASSWORD_GENERATE_ENDPOINT = "/api/v1/password/generate"


def test_wrong_method(client: FlaskClient):
    response = client.post(PASSWORD_GENERATE_ENDPOINT)

    assert response.status_code == 405
    data = response.get_json()
    assert "message" in data
    assert (
        data["message"] == "The method is not allowed for the requested URL."
    ), "Invalid response message."


def test_get_without_data(client: FlaskClient):
    response = client.get(PASSWORD_GENERATE_ENDPOINT)

    assert response.status_code == 200, "'200' is the expected response status code."
    data = response.get_json()
    assert (
        "password" in data
    ), "'password' key is expected to be present in responde data."

    password = data["password"]
    assert len(password) == 24, "Password by default is expected to be 24 chars long."
    assert (
        any(char.islower() for char in password)
        and any(char.isupper() for char in password)
        and any(char.isdigit() for char in password)
        and any(char in punctuation for char in password)
    ), "The generated password must contain at least:one lowercase letter, one uppercase letter, one number and one special character."


def test_incorrect_password_lengths(client: FlaskClient):
    password_lengths_to_test = [7, 25]

    for pl in password_lengths_to_test:
        response = client.get(f"{PASSWORD_GENERATE_ENDPOINT}?passwordLength={pl}")

        assert (
            response.status_code == 400
        ), "'400' is the expected response status code."
        data = response.get_json()
        assert (
            "errors" in data
        ), "'errors' key is expected to be present in responde data."
        assert (
            "passwordLength" in data["errors"]
        ), "'passwordLength' key is expected to be present in responde data['errors']."
        assert (
            data["errors"]["passwordLength"]
            == f"Password length is required to be between 8 to 24 characters. The value '{pl}' is not a valid choice for 'passwordLength'."
        ), "Error message for 'passwordLength' is incorrect."


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            {
                "includeUppercase": False,
                "includeNumbers": False,
                "includeSpecialChars": False,
            },
            {
                "all_lower": True,
                "any_is_lower": True,
                "any_is_upper": False,
                "any_is_number": False,
                "any_is_special": False,
            },
        ),
        (
            {
                "includeUppercase": True,
                "includeNumbers": False,
                "includeSpecialChars": False,
            },
            {
                "all_lower": False,
                "any_is_lower": True,
                "any_is_upper": True,
                "any_is_number": False,
                "any_is_special": False,
            },
        ),
        (
            {
                "includeUppercase": True,
                "includeNumbers": True,
                "includeSpecialChars": False,
            },
            {
                "all_lower": False,
                "any_is_lower": True,
                "any_is_upper": True,
                "any_is_number": True,
                "any_is_special": False,
            },
        ),
        (
            {
                "includeUppercase": True,
                "includeNumbers": True,
                "includeSpecialChars": True,
            },
            {
                "all_lower": False,
                "any_is_lower": True,
                "any_is_upper": True,
                "any_is_number": True,
                "any_is_special": True,
            },
        ),
        (
            {
                "includeUppercase": False,
                "includeNumbers": True,
                "includeSpecialChars": True,
            },
            {
                "all_lower": False,
                "any_is_lower": True,
                "any_is_upper": False,
                "any_is_number": True,
                "any_is_special": True,
            },
        ),
        (
            {
                "includeUppercase": False,
                "includeNumbers": False,
                "includeSpecialChars": True,
            },
            {
                "all_lower": False,
                "any_is_lower": True,
                "any_is_upper": False,
                "any_is_number": False,
                "any_is_special": True,
            },
        ),
    ],
)
def test_all_possible_positive_requests(
    input: dict, expected: dict, client: FlaskClient
):
    test_request_parameters = input
    for pl in range(8, 25):
        test_request_parameters["passwordLength"] = pl

        response = client.get(
            PASSWORD_GENERATE_ENDPOINT, query_string=test_request_parameters
        )

        assert (
            response.status_code == 200
        ), "'200' is the expected response status code."
        data = response.get_json()

        assert (
            "password" in data
        ), "'password' key is expected to be present in responde data."
        assert len(data["password"]) == pl, "Invalid password len returned."

        assert (
            all(c.islower() for c in data["password"]) == expected["all_lower"]
        ), "Password expected to have only lowercase characters."

        assert (
            any(c.islower() for c in data["password"]) == expected["any_is_lower"]
        ), "Password expected to have at least one lowercase characters."

        assert (
            any(c.isupper() for c in data["password"]) == expected["any_is_upper"]
        ), "Password expected to have at least one uppercase characters."

        assert (
            any(c.isnumeric() for c in data["password"]) == expected["any_is_number"]
        ), "Password expected to have at least one digit."

        assert (
            any(c in punctuation for c in data["password"])
            == expected["any_is_special"]
        ), "Password expected to have at least one special characters."
