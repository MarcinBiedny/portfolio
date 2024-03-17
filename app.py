from dotenv import load_dotenv

# Loading environment variables from '.env file
# before anu other code
load_dotenv()

from app import create_app
from os import getenv


if __name__ == "__main__":
    app = create_app(getenv("FLASK_ENV", "production"))

    app_host = getenv("FLASK_RUN_HOST", "0.0.0.0")
    app_port = int(getenv("FLASK_RUN_PORT", 5000))

    app.run(host=app_host, port=app_port)
