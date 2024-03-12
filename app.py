from os import getenv
from src import create_app


app = create_app(getenv("FLASK_ENV", "production"))

if __name__ == "__main__":
    app_host = getenv("FLASK_RUN_HOST", "0.0.0.0")
    app_port = int(getenv("FLASK_RUN_PORT", 5000))

    app.run(host=app_host, port=app_port)
