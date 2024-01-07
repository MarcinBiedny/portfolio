import os
from dotenv import load_dotenv
from src import create_app

load_dotenv()

app = create_app()

if __name__ == "__main__":
    app_host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
    app_port = int(os.environ.get("FLASK_RUN_PORT", 5000))
    app_debug = bool(os.environ.get("FLASK_DEBUG", True))

    app.run(host=app_host, port=app_port, debug=app_debug)
