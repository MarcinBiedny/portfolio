"""
https://flask-restx.readthedocs.io/en/latest/
"""

from flask_restx import Api
from app.api.v1 import password_ns

api_v1 = Api(
    version="1.0",
    prefix="/api/v1",
    title="API v1",
    description="Version 1 of the API",
    doc="/api/v1/docs/",
)

api_v1.add_namespace(password_ns.ns)
