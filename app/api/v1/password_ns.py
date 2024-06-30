"""
    Useful docs:
     - flask_json:
        - Basic usage: https://flask-json.readthedocs.io/en/latest/#basic-usage
        - 'type=inputs.boolean': https://flask-restx.readthedocs.io/en/latest/parsing.html#advanced-types-handling
"""

from flask_restx import Namespace, Resource, reqparse, inputs
from flask_json import json_response
from app.services.password_generator import PasswordGenerator
from flask import current_app


ns = Namespace(name="password", description="Password namespace")
parser = reqparse.RequestParser()
parser.add_argument(
    name="includeUppercase",
    dest="include_uppercase",
    required=False,
    default=True,
    type=inputs.boolean,
)

parser.add_argument(
    name="includeNumbers",
    dest="include_numbers",
    required=False,
    default=True,
    type=inputs.boolean,
)

parser.add_argument(
    name="includeSpecialChars",
    dest="include_special_chars",
    required=False,
    default=True,
    type=inputs.boolean,
)

parser.add_argument(
    name="passwordLength",
    dest="password_length",
    required=False,
    default=24,
    type=int,
    help="Password length is required to be between 8 to 24 characters.",
    choices=[v for v in range(8, 25)],
)


@ns.route("/generate/")
@ns.route("/generate")
class Generate(Resource):
    @ns.expect(parser, validate=True)
    def get(self):
        args = parser.parse_args(strict=True)

        try:
            pg = PasswordGenerator()
            password = pg.generate(
                include_uppercase=args.include_uppercase,
                include_numbers=args.include_numbers,
                include_special_chars=args.include_special_chars,
                password_length=args.password_length,
            )
        except Exception as e:
            current_app.logger.critical(e)
            return json_response(
                message=str("Sorry, something went wrong. We are working on it!"),
                status_=500,
            )

        return json_response(password=password)
